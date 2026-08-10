# Nexus Repository Manager - Setup & Integration

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [GitHub Integration](#github-integration)
5. [GitLab Integration](#gitlab-integration)
6. [Best Practices](#best-practices)

---

## Introduction

### What is Nexus?
Nexus Repository Manager is a universal package repository manager that:
- Stores build artifacts (JAR, WAR, Docker images, npm packages, etc.)
- Caches dependencies from upstream repositories
- Manages different repository formats (Maven, npm, Docker, Python, etc.)
- Controls access and permissions
- Manages releases and snapshots
- Integrates with CI/CD pipelines

### Official Documentation
https://help.sonatype.com/repomanager3

**Key Installation Guides:**
- [Install Nexus Repository with PostgreSQL Database](https://help.sonatype.com/en/install-nexus-repository-with-a-postgresql-database.html)

### Repository Formats
- Maven (Java)
- npm (JavaScript)
- Python (PyPI)
- Docker
- NuGet (.NET)
- Apt (Debian/Ubuntu)
- Yum (RedHat/CentOS)
- Raw format

---

## Installation

### Option 1: Docker (Recommended for Development)

```bash
# Run Nexus with Docker
docker run -d \
  --name nexus \
  -p 8081:8081 \
  -e INSTALL4J_ADD_VM_PARAMS="-Xmx2703m -Xms2703m" \
  -v nexus-data:/nexus-data \
  sonatype/nexus3:latest

# Access at http://localhost:8081
# Default credentials: admin/admin123
# Initial password in /nexus-data/admin.password
```

### Option 2: Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.9'

services:
  nexus:
    image: sonatype/nexus3:latest
    container_name: nexus
    ports:
      - "8081:8081"
      - "8082:8082"  # Docker repository port
    environment:
      INSTALL4J_ADD_VM_PARAMS: "-Xmx2703m -Xms2703m"
    volumes:
      - nexus_data:/nexus-data
    restart: unless-stopped
    networks:
      - devops-network

volumes:
  nexus_data:

networks:
  devops-network:
    driver: bridge
```

```bash
docker-compose up -d
# Get initial admin password:
docker exec nexus cat /nexus-data/admin.password
```

### Option 3: Standalone Installation (Ubuntu/Debian)

```bash
# Install Java
sudo apt-get update
sudo apt-get install -y openjdk-11-jdk

# Download Nexus
cd /opt
sudo wget https://download.sonatype.com/nexus/3/nexus-3.53.0-01-unix.tar.gz
sudo tar -xzf nexus-3.53.0-01-unix.tar.gz
sudo chown -R nexus:nexus nexus-3.53.0-01

# Create nexus user
sudo useradd -r -s /bin/bash nexus

# Start Nexus
cd nexus-3.53.0-01
bin/nexus start

# Access at http://localhost:8081
# View initial password:
sudo cat /opt/sonatype-work/nexus3/admin.password
```

---

## Configuration

### Initial Setup

1. Access http://localhost:8081
2. Click "Sign in" (top right)
3. Username: `admin`
4. Password: Check `/nexus-data/admin.password` or initial prompt
5. Complete setup wizard
6. Change admin password
7. Configure repositories

### Create Repositories

#### npm Repository

1. Go to Administration → Repositories
2. Click "Create repository"
3. Select "npm (hosted)"
4. Set name: `npm-releases`
5. Set repository type: `Hosted`
6. Version policy: `Release`
7. Save

Repeat for snapshots:
- Name: `npm-snapshots`
- Version policy: `Snapshot`

Create proxy repository:
- Name: `npm-proxy`
- Select "npm (proxy)"
- Remote storage: `https://registry.npmjs.org`

#### Maven Repository

```
Maven Snapshots: `maven-snapshots` (Snapshot)
Maven Releases: `maven-releases` (Release)
Maven Proxy: `maven-central-proxy` (Proxy to Maven Central)
```

#### Docker Repository

1. Create hosted repository:
   - Name: `docker-releases`
   - Enable Docker API
   - HTTP port: `8082`

2. Create proxy repository:
   - Name: `docker-proxy`
   - Remote storage: `https://registry.hub.docker.com`

### Create Users & Roles

1. Go to Administration → Security → Users
2. Click "Create user"
3. Username: `ci-user`
4. Password: Generate strong password
5. Roles: Select `nx-admin` (or custom role)
6. Save

---

## GitHub Integration

### Method 1: Publish npm Package to Nexus

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to Nexus

on:
  push:
    tags:
      - 'v*'

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Configure npm registry
        run: |
          echo "@mycompany:registry=http://nexus.example.com:8081/repository/npm-releases/" > ~/.npmrc
          echo "http://nexus.example.com:8081/repository/npm-releases/:_authToken=${{ secrets.NEXUS_TOKEN }}" >> ~/.npmrc

      - name: Publish to Nexus
        run: npm publish --registry http://nexus.example.com:8081/repository/npm-releases/
```

### Method 2: Publish Docker Image to Nexus

Create `.github/workflows/docker-publish.yml`:

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [main]
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Login to Nexus Docker Registry
        uses: docker/login-action@v2
        with:
          registry: nexus.example.com:8082
          username: ${{ secrets.NEXUS_USERNAME }}
          password: ${{ secrets.NEXUS_PASSWORD }}

      - name: Build and Push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: |
            nexus.example.com:8082/my-app:latest
            nexus.example.com:8082/my-app:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

### Add GitHub Secrets

1. Go to Repository Settings → Secrets and variables → Actions
2. Add `NEXUS_TOKEN`: Your Nexus API token
3. Add `NEXUS_USERNAME`: Nexus username
4. Add `NEXUS_PASSWORD`: Nexus password

---

## GitLab Integration

### Method 1: Publish npm Package via GitLab CI

Create `.gitlab-ci.yml`:

```yaml
stages:
  - test
  - publish

variables:
  NEXUS_REGISTRY: "nexus.example.com:8081/repository"

test:
  stage: test
  image: node:18-alpine
  script:
    - npm ci
    - npm test

publish:
  stage: publish
  image: node:18-alpine
  script:
    - echo "@mycompany:registry=${NEXUS_REGISTRY}/npm-releases/" > ~/.npmrc
    - echo "${NEXUS_REGISTRY}/npm-releases/:_authToken=${NEXUS_TOKEN}" >> ~/.npmrc
    - npm publish --registry ${NEXUS_REGISTRY}/npm-releases/
  only:
    - tags
```

### Method 2: Publish Docker Image via GitLab CI

Create `.gitlab-ci.yml`:

```yaml
stages:
  - test
  - build
  - publish

test:
  stage: test
  image: node:18-alpine
  script:
    - npm ci
    - npm test

build_docker:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t myapp:latest .
    - docker tag myapp:latest ${CI_REGISTRY}/myapp:${CI_COMMIT_SHA}
    - docker tag myapp:latest ${CI_REGISTRY}/myapp:latest
  artifacts:
    reports:
      dotenv: build.env

push_to_nexus:
  stage: publish
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker login -u $NEXUS_USERNAME -p $NEXUS_PASSWORD nexus.example.com:8082
    - docker tag myapp:latest nexus.example.com:8082/myapp:${CI_COMMIT_SHA}
    - docker tag myapp:latest nexus.example.com:8082/myapp:latest
    - docker push nexus.example.com:8082/myapp:${CI_COMMIT_SHA}
    - docker push nexus.example.com:8082/myapp:latest
  only:
    - main
    - tags
```

### Add GitLab Variables

1. Go to GitLab Repository → Settings → CI/CD → Variables
2. Add `NEXUS_TOKEN`: Your Nexus API token
3. Add `NEXUS_USERNAME`: Nexus username
4. Add `NEXUS_PASSWORD`: Nexus password
5. Add `NEXUS_REGISTRY`: `nexus.example.com:8081/repository`

---

## Using Nexus Repositories

### npm

Configure `~/.npmrc`:

```
@mycompany:registry=http://nexus.example.com:8081/repository/npm-releases/
http://nexus.example.com:8081/repository/npm-releases/:_authToken=YOUR_TOKEN
http://nexus.example.com:8081/repository/npm-proxy/:_authToken=YOUR_TOKEN
```

Or use `package.json`:

```json
{
  "publishConfig": {
    "registry": "http://nexus.example.com:8081/repository/npm-releases/"
  }
}
```

Publish:

```bash
npm publish
```

### Maven

Configure `~/.m2/settings.xml`:

```xml
<settings>
  <servers>
    <server>
      <id>nexus-releases</id>
      <username>admin</username>
      <password>YOUR_PASSWORD</password>
    </server>
    <server>
      <id>nexus-snapshots</id>
      <username>admin</username>
      <password>YOUR_PASSWORD</password>
    </server>
  </servers>
  <repositories>
    <repository>
      <id>nexus-releases</id>
      <url>http://nexus.example.com:8081/repository/maven-releases</url>
    </repository>
    <repository>
      <id>nexus-snapshots</id>
      <url>http://nexus.example.com:8081/repository/maven-snapshots</url>
    </repository>
  </repositories>
</settings>
```

### Docker

Login:

```bash
docker login nexus.example.com:8082 -u USERNAME -p PASSWORD
```

Push:

```bash
docker tag myapp:1.0 nexus.example.com:8082/myapp:1.0
docker push nexus.example.com:8082/myapp:1.0
```

Pull:

```bash
docker pull nexus.example.com:8082/myapp:1.0
```

### Python

Configure `~/.pypirc`:

```
[distutils]
index-servers =
  nexus

[nexus]
repository: http://nexus.example.com:8081/repository/python-releases/
username: admin
password: YOUR_PASSWORD
```

Publish:

```bash
python setup.py upload -r nexus
# or
twine upload -r nexus dist/*
```

---

## Best Practices

### Repository Structure

✅ **Separate repositories by purpose**:
- Snapshots: Development builds (temporary)
- Releases: Production builds (permanent)
- Proxy: External dependencies cache

### Artifact Naming

✅ **Consistent naming convention**:
```
{organization}-{project}-{component}-{version}.jar
company-app-api-1.0.0.jar
company-app-ui-1.0.0.zip
```

### Cleanup Policies

1. Go to Administration → Repositories → Select repository
2. Set cleanup policy:
   - Keep last 30 releases
   - Delete if not accessed for 90 days
   - Delete pre-release versions

### Security

✅ Use strong passwords
✅ Enable authentication on all repositories
✅ Use API tokens instead of passwords
✅ Audit access logs regularly
✅ Restrict repository access by role

### Backup & Recovery

```bash
# Backup Nexus data
docker exec nexus tar -czf /nexus-data/backup.tar.gz /nexus-data

# Copy backup
docker cp nexus:/nexus-data/backup.tar.gz ./

# Restore backup
docker cp ./backup.tar.gz nexus:/nexus-data/
docker exec nexus tar -xzf /nexus-data/backup.tar.gz -C /
```

---

## Troubleshooting

**Issue**: Cannot push artifacts
**Solution**: Check credentials, verify user has upload role

**Issue**: Slow artifact retrieval
**Solution**: Increase heap memory, optimize repository settings

**Issue**: Disk space issues
**Solution**: Set cleanup policies, remove old artifacts

**Issue**: Cannot download from proxy
**Solution**: Check remote repository URL, verify network access

---

## Official Resources

- **Nexus Documentation**: https://help.sonatype.com/repomanager3
- **API Documentation**: https://help.sonatype.com/repomanager3/nexus-repository-administration/rest-and-integration-api
- **User Guide**: https://help.sonatype.com/repomanager3/getting-started
- **Community Support**: https://community.sonatype.com

---

**Last Updated**: August 2026
**Version**: 1.0
