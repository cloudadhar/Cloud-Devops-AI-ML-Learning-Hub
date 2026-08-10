# Sample CI/CD Pipeline Project - Complete Integration Guide

A comprehensive example project demonstrating real-world CI/CD pipeline with SonarQube, Nexus, Trivy, Orca, Terraform, and AWS integration using both GitHub Actions and GitLab CI/CD.

## 📋 Project Overview

This sample project shows a complete DevOps workflow:
- **Source Code Management**: GitHub/GitLab with proper branching
- **Code Quality**: SonarQube scanning and quality gates
- **Security Scanning**: Trivy (container) + Orca (cloud) + Mend (SCA)
- **Artifact Management**: Nexus Repository for Docker images and packages
- **Infrastructure**: Terraform to provision AWS resources
- **Deployment**: Automated to AWS ECS/EKS

## 🏗️ Project Structure

```
sample-cicd-pipeline-project/
├── .github/workflows/              # GitHub Actions workflows
│   ├── 01-build-test-scan.yml     # Build, test, code quality scan
│   ├── 02-security-scan.yml       # Trivy + Orca + Mend scanning
│   ├── 03-push-artifact.yml       # Push to Nexus Repository
│   └── 04-terraform-deploy.yml    # Terraform workflow for AWS
├── .gitlab-ci.yml                  # GitLab CI/CD pipeline (all-in-one)
├── src/                            # Application source code
│   ├── main.py                    # Python application
│   ├── requirements.txt           # Python dependencies
│   └── tests/                     # Unit tests
├── terraform/                      # Infrastructure as Code
│   ├── main.tf                    # AWS VPC, Security Groups, ECS
│   ├── variables.tf               # Terraform variables
│   ├── outputs.tf                 # Terraform outputs
│   └── backend.tf                 # S3 state management
├── .docker/                        # Docker configuration
│   ├── Dockerfile                 # Multi-stage Docker build
│   └── .dockerignore              # Files to exclude from Docker
├── sonar-project.properties        # SonarQube configuration
├── nexus-publish.sh               # Script to publish to Nexus
└── README.md                       # This file
```

---

## 🚀 Quick Start Guide

### Prerequisites
- GitHub/GitLab account
- AWS account with credentials
- SonarQube instance (cloud or self-hosted)
- Nexus Repository instance
- Trivy installed or use Docker image
- Terraform 1.0+

### Step 1: Clone and Setup Repository

```bash
# Clone the repository
git clone https://github.com/your-org/sample-cicd-pipeline.git
cd sample-cicd-pipeline

# Create feature branch
git checkout -b feature/add-api-endpoint
```

### Step 2: Make Code Changes

```bash
# Edit source code
vim src/main.py

# Run tests locally
python -m pytest src/tests/

# Commit changes
git add .
git commit -m "feat: add new API endpoint for user management"
```

### Step 3: Push to Repository

```bash
# Push to GitHub/GitLab
git push origin feature/add-api-endpoint
```

### Step 4: Automated Pipeline Triggers

Once you push, the CI/CD pipeline automatically:
1. ✅ Builds application
2. ✅ Runs unit tests
3. ✅ Scans code with SonarQube
4. ✅ Scans container with Trivy
5. ✅ Scans with Orca (cloud security)
6. ✅ Scans dependencies with Mend
7. ✅ Pushes image to Nexus
8. ✅ Provisions infrastructure with Terraform
9. ✅ Deploys to AWS

---

## 📚 Tool Integration Details

### 1. SonarQube Integration

**Why SonarQube?**
- Detects bugs before production
- Ensures code quality standards
- Security vulnerability detection
- Technical debt tracking
- Enforces quality gates (must pass before merge)

**How It Works:**
- Scans your code during CI/CD
- Reports issues with severity levels
- Blocks PRs if quality gates fail
- Tracks metrics over time

**Configuration:** `sonar-project.properties`
```properties
sonar.projectKey=sample-cicd-project
sonar.projectName=Sample CI/CD Project
sonar.sources=src
sonar.exclusions=src/tests/**
sonar.python.coverage.reportPaths=coverage.xml
sonar.qualitygate.wait=true
```

**GitHub Integration:**
- Runs on every PR and commit
- Comments on PRs with findings
- Blocks merge if quality gate fails

**GitLab Integration:**
- Integrates with GitLab CI pipeline
- Shows results in merge requests
- Quality gates block merge

