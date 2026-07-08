# Tool Selection Guide

Do not choose tools because they are popular. Choose tools by problem, team size, cost, support, integration, and learning value.

## Selection Criteria

| Criteria | Question |
| --- | --- |
| Purpose | What exact problem does this tool solve? |
| Integration | Does it work with our Git, CI/CD, cloud, and security tools? |
| Learning curve | Can beginners use it without weeks of confusion? |
| Operations | How do we backup, upgrade, monitor, and secure it? |
| Cost | Is it open source, SaaS, enterprise, or usage-based? |
| Community | Are docs, examples, and community support strong? |
| Lock-in | Can we move away later if needed? |

## Starter Choices

| Need | Beginner Choice | Advanced Choice |
| --- | --- | --- |
| Source control | GitHub | GitHub Enterprise or GitLab |
| CI/CD | GitHub Actions | Jenkins, GitLab CI/CD, Argo CD |
| Containers | Docker | Docker + Kubernetes |
| Reverse proxy | Nginx | Nginx Ingress Controller |
| API gateway | Kong Gateway | Kong + decK + Terraform |
| IaC | Terraform | Terraform/OpenTofu with modules and policy |
| Monitoring | Prometheus + Grafana | OpenTelemetry + Grafana/Loki/Tempo |
| Code quality | SonarQube | SonarQube with quality gates |
| Artifact repo | GitHub Packages | Nexus or Artifactory |
| Secrets | Cloud secret manager | Vault + cloud secret manager |

## Decision Record Template

```md
# Tool Decision: <Tool Name>

## Problem

## Options Compared

## Selected Tool

## Why

## Risks

## Cost

## Security Considerations

## Exit Plan
```
