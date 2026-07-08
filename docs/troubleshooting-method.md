# Troubleshooting Method

Use this method whenever something breaks.

## 1. State the Problem

Write what you expected and what actually happened.

## 2. Capture Evidence

Collect:

- Error messages
- Logs
- Command output
- Config files
- Recent changes
- Environment details

## 3. Identify the Layer

Common layers:

- Code
- Dependency
- Container
- Network
- DNS
- IAM
- Database
- CI/CD
- Kubernetes
- Cloud provider

## 4. Form a Hypothesis

Example:

```text
The app is healthy locally but failing in Kubernetes, so the issue may be environment variables, service routing, image tag, or resource limits.
```

## 5. Test One Change

Change one thing at a time.

## 6. Document the Fix

Use [Troubleshooting Log Template](../logs/troubleshooting-log-template.md).

## Helpful Commands

```bash
# Linux
systemctl status <service>
journalctl -u <service>
ss -tulpn
curl -v http://localhost:8080

# Docker
docker ps
docker logs <container>
docker exec -it <container> sh

# Kubernetes
kubectl get pods
kubectl describe pod <pod>
kubectl logs <pod>
kubectl get events --sort-by=.metadata.creationTimestamp

# Terraform
terraform fmt
terraform validate
terraform plan

# GitHub Actions
# Read job logs, failed step, environment variables, and permissions.
```
