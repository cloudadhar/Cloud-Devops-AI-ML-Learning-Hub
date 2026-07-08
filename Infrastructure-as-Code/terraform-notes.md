# Terraform Notes

## Core Concepts

- Provider: plugin for a platform such as AWS, Azure, or GCP.
- Resource: infrastructure object to create.
- Variable: input value.
- Output: exported value.
- State: record of managed resources.
- Module: reusable Terraform package.

## Workflow

```bash
terraform fmt
terraform init
terraform validate
terraform plan
terraform apply
terraform destroy
```

## Safety Rules

- Never commit real `.tfvars` with secrets.
- Use remote state for team projects.
- Review plans before apply.
- Tag resources for ownership and cost.
- Always document destroy steps.

## Interview Notes

- Explain why state is important.
- Explain drift.
- Explain module benefits.
- Explain plan vs apply.
- Explain how secrets should be handled.
