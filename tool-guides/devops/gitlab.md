# GitLab Zero to Hero Guide

## What It Is

GitLab is a DevSecOps platform that combines Git repositories, issues, merge requests, CI/CD, packages, security scanning, environments, and releases.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

GitLab started in 2011 as an open source Git repository management tool and evolved into a full DevSecOps platform for source control, CI/CD, planning, packaging, security, and operations.

## Architecture and Core Concepts

Core architecture:

```text
Repository -> Merge request -> .gitlab-ci.yml -> GitLab Runner -> Jobs -> Artifacts -> Environments
```

Key concepts:

- Project, group, merge request, issue, milestone.
- GitLab Runner executes CI/CD jobs.
- Stages, jobs, artifacts, cache, variables, environments.
- Container registry and package registry.

## Zero to Hero Learning Path

1. Create a project and push code.
2. Open merge requests and review changes.
3. Write a `.gitlab-ci.yml` pipeline.
4. Configure variables and protected branches.
5. Build Docker images.
6. Use GitLab environments and deployments.
7. Add security scans.
8. Use groups and permissions.

## How to Start Using It

Basic GitLab CI file:

```yaml
stages:
  - test

test:
  stage: test
  script:
    - echo "Run tests here"
```


## Common Integrations and Pipeline Usage

Typical pipeline:

```text
commit -> merge request -> GitLab CI -> tests -> security scans -> container image -> environment deploy
```

Integrates with Kubernetes, Terraform, Docker registries, SonarQube, Jira, Slack, and cloud providers.

## Advanced Topics

- Parent-child pipelines.
- Dynamic environments.
- GitLab security dashboards.
- Protected variables and protected environments.
- Self-managed GitLab operations.
- Runner autoscaling and isolation.

## Hands-on Project

Build a GitLab pipeline that tests a web app, builds a container, pushes to the registry, and deploys to a staging environment.

## Interview Questions

- GitHub vs GitLab?
- What is GitLab Runner?
- What is `.gitlab-ci.yml`?
- How do protected variables work?
- How do environments help deployments?

## References

- [GitLab Docs](https://docs.gitlab.com/)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ci/)
