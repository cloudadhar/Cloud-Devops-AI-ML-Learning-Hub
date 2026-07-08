# Git and GitHub Zero to Hero Guide

## What It Is

Git is distributed version control. GitHub is a collaboration platform for repositories, pull requests, issues, Actions, packages, security features, and open source contribution.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Git was created by Linus Torvalds in 2005 to support Linux kernel development. GitHub launched in 2008 and popularized pull-request based collaboration, social coding, and repository-hosted automation.

## Architecture and Core Concepts

Core architecture:

```text
Working tree -> Staging area -> Local commits -> Remote repository -> Pull request -> Merge
```

Git concepts:

- Repository, branch, commit, tag, remote, merge, rebase, stash.
- Pull request, code review, branch protection, releases.
- GitHub Actions workflows and repository secrets.

## Zero to Hero Learning Path

1. Learn init, clone, status, add, commit, log.
2. Learn branch, checkout/switch, merge, pull, push.
3. Learn pull requests and review comments.
4. Learn conflict resolution.
5. Learn tags and releases.
6. Learn GitHub Issues and Projects.
7. Learn GitHub Actions basics.
8. Learn branch protection and CODEOWNERS.

## How to Start Using It

Start with a small notes repository:

```bash
git init
git status
git add README.md
git commit -m "Add README"
git branch feature-notes
git push origin main
```

## Common Integrations and Pipeline Usage

GitHub is the trigger point for most DevOps automation:

```text
Push or PR -> GitHub Actions -> Tests -> Docker build -> Security scan -> Deploy
```

Integrates with GitHub Actions, SonarQube, Docker registries, Terraform Cloud, AWS OIDC, Azure federated credentials, GCP workload identity, Jira, Slack, and Argo CD.

## Advanced Topics

- Rebase vs merge workflows.
- Signed commits and branch protection.
- GitHub Actions OIDC cloud authentication.
- Monorepo strategies.
- Release automation and semantic versioning.
- Secret scanning and dependency review.

## Hands-on Project

Create a repo with a protected main branch, a feature branch, a pull request, a GitHub Actions workflow, and a release tag.

## Interview Questions

- What is the difference between Git and GitHub?
- What is a pull request?
- Merge vs rebase?
- How do you resolve a conflict?
- How do you revert a bad commit?
- How do branch protection rules help teams?

## References

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
