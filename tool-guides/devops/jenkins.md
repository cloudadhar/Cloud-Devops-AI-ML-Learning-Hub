# Jenkins Zero to Hero Guide

## What It Is

Jenkins is an open source automation server used for CI/CD pipelines, build automation, testing, deployments, and legacy enterprise delivery workflows.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Jenkins originated from the Hudson project. The Jenkins community formed around 2011 and Jenkins became one of the most widely used CI servers due to its plugin ecosystem and flexibility.

## Architecture and Core Concepts

Core architecture:

```text
Controller -> Agent -> Job/Pipeline -> Stages -> Steps -> Plugins
```

Key concepts:

- Controller manages configuration and scheduling.
- Agents execute builds.
- Jenkinsfile defines pipeline as code.
- Plugins integrate SCM, cloud, credentials, notifications, and deployment tools.

## Zero to Hero Learning Path

1. Install Jenkins locally or in a container.
2. Create a freestyle job.
3. Create a pipeline job with Jenkinsfile.
4. Connect GitHub or GitLab webhooks.
5. Add credentials safely.
6. Run tests and publish artifacts.
7. Build Docker images.
8. Deploy to Kubernetes or cloud.

## How to Start Using It

Declarative pipeline example:

```groovy
pipeline {
  agent any
  stages {
    stage('Test') {
      steps { sh 'echo Run tests' }
    }
  }
}
```


## Common Integrations and Pipeline Usage

Jenkins often integrates with mature enterprise toolchains:

```text
Git -> Jenkins -> Maven/npm -> SonarQube -> Nexus/Artifactory -> Docker -> Kubernetes
```

Common integrations: GitHub, GitLab, Bitbucket, Maven, Gradle, npm, SonarQube, Nexus, Artifactory, Docker, Kubernetes, Ansible, Terraform, Jira, Slack.

## Advanced Topics

- Jenkins shared libraries.
- Controller and agent scaling.
- Credential binding and secret masking.
- Pipeline replay risks.
- Plugin lifecycle management.
- Jenkins on Kubernetes agents.

## Hands-on Project

Create a Jenkins pipeline that pulls code, runs tests, scans with SonarQube, publishes an artifact to Nexus, and deploys with Ansible.

## Interview Questions

- What is a Jenkins agent?
- Declarative vs scripted pipeline?
- How are credentials stored?
- How do Jenkins plugins help and hurt?
- How would you scale Jenkins builds?

## References

- [Jenkins Documentation](https://www.jenkins.io/doc/)
