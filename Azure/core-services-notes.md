# Azure Core Services Notes

## Structure

- Tenant: identity boundary.
- Subscription: billing and resource boundary.
- Resource group: logical container for resources.
- Region: physical location.

## Identity

- Microsoft Entra ID manages identities.
- RBAC controls access to Azure resources.
- Managed identities let services access other services without stored secrets.

## Core Services

- Virtual Machines for compute.
- App Service for managed web apps.
- Blob Storage for objects.
- Azure SQL and Cosmos DB for databases.
- VNet for networking.
- AKS for Kubernetes.
- ACR for container images.

## DevOps and Observability

- Azure DevOps supports boards, repos, pipelines, and artifacts.
- Azure Monitor collects logs and metrics.
- Managed Grafana can visualize metrics.

## Practice

- Deploy VM.
- Deploy App Service.
- Push container to ACR.
- Deploy app to AKS.
- Store secrets in Key Vault.
