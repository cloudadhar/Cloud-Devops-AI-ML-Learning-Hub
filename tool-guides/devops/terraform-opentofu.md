# Terraform and OpenTofu Zero to Hero Guide

## What It Is

Terraform and OpenTofu are Infrastructure as Code tools used to provision cloud resources with declarative configuration.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Terraform was introduced by HashiCorp in 2014 and became widely adopted for multi-cloud Infrastructure as Code. OpenTofu later emerged as an open source fork in response to licensing changes.

## Architecture and Core Concepts

Core architecture:

```text
Configuration -> Provider -> Plan -> Apply -> State -> Real infrastructure
```

Key concepts:

- Provider, resource, data source, variable, output, module.
- State, backend, lock, plan, apply, destroy.
- Drift between state and real infrastructure.

## Zero to Hero Learning Path

1. Install Terraform or OpenTofu.
2. Write one resource.
3. Use variables and outputs.
4. Run fmt, init, validate, plan, apply.
5. Understand state files.
6. Create modules.
7. Use remote state and locking.
8. Add policy and security scanning.

## How to Start Using It

Core commands:

```bash
terraform fmt
terraform init
terraform validate
terraform plan
terraform apply
terraform destroy
```


## Common Integrations and Pipeline Usage

Cloud deployment pipeline:

```text
PR -> terraform fmt -> validate -> security scan -> plan -> approval -> apply
```

Integrates with AWS, Azure, GCP, GitHub Actions, GitLab CI, Jenkins, Spacelift, Atlantis, Checkov, tfsec, Infracost, Vault, and cloud secret managers.

## Advanced Topics

- Remote state and state locking.
- Module design and versioning.
- Workspaces vs separate state.
- Policy as code.
- Drift detection.
- Importing existing resources.
- Safe destroy and cost controls.

## Hands-on Project

Build a reusable Terraform module for a VM, network, security rules, Nginx bootstrap, and outputs. Add CI plan checks.

## Interview Questions

- What is Terraform state?
- What is drift?
- Plan vs apply?
- Why use modules?
- How do you protect secrets?
- How do you manage remote state?

## References

- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [OpenTofu Documentation](https://opentofu.org/docs/)
