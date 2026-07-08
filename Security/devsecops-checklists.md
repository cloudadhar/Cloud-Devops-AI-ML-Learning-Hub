# DevSecOps Checklists

## Code Security

- SAST scan added.
- Dependency scan added.
- Secrets scan added.
- Branch protection enabled.
- Pull request review required.

## Container Security

- Minimal base image.
- Non-root user where possible.
- Image scanned.
- No secrets in image layers.
- Resource limits defined.

## Infrastructure Security

- IaC scan added.
- Public access reviewed.
- IAM least privilege used.
- State files protected.
- Cloud logs enabled.

## API Security

- Authentication exists.
- Authorization exists.
- Rate limiting exists.
- Input validation exists.
- Audit logs exist.
- TLS enabled.

## CI/CD Security

- Minimal workflow permissions.
- Secrets stored in secret manager.
- No untrusted scripts without review.
- Deployment requires approval for production.
