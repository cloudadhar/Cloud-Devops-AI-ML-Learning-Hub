# Azure Zero to Hero Guide

## What It Is

Azure is Microsoft cloud platform for compute, identity, storage, networking, databases, DevOps, security, and AI/ML services.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Azure evolved from Microsoft cloud services and became a major enterprise cloud platform, strongly integrated with Microsoft Entra ID, Windows, Linux, developer tools, and enterprise identity.

## Architecture and Core Concepts

Core architecture:

```text
Tenant -> Subscription -> Resource Group -> VNet -> Compute -> Storage/Database -> Monitor/Security
```

Key services:

- Microsoft Entra ID, RBAC, Virtual Machines, App Service, Blob Storage, VNet, Azure SQL, Cosmos DB, AKS, ACR, Key Vault, Azure Monitor, Azure Machine Learning.

## Zero to Hero Learning Path

1. Understand tenant, subscription, resource group.
2. Learn Entra ID and RBAC.
3. Create VM, storage, and VNet.
4. Deploy App Service or Container Apps.
5. Use ACR and AKS.
6. Use Azure Monitor and Key Vault.
7. Create Azure DevOps or GitHub Actions pipeline.
8. Learn cost, security, and governance.

## How to Start Using It

Beginner flow:

```text
GitHub -> Terraform/Bicep -> Azure VM/App Service -> Logs -> Cleanup
```


## Common Integrations and Pipeline Usage

Production flow:

```text
GitHub/Azure DevOps -> ACR -> AKS -> Application Gateway/API Management -> Azure Monitor -> Defender for Cloud
```

Integrates with GitHub Actions, Azure DevOps, Terraform, Bicep, Docker, Kubernetes, Nginx, Kong, Prometheus, Grafana, and Azure Machine Learning.

## Advanced Topics

- Managed identities.
- Private endpoints.
- AKS operations.
- Azure Policy.
- Defender for Cloud.
- Key Vault integration.
- Cost management and budgets.

## Hands-on Project

Deploy a containerized API to Azure App Service or AKS with CI/CD, Key Vault, and Azure Monitor logs.

## Interview Questions

- Tenant vs subscription vs resource group?
- What is RBAC?
- What are managed identities?
- App Service vs AKS?
- How do you secure secrets in Azure?
- How do you monitor apps in Azure?

## References

- [Azure Documentation](https://learn.microsoft.com/en-us/azure/)
- [Azure Machine Learning Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/)
- [Azure DevOps Documentation](https://learn.microsoft.com/en-us/azure/devops/)
