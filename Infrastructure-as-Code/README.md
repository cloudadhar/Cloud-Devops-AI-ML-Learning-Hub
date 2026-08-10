# Infrastructure as Code Guide

## Concepts

- Declarative vs imperative automation
- State management
- Providers
- Modules
- Variables and outputs
- Plan/apply lifecycle
- Drift detection
- Policy as code
- Secrets handling
- Remote state and locking

## Tools

- Terraform
- OpenTofu
- CloudFormation
- Azure Bicep
- Pulumi
- Ansible
- Packer
- Checkov
- tfsec

## Official Documentation References

### Core IaC Tools

**Terraform**
- [Official Terraform Docs](https://developer.hashicorp.com/terraform/docs) - Complete Terraform documentation
- [Terraform CLI Reference](https://developer.hashicorp.com/terraform/cli/commands) - Command line interface
- [Terraform Language](https://developer.hashicorp.com/terraform/language) - HCL syntax and concepts
- [Terraform Registry](https://registry.terraform.io) - Modules and providers

**OpenTofu** (Open-source Terraform fork)
- [OpenTofu Documentation](https://opentofu.org/docs/) - Full OpenTofu docs
- [OpenTofu GitHub](https://github.com/opentofu/opentofu) - Source code

**AWS CloudFormation**
- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/) - AWS IaC docs
- [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/) - Complete guide
- [CloudFormation Template Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) - Resource types

**Azure Bicep**
- [Azure Bicep Documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/) - Azure IaC docs
- [Bicep Language Reference](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/file) - Bicep syntax
- [Bicep GitHub](https://github.com/Azure/bicep) - Source code

**Pulumi**
- [Pulumi Documentation](https://www.pulumi.com/docs/) - Full Pulumi docs
- [Pulumi CLI](https://www.pulumi.com/docs/cli/) - Command line interface
- [Pulumi Languages](https://www.pulumi.com/docs/concepts/languages/) - Python, Go, JavaScript, C#

### Configuration Management

**Ansible**
- [Ansible Documentation](https://docs.ansible.com/) - Official Ansible community docs
- [Ansible Getting Started](https://docs.ansible.com/ansible/latest/getting_started/index.html) - Beginner guide
- [Ansible Playbook Guide](https://docs.ansible.com/ansible/latest/playbook_guide/index.html) - Playbook concepts
- [Ansible Modules](https://docs.ansible.com/ansible/latest/collections/all_modules.html) - Module reference

### Image & VM Management

**Packer**
- [Packer Documentation](https://developer.hashicorp.com/packer/docs) - Official Packer docs
- [Packer Builders](https://developer.hashicorp.com/packer/plugins) - Supported platforms
- [Packer Templates](https://developer.hashicorp.com/packer/docs/templates) - Template syntax

### Security & Compliance

**Checkov** (Infrastructure scanning)
- [Checkov GitHub](https://github.com/bridgecrewio/checkov) - Source and documentation
- [Checkov Docs](https://www.checkov.io/) - Official documentation
- [Checkov Checks](https://www.checkov.io/docs/getting-started) - Available checks

**tfsec** (Terraform security scanning)
- [tfsec GitHub](https://github.com/aquasecurity/tfsec) - Source code
- [tfsec Documentation](https://aquasecurity.github.io/tfsec/latest/) - Full documentation
- [tfsec Checks](https://aquasecurity.github.io/tfsec/latest/checks/) - Security checks

**Terraform Cloud/Enterprise**
- [Terraform Cloud](https://cloud.hashicorp.com/products/terraform) - Managed Terraform service
- [Terraform Cloud Documentation](https://developer.hashicorp.com/terraform/cloud-docs) - Docs

---

## Key Learning Paths

| Tool | Best For | Difficulty | Time to Learn |
|------|----------|-----------|---|
| **Terraform** | AWS, Azure, GCP, multi-cloud | Medium | 2-4 weeks |
| **CloudFormation** | AWS-only, JSON/YAML | Medium | 2-3 weeks |
| **Bicep** | Azure-only, simple syntax | Easy | 1-2 weeks |
| **Ansible** | Configuration management, VMs | Medium | 2-3 weeks |
| **Packer** | VM image building | Medium | 1-2 weeks |
| **Pulumi** | Code-driven IaC (Python/Go/JS) | Hard | 3-4 weeks |

---

## Validated References

- [Terraform documentation](https://developer.hashicorp.com/terraform/docs) - official Terraform docs.
- [Ansible documentation](https://docs.ansible.com/) - official Ansible community docs.
- [AWS CloudFormation documentation](https://docs.aws.amazon.com/cloudformation/) - AWS IaC docs.
- [Azure Bicep documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/) - Azure IaC docs.
- [OpenTofu documentation](https://opentofu.org/docs/) - Open-source Terraform alternative
- [Packer documentation](https://developer.hashicorp.com/packer/docs) - Image building tool
- [Checkov documentation](https://www.checkov.io/) - Infrastructure as code scanning
- [tfsec documentation](https://aquasecurity.github.io/tfsec/latest/) - Terraform security scanning

## Supporting Docs

- [Terraform Notes](terraform-notes.md)


