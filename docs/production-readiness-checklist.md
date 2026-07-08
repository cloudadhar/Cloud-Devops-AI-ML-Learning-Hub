# Production Readiness Checklist

Use this before calling any project production-style.

## Code

- Tests exist.
- Linting exists.
- Configuration is outside code.
- Errors are handled.
- Dependencies are pinned or controlled.

## Build and Release

- CI/CD pipeline exists.
- Build artifacts are stored.
- Rollback is documented.
- Versioning is clear.

## Infrastructure

- Infrastructure is defined as code.
- Environments are separated.
- State and secrets are protected.
- Backups are considered.

## Security

- Secrets are not in Git.
- Least privilege IAM is used.
- Images are scanned.
- Dependencies are scanned.
- OWASP risks are considered.
- Public ports are intentional.

## Observability

- Logs are available.
- Metrics are available.
- Alerts are meaningful.
- Dashboards show service health.
- Traces are considered for distributed systems.

## Operations

- Runbook exists.
- Cleanup steps exist.
- Cost controls exist.
- Incident response steps exist.
- Ownership is clear.
