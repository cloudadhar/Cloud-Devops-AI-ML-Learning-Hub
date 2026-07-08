# Helm and Argo CD Zero to Hero Guide

## What It Is

Helm packages Kubernetes manifests as reusable charts. Argo CD continuously deploys Kubernetes applications from Git using GitOps principles.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Helm grew as the package manager for Kubernetes. Argo CD was created by Intuit and became a popular CNCF GitOps tool for declarative Kubernetes delivery.

## Architecture and Core Concepts

Architecture:

```text
Helm chart -> Rendered Kubernetes manifests -> Git repo -> Argo CD -> Kubernetes cluster
```

Helm concepts:

- Chart, values.yaml, templates, release.

Argo CD concepts:

- Application, project, sync, health, diff, desired state, live state.

## Zero to Hero Learning Path

1. Install Helm and deploy a public chart.
2. Create a simple chart for your app.
3. Use values for environment differences.
4. Commit manifests or charts to Git.
5. Install Argo CD.
6. Create an Argo CD Application.
7. Use sync and rollback.
8. Add promotion strategy across dev, stage, prod.

## How to Start Using It

Example flow:

```bash
helm create my-app
helm template my-app ./my-app
helm upgrade --install my-app ./my-app
```


## Common Integrations and Pipeline Usage

GitOps deployment:

```text
Developer PR -> Git merge -> Argo CD detects diff -> sync -> Kubernetes rollout
```

Integrates with GitHub, GitLab, Helm repos, Kustomize, Kubernetes, SSO, notifications, Prometheus, and policy tools.

## Advanced Topics

- ApplicationSets.
- Multi-cluster GitOps.
- Helm dependency management.
- Chart testing.
- Argo CD RBAC and SSO.
- Progressive delivery with Argo Rollouts.

## Hands-on Project

Create a Helm chart for an API and deploy it using Argo CD from a Git repository. Add environment-specific values.

## Interview Questions

- What is Helm?
- What is GitOps?
- What does Argo CD sync do?
- How do you roll back a Helm release?
- How do you manage different values per environment?

## References

- [Helm Documentation](https://helm.sh/docs/)
- [Argo CD Documentation](https://argo-cd.readthedocs.io/en/stable/)
