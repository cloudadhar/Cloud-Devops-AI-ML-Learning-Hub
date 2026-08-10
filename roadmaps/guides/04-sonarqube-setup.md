# SonarQube - Code Quality & Security Analysis

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [GitHub Integration](#github-integration)
5. [GitLab Integration](#gitlab-integration)
6. [Quality Gates](#quality-gates)
7. [Best Practices](#best-practices)

---

## Introduction

### What is SonarQube?
SonarQube is a static code analysis tool that:
- Detects bugs and security vulnerabilities
- Measures code quality and technical debt
- Identifies code smells
- Tracks code coverage
- Enforces quality standards

### Official Documentation
https://docs.sonarqube.org

**Installation Guides:**
- [SonarQube Server Installation & Upgrade](https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/install-the-server/introduction)
- [SonarQube Documentation](https://docs.sonarsource.com/sonarqube-server/latest/)

### Key Features
- Multi-language support (Java, C#, C++, Python, JavaScript, etc.)
- Security analysis (OWASP, CWE)
- Code duplication detection
- Code coverage integration
- Custom quality gates
- Pull request analysis
- Branch analysis

---

## Installation

### Option 1: Docker (Recommended for Development)

```bash
# Run SonarQube with Docker
docker run -d --name sonarqube \
  -p 9000:9000 \
  -e SONAR_JDBC_URL=jdbc:h2:tcp://localhost:9092/sonar \
  -e SONAR_JDBC_USERNAME=sa \
  -e SONAR_JDBC_PASSWORD= \
  sonarqube:latest

# Access at http://localhost:9000
# Default credentials: admin/admin
```

### Option 2: Docker Compose (With PostgreSQL)

Create `docker-compose.yml`:

```yaml
version: '3.9'

services:
  sonarqube:
    image: sonarqube:latest
    container_name: sonarqube
    ports:
      - "9000:9000"
    environment:
      SONAR_JDBC_URL: jdbc:postgresql://db:5432/sonarqube
      SONAR_JDBC_USERNAME: sonarqube
      SONAR_JDBC_PASSWORD: sonarqube
    depends_on:
      - db
    networks:
      - sonar-network
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_extensions:/opt/sonarqube/extensions
    restart: unless-stopped

  db:
    image: postgres:15-alpine
    container_name: sonarqube-db
    environment:
      POSTGRES_DB: sonarqube
      POSTGRES_USER: sonarqube
      POSTGRES_PASSWORD: sonarqube
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - sonar-network
    restart: unless-stopped

volumes:
  sonarqube_data:
  sonarqube_extensions:
  postgres_data:

networks:
  sonar-network:
    driver: bridge
```

```bash
docker-compose up -d
# Access at http://localhost:9000
```

### Option 3: Standalone Installation (Ubuntu/Debian)

```bash
# Install Java
sudo apt-get update
sudo apt-get install -y openjdk-17-jdk

# Download SonarQube
cd /opt
sudo wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.9.3.79811.zip
sudo unzip sonarqube-9.9.3.79811.zip
sudo mv sonarqube-9.9.3.79811 sonarqube
sudo chown -R sonar:sonar sonarqube

# Create sonar user
sudo useradd -r -s /bin/bash sonar

# Start SonarQube
cd sonarqube
./bin/linux-x86-64/sonar.sh start

# Access at http://localhost:9000
```

---

## Configuration

### Initial Setup

1. Go to http://localhost:9000
2. Login with `admin/admin`
3. Change admin password
4. Create new project

### Create Project

**Via Web UI**:
1. Click "Create project"
2. Enter project key (e.g., `my-company:my-app`)
3. Set project name
4. Set quality gate (optional)
5. Continue

**Via SonarQube Scanner**:

First, generate a token:
1. Go to Administration → Security → Users → admin
2. Generate Token
3. Copy token

### Install SonarQube Scanner

```bash
# macOS
brew install sonar-scanner

# Ubuntu/Debian
sudo apt-get install -y sonar-scanner

# or download manually
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.10.0.2000-linux.zip
unzip sonar-scanner-cli-4.10.0.2000-linux.zip
export PATH=$PATH:/path/to/sonar-scanner/bin
```

### Analyze Project Locally

Create `sonar-project.properties`:

```properties
# Project information
sonar.projectKey=my-company:my-app
sonar.projectName=My Application
sonar.projectVersion=1.0.0

# Source code location
sonar.sources=src
sonar.exclusions=**/node_modules/**,**/dist/**

# Test code
sonar.tests=tests
sonar.test.inclusions=**/*.test.js,**/*.spec.js

# Code coverage (optional)
sonar.javascript.lcov.reportPaths=coverage/lcov.info

# Server details
sonar.host.url=http://localhost:9000
sonar.login=<YOUR_TOKEN>
```

Run analysis:

```bash
# From project root directory
sonar-scanner

# or with explicit parameters
sonar-scanner \
  -Dsonar.projectKey=my-app \
  -Dsonar.sources=src \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=<TOKEN>
```

---

## GitHub Integration

### Method 1: GitHub Actions

Create `.github/workflows/sonarqube.yml`:

```yaml
name: SonarQube Analysis

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  sonarqube:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Full history for better analysis

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Run tests with coverage
        run: npm run test:coverage

      - name: SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@master
        env:
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        with:
          args: >
            -Dsonar.projectKey=my-app
            -Dsonar.projectName=My Application
            -Dsonar.sources=src
            -Dsonar.tests=tests
            -Dsonar.javascript.lcov.reportPaths=coverage/lcov.info

      - name: SonarQube Quality Gate
        uses: SonarSource/sonarqube-quality-gate-action@master
        timeout-minutes: 5
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

### Method 2: GitHub App Integration

1. Go to SonarQube Administration → DevOps Platform Integration
2. Select GitHub
3. Click "Install GitHub App"
4. Follow OAuth flow
5. Configure webhook settings

### Add Secrets to GitHub

1. Go to Repository Settings → Secrets and variables → Actions
2. Add `SONAR_HOST_URL`: `http://your-sonarqube-server:9000`
3. Add `SONAR_TOKEN`: Your SonarQube token

---

## GitLab Integration

### Method 1: GitLab CI/CD

Create `.gitlab-ci.yml`:

```yaml
stages:
  - build
  - test
  - sonarqube

variables:
  SONAR_HOST_URL: ${SONAR_HOST_URL}
  SONAR_TOKEN: ${SONAR_TOKEN}

build:
  stage: build
  image: node:18-alpine
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist

test:
  stage: test
  image: node:18-alpine
  script:
    - npm ci
    - npm run test:coverage
  artifacts:
    paths:
      - coverage
    coverage: '/Lines\s*:\s*(\d+\.\d+)%/'

sonarqube:
  stage: sonarqube
  image: sonarsource/sonar-scanner-cli:latest
  script:
    - sonar-scanner
      -Dsonar.projectKey=${CI_PROJECT_NAME}
      -Dsonar.projectName=${CI_PROJECT_NAME}
      -Dsonar.sources=src
      -Dsonar.tests=tests
      -Dsonar.javascript.lcov.reportPaths=coverage/lcov.info
      -Dsonar.host.url=${SONAR_HOST_URL}
      -Dsonar.login=${SONAR_TOKEN}
  allow_failure: true
```

### Method 2: GitLab Integration

1. Go to SonarQube Administration → DevOps Platform Integration
2. Select GitLab
3. Enter GitLab URL and personal access token
4. Configure webhook settings

### Add GitLab Variables

1. Go to GitLab Repository → Settings → CI/CD → Variables
2. Add `SONAR_HOST_URL`: `http://your-sonarqube-server:9000`
3. Add `SONAR_TOKEN`: Your SonarQube token

---

## Quality Gates

### Create Quality Gate

1. Go to Quality Gates
2. Click "Create"
3. Set name: "Strict"
4. Add conditions:

```
Condition                          | Error Threshold
Reliability Rating                 | A (worst)
Security Rating                    | A
Maintainability Rating             | A
Coverage                           | < 80%
Duplicated Lines (%)               | > 3%
Cyclomatic Complexity              | > 15 (per function)
Cognitive Complexity               | > 25 (per function)
Blocker Issues                     | > 0
Critical Issues                    | > 0
```

### Assign Quality Gate to Project

1. Go to Project → Project Settings
2. Select "Quality Gate"
3. Choose your quality gate (e.g., "Strict")

### Enforce Quality Gate in CI/CD

```yaml
# GitHub Actions
- name: SonarQube Quality Gate
  uses: SonarSource/sonarqube-quality-gate-action@master
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}

# GitLab CI - Built-in
# If SonarQube quality gate fails, CI/CD fails
```

---

## Best Practices

### Code Analysis Configuration

**sonar-project.properties**:
```properties
# Project identification
sonar.projectKey=company:app-name
sonar.projectName=App Name
sonar.projectVersion=${CI_COMMIT_SHA}

# Language-specific
sonar.sources=src
sonar.tests=tests
sonar.exclusions=**/node_modules/**,**/dist/**,**/build/**

# JavaScript/TypeScript
sonar.javascript.lcov.reportPaths=coverage/lcov.info
sonar.typescript.tsconfigPath=tsconfig.json

# Python
sonar.python.coverage.reportPaths=coverage.xml

# Java
sonar.java.binaries=target/classes

# Coverage
sonar.coverage.exclusions=**/*.test.ts,**/*.spec.ts

# Duplications
sonar.cpd.exclusions=**/node_modules/**

# Issues
sonar.issue.ignore.multiline.block1.ruleKey=
sonar.issue.ignore.multiline.block1.pattern=@javax.annotation.Generated
```

### Branch & PR Analysis

```properties
# Analyze specific branches
sonar.branch.name=main
sonar.branch.target=main

# Pull request analysis (GitHub)
sonar.pullrequest.key=${GITHUB_PR_NUMBER}
sonar.pullrequest.branch=${GITHUB_HEAD_REF}
sonar.pullrequest.base=${GITHUB_BASE_REF}
```

### Continuous Integration Best Practices

- ✅ Run analysis on every commit
- ✅ Fail build if quality gate fails
- ✅ Block merging if PR fails quality gate
- ✅ Track metrics trends over time
- ✅ Review technical debt regularly
- ✅ Set realistic quality gate thresholds

### Common Issues & Solutions

**Issue**: "Quality gate failed"
**Solution**: Fix issues reported in SonarQube, or adjust quality gate thresholds

**Issue**: "Cannot connect to SonarQube"
**Solution**: Check SONAR_HOST_URL and SONAR_TOKEN are correct

**Issue**: "Low code coverage"
**Solution**: Increase test coverage, or adjust coverage threshold in quality gate

---

## Useful Commands

```bash
# Analyze specific directory
sonar-scanner -Dsonar.sources=src

# Skip tests during analysis
sonar-scanner -Dsonar.tests=

# Analyze multiple languages
sonar-scanner \
  -Dsonar.sources=src \
  -Dsonar.java.binaries=target/classes \
  -Dsonar.python.coverage.reportPaths=coverage.xml

# Verbose output for debugging
sonar-scanner -X

# Preview mode (doesn't write to database)
sonar-scanner -Dsonar.analysis.mode=preview
```

---

## Official Resources

- **SonarQube Documentation**: https://docs.sonarqube.org
- **SonarQube Rules**: https://rules.sonarsource.com
- **Community Forum**: https://community.sonarsource.com
- **GitHub Actions**: https://github.com/SonarSource/sonarqube-scan-action

---

**Last Updated**: August 2026
**Version**: 1.0
