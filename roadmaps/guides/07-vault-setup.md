# HashiCorp Vault - Secret Management

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Basic Operations](#basic-operations)
4. [Authentication Methods](#authentication-methods)
5. [CI/CD Integration](#cicd-integration)
6. [Best Practices](#best-practices)

---

## Introduction

### What is HashiCorp Vault?
Vault is a tool for securely storing and accessing secrets:
- Centralized secret management
- Encryption as a service
- Authentication and authorization
- Audit logging
- Secret rotation
- Dynamic credentials
- Lease-based secret expiration

**Official Documentation**: https://www.vaultproject.io/docs

**Key Components**:
- **Secrets Engine**: Stores secrets (KV, AWS, Database, PKI)
- **Auth Methods**: Login mechanisms (GitHub, OIDC, Kubernetes, JWT)
- **Policies**: Access control rules
- **Audit Log**: Tracks all operations

---

## Installation

### Option 1: Docker (Recommended for Development)

```bash
# Run Vault in development mode (insecure, for testing only)
docker run -d \
  --name vault \
  -p 8200:8200 \
  -e VAULT_DEV_ROOT_TOKEN_ID="myroot" \
  -e VAULT_DEV_LISTEN_ADDRESS="0.0.0.0:8200" \
  vault:latest

# Access at http://localhost:8200
# Token: myroot
```

### Option 2: Docker Compose (Production Setup)

Create `docker-compose.yml`:

```yaml
version: '3.9'

services:
  vault:
    image: vault:latest
    container_name: vault
    ports:
      - "8200:8200"
    environment:
      VAULT_ADDR: "http://0.0.0.0:8200"
      VAULT_API_ADDR: "http://vault:8200"
    volumes:
      - ./vault-config.hcl:/vault/config/vault-config.hcl
      - vault_data:/vault/data
    command: server -config=/vault/config/vault-config.hcl
    cap_add:
      - IPC_LOCK
    restart: unless-stopped
    networks:
      - vault-network

volumes:
  vault_data:

networks:
  vault_network:
    driver: bridge
```

### Option 3: Standalone Installation

```bash
# macOS
brew tap hashicorp/tap
brew install hashicorp/tap/vault

# Ubuntu/Debian
wget https://releases.hashicorp.com/vault/1.15.0/vault_1.15.0_linux_amd64.zip
unzip vault_1.15.0_linux_amd64.zip
sudo mv vault /usr/local/bin/
sudo setcap cap_ipc_lock=+ep /usr/local/bin/vault

# Verify
vault --version
```

---

## Basic Operations

### Initialize & Unseal Vault

```bash
# Set Vault address
export VAULT_ADDR="http://localhost:8200"

# Initialize Vault (generates unseal keys and root token)
vault operator init \
  -key-shares=5 \
  -key-threshold=3

# Output:
# Unseal Key 1: ...
# Unseal Key 2: ...
# ...
# Initial Root Token: ...

# Unseal Vault (need 3 of 5 keys)
vault operator unseal <key-1>
vault operator unseal <key-2>
vault operator unseal <key-3>

# Check seal status
vault status

# Login with root token
vault login <root-token>
```

### Enable Secrets Engine

```bash
# List enabled secrets engines
vault secrets list

# Enable KV (Key-Value) secrets engine
vault secrets enable -path=secret kv-v2

# Enable other engines
vault secrets enable aws
vault secrets enable database
vault secrets enable pki
```

### Store and Retrieve Secrets

```bash
# Store a secret
vault kv put secret/app/database \
  username="admin" \
  password="secure-password" \
  host="db.example.com"

# Read a secret
vault kv get secret/app/database

# Read as JSON
vault kv get -format=json secret/app/database

# List secrets
vault kv list secret/app

# Delete a secret
vault kv delete secret/app/database

# Update a secret
vault kv patch secret/app/database \
  password="new-password"
```

### Create Policies

```bash
# Create a policy file
cat > app-policy.hcl <<EOF
# Read secrets
path "secret/app/*" {
  capabilities = ["read", "list"]
}

# Write secrets
path "secret/app/config" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Use database secrets
path "database/static/app" {
  capabilities = ["read"]
}
EOF

# Write policy to Vault
vault policy write app-policy app-policy.hcl

# List policies
vault policy list

# Read policy
vault policy read app-policy
```

---

## Authentication Methods

### 1. GitHub Authentication

**Enable GitHub auth**:
```bash
vault auth enable github

vault write auth/github/config \
  organization=my-company \
  ttl=1h \
  max_ttl=24h
```

**Map GitHub teams to policies**:
```bash
vault write auth/github/map/teams/devops \
  value=app-policy,admin-policy

vault write auth/github/map/users/john.doe \
  value=app-policy
```

**Login with GitHub**:
```bash
vault login -method=github token=<github-personal-access-token>
```

### 2. Kubernetes Authentication

**Enable Kubernetes auth**:
```bash
vault auth enable kubernetes

vault write auth/kubernetes/config \
  kubernetes_host="https://kubernetes.default" \
  kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt \
  token_reviewer_jwt=@/var/run/secrets/kubernetes.io/serviceaccount/token
```

**Map service accounts to policies**:
```bash
vault write auth/kubernetes/role/app \
  bound_service_account_names=app \
  bound_service_account_namespaces=default \
  policies=app-policy \
  ttl=24h
```

**In Kubernetes pod** (automatic):
```bash
# Vault Agent automatically handles authentication
# No manual login needed
```

### 3. JWT/OIDC Authentication

**Enable OIDC auth**:
```bash
vault auth enable jwt

vault write auth/jwt/config \
  oidc_discovery_url="https://your-auth-provider" \
  oidc_client_id="your-client-id" \
  oidc_client_secret="your-client-secret"
```

**Map roles**:
```bash
vault write auth/jwt/role/app \
  bound_audiences="vault-app" \
  user_claim="sub" \
  policies=app-policy
```

### 4. AppRole Authentication (For Applications)

**Enable AppRole**:
```bash
vault auth enable approle

vault write auth/approle/role/app \
  policies=app-policy \
  bind_secret_id=true \
  secret_id_ttl=0h \
  secret_id_num_uses=0
```

**Generate credentials**:
```bash
# Get Role ID
vault read auth/approle/role/app/role-id

# Generate Secret ID
vault write -f auth/approle/role/app/secret-id

# Login
vault write auth/approle/login \
  role_id=<role-id> \
  secret_id=<secret-id>
```

---

## CI/CD Integration

### GitHub Actions Integration

Create `.github/workflows/vault-secrets.yml`:

```yaml
name: Fetch Secrets from Vault

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Import Secrets
        uses: hashicorp/vault-action@v2
        with:
          url: ${{ secrets.VAULT_ADDR }}
          role: github-action-role
          jwtGithubAudience: ${{ secrets.VAULT_ADDR }}
          secrets: |
            secret/app/database username | DB_USERNAME;
            secret/app/database password | DB_PASSWORD;
            secret/app/api api-key | API_KEY

      - name: Use Secrets
        run: |
          echo "Username: ${{ env.DB_USERNAME }}"
          npm run deploy
        env:
          DATABASE_URL: "postgres://${{ env.DB_USERNAME }}:${{ env.DB_PASSWORD }}@db.example.com"
          API_KEY: ${{ env.API_KEY }}
```

### GitLab CI Integration

Create `.gitlab-ci.yml`:

```yaml
stages:
  - deploy

deploy:
  stage: deploy
  image: vault:latest
  script:
    # Login to Vault
    - export VAULT_TOKEN=$(vault write -field=token auth/jwt/login role=gitlab jwt=$CI_JOB_JWT)
    
    # Fetch secrets
    - export DB_USER=$(vault kv get -field=username secret/app/database)
    - export DB_PASS=$(vault kv get -field=password secret/app/database)
    - export API_KEY=$(vault kv get -field=api-key secret/app/api)
    
    # Deploy
    - npm run deploy
```

### Kubernetes Pod Integration

Create Vault Agent config:

```hcl
# vault-agent-config.hcl
vault {
  address = "http://vault:8200"
}

auto_auth {
  method {
    type = "kubernetes"
    config = {
      role = "app"
    }
  }

  sink {
    type = "file"
    config = {
      path = "/vault/secrets/.vault-token"
    }
  }
}

cache {
  use_auto_auth_token = true
}

listener "unix" {
  address = "/vault/secrets/agent.sock"
  tls_disable = true
}

listener "tcp" {
  address = "127.0.0.1:8200"
  tls_disable = true
}
```

Use in Kubernetes:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  serviceAccountName: app
  containers:
  - name: app
    image: myapp:latest
    env:
    - name: VAULT_ADDR
      value: "http://vault:8200"
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
  initContainers:
  - name: vault-agent
    image: vault:latest
    args:
      - agent
      - -config=/vault/config/agent.hcl
    volumeMounts:
    - name: vault-config
      mountPath: /vault/config
    - name: vault-secrets
      mountPath: /vault/secrets
  volumes:
  - name: vault-config
    configMap:
      name: vault-agent-config
  - name: vault-secrets
    emptyDir:
      medium: Memory
```

---

## Best Practices

### Secret Rotation

```bash
# Set automatic password rotation for database
vault write -f database/rotate-root/my-db

# Set rotation policy
vault write database/config/my-db \
  rotation_statements="ALTER USER '{{name}}' IDENTIFIED BY '{{password}}';" \
  rotate_safely=true
```

### Audit Logging

```bash
# Enable audit logging
vault audit enable file file_path=/var/log/vault-audit.log

# View audit logs
vault audit list
```

### Least Privilege

```bash
# Create minimal policy for read-only
cat > read-only.hcl <<EOF
path "secret/app/*" {
  capabilities = ["read", "list"]
}
EOF

vault policy write read-only read-only.hcl
```

### Backup & Disaster Recovery

```bash
# Enable Raft storage for HA
vault operator raft bootstrap
vault operator raft join-raft

# Take snapshot
vault operator raft snapshot save backup.snap

# Restore from snapshot
vault operator raft snapshot restore backup.snap
```

### Secret Management Strategy

✅ **Use different auth methods for different consumers**:
- Humans: GitHub/OIDC
- CI/CD: JWT/AppRole
- Kubernetes: Kubernetes auth
- Applications: AppRole

✅ **Implement secret rotation**:
- Database passwords
- API keys
- TLS certificates

✅ **Audit all secret access**:
- Enable audit logging
- Monitor anomalies
- Review access patterns

✅ **Use short TTLs** (Time To Live):
- Reduce exposure window
- Force re-authentication
- Easier revocation

---

## Troubleshooting

**Issue**: "permission denied" on secret read
**Solution**: Check policy allows "read" capability

**Issue**: Authentication fails
**Solution**: Verify auth method configured, token/credentials valid

**Issue**: Vault sealed
**Solution**: Use unseal keys to unseal Vault

---

## Official Resources

- **Vault Documentation**: https://www.vaultproject.io/docs
- **API Documentation**: https://www.vaultproject.io/api-docs
- **Community Forum**: https://discuss.hashicorp.com/c/vault

---

**Last Updated**: August 2026
**Version**: 1.0
