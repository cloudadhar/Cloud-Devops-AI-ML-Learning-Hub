# SonarQube Zero to Hero Guide

## What It Is

SonarQube analyzes source code for bugs, code smells, duplications, maintainability issues, and security hotspots.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

SonarQube began as Sonar in the late 2000s and became a common quality gate tool for CI/CD pipelines across many languages.

## Architecture and Core Concepts

Architecture:

```text
Source code -> Scanner -> SonarQube Server -> Quality Gate -> CI/CD decision
```

Key concepts:

- Project, scanner, rules, issues, quality profile, quality gate.
- Bugs, vulnerabilities, code smells, security hotspots, coverage.

## Zero to Hero Learning Path

1. Run SonarQube locally or use SonarCloud.
2. Scan a simple project.
3. Review issues and quality gate.
4. Integrate scan into CI/CD.
5. Fail builds on quality gate failure.
6. Tune quality profiles carefully.
7. Add pull request decoration.
8. Use metrics for continuous improvement.

## How to Start Using It

CI/CD position:

```text
checkout -> build/test -> coverage -> SonarQube scan -> quality gate -> package
```


## Common Integrations and Pipeline Usage

Integrates with GitHub Actions, GitLab CI, Jenkins, Maven, Gradle, npm, Python coverage tools, Azure DevOps, and pull request checks.

## Advanced Topics

- Quality profile customization.
- Pull request decoration.
- Coverage integration.
- Security hotspot review process.
- False positive triage.
- Enterprise portfolio reporting.

## Hands-on Project

Add SonarQube scanning to a sample API project and make CI fail when the quality gate fails.

## Interview Questions

- What is a quality gate?
- What are code smells?
- SAST vs SonarQube code quality?
- How do you handle false positives?
- How do you integrate coverage?

## References

- [SonarQube Server Documentation](https://docs.sonarsource.com/sonarqube-server/)
