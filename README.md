# Cloud DevOps AI/ML Learning Hub

Zero-to-advanced learning repository for students, freshers, and working engineers who want to learn **Cloud, DevOps, DevSecOps, Linux, Networking, AI, ML, MLOps, Agentic AI, Observability, and platform engineering** through roadmaps, notes, tools, projects, interview preparation, and validated references.

Inspired by the broad folder-based style of [Tikam02/DevOps-Guide](https://github.com/Tikam02/DevOps-Guide), but extended for modern Cloud + DevOps + AI/ML learning.

## Start Here

- [Student Start Here](STUDENT_START_HERE.md)
- [Foundation Roadmap](roadmaps/00-foundation-roadmap.md)
- [Cloud & DevOps Roadmap](roadmaps/cloud-devops-roadmap.md)
- [AI / ML / MLOps Roadmap](roadmaps/ai-ml-mlops-roadmap.md)
- [Cybersecurity Roadmap](roadmaps/cybersecurity-roadmap.md)
- [Trending Projects](projects/trending-project-ideas.md)
- [Certification Guidance](certifications/certification-guidance.md)
- [Roadmap Index](ROADMAP_INDEX.md)
- [Technology Stack Maps](stacks/README.md)
- [Hands-on Labs](labs/README.md)


## Detailed Learning System

| Need | Guide |
| --- | --- |
| How to use the repo | [docs/how-to-use-this-repo.md](docs/how-to-use-this-repo.md) |
| Learning method | [docs/learning-method.md](docs/learning-method.md) |
| Zero-to-advanced plan | [docs/zero-to-advanced-study-plan.md](docs/zero-to-advanced-study-plan.md) |
| Weekly practice plan | [docs/weekly-practice-plan.md](docs/weekly-practice-plan.md) |
| Interview preparation | [docs/interview-preparation-guide.md](docs/interview-preparation-guide.md) |
| Portfolio and GitHub guide | [docs/portfolio-github-guide.md](docs/portfolio-github-guide.md) |
| Tool selection | [docs/tool-selection-guide.md](docs/tool-selection-guide.md) |
| URL validation policy | [docs/url-research-validation-policy.md](docs/url-research-validation-policy.md) |
| Contribution workflow | [docs/contribution-workflow.md](docs/contribution-workflow.md) |
| Production readiness | [docs/production-readiness-checklist.md](docs/production-readiness-checklist.md) |
| Troubleshooting method | [docs/troubleshooting-method.md](docs/troubleshooting-method.md) |
| Hands-on labs | [labs/README.md](labs/README.md) |

## Learning Domains

| Domain | Guide |
| --- | --- |
| Linux | [LINUX/README.md](LINUX/README.md) |
| Networking | [Networking/README.md](Networking/README.md) |
| AWS | [AWS/README.md](AWS/README.md) |
| Azure | [Azure/README.md](Azure/README.md) |
| GCP | [GCP/README.md](GCP/README.md) |
| Multi-cloud | [Cloud_providers/README.md](Cloud_providers/README.md) |
| DevOps | [DevOps/README.md](DevOps/README.md) |
| CI/CD | [CI-CD/README.md](CI-CD/README.md) |
| Containers | [Containers/README.md](Containers/README.md) |
| Kubernetes | [Kubernetes/README.md](Kubernetes/README.md) |
| Infrastructure as Code | [Infrastructure-as-Code/README.md](Infrastructure-as-Code/README.md) |
| DevSecOps & Security | [DevSecOps/README.md](DevSecOps/README.md) |
| Security | [Security/README.md](Security/README.md) |
| Observability | [Observability/README.md](Observability/README.md) |
| AI / ML / MLOps | [AI-ML-MLOps/README.md](AI-ML-MLOps/README.md) |
| Agentic AI | [Agentic-AI/README.md](Agentic-AI/README.md) |
| Tools | [Tools/README.md](Tools/README.md) |
| Interview Prep | [Interview/README.md](Interview/README.md) |
| Books & References | [Books/README.md](Books/README.md) |

## Stack Maps

| Stack | Guide |
| --- | --- |
| DevOps Tool Stack | [stacks/devops-tool-stack.md](stacks/devops-tool-stack.md) |
| Cloud Tool Stack | [stacks/cloud-tool-stack.md](stacks/cloud-tool-stack.md) |
| AI / ML / MLOps Tool Stack | [stacks/ai-ml-mlops-tool-stack.md](stacks/ai-ml-mlops-tool-stack.md) |
| Full-Stack Developer Tool Stack | [stacks/full-stack-tool-stack.md](stacks/full-stack-tool-stack.md) |

## Tool Coverage

This repo includes learning tracks for Git, GitHub, GitLab, Jenkins, GitHub Actions, GitLab CI/CD, Docker, Kubernetes, Helm, Terraform, Ansible, Argo CD, Nginx, Kong Gateway, Prometheus, Grafana, OpenTelemetry, SonarQube, Nexus Repository, JFrog Artifactory, Jira, Confluence, draw.io, Trivy, Checkov, Snyk, OWASP, AWS, Azure, GCP, SageMaker, Azure ML, Vertex AI, MLflow, Kubeflow, vector databases, RAG, and agentic AI systems.

## Practical Demo

This repository keeps the existing classroom AWS demo:

```text
VS Code -> GitHub -> GitHub Actions -> Terraform -> AWS EC2 -> User Data -> Live Website
```

See:

- [demo/demo-script.md](demo/demo-script.md)
- [demo/cleanup-guide.md](demo/cleanup-guide.md)
- [terraform/](terraform/)

## Repository Structure

```text
.
├── AWS/ Azure/ GCP/ Cloud_providers/
├── DevOps/ DevSecOps/ Security/
├── CI-CD/ Containers/ Kubernetes/ Infrastructure-as-Code/
├── AI-ML-MLOps/ Agentic-AI/
├── Observability/ LINUX/ Networking/ Tools/
├── Interview/ Books/
├── docs/ stacks/ labs/ roadmaps/ projects/ certifications/
├── demo/ terraform/ logs/
├── logs/url-validation-log.md
├── CONTRIBUTING.md
└── README.md
```

## URL Validation

All major starter links were checked on **2026-07-08** against official documentation or maintained project documentation where possible. See [logs/url-validation-log.md](logs/url-validation-log.md).

Contributors should prefer official documentation, CNCF/project documentation, cloud provider docs, or vendor docs over random blogs. Blog posts are welcome only when they add practical hands-on value.

The repository also includes a pull-request link checker at [.github/workflows/link-check.yml](.github/workflows/link-check.yml).

## Logs and Templates

- [URL Validation Log](logs/url-validation-log.md)
- [Research Notes](logs/research-notes.md)
- [Learning Log Template](logs/learning-log-template.md)
- [Troubleshooting Log Template](logs/troubleshooting-log-template.md)

## Contribution Welcome

This repository is designed for community contribution. Learners can contribute:

- Notes
- Commands
- Diagrams
- Interview questions
- Labs
- Project ideas
- Validated resource links
- Troubleshooting logs
- Cloud cost cleanup steps

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Important Message

Do not learn randomly. Build Linux, networking, Git, cloud, and scripting fundamentals first. Then choose a track, build projects, document everything, and contribute back.
