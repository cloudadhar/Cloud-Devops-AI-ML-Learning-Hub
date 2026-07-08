# AWS Zero to Hero Guide

## What It Is

AWS is a major cloud provider offering compute, storage, networking, databases, security, DevOps, AI/ML, analytics, and managed services.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

AWS grew from Amazon internal infrastructure and launched public cloud services in the mid-2000s. It became one of the most widely used cloud platforms for startups, enterprises, and public sector systems.

## Architecture and Core Concepts

Core architecture:

```text
Account -> IAM -> VPC -> Subnets -> Compute -> Storage/Database -> Monitoring/Security
```

Key services:

- IAM, VPC, EC2, S3, RDS, DynamoDB, Lambda, ECS, EKS, CloudWatch, CloudTrail, KMS, Secrets Manager, SageMaker AI.

## Zero to Hero Learning Path

1. Create account safety basics: MFA, budgets, IAM.
2. Learn EC2, S3, VPC, security groups.
3. Learn RDS and DynamoDB basics.
4. Deploy with Terraform.
5. Use CloudWatch logs and metrics.
6. Use GitHub Actions OIDC to deploy.
7. Learn ECS or EKS.
8. Learn security, cost, backup, and Well-Architected principles.

## How to Start Using It

Beginner project flow:

```text
GitHub -> Terraform -> AWS EC2 -> User Data -> Nginx -> CloudWatch -> Destroy
```


## Common Integrations and Pipeline Usage

Production flow:

```text
GitHub Actions -> Terraform -> ECR -> EKS/ECS -> ALB/API Gateway -> CloudWatch -> Security Hub
```

Integrates with Terraform, GitHub Actions, GitLab CI, Jenkins, Docker, Kubernetes, Nginx, Kong, Prometheus, Grafana, SonarQube, and SageMaker AI.

## Advanced Topics

- IAM least privilege.
- Multi-account strategy.
- VPC private networking.
- EKS production operations.
- CloudWatch dashboards and alarms.
- GuardDuty and Security Hub.
- Cost allocation tags and budgets.

## Hands-on Project

Create a Terraform project that deploys a secure EC2 Nginx website, adds CloudWatch logs, and includes destroy steps.

## Interview Questions

- What is IAM?
- What is VPC?
- Public vs private subnet?
- Security group vs NACL?
- How do you avoid AWS cost surprises?
- How do you deploy with OIDC instead of access keys?

## References

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/)
- [Amazon SageMaker AI Documentation](https://docs.aws.amazon.com/sagemaker/)
