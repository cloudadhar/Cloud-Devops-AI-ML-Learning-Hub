# Cloud Engineering: AWS, Azure, and Google Cloud

![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white) ![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)

## Who This Track Is For

Learners targeting cloud engineer, junior solution architect, cloud support, DevOps cloud, or platform roles.

## Outcomes

- Explain core cloud building blocks: identity, network, compute, storage, database, monitoring, and cost.
- Compare AWS, Azure, and Google Cloud services without becoming tool-confused.
- Build small cloud deployments with least privilege, tagging, budgets, and cleanup.


## Architecture Mental Model

```text
User -> DNS/CDN -> Load balancer -> Public subnet -> Private app subnet -> Database/storage -> IAM -> Logs/metrics -> Budget alerts
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Learn shared responsibility, regions/zones, IAM, VPC/VNet, subnets, security groups/firewall rules, and compute.
- Launch a temporary Linux VM, connect with SSH, install Nginx, verify logs, and delete resources.
- Create a cost safety checklist before every lab.

### Days 31-60

- Deploy a small web app with load balancer, managed database, object storage, and monitoring.
- Learn IaC basics using Terraform or CloudFormation/Bicep equivalent.
- Practice IAM policies: admin vs least privilege vs service role.

### Days 61-90

- Design a secure multi-tier app with private database, CI/CD, secrets, backups, and alarms.
- Explain high availability, disaster recovery, RTO/RPO, autoscaling, and rollout strategy.
- Prepare one architecture diagram for AWS, one for Azure, and one for Google Cloud.

## Hands-on Labs

- AWS EC2 plus security group plus Nginx plus cleanup.
- Azure App Service or VM deployment with logs and budget notes.
- Google Cloud Cloud Run or Compute Engine deployment with IAM and monitoring.
- Terraform multi-cloud comparison: provider, state, plan, apply, destroy.

## Scenario-Based Interview Questions

1. A public cloud VM was hacked through SSH. What network, IAM, patching, logging, and key-management controls do you verify?
2. Your app works from one region but not another. How do region, DNS, TLS, IAM, and database replication affect the design?
3. The cloud bill suddenly increased. How do you investigate cost by service, tag, region, network egress, and idle resources?
4. A database must not be publicly reachable. Design the network path from user to app to database.
5. A junior engineer asks why IAM role is safer than hardcoded access keys. Explain with CI/CD example.

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
- https://learn.microsoft.com/en-us/devops/what-is-devops
- https://cloud.google.com/devops