---

### 2. Nexus Repository Integration

**Why Nexus?**
- Centralized artifact management
- Caches dependencies (faster builds)
- Stores your Docker images
- Manages multiple package formats
- Access control and permissions

**How It Works:**
1. Build creates Docker image
2. Image scanned by Trivy
3. Clean image pushed to Nexus
4. Nexus stores all versions
5. Can be deployed from Nexus registry

**Configuration:**
```bash
# Login to Nexus registry
docker login registry.nexus.company.com

# Tag image
docker tag myapp:1.0 registry.nexus.company.com/myapp:1.0

# Push to Nexus
docker push registry.nexus.company.com/myapp:1.0

# Pull for deployment
docker pull registry.nexus.company.com/myapp:1.0
```

**Nexus Formats Supported:**
- Docker images
- npm packages
- Maven artifacts (JAR, WAR)
- Python packages
- Ruby gems
- Raw files

---

### 3. Trivy Container Scanning

**Why Trivy?**
- Scans Docker images for vulnerabilities
- Fast and lightweight
- Finds OS package vulnerabilities
- Application dependency vulnerabilities
- Can be integrated into CI/CD pipeline

**How It Works:**
1. After Docker build, Trivy scans image
2. Checks against CVE databases
3. Reports vulnerabilities with severity
4. Can fail build if critical vulns found

**Command:**
```bash
# Scan Docker image
trivy image myapp:1.0

# Output in JSON
trivy image --format json --output results.json myapp:1.0

# Fail on critical vulnerabilities
trivy image --severity CRITICAL --exit-code 1 myapp:1.0
```

**GitHub Actions Example:**
```yaml
- name: Run Trivy vulnerability scan
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: myapp:1.0
    format: 'sarif'
    output: 'trivy-results.sarif'

- name: Upload Trivy results to GitHub Security tab
  uses: github/codeql-action/upload-sarif@v2
  with:
    sarif_file: 'trivy-results.sarif'
```

---

### 4. Orca Cloud Security Scanning

**Why Orca?**
- Scans cloud infrastructure for misconfigurations
- Detects overly permissive security groups
- Finds exposed databases
- Identifies compliance violations
- Cloud-native security

**How It Works:**
1. Scans deployed infrastructure
2. Checks AWS/Azure/GCP configurations
3. Identifies security misconfigurations
4. Reports compliance issues
5. Suggests remediation

**Command:**
```bash
# Scan AWS account
orca scan --cloud-provider aws --region us-east-1

# Scan specific service
orca scan --resource-type ec2,s3,rds
```

**Integration in Pipeline:**
```bash
# After Terraform deployment, scan infrastructure
orca scan \
  --project-name sample-cicd-project \
  --format json \
  --exit-code 1  # Fail if critical issues found
```

---

### 5. Mend (formerly WhiteSource) SCA

**Why Mend?**
- Scans open source dependencies
- Finds vulnerable packages
- Checks licenses for compliance
- Continuous monitoring
- Automatic updates

**How It Works:**
1. Analyzes package.json, requirements.txt, pom.xml
2. Checks against CVE databases
3. Identifies license compliance issues
4. Recommends updates

**Command:**
```bash
# Install Mend CLI
npm install -g mend

# Scan project
mend scan --project ./

# Generate report
mend report --format json
```

---

### 6. Terraform Workflow for AWS

**Why Terraform?**
- Infrastructure as Code (reproducible)
- Version controlled infrastructure
- Easy to scale and replicate
- Document everything
- Rollback capability

**AWS Resources Provisioned:**
- VPC with subnets (networking)
- Security Groups (firewall rules)
- ECR Registry (Docker image repository)
- ECS Cluster (container orchestration)
- RDS Database (MySQL/PostgreSQL)
- Load Balancer (distribute traffic)
- IAM Roles (access control)

**Terraform Files:**

**main.tf** - Main infrastructure:
```hcl
# Create VPC
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  tags = { Name = "sample-vpc" }
}

# Create subnets
resource "aws_subnet" "public" {
  vpc_id = aws_vpc.main.id
  cidr_block = var.public_subnet_cidr
  availability_zone = data.aws_availability_zones.available.names[0]
}

# Create ECS cluster
resource "aws_ecs_cluster" "main" {
  name = "sample-cluster"
}

# Create RDS database
resource "aws_db_instance" "main" {
  allocated_storage = 20
  engine = "mysql"
  instance_class = "db.t3.micro"
  username = var.db_username
  password = var.db_password
}
```

