# Interview Preparation Guide

Interview preparation should happen while you build projects, not after everything is complete.

## Interview Formula

Use this structure for answers:

1. Define the concept.
2. Explain why it exists.
3. Give a real project example.
4. Mention a failure or tradeoff.
5. Mention how to secure or monitor it.

## Core Questions

### Linux

- How do permissions work in Linux?
- What is the difference between a process and a service?
- How do you check logs for a failed service?
- What happens when disk space is full?

### Networking

- What happens when you type a URL in a browser?
- DNS vs IP address?
- HTTP vs HTTPS?
- TCP vs UDP?
- Load balancer vs reverse proxy?

### Git

- Merge vs rebase?
- How do you resolve conflicts?
- What is a pull request?
- How do you revert a bad commit?

### DevOps

- What is CI/CD?
- What are pipeline stages?
- How do you roll back a deployment?
- What is artifact management?
- Why do teams use Infrastructure as Code?

### Nginx and Kong

- What is Nginx used for?
- What is a reverse proxy?
- What is an API gateway?
- Nginx vs Kong Gateway?
- How do you add rate limiting and authentication for APIs?

### Docker and Kubernetes

- Image vs container?
- Dockerfile vs docker-compose?
- Pod vs deployment?
- Service vs ingress?
- ConfigMap vs Secret?
- What is Helm?

### Cloud

- What is IAM?
- What is VPC/VNet?
- Public subnet vs private subnet?
- Security group vs firewall rule?
- How do you avoid cloud cost surprises?

### DevSecOps

- SAST vs DAST?
- What is secret scanning?
- What is container scanning?
- What is OWASP Top 10?
- How do you secure a CI/CD pipeline?

### AI/ML/MLOps

- What is overfitting?
- What is model drift?
- What is experiment tracking?
- What is a model registry?
- What is RAG?
- What is a vector database?
- How do you monitor an AI API?

## Project Story Template

Use this template for every portfolio project:

```text
Problem:
Users:
Architecture:
Tools used:
CI/CD flow:
Security controls:
Monitoring:
Failure faced:
How I fixed it:
What I would improve next:
```

## Mock Interview Routine

- Pick one project.
- Explain it in 2 minutes.
- Draw architecture in 3 minutes.
- Answer 5 troubleshooting questions.
- Answer 3 security questions.
- Answer 2 cost questions.
