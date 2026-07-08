# DevSecOps and Security

![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white) ![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white) ![OPA](https://img.shields.io/badge/OPA-Policy%20as%20Code-7D9199?style=for-the-badge)

## Who This Track Is For

Learners targeting DevSecOps, application security, cloud security, platform security, and secure CI/CD roles.

## Outcomes

- Add security checks before commit, during CI, before deploy, and after release.
- Explain SAST, SCA, secrets scanning, IaC scanning, container scanning, DAST, policy as code, and SBOM.
- Design a secure pipeline with least privilege and useful vulnerability management.


## Architecture Mental Model

```text
Developer -> pre-commit -> SAST/SCA/secrets -> build -> image scan -> IaC policy -> deploy approval -> runtime monitoring -> vulnerability backlog
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Learn OWASP Top 10, secrets handling, dependency risk, and secure Git workflow.
- Add secret scanning and dependency review to a sample repo.
- Understand severity, exploitability, reachability, and false positives.

### Days 31-60

- Add SonarQube, Trivy, Checkov, and dependency scanning gates to CI.
- Create vulnerability triage rules: block, warn, defer with owner and date.
- Learn OIDC and least privilege for cloud deployments.

### Days 61-90

- Create policy as code for Terraform/Kubernetes with OPA or equivalent.
- Design an SBOM and artifact signing workflow.
- Build a DevSecOps dashboard with findings, risk owners, and remediation SLA.

## Hands-on Labs

- Add SAST and quality gate to a pipeline.
- Scan a Docker image and fix high-risk base image vulnerabilities.
- Write a policy that blocks public cloud storage or privileged Kubernetes pods.
- Create a secrets incident response runbook.

## Scenario-Based Interview Questions

1. A scanner reports 80 vulnerabilities. How do you prioritize without blocking all delivery blindly?
2. A developer hardcoded a cloud key. What are the rotation, audit, prevention, and education steps?
3. A container image has critical CVEs but the app must ship today. How do risk acceptance, compensating controls, and approvals work?
4. A Terraform plan opens SSH to the world. Where should policy block it and how should the developer fix it?
5. A quality gate fails for duplicated code and security issues. How do you explain gate policy to developers without making security the enemy?

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://owasp.org/www-project-devsecops-guideline/latest/
- https://docs.sonarsource.com/sonarqube-server
- https://www.openpolicyagent.org/docs
- https://docs.github.com/en/code-security/getting-started/github-security-features