**Workflow:**
```bash
# 1. Initialize Terraform
terraform init

# 2. Plan changes
terraform plan -out=tfplan

# 3. Apply changes
terraform apply tfplan

# 4. Get outputs (database URL, load balancer IP, etc.)
terraform output

# 5. For rollback
terraform destroy
```

---

## 🔄 Complete Pipeline Examples

### GitHub Actions Pipeline

See `.github/workflows/` for complete examples:
1. **01-build-test-scan.yml** - Build, test, SonarQube
2. **02-security-scan.yml** - Trivy, Orca, Mend
3. **03-push-artifact.yml** - Push to Nexus
4. **04-terraform-deploy.yml** - Terraform deploy to AWS

**How to Use:**
1. Copy `.github/workflows/*.yml` files to your repo
2. Configure secrets in GitHub:
   - `SONAR_TOKEN` - From SonarQube
   - `NEXUS_USERNAME` / `NEXUS_PASSWORD`
   - `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`
   - `ORCA_PROJECT_KEY` - From Orca
3. Push code → Pipeline runs automatically

### GitLab CI Pipeline

See `.gitlab-ci.yml` for complete example with all stages:
1. **build** - Compile/build application
2. **test** - Run unit tests
3. **sonarqube** - Code quality scan
4. **security** - Trivy, Orca, Mend scans
5. **push_artifact** - Push to Nexus
6. **terraform_plan** - Plan infrastructure
7. **terraform_apply** - Deploy to AWS
8. **deploy** - Deploy to ECS/EKS

**How to Use:**
1. Copy `.gitlab-ci.yml` to root of repo
2. Configure CI/CD variables in GitLab:
   - `SONAR_TOKEN`
   - `NEXUS_USERNAME` / `NEXUS_PASSWORD`
   - `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`
3. Commit → Pipeline auto-runs

---

## 🔐 Secrets and Configuration

### GitHub Secrets Setup

```bash
# Add to GitHub repo > Settings > Secrets and variables > Actions

SONAR_HOST_URL=https://sonarqube.company.com
SONAR_TOKEN=squ_xxxxxxxxxxxx

NEXUS_REGISTRY=registry.nexus.company.com
NEXUS_USERNAME=admin
NEXUS_PASSWORD=nexus_password

AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_REGION=us-east-1

ORCA_PROJECT_KEY=orca_project_key
MEND_API_KEY=mend_api_key
```

### GitLab CI Variables

```bash
# Settings > CI/CD > Variables

SONAR_HOST_URL=https://sonarqube.company.com
SONAR_TOKEN=squ_xxxxxxxxxxxx (protected, masked)

NEXUS_REGISTRY=registry.nexus.company.com
NEXUS_USERNAME=admin (protected, masked)
NEXUS_PASSWORD=password (protected, masked)

AWS_ACCESS_KEY_ID=xxx (protected, masked)
AWS_SECRET_ACCESS_KEY=xxx (protected, masked)

TF_VAR_aws_region=us-east-1
TF_VAR_app_name=sample-app
```

---

## 📊 Pipeline Flow Diagram

```
Code Push
   ↓
[GitHub/GitLab] → Triggers CI/CD
   ↓
[Build] → Compile application
   ↓
[Test] → Run unit tests (pytest, Jest, etc.)
   ↓
[SonarQube] → Code quality scan & quality gate
   ↓
[Docker Build] → Create container image
   ↓
[Trivy Scan] → Scan image for vulnerabilities
   ↓
[Orca Scan] → Cloud security scan (if deployed)
   ↓
[Mend Scan] → SCA for dependencies
   ↓
[Nexus Push] → Push image to registry
   ↓
[Terraform Plan] → Plan AWS infrastructure
   ↓
[Terraform Apply] → Provision AWS resources
   ↓
[Deploy] → Deploy to ECS/EKS
   ↓
[Smoke Tests] → Quick verification tests
   ↓
✅ Complete - Live in AWS
```

---

## 🛠️ Common Commands

### Git Workflow
```bash
# Clone repository
git clone https://github.com/org/repo.git
cd repo

# Create feature branch
git checkout -b feature/feature-name

# Make changes
git add .

# Commit with conventional commit
git commit -m "feat: add new feature"
git commit -m "fix: resolve bug"
git commit -m "docs: update README"

# Push to origin
git push origin feature/feature-name

# Create Pull Request (GitHub) or Merge Request (GitLab)
# GitHub: GitHub UI or `gh pr create`
# GitLab: GitLab UI or `glab mr create`

# After approval, merge
git checkout main
git pull
git merge feature/feature-name
git push origin main
```

