# AWS Core Services Notes

## Identity

- IAM users are identities for people or workloads.
- IAM roles are preferred for temporary permissions.
- Policies define allowed and denied actions.
- MFA should be enabled for human access.

## Networking

- VPC is your private cloud network boundary.
- Subnets divide the VPC by CIDR and availability zone.
- Route tables control where traffic goes.
- Security groups are stateful instance-level firewalls.
- NACLs are stateless subnet-level filters.

## Compute

- EC2 runs virtual machines.
- Auto Scaling adjusts capacity.
- Load balancers distribute traffic.
- Lambda runs event-driven functions.

## Storage and Databases

- S3 stores objects.
- EBS is block storage for EC2.
- RDS is managed relational database.
- DynamoDB is managed NoSQL.

## DevOps and Observability

- CloudWatch collects metrics and logs.
- CloudTrail records API activity.
- CodeBuild, CodeDeploy, and CodePipeline support AWS-native delivery.

## Practice

- Create billing alert.
- Create least privilege IAM role.
- Deploy EC2 with Terraform.
- Serve website with Nginx.
- Clean up all resources.
