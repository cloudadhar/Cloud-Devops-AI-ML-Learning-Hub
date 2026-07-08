# Cloud Tool Stack

A cloud stack combines service models, cloud provider services, and operational tools used to run applications reliably.

## Cloud Service Models

| Model | What You Manage | Examples |
| --- | --- | --- |
| IaaS | OS, runtime, app, data, some networking | AWS EC2, Azure Virtual Machines, Google Compute Engine |
| PaaS | App and data while provider manages runtime platform | Heroku, Google App Engine, Azure App Service, Cloud Run |
| SaaS | Configuration and usage of a ready product | Google Workspace, Salesforce, GitHub, Jira |

## Operational Cloud Stack

| Layer | Purpose | Tools and Services |
| --- | --- | --- |
| Cloud provider | Base infrastructure | AWS, Azure, GCP |
| Identity | Access and permissions | AWS IAM, Microsoft Entra ID, Google Cloud IAM |
| Networking | Private networks and connectivity | VPC/VNet, subnets, route tables, security groups, firewalls, load balancers |
| Compute | Run applications | VMs, serverless functions, app services, containers |
| Storage | Store objects and files | S3, Azure Blob Storage, Google Cloud Storage |
| Databases | Transactional and analytical data | PostgreSQL, MySQL, MongoDB Atlas, DynamoDB, BigQuery, Cosmos DB |
| IaC | Repeatable provisioning | Terraform, OpenTofu, CloudFormation, Azure Bicep, Pulumi |
| Containers | Portable packaging | Docker, Podman |
| Orchestration | Scaling and self-healing | EKS, AKS, GKE, ECS, Cloud Run |
| CI/CD | Automated delivery | GitHub Actions, GitLab CI/CD, Jenkins, Azure Pipelines, Cloud Build |
| API edge | Route and protect APIs | Nginx, Kong Gateway, AWS API Gateway, Apigee |
| Observability | Metrics, logs, traces, alerts | Prometheus, Grafana, Datadog, New Relic, CloudWatch, Azure Monitor, Google Cloud Monitoring |
| Security | Guardrails and detection | IAM, KMS, Vault, Snyk, Trivy, Security Hub, Defender for Cloud, Security Command Center |
| Cost | Spend visibility and cleanup | AWS Budgets, Azure Cost Management, Google Cloud Billing, Infracost |

## Beginner Cloud Stack

```text
GitHub -> Terraform -> AWS/Azure/GCP VM -> Nginx -> Monitoring -> Cleanup
```

## Production Cloud Stack

```text
GitHub/GitLab -> CI/CD -> Terraform -> Kubernetes -> Nginx/Kong -> Observability -> Security -> Cost Controls
```

## Private or Hybrid Cloud

- OpenStack - modular private cloud platform.
- Apache CloudStack - infrastructure platform for managing compute, storage, and network resources.
- Kubernetes on bare metal - useful for platform engineering and edge workloads.

## Validated References

- [MongoDB cloud computing stack](https://www.mongodb.com/resources/basics/cloud-explained/cloud-computing-stack) - cloud stack overview.
- [AWS Documentation](https://docs.aws.amazon.com/) - official AWS docs.
- [Azure documentation](https://learn.microsoft.com/en-us/azure/) - official Azure docs.
- [Google Cloud documentation](https://cloud.google.com/docs) - official Google Cloud docs.
- [Nginx documentation](https://nginx.org/en/docs/) - official Nginx docs.
- [Kong Gateway documentation](https://docs.konghq.com/gateway/latest/) - official Kong Gateway docs.
