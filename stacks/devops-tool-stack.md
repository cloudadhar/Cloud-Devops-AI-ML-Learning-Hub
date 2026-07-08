# DevOps Tool Stack

A DevOps stack is a connected set of tools used to plan, code, build, test, package, deploy, monitor, secure, and improve software systems. The goal is not to learn every tool at once. The goal is to understand the delivery lifecycle and know which tool solves which problem.

## Stack Layers

| Layer | Purpose | Tools to Learn |
| --- | --- | --- |
| Planning and collaboration | Track work, decisions, docs, and incidents | Jira, Confluence, GitHub Issues, GitLab Issues, Slack, Microsoft Teams |
| Source control | Version code and enable review | Git, GitHub, GitLab, Bitbucket |
| IDE and developer workflow | Write, debug, and review code | VS Code, IntelliJ IDEA, GitHub Codespaces |
| CI/CD | Build, test, scan, and deploy automatically | GitHub Actions, GitLab CI/CD, Jenkins, CircleCI |
| Artifact management | Store packages, images, and release assets | Nexus Repository, JFrog Artifactory, GitHub Packages, GitLab Package Registry |
| Containers | Package apps consistently | Docker, Podman, BuildKit |
| Orchestration | Run and scale containers | Kubernetes, OpenShift, Nomad |
| Kubernetes packaging | Manage repeatable Kubernetes installs | Helm, Kustomize |
| Ingress and reverse proxy | Route traffic into apps | Nginx, Nginx Ingress Controller, Traefik |
| API gateway | Secure, route, throttle, and observe APIs | Kong Gateway, AWS API Gateway, Apigee, Azure API Management |
| Infrastructure as Code | Provision infrastructure from code | Terraform, OpenTofu, Pulumi, CloudFormation, Azure Bicep |
| Configuration management | Configure servers and apps | Ansible, Chef, Puppet |
| GitOps | Reconcile desired state from Git | Argo CD, Flux CD |
| Observability | Measure health using metrics, logs, traces | Prometheus, Grafana, Loki, OpenTelemetry, ELK/OpenSearch, Datadog |
| Security | Shift security earlier in delivery | SonarQube, Trivy, Checkov, Semgrep, Gitleaks, OWASP ZAP, HashiCorp Vault |
| Platform engineering | Create reusable developer workflows | Backstage, Port, Spacelift, Qovery |

## Beginner Stack

Use this for your first complete project:

```text
GitHub -> GitHub Actions -> Docker -> Terraform -> AWS EC2 -> Nginx -> Prometheus/Grafana
```

## Kubernetes Stack

Use this when learners are ready for cloud-native deployment:

```text
GitHub -> GitHub Actions -> Docker -> Kubernetes -> Helm -> Nginx Ingress -> Argo CD -> Prometheus/Grafana
```

## DevSecOps Stack

Add security gates to the pipeline:

```text
GitHub -> Gitleaks -> SonarQube -> Trivy -> Checkov -> Docker Registry -> Kubernetes -> Runtime Monitoring
```

## API Platform Stack

Use this when building microservices or AI APIs:

```text
Client -> Nginx or Cloud Load Balancer -> Kong Gateway -> Service APIs -> Observability -> Security Logs
```

## Nginx vs Kong

| Tool | Best For | Learner Notes |
| --- | --- | --- |
| Nginx | Web server, reverse proxy, static files, load balancing, ingress | Start here to understand HTTP routing and reverse proxy basics. |
| Kong Gateway | API gateway, authentication, rate limiting, plugins, AI/API governance | Learn after HTTP basics, especially for microservices and AI APIs. |

## Interview Checkpoints

- Explain CI vs CD.
- Explain reverse proxy vs API gateway.
- Explain Docker image vs container.
- Explain Kubernetes deployment, service, ingress, and config map.
- Explain Terraform state.
- Explain why secrets should not be stored in Git.
- Explain how monitoring differs from observability.

## Validated References

- [Spacelift DevOps tech stack](https://spacelift.io/blog/devops-tech-stack) - practical article about selecting DevOps stack categories.
- [Nginx documentation](https://nginx.org/en/docs/) - official Nginx documentation.
- [Kong Gateway documentation](https://docs.konghq.com/gateway/latest/) - official Kong Gateway documentation route.
- [GitHub Actions documentation](https://docs.github.com/en/actions) - official GitHub Actions docs.
- [GitLab CI/CD documentation](https://docs.gitlab.com/ci/) - official GitLab CI/CD docs.
- [Jenkins documentation](https://www.jenkins.io/doc/) - official Jenkins docs.
