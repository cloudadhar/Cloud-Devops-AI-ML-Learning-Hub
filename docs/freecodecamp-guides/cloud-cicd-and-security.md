# Cloud CI/CD and Security Detailed Guide

This guide covers Azure DevOps, AWS, GitHub Actions, GitLab CI, OIDC, RBAC, feature flags, Cloudflare deployment, production pipelines, and homelab references from the freeCodeCamp list.

## 1. Azure Repositories At Scale

Reference: [How to Organize and Maintain Azure Repositories at Scale](https://www.freecodecamp.org/news/how-to-organize-and-maintain-azure-repositories-at-scale/)

### Learning Goal

Learn how teams organize many repositories with consistent naming, access control, branch policies, ownership, and maintenance standards.

### Step-by-Step Learner Flow

1. Define repository naming conventions.
2. Decide monorepo vs multirepo boundaries.
3. Create branch rules for main, release, feature, and hotfix branches.
4. Add required reviewers and build validation.
5. Define permissions by team and role.
6. Add templates for README, pull requests, and issues.
7. Add repository maintenance checks.
8. Document archive and cleanup rules.

### Practice Lab

Design an Azure DevOps repo governance template for a company with application, platform, infrastructure, and security teams.

### Deliverables

- Repo naming standard
- Branch policy table
- Permissions matrix
- PR template
- Maintenance checklist

### Interview Questions

1. Why do large teams need repository standards?
2. What is a branch policy?
3. How do required reviewers reduce risk?
4. When would you choose monorepo vs multirepo?
5. What should be included in a repository README?

## 2. Azure DevOps CI/CD For Enterprise .NET Applications

Reference: [Cloud Native Development with Azure DevOps CI/CD Pipelines in Enterprise .NET Applications](https://www.freecodecamp.org/news/cloud-native-development-with-azure-devops-ci-cd-pipelines-in-enterprise-net-applications/)

### Learning Goal

Understand an enterprise-style pipeline for building, testing, containerizing, scanning, and deploying cloud-native applications with Azure DevOps.

### Step-by-Step Learner Flow

1. Create repository structure for application and pipeline files.
2. Add build stage for restore, compile, and unit tests.
3. Add code quality and security checks.
4. Build a container image.
5. Push the image to a registry.
6. Deploy to an environment such as AKS or app service.
7. Add approvals for higher environments.
8. Add monitoring, rollback, and release notes.

### Practice Lab

Write an Azure pipeline design for:

```text
Commit -> Build -> Test -> Scan -> Docker Build -> Registry -> Deploy -> Smoke Test
```

### Deliverables

- Pipeline stage diagram
- Example YAML skeleton
- Environment approval policy
- Rollback plan
- Observability checklist

### Interview Questions

1. What is a pipeline stage?
2. Why separate build and deploy stages?
3. Why scan container images?
4. What is an environment approval?
5. How would you rollback a bad deployment?

## 3. Production-Ready DevOps Pipeline With Free Tools

Reference: [How to Build a Production-Ready DevOps Pipeline with Free Tools](https://www.freecodecamp.org/news/how-to-build-a-production-ready-devops-pipeline-with-free-tools/)

### Learning Goal

Combine free or open tools into a pipeline that behaves like a real production delivery system.

### Step-by-Step Learner Flow

1. Pick a sample app.
2. Add source control and pull request workflow.
3. Add linting and automated tests.
4. Add secret scanning.
5. Add dependency scanning.
6. Build a Docker image.
7. Scan the image.
8. Deploy to a test environment.
9. Run smoke tests.
10. Add rollback and release notes.

### Practice Lab

Build a GitHub Actions pipeline using:

- Lint
- Tests
- Dependency scan
- Docker build
- Container scan
- Deployment
- Smoke test

### Deliverables

- `.github/workflows/` pipeline
- Pipeline diagram
- Security scan output
- Deployment URL
- Rollback notes

### Interview Questions

1. What makes a pipeline production-ready?
2. Why should scans run before deployment?
3. What is a smoke test?
4. What is the difference between CI and CD?
5. How do you handle a failed production deployment?

## 4. Feature Flags And RBAC In DevOps

Reference: [Feature Flags and Role-Based Access Control in DevOps](https://www.freecodecamp.org/news/feature-flags-and-role-based-access-control-devops/#heading-why-is-rbac-important)

### Learning Goal

Understand how feature flags reduce release risk and how RBAC ensures only the right users can perform sensitive operations.

### Step-by-Step Learner Flow

1. Identify a feature that should be released gradually.
2. Add a feature flag check around the feature.
3. Define rollout rules by user, role, percentage, or environment.
4. Define RBAC roles such as viewer, developer, operator, admin, and auditor.
5. Map permissions to actions.
6. Add audit logs for flag and permission changes.
7. Add rollback rules for bad releases.
8. Test unauthorized access.

### Practice Lab

Create a small app with:

- Admin-only feature flag management
- Role-based dashboard access
- Audit log of changes
- Rollback toggle

### Deliverables

- RBAC matrix
- Feature flag rollout plan
- Audit log example
- Test cases
- Security notes

### Interview Questions

1. Why use feature flags?
2. What is RBAC?
3. Why are audit logs important?
4. How do feature flags help rollback?
5. What is the risk of giving everyone admin access?

## 5. AWS Basics For DevOps

Reference: [AWS Basics for DevOps](https://www.freecodecamp.org/news/aws-basics-for-devops/)

### Learning Goal

Learn basic AWS operations that every DevOps learner should know before building larger cloud deployments.

### Step-by-Step Learner Flow

1. Understand account security and MFA.
2. Learn IAM user, group, role, and policy basics.
3. Launch a temporary EC2 instance.
4. Configure security group rules carefully.
5. Connect with SSH.
6. Install packages such as Nginx or Docker.
7. Check system logs and service status.
8. Stop or terminate resources after practice.
9. Estimate cost and document cleanup.

### Practice Lab

Deploy a static Nginx page on EC2:

- SSH into instance
- Install Nginx
- Open only required inbound rules
- Verify in browser
- Capture logs
- Terminate resource

### Deliverables

- AWS setup notes
- IAM and security group explanation
- EC2 command log
- Cleanup proof
- Cost awareness note

### Interview Questions

1. What is IAM?
2. What is a security group?
3. Why should SSH not be open to the world?
4. What is the difference between stop and terminate?
5. How do you avoid surprise cloud cost?

## 6. Local DevOps Homelab With Docker, Kubernetes, And Ansible

Reference: [How to Build a Local DevOps Homelab with Docker, Kubernetes, and Ansible](https://www.freecodecamp.org/news/how-to-build-a-local-devops-homelab-with-docker-kubernetes-and-ansible/)

### Learning Goal

Build a local environment where learners can practice infrastructure, containers, orchestration, configuration management, and troubleshooting without cloud cost.

### Step-by-Step Learner Flow

1. Decide laptop resource limits.
2. Install Docker.
3. Create containers for sample services.
4. Install a local Kubernetes option such as kind, minikube, or k3d.
5. Deploy a simple app to the cluster.
6. Add Ansible for repeatable setup tasks.
7. Add monitoring basics.
8. Write teardown commands.
9. Document every failure and fix.

### Practice Lab

Build a local homelab:

```text
Laptop -> Docker -> kind/minikube -> sample app -> Ansible setup -> logs
```

### Deliverables

- Homelab architecture diagram
- Setup commands
- Ansible playbook
- Kubernetes manifests
- Troubleshooting log
- Cleanup instructions

### Interview Questions

1. Why build a homelab?
2. What is the difference between Docker and Kubernetes?
3. What does Ansible automate?
4. How do you clean up local clusters?
5. How does a homelab help with interviews?

## 7. DevOps With GitLab CI Course

Reference: [DevOps with GitLab CI Course](https://www.freecodecamp.org/news/devops-with-gitlab-ci-course/)

### Learning Goal

Learn GitLab CI pipeline concepts and compare them with GitHub Actions and Jenkins.

### Step-by-Step Learner Flow

1. Create a GitLab project.
2. Add `.gitlab-ci.yml`.
3. Define stages such as build, test, package, deploy.
4. Add jobs and runners.
5. Store secrets as CI variables.
6. Add artifacts and reports.
7. Add manual approvals.
8. Compare the same flow in GitHub Actions.

### Practice Lab

Create the same pipeline in GitLab CI and GitHub Actions:

- Install dependencies
- Run tests
- Build Docker image
- Deploy to test environment

### Deliverables

- `.gitlab-ci.yml`
- GitHub Actions comparison
- Pipeline screenshots
- Secret handling notes
- Runner explanation

### Interview Questions

1. What is a GitLab runner?
2. What is a CI stage?
3. How are artifacts used?
4. How do GitLab CI and GitHub Actions differ?
5. Where should secrets be stored?

## 8. Next.js On Cloudflare Workers With GitHub Actions

Reference: [How to Deploy a Full-Stack Next.js App on Cloudflare Workers with GitHub Actions CI/CD](https://www.freecodecamp.org/news/how-to-deploy-a-full-stack-next-js-app-on-cloudflare-workers-with-github-actions-ci-cd/)

### Learning Goal

Deploy a full-stack web app to an edge platform using GitHub Actions.

### Step-by-Step Learner Flow

1. Create a Next.js app.
2. Configure the app for the target runtime.
3. Add local build and preview commands.
4. Create Cloudflare project configuration.
5. Store deployment credentials as GitHub secrets.
6. Add GitHub Actions workflow.
7. Deploy preview and production versions.
8. Verify routes, environment variables, and logs.
9. Document rollback.

### Practice Lab

Deploy a learner portfolio site with:

- Home page
- Projects page
- API route if supported
- GitHub Actions deployment
- Production URL

### Deliverables

- App repository
- Workflow file
- Cloudflare deployment notes
- Secret management notes
- Rollback steps

### Interview Questions

1. What is edge deployment?
2. Why use GitHub Actions for deployment?
3. How are secrets used safely?
4. What is preview deployment?
5. How do you verify a production deployment?

## 9. OIDC In GitHub Actions For AWS

Reference: [How to Set Up OpenID Connect OIDC in GitHub Actions for AWS](https://www.freecodecamp.org/news/how-to-set-up-openid-connect-oidc-in-github-actions-for-aws/)

### Learning Goal

Use short-lived AWS credentials from GitHub Actions instead of long-lived static access keys.

### Step-by-Step Learner Flow

1. Understand why long-lived cloud keys are risky.
2. Create an IAM OIDC identity provider for GitHub.
3. Create an IAM role with a trust policy for a specific repo, branch, or environment.
4. Attach least-privilege permissions.
5. Configure GitHub Actions permissions for OIDC token access.
6. Assume the AWS role during workflow execution.
7. Run a safe AWS command.
8. Add environment approval for production.
9. Monitor CloudTrail for role usage.

### Practice Lab

Create a workflow that lists S3 buckets or deploys a small artifact using OIDC-based role assumption.

### Deliverables

- Trust policy explanation
- GitHub Actions YAML
- Least privilege policy
- CloudTrail verification
- Security notes

### Interview Questions

1. Why is OIDC safer than static AWS keys?
2. What is an IAM trust policy?
3. What is least privilege?
4. How do GitHub environments improve security?
5. How do you audit role assumption?
