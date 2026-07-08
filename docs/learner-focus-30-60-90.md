# 30-60-90 Day Learner Focus Plan

This plan helps learners avoid random learning.

## First 30 Days: Foundation

Focus:

- Linux basics
- Networking basics
- Git and GitHub
- One programming language: Python or JavaScript
- Basic cloud concepts

Deliverables:

- Linux command notes
- GitHub profile README
- One static website
- One simple API
- One learning log

Interview readiness:

- Explain DNS, HTTP, Git branch, Linux permissions, process, service, and cloud service models.

## Days 31-60: DevOps and Cloud Projects

Focus:

- GitHub Actions or GitLab CI/CD
- Docker
- Nginx
- Terraform
- AWS/Azure/GCP basics
- Monitoring basics

Deliverables:

- CI/CD pipeline
- Dockerized API
- Nginx reverse proxy setup
- Terraform VM deployment
- Cleanup guide

Interview readiness:

- Explain CI/CD, Docker image vs container, reverse proxy, Terraform state, IAM, VPC/VNet, security groups, and cost cleanup.

## Days 61-90: Advanced Track

Choose one track.

### Cloud DevOps Track

- Kubernetes
- Helm
- Argo CD
- Prometheus and Grafana
- Kong Gateway
- DevSecOps scans

Project:

```text
GitHub -> CI/CD -> Docker -> Registry -> Kubernetes -> Nginx/Kong -> Prometheus/Grafana -> Security scan
```

### AI / MLOps Track

- FastAPI model serving
- MLflow
- Docker
- RAG basics
- Vector database
- Evaluation and monitoring

Project:

```text
Documents -> Embeddings -> Vector DB -> RAG API -> Kong/Nginx -> Logs/Evaluation
```

Starter build: [Private RAG Q&A AI Agent](../projects/private-rag-qa-agent/README.md)

### DevSecOps Track

- Secret scanning
- SAST
- Container scanning
- IaC scanning
- API gateway security
- Incident response

Project:

```text
PR -> Secret scan -> SAST -> Tests -> Docker build -> Image scan -> IaC scan -> Deploy approval
```

## Weekly Rule

Every week produce:

- One note
- One lab
- One troubleshooting log
- Five interview questions
- One GitHub commit
