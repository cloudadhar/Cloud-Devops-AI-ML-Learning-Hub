# Collaboration, Artifacts, and Quality Tools

![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white) ![Confluence](https://img.shields.io/badge/Confluence-172B4D?style=for-the-badge&logo=confluence&logoColor=white) ![JFrog](https://img.shields.io/badge/JFrog-41BF47?style=for-the-badge&logo=jfrog&logoColor=white)

## Who This Track Is For

Learners joining enterprise teams where planning, documentation, diagrams, code quality, and artifact repositories are part of daily work.

## Outcomes

- Use Jira for backlog, sprint, incident, and release tracking.
- Use Confluence/draw.io for architecture, runbooks, decision records, and onboarding docs.
- Explain SonarQube, Nexus Repository, and JFrog Artifactory in CI/CD and release governance.


## Architecture Mental Model

```text
Requirement -> Jira issue -> code branch -> CI quality gate -> artifact repository -> release note -> Confluence runbook -> production support
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Learn issue types, workflow states, labels, components, owners, and acceptance criteria.
- Create architecture diagrams and runbook pages for every project.
- Understand artifact repository purpose and why teams do not deploy random build files.

### Days 31-60

- Use SonarQube quality gate and explain maintainability, reliability, security, coverage, duplication, and new-code policy.
- Understand Nexus/Artifactory hosted, proxy, and group repositories.
- Document release checklist and incident runbook.

### Days 61-90

- Design enterprise delivery governance with traceability from Jira issue to commit to artifact to deployment.
- Create architecture decision records and service ownership documentation.
- Add artifact retention, promotion, access control, and audit policy.

## Hands-on Labs

- Create a Jira-style project board in markdown with epics, stories, tasks, and bugs.
- Create a Confluence-style runbook page for an app deployment.
- Add SonarQube scan to pipeline and record quality gate result.
- Design Nexus/Artifactory repository flow for dev, staging, and prod artifacts.

## Scenario-Based Interview Questions

1. A production bug has no linked Jira ticket or release note. How do you restore traceability and prevent repeats?
2. A team uploads artifacts manually to production. What risks does this create and how should a repository manager help?
3. A quality gate blocks release two hours before go-live. How do you decide fix, defer, or rollback?
4. Architecture diagrams are outdated. What ownership and review process keeps docs useful?
5. A new engineer joins. What Confluence/runbook pages must exist for fast onboarding?

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://support.atlassian.com/jira-software-cloud/
- https://support.atlassian.com/confluence-cloud/
- https://docs.sonarsource.com/sonarqube-server
- https://help.sonatype.com/en/sonatype-nexus-repository.html
- https://jfrog.com/help/r/jfrog-artifactory-documentation/artifactory
