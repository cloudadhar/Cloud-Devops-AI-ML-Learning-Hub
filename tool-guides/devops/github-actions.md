# GitHub Actions Zero to Hero Guide

## What It Is

GitHub Actions is GitHub native automation for CI/CD, testing, security scans, releases, and cloud deployments.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

GitHub Actions became generally available in 2019 and brought workflow automation directly into GitHub repositories using YAML workflows and hosted or self-hosted runners.

## Architecture and Core Concepts

Core architecture:

```text
Event -> Workflow -> Job -> Step -> Action or shell command -> Runner
```

Key concepts:

- Events: push, pull_request, workflow_dispatch, schedule.
- Workflows in `.github/workflows`.
- Jobs run on runners.
- Steps run commands or reusable actions.
- Secrets, variables, environments, permissions, artifacts, cache.

## Zero to Hero Learning Path

1. Create a workflow triggered by push.
2. Run lint and unit tests.
3. Upload build artifacts.
4. Use repository secrets safely.
5. Build and scan Docker images.
6. Use manual approvals with environments.
7. Deploy to AWS/Azure/GCP using OIDC.
8. Create reusable workflows for teams.

## How to Start Using It

Minimal workflow:

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Run tests here"
```


## Common Integrations and Pipeline Usage

Common pipeline:

```text
pull_request -> checkout -> install -> lint -> test -> secret scan -> build -> artifact -> deploy approval
```

Common integrations: Docker Hub, GHCR, AWS OIDC, Azure login, Google auth, Terraform, SonarQube, Trivy, Checkov, Slack, Jira, and Argo CD.

## Advanced Topics

- Workflow permissions and least privilege.
- OIDC cloud authentication instead of static keys.
- Matrix builds.
- Reusable workflows.
- Concurrency and deployment locks.
- Artifact retention and cache strategy.
- Self-hosted runner security.

## Hands-on Project

Create a full CI pipeline that runs tests, builds a Docker image, scans it with Trivy, and deploys only after manual approval.

## Interview Questions

- What is a runner?
- What is the difference between job and step?
- How do secrets work in GitHub Actions?
- How do you deploy to AWS without storing AWS keys?
- How do you prevent two deployments at the same time?

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Security Hardening](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
