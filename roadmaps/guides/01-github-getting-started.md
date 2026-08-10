# GitHub Getting Started - Complete Guide

## Table of Contents
1. [Setup & Installation](#setup--installation)
2. [Basic Concepts](#basic-concepts)
3. [Workflow & Branching](#workflow--branching)
4. [Pull Requests & Code Review](#pull-requests--code-review)
5. [GitHub Actions](#github-actions)
6. [Best Practices](#best-practices)

---

## Setup & Installation

### 1. Create GitHub Account
- Go to https://github.com/signup
- Create account with email
- Verify email
- Set up profile picture and bio

### 2. Install Git
```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt-get install git

# Windows
# Download from https://git-scm.com/download/win
```

### 3. Configure Git
```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list

# Optional: Set default editor
git config --global core.editor "vim"

# Optional: Set default branch name
git config --global init.defaultBranch main
```

### 4. Generate SSH Keys (Recommended for Security)
```bash
# Generate SSH key pair
ssh-keygen -t ed25519 -C "your.email@example.com"
# or for older systems:
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Press Enter to accept default location (~/.ssh/id_ed25519)
# Enter a passphrase (optional but recommended)

# Copy public key
cat ~/.ssh/id_ed25519.pub
```

### 5. Add SSH Key to GitHub
- Go to GitHub Settings → SSH and GPG keys
- Click "New SSH key"
- Paste your public key
- Click "Add SSH key"

### 6. Test SSH Connection
```bash
ssh -T git@github.com
# Output: Hi username! You've successfully authenticated...
```

---

## Basic Concepts

### Repository
A repository (repo) is a project folder containing all your code and version history.

```bash
# Clone a repository
git clone git@github.com:username/repo-name.git

# Create a new repository locally
git init

# Add remote origin
git remote add origin git@github.com:username/repo-name.git
```

### Commits
Commits are snapshots of your code at a point in time.

```bash
# Check status
git status

# Stage changes
git add file.js
git add .  # Add all changes

# Commit changes
git commit -m "Add login feature"

# View commit history
git log
git log --oneline
git log --graph --all --decorate
```

### Branches
Branches allow you to work on features independently.

```bash
# List branches
git branch
git branch -a  # All branches including remote

# Create a new branch
git branch feature/login

# Switch to a branch
git checkout feature/login
# or modern syntax:
git switch feature/login

# Create and switch in one command
git checkout -b feature/login

# Delete a branch
git branch -d feature/login
git branch -D feature/login  # Force delete

# Rename a branch
git branch -m old-name new-name
```

---

## Workflow & Branching

### Recommended: GitFlow Branching Strategy

```
main (production)
  ↓
develop (staging)
  ↓
feature/feature-name (development)
```

**Main branch**: Production-ready code, tagged with versions
**Develop branch**: Integration branch, staging environment
**Feature branches**: Individual features, created from develop

### Complete Workflow Example

```bash
# 1. Start from develop branch
git checkout develop
git pull origin develop

# 2. Create feature branch
git checkout -b feature/user-authentication

# 3. Make changes and commit
echo "New code" >> auth.js
git add auth.js
git commit -m "Add user authentication logic"

# 4. Push to remote
git push origin feature/user-authentication

# 5. Create Pull Request on GitHub
# (Continue to Pull Requests section)

# 6. After PR is merged
git checkout develop
git pull origin develop

# 7. Delete local feature branch
git branch -d feature/user-authentication
git push origin --delete feature/user-authentication
```

### Branch Naming Conventions
```
feature/add-login-page
bugfix/fix-memory-leak
hotfix/patch-security-issue
release/v1.2.0
docs/update-readme
refactor/optimize-database-queries
```

---

## Pull Requests & Code Review

### Creating a Pull Request

#### Method 1: Via CLI (GitHub CLI)
```bash
# Install GitHub CLI
# macOS: brew install gh
# Ubuntu: sudo apt install gh

# Authenticate
gh auth login

# Create PR from current branch
gh pr create --title "Add user authentication" --body "Implements login feature"

# View PRs
gh pr list
gh pr view <number>

# Check PR status
gh pr status
```

#### Method 2: Via GitHub Web Interface

1. Push your branch to GitHub
2. Go to repository on GitHub
3. Click "Compare & pull request" button
4. Fill in title and description
5. Select target branch (usually develop)
6. Click "Create pull request"

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests pass locally
```

### Code Review Best Practices

**For Reviewers**:
```bash
# Check out the PR branch locally
git fetch origin pull/<PR_NUMBER>/head:pr-<PR_NUMBER>
git checkout pr-<PR_NUMBER>

# Run tests and review code
npm test
# Review changes
git log --oneline develop..HEAD

# Approve or request changes
# On GitHub: Click "Review changes" → Select "Approve" or "Request changes"
```

**For Authors**:
- Explain the "why" in PR description
- Keep PRs focused on single feature
- Respond to review comments quickly
- Push fixes as new commits (don't force push)
- Rebase if needed before merge: `git rebase develop`

### Merging Strategies

```bash
# Merge commit (default)
git merge --no-ff feature/branch

# Squash commits before merging
git merge --squash feature/branch
git commit

# Rebase and merge (linear history)
git rebase develop
git merge --ff-only
```

---

## GitHub Actions

### Basic Workflow

Create file: `.github/workflows/ci.yml`

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test
      
      - name: Run linter
        run: npm run lint
      
      - name: Build
        run: npm run build
```

### Secrets & Environment Variables

**Add secrets in GitHub**:
- Go to Settings → Secrets and variables → Actions
- Click "New repository secret"
- Add secret name and value

**Use secrets in workflow**:
```yaml
- name: Deploy
  env:
    API_KEY: ${{ secrets.API_KEY }}
    DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
  run: npm run deploy
```

### Conditional Steps

```yaml
- name: Deploy to production
  if: github.ref == 'refs/heads/main'
  run: npm run deploy:prod

- name: Deploy to staging
  if: github.ref == 'refs/heads/develop'
  run: npm run deploy:staging
```

---

## Best Practices

### Commit Messages
```
Format: <type>(<scope>): <subject>

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Code style (formatting, missing semicolons)
- refactor: Code refactoring
- test: Adding tests
- chore: Build, dependencies, tools

Examples:
- feat(auth): add login functionality
- fix(api): handle null response
- docs(readme): update installation steps
- refactor(database): optimize queries
```

### Keep History Clean
```bash
# View what will be pushed
git log origin/develop..HEAD

# Combine multiple commits before pushing
git rebase -i HEAD~3  # Rebase last 3 commits

# Edit, squash, reword commits as needed
```

### Regular Sync with Main Branch
```bash
# Pull latest changes from develop
git fetch origin
git rebase origin/develop
# or
git merge origin/develop
```

### Avoid These Mistakes

❌ **Don't**:
- Commit to main/develop directly
- Force push to shared branches (`git push -f`)
- Commit secrets or credentials
- Leave branches undeleted
- Write vague commit messages

✅ **Do**:
- Create feature branches for each task
- Write descriptive commit messages
- Keep commits atomic and focused
- Delete merged branches
- Use PR reviews before merging

---

## Useful Git Commands

```bash
# View differences
git diff                    # Unstaged changes
git diff --staged          # Staged changes
git diff develop feature   # Between branches

# Undo changes
git restore file.js        # Discard changes to file
git restore --staged file.js  # Unstage file
git revert <commit-id>     # Create new commit that undoes changes
git reset --soft HEAD~1    # Undo last commit, keep changes staged
git reset --hard HEAD~1    # Undo last commit, discard changes

# Search history
git log --grep="bug"       # Search commit messages
git log -S "searchTerm"    # Search code changes
git blame file.js          # See who changed each line

# Stash work in progress
git stash                  # Save changes temporarily
git stash list             # List stashes
git stash pop              # Restore changes
```

---

## GitHub CLI Useful Commands

```bash
# Clone repo
gh repo clone owner/repo

# View repo info
gh repo view
gh repo view --web  # Open in browser

# List issues
gh issue list
gh issue create --title "Bug title" --body "Description"

# List pull requests
gh pr list
gh pr view <number>
gh pr checkout <number>  # Check out PR branch

# Comment on PR
gh pr comment <number> --body "Looks good!"

# Merge PR
gh pr merge <number>

# Watch repo for notifications
gh repo watch
```

---

## Integration with IDE

### VS Code
- Install "GitHub Pull Requests and Issues" extension
- View PRs, issues, branches in sidebar
- Review code without leaving editor
- Auto-complete with GitHub's Copilot

### IntelliJ/WebStorm
- Built-in Git and GitHub integration
- VCS menu has all Git operations
- Built-in GitHub issue tracker

### Terminal (GitKraken or Lazygit)
```bash
# Install lazygit (macOS)
brew install lazygit

# Run
lazygit

# Navigate with arrow keys, follow on-screen prompts
```

---

## Common Workflows

### Feature Development
```bash
git checkout -b feature/new-api
# ... make changes ...
git add .
git commit -m "feat(api): add new endpoint"
git push origin feature/new-api
# Create PR on GitHub
# After review and approval:
git checkout develop
git pull origin develop
git merge feature/new-api
git push origin develop
```

### Bug Fixes
```bash
git checkout -b bugfix/login-crash
# ... fix the bug ...
git add .
git commit -m "fix(auth): handle null user object"
git push origin bugfix/login-crash
# Create PR on GitHub
```

### Hotfixes (Production)
```bash
git checkout main
git checkout -b hotfix/security-patch
# ... fix security issue ...
git add .
git commit -m "fix(security): patch vulnerability"
git push origin hotfix/security-patch
# Create PR to main
# After merge, also merge to develop:
git checkout develop
git merge main
git push origin develop
```

---

## Resources

**Official Documentation**: https://docs.github.com
**Git Documentation**: https://git-scm.com/doc
**GitHub CLI**: https://cli.github.com
**GitHub Guides**: https://guides.github.com

**Additional Tools**:
- GitKraken: https://www.gitkraken.com (GUI)
- GitHub Desktop: https://desktop.github.com (Beginner-friendly GUI)
- Lazygit: https://github.com/jessiduffield/lazygit (Terminal UI)

---

**Last Updated**: August 2026
**Version**: 1.0
