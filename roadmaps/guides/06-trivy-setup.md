# Security Scanning Tools - Trivy, Orca, Mend

## Table of Contents
1. [Trivy - Vulnerability Scanning](#trivy---vulnerability-scanning)
2. [Orca - Cloud Security](#orca---cloud-security)
3. [Mend - Software Composition Analysis](#mend---software-composition-analysis)
4. [Integration in CI/CD](#integration-in-cicd)
5. [Best Practices](#best-practices)

---

## Trivy - Vulnerability Scanning

### Introduction

**What is Trivy?**
- Vulnerability scanner for container images
- Scans for OS package vulnerabilities
- Detects application dependency vulnerabilities
- Scans infrastructure-as-code (Terraform, Kubernetes)
- Finds secrets and misconfigurations
- Fast and reliable

**Official Documentation**: https://aquasecurity.github.io/trivy

### Installation

**macOS**:
```bash
brew install aquasecurity/trivy/trivy
trivy version
```

**Ubuntu/Debian**:
```bash
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo "deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy
```

**Docker**:
```bash
docker run aquasec/trivy --version
```

**Manual**:
```bash
wget https://github.com/aquasecurity/trivy/releases/download/v0.46.0/trivy_0.46.0_Linux-64bit.tar.gz
tar -xzf trivy_0.46.0_Linux-64bit.tar.gz
./trivy --version
```

### Usage

**Scan Container Image**:
```bash
# Scan local image
trivy image myapp:1.0

# Scan public image
trivy image nginx:latest

# Scan with detailed output
trivy image --severity HIGH,CRITICAL myapp:1.0

# Generate report
trivy image --format json --output report.json myapp:1.0
trivy image --format sarif --output report.sarif myapp:1.0
trivy image --format table --output report.txt myapp:1.0
```

**Scan Filesystem**:
```bash
# Scan project directory
trivy fs .

# Scan specific directory
trivy fs ./src

# Scan with severity filter
trivy fs --severity CRITICAL,HIGH .
```

**Scan Infrastructure-as-Code**:
```bash
# Scan Terraform files
trivy config ./terraform/

# Scan Kubernetes manifests
trivy config ./k8s/

# Scan Docker Compose
trivy config docker-compose.yml
```

**Scan for Secrets**:
```bash
# Enable secret scanning
trivy image --secret-config trivy-secret.yaml myapp:1.0

# Scan filesystem for secrets
trivy fs --security-checks secret .
```

**Report Formats**:
```bash
# JSON
trivy image --format json myapp:1.0 > report.json

# SARIF (for GitHub)
trivy image --format sarif myapp:1.0 > report.sarif

# Table
trivy image --format table myapp:1.0

# CycloneDX (SBOM)
trivy image --format cyclonedx myapp:1.0 > sbom.xml
```

### Create Configuration File

Create `trivy.yaml`:

```yaml
# Scan configurations
severity:
  - CRITICAL
  - HIGH
  - MEDIUM

# Skip specific vulnerabilities
skip_files:
  - node_modules
  - vendor

# Exit code on vulnerabilities
exit-code: 1

# Report format
format: json

# Security checks
security-checks:
  - vuln
  - config
  - secret

# Ignore vulnerabilities
ignorefile: .trivyignore
```

Use configuration:

```bash
trivy image --config trivy.yaml myapp:1.0
```

---

## GitHub Actions Integration

Create `.github/workflows/trivy.yml`:

```yaml
name: Trivy Vulnerability Scan

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Build Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: false
          load: true
          tags: myapp:${{ github.sha }}

      - name: Run Trivy scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'

      - name: Upload Trivy results to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v2
        if: always()
        with:
          sarif_file: 'trivy-results.sarif'

      - name: Generate JSON report
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          format: 'json'
          output: 'trivy-results.json'

      - name: Comment PR with results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const results = JSON.parse(fs.readFileSync('trivy-results.json', 'utf8'));
            const vulnerabilities = results.Results?.flatMap(r => r.Misconfigurations || []) || [];
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## Trivy Scan Results\n\nVulnerabilities found: ${vulnerabilities.length}`
            });
```

### GitLab CI Integration

Create `.gitlab-ci.yml`:

```yaml
stages:
  - build
  - scan

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t myapp:${CI_COMMIT_SHA} .
  artifacts:
    reports:
      dotenv: build.env

trivy_scan:
  stage: scan
  image: aquasec/trivy:latest
  script:
    - trivy image --format json --output trivy-report.json myapp:${CI_COMMIT_SHA}
    - trivy image --severity CRITICAL,HIGH myapp:${CI_COMMIT_SHA}
  artifacts:
    reports:
      sast: trivy-report.json
  allow_failure: true
```

---

## Orca - Cloud Security Posture Management

### Introduction

**What is Orca?**
- Cloud security posture management platform
- Monitors cloud misconfigurations
- Detects compliance violations
- Provides risk scoring
- Prioritizes security issues
- Integrates with multiple cloud providers (AWS, Azure, GCP)

**Official Site**: https://orca.security

### Setup

1. Sign up at https://orca.security
2. Connect cloud account (AWS, Azure, GCP)
3. Create API token
4. Configure scanning

### GitHub Actions Integration

Create `.github/workflows/orca-scan.yml`:

```yaml
name: Orca Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  orca-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Orca Scan
        uses: orcasecurity/shiftleft-scan-action@master
        with:
          api_token: ${{ secrets.ORCA_API_TOKEN }}
          project_key: ${{ secrets.ORCA_PROJECT_KEY }}

      - name: Upload results
        uses: orcasecurity/shiftleft-scan-action/reporting@master
        if: always()
        with:
          api_token: ${{ secrets.ORCA_API_TOKEN }}
```

---

## Mend - Software Composition Analysis

### Introduction

**What is Mend (formerly WhiteSource)?**
- Software composition analysis platform
- Scans dependencies for vulnerabilities
- Detects license compliance issues
- Identifies outdated libraries
- Provides remediation recommendations
- Supports multiple package managers

**Official Site**: https://www.mend.io

### Installation

**npm**:
```bash
npm install -g @whitesource/mend

# Scan project
mend scan
```

**Python**:
```bash
pip install mend-cli

# Scan project
mend scan
```

**Docker**:
```bash
docker run whitesourcesoftware/mend-cli \
  --url https://app.whitesourcesoftware.com \
  --apiKey YOUR_API_KEY \
  --productToken YOUR_PRODUCT_TOKEN
```

### GitHub Actions Integration

Create `.github/workflows/mend-scan.yml`:

```yaml
name: Mend Security Scan

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  mend-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Run Mend scan
        uses: whitesource/mend-scan-action@v1
        with:
          apiKey: ${{ secrets.MEND_API_KEY }}
          productToken: ${{ secrets.MEND_PRODUCT_TOKEN }}

      - name: Upload SBOM
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: mend-sbom
          path: mend-report.json
```

---

## Integration in CI/CD

### Complete Security Scanning Pipeline

```yaml
# .github/workflows/complete-security.yml
name: Complete Security Scanning

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      # 1. SAST (Static Analysis)
      - name: Run SonarQube
        uses: SonarSource/sonarqube-scan-action@master
        env:
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}

      # 2. Dependency Scanning
      - name: Mend Dependency Scan
        uses: whitesource/mend-scan-action@v1
        with:
          apiKey: ${{ secrets.MEND_API_KEY }}
          productToken: ${{ secrets.MEND_PRODUCT_TOKEN }}

      # 3. Secret Scanning
      - name: TruffleHog Secret Scan
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          head: HEAD

      # 4. Build Docker Image
      - name: Build Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: false
          load: true
          tags: myapp:${{ github.sha }}

      # 5. Container Scanning
      - name: Trivy Container Scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'

      # 6. Infrastructure Scanning
      - name: Trivy IaC Scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'config'
          scan-ref: './terraform'
          format: 'sarif'
          output: 'trivy-iac-results.sarif'

      # 7. Upload all results
      - name: Upload scan results
        uses: github/codeql-action/upload-sarif@v2
        if: always()
        with:
          sarif_file: |
            trivy-results.sarif
            trivy-iac-results.sarif
```

---

## Best Practices

### Security Scanning Strategy

✅ **Scan at multiple stages**:
1. **Pre-commit**: Local scanning with pre-commit hooks
2. **PR stage**: Scan on pull requests (block if critical)
3. **Build stage**: Scan Docker images before push
4. **Registry stage**: Scan in container registry
5. **Runtime stage**: Continuous monitoring in production

### Ignore Vulnerabilities Safely

Create `.trivyignore`:

```
# CVE-2021-1234
# Reason: Patched in next release
# Expires: 2026-12-31

CVE-2021-1234
CVE-2021-5678
```

### Reporting and Remediation

- ✅ Generate reports in JSON format
- ✅ Integrate with issue tracking
- ✅ Set severity thresholds
- ✅ Track remediation progress
- ✅ Schedule regular scans

### SBOM (Software Bill of Materials)

```bash
# Generate SBOM with Trivy
trivy image --format cyclonedx myapp:1.0 > sbom.xml

# Generate SBOM with Mend
mend scan --outputFormat cyclonedx
```

---

## Official Resources

- **Trivy Docs**: https://aquasecurity.github.io/trivy
- **Trivy GitHub**: https://github.com/aquasecurity/trivy
- **Orca Docs**: https://docs.orca.security
- **Mend Docs**: https://docs.mend.io
- **SBOM Format**: https://cyclonedx.org

---

**Last Updated**: August 2026
**Version**: 1.0
