# DevSecOps Guide

## What DevSecOps Means

DevSecOps integrates security into every stage of software delivery: code, dependencies, containers, infrastructure, cloud, runtime, and incident response.

## Pipeline Security Gates

```text
pre-commit -> SAST -> dependency scan -> secret scan -> IaC scan -> container scan -> deploy policy -> runtime monitoring
```

## Tools

- SonarQube for code quality and security review
- Trivy for containers, filesystems, IaC, and dependencies
- Checkov for IaC scanning
- Gitleaks for secret scanning
- OWASP ZAP for web app testing
- Snyk for dependencies and containers
- GitHub Advanced Security
- GitLab security scanners
- Falco for runtime detection

## Validated References

- [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/) - DevSecOps practices.
- [SonarQube Server documentation](https://docs.sonarsource.com/sonarqube-server/) - code quality and security analysis.
- [GitHub Actions documentation](https://docs.github.com/en/actions) - CI/CD automation surface.