### Docker Commands
```bash
# Build image
docker build -f .docker/Dockerfile -t myapp:1.0 .

# Test image locally
docker run -p 8080:8080 myapp:1.0

# Tag for registry
docker tag myapp:1.0 registry.nexus.com/myapp:1.0

# Push to Nexus
docker push registry.nexus.com/myapp:1.0

# Pull from Nexus
docker pull registry.nexus.com/myapp:1.0
```

### Terraform Commands
```bash
# Initialize working directory
terraform init

# Format HCL files
terraform fmt -recursive

# Validate configuration
terraform validate

# Plan changes
terraform plan -out=tfplan

# Apply changes
terraform apply tfplan

# Show state
terraform show

# Output values
terraform output

# Destroy resources
terraform destroy -auto-approve
```

### SonarQube Scanner
```bash
# Scan with SonarQube
sonar-scanner \
  -Dsonar.projectKey=sample-cicd-project \
  -Dsonar.sources=src \
  -Dsonar.host.url=https://sonarqube.company.com \
  -Dsonar.login=squ_xxxxxxxxxxxx

# Or with Maven
mvn clean verify sonar:sonar \
  -Dsonar.projectKey=sample-cicd-project \
  -Dsonar.host.url=https://sonarqube.company.com \
  -Dsonar.login=squ_xxxxxxxxxxxx
```

### Trivy Scanning
```bash
# Scan image
trivy image myapp:1.0

# Scan filesystem
trivy fs ./src

# Export to JSON
trivy image --format json --output results.json myapp:1.0

# Fail on HIGH severity
trivy image --severity HIGH --exit-code 1 myapp:1.0
```

---

## 🔍 Troubleshooting

### SonarQube Issues
- **Quality gate fails**: Check sonar-project.properties, increase coverage, fix critical issues
- **No token**: Create token in SonarQube UI (My Account > Security > Tokens)
- **Connection timeout**: Verify SonarQube URL, network connectivity

### Nexus Issues
- **Login fails**: Verify credentials, check realm (Docker Realm enabled?)
- **Push fails**: Check image name format, verify push permissions
- **Pull fails**: Check repository URL, verify network access

### Terraform Issues
- **State lock**: Remove lock file: `rm .terraform.tfstate.lock.hcl`
- **API limits**: Add delay between resources with `depends_on`
- **AWS auth fails**: Verify AWS credentials, check IAM permissions

### Trivy Issues
- **DB update fails**: Offline mode: `trivy image --skip-db-update myapp:1.0`
- **Timeout**: Increase timeout: `--timeout 10m`

---

## 📖 Next Steps

1. **Customize for your project**:
   - Update `sonar-project.properties`
   - Modify Terraform variables
   - Add your application code

2. **Set up monitoring**:
   - Add Prometheus + Grafana
   - Monitor pipeline metrics
   - Alert on failures

3. **Add more stages**:
   - Performance testing
   - Load testing
   - Blue-green deployments

4. **Scale to multiple environments**:
   - Dev environment
   - Staging environment
   - Production environment

---

## 📚 References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci)
- [SonarQube Documentation](https://docs.sonarqube.org)
- [Nexus Documentation](https://help.sonatype.com/repomanager3)
- [Trivy Documentation](https://aquasecurity.github.io/trivy)
- [Orca Documentation](https://docs.orca.security)
- [Terraform Documentation](https://www.terraform.io/docs)
- [AWS Documentation](https://docs.aws.amazon.com)

---

## 💡 Tips & Best Practices

1. **Always use branches** - Never commit directly to main
2. **Require code review** - Enforce PR/MR reviews before merge
3. **Use quality gates** - SonarQube gates block bad code
4. **Monitor vulnerabilities** - Regular Trivy/Orca scans essential
5. **Keep Terraform state** - Store in S3 with remote backend
6. **Automate everything** - Manual steps = human errors
7. **Use semantic versioning** - v1.2.3 format
8. **Document changes** - Keep CHANGELOG.md updated
9. **Test in staging** - Never test directly in production
10. **Rollback plan** - Know how to revert if needed

