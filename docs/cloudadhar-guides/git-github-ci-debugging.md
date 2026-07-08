# Git, GitHub, and CI Debugging Detailed Guide

This guide covers Git, GitHub collaboration, pull requests, and CI troubleshooting resources from the CloudAdhar list.

## 1. Fix Failing GitHub PR CI

Reference: How to Fix Failing GitHub PR CI: Lint and Build Errors

### Learning Goal

Learn a systematic way to debug pull request checks instead of randomly changing files until CI passes.

### Step-by-Step Learner Flow

1. Open the failing pull request.
2. Identify which check failed: lint, test, build, typecheck, security scan, or deploy preview.
3. Open the failed job log.
4. Find the first real error, not only the final failure message.
5. Reproduce the same command locally.
6. Fix the smallest cause.
7. Run the relevant local command again.
8. Commit the fix.
9. Push and wait for CI.
10. Write a short note explaining the root cause.

### Practice Lab

Create intentional failures in a sample repo:

- Formatting issue
- Lint rule violation
- Test failure
- Build failure
- Missing environment variable

Fix each one and write a troubleshooting log.

### Deliverables

- CI failure runbook
- Five failure examples
- Root cause notes
- Fixed pull request
- Before and after CI screenshots

### Interview Questions

1. Why should you inspect the first real error?
2. How do you reproduce CI locally?
3. What is the difference between lint and build failure?
4. Why should CI logs be readable?
5. What should a good PR fix summary include?

## 2. Git And GitHub Crash Course For Beginners

Reference: Git and GitHub Crash Course for Beginners

### Learning Goal

Understand the basic workflow for tracking code, collaborating, and publishing work on GitHub.

### Step-by-Step Learner Flow

1. Install Git.
2. Configure username and email.
3. Create or clone a repository.
4. Check status before every change.
5. Stage selected files.
6. Commit with a clear message.
7. Create a branch for new work.
8. Push branch to GitHub.
9. Open a pull request.
10. Review, merge, and sync local main branch.

### Practice Lab

Build a Git practice repo:

- Add a README
- Create two branches
- Make commits
- Open one pull request
- Resolve a simple conflict
- Add a tag

### Deliverables

- Git command cheat sheet
- GitHub repo link
- PR screenshot
- Conflict resolution notes
- Commit history screenshot

### Interview Questions

1. What is the difference between Git and GitHub?
2. What does `git status` show?
3. What is a branch?
4. What is a pull request?
5. How do you resolve a merge conflict?

## 3. Git And GitHub Beginner-Friendly Handbook

Reference: Learn How to Use Git and GitHub: A Beginner-Friendly Handbook

### Learning Goal

Go beyond basic commands and understand how Git helps teams collaborate safely.

### Step-by-Step Learner Flow

1. Learn repository, commit, branch, remote, and merge concepts.
2. Practice local commits before pushing.
3. Use branches for every change.
4. Pull latest changes before starting work.
5. Open pull requests for review.
6. Use meaningful commit messages.
7. Learn revert vs reset at a high level.
8. Learn `.gitignore` for generated files and secrets.
9. Practice resolving conflicts.
10. Document your team workflow.

### Practice Lab

Create a team simulation with two folders or two clones:

- Developer A edits one file
- Developer B edits same file
- Push changes
- Resolve conflict
- Merge through pull request

### Deliverables

- Beginner Git handbook notes
- Command examples
- Team workflow diagram
- `.gitignore` example
- Conflict resolution proof

### Interview Questions

1. Why should generated files be ignored?
2. What is a remote?
3. What is the difference between fetch and pull?
4. Why should teams use pull requests?
5. When would you use revert?
