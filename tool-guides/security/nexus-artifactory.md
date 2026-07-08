# Nexus and Artifactory Zero to Hero Guide

## What It Is

Nexus Repository and JFrog Artifactory store build artifacts, packages, container images, and release assets for repeatable software delivery.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Artifact repositories became important as teams needed reliable storage for Maven, npm, Docker, Python, and binary release artifacts. Nexus and Artifactory are two widely used enterprise artifact managers.

## Architecture and Core Concepts

Architecture:

```text
CI build -> Artifact repository -> Deployment pipeline -> Runtime environment
```

Key concepts:

- Hosted repository, proxy repository, group repository.
- Package formats: Maven, npm, PyPI, NuGet, Docker, Helm.
- Versioned artifacts and promotion between environments.

## Zero to Hero Learning Path

1. Understand why artifacts should not only live on CI runners.
2. Publish a package or build artifact.
3. Use repository credentials safely.
4. Proxy public package registries.
5. Push Docker images.
6. Promote artifacts from dev to prod.
7. Add retention cleanup.
8. Connect vulnerability scanning where available.

## How to Start Using It

Pipeline position:

```text
source -> build -> test -> publish artifact -> deploy same artifact
```


## Common Integrations and Pipeline Usage

Integrates with Maven, Gradle, npm, pip, Docker, Helm, Jenkins, GitHub Actions, GitLab CI, Kubernetes, SonarQube, Snyk, and release automation.

## Advanced Topics

- Artifact promotion strategies.
- Repository cleanup policies.
- Immutable release artifacts.
- SBOM storage.
- Proxy cache governance.
- Access control and audit logs.

## Hands-on Project

Build a pipeline that publishes a versioned package or Docker image to Nexus/Artifactory and deploys only that immutable artifact.

## Interview Questions

- Why use an artifact repository?
- What is artifact promotion?
- How is a package registry different from Git?
- How do you manage artifact retention?
- How do you secure repository credentials?

## References

- [Sonatype Nexus Repository Documentation](https://help.sonatype.com/en/sonatype-nexus-repository.html)
- [JFrog Artifactory Documentation](https://jfrog.com/help/r/jfrog-artifactory-documentation/artifactory-documentation)
