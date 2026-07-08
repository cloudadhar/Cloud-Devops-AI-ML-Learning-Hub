# DevOps Engineering: CI/CD, Automation, and Release

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white) ![GitLab](https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white) ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)

## Who This Track Is For

Learners preparing for DevOps engineer, build/release engineer, CI/CD engineer, and automation engineer roles.

## Outcomes

- Build CI pipelines with lint, test, build, artifact, scan, publish, deploy, smoke test, and rollback stages.
- Use GitHub Actions, GitLab CI, Jenkins, and Argo CD at architecture level.
- Explain release safety: approvals, environments, feature flags, rollback, and audit logs.


## Architecture Mental Model

```text
Git push -> CI runner -> lint/test -> build artifact/image -> security scan -> registry -> deploy stage -> smoke test -> monitoring -> rollback
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Learn Git workflow, YAML syntax, job/stage/step concepts, runners, artifacts, and environment variables.
- Create a CI pipeline for a small app with lint and tests.
- Learn failure reading: logs, exit codes, artifacts, and cache problems.

### Days 31-60

- Add Docker build, image push, secret handling, environment approvals, and deployment job.
- Add SonarQube/Trivy/Checkov style quality and security gates.
- Write rollback and incident notes for a failed deployment.

### Days 61-90

- Design multi-environment pipelines with dev, test, staging, production, approvals, OIDC, and audit.
- Compare GitHub Actions, GitLab CI, and Jenkins for enterprise teams.
- Add GitOps deployment with Argo CD for Kubernetes.

## Hands-on Labs

- Build one GitHub Actions pipeline for a Python or Node app.
- Build equivalent GitLab CI pipeline and compare syntax.
- Create a Jenkinsfile pipeline with build, test, package, and archive stages.
- Add pipeline failure runbook with screenshots and fix notes.

## Scenario-Based Interview Questions

1. A pipeline passes tests but production deployment fails. How do you separate build correctness from deploy correctness?
2. Secrets leaked in CI logs. What immediate rotation, audit, and pipeline changes are required?
3. A release must be stopped after deployment to 10 percent users. How do feature flags, canary, and rollback help?
4. Jenkins agents are slow and unreliable. What do you check: executor count, workspace cleanup, Docker cache, network, plugins, or controller health?
5. A PR CI fails only on GitHub runners but works locally. How do you debug OS, dependencies, env vars, cache, and path differences?

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://docs.github.com/en/actions/get-started/understand-github-actions
- https://docs.gitlab.com/ci/
- https://www.jenkins.io/doc/book/pipeline/
- https://argo-cd.readthedocs.io/en/stable/
