# CI/CD Guide

## Concepts

- Pipeline stages
- Build artifacts
- Unit, integration, and end-to-end tests
- Secrets and environment variables
- Runners and agents
- Deployment approvals
- Blue-green, canary, and rolling deployments
- Rollback strategy
- Quality gates
- Security scans

## Tools

- GitHub Actions
- GitLab CI/CD
- Jenkins
- Azure Pipelines
- Argo CD
- Spinnaker
- CircleCI

## Starter Pipeline Pattern

```text
checkout -> lint -> test -> security scan -> build -> publish artifact -> deploy -> smoke test -> notify
```

## Validated References

- [GitHub Actions documentation](https://docs.github.com/en/actions) - official GitHub Actions docs.
- [GitLab CI/CD documentation](https://docs.gitlab.com/ci/) - official GitLab CI/CD docs.
- [Jenkins documentation](https://www.jenkins.io/doc/) - official Jenkins docs.
- [Argo CD documentation](https://argo-cd.readthedocs.io/en/stable/) - GitOps CD for Kubernetes.
