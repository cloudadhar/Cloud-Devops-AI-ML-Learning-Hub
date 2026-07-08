# Multi-cloud Guide

## What to Compare

| Concept | AWS | Azure | GCP |
| --- | --- | --- | --- |
| Account boundary | Account | Subscription | Project |
| Identity | IAM | Microsoft Entra ID + RBAC | IAM |
| Object storage | S3 | Blob Storage | Cloud Storage |
| VM | EC2 | Virtual Machines | Compute Engine |
| Kubernetes | EKS | AKS | GKE |
| Registry | ECR | ACR | Artifact Registry |
| Serverless compute | Lambda | Functions | Cloud Functions / Cloud Run |
| Monitoring | CloudWatch | Azure Monitor | Cloud Monitoring |
| ML platform | SageMaker AI | Azure Machine Learning | Vertex AI / Google AI docs |
| API edge | API Gateway / ALB / Nginx / Kong | API Management / App Gateway / Nginx / Kong | Apigee / Cloud Load Balancing / Nginx / Kong |

## What Learners Should Master

- Shared responsibility model
- IAM and least privilege
- Networking fundamentals
- Compute, storage, database basics
- Managed Kubernetes tradeoffs
- Logging, monitoring, and alerting
- Backup and disaster recovery
- Cost management and cleanup
- Terraform for multi-cloud provisioning

## Project Ideas

- Same static website on AWS, Azure, and GCP.
- Same container app on ECS, AKS, and GKE.
- Same Terraform module pattern across all providers.
- Same observability dashboard pattern across all clouds.
- Same Nginx reverse proxy and Kong API gateway pattern across all clouds.

## Tool Stack Map

Read [stacks/cloud-tool-stack.md](../stacks/cloud-tool-stack.md) for a layered cloud tool stack across IaaS, PaaS, SaaS, IaC, containers, CI/CD, API edge, observability, security, and cost management.
