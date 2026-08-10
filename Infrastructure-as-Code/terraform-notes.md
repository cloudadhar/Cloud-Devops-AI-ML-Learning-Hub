# Terraform Notes - Complete Reference

## 📚 Official Documentation

- [Terraform Official Docs](https://developer.hashicorp.com/terraform/docs)
- [Terraform CLI Reference](https://developer.hashicorp.com/terraform/cli/commands)
- [Terraform Language Reference](https://developer.hashicorp.com/terraform/language)
- [Terraform Registry](https://registry.terraform.io) - Modules & Providers
- [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [GCP Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)

---

## Core Concepts

- **Provider**: plugin for a platform such as AWS, Azure, or GCP.
- **Resource**: infrastructure object to create.
- **Variable**: input value.
- **Output**: exported value.
- **State**: record of managed resources.
- **Module**: reusable Terraform package.
- **Data Source**: read-only reference to existing resources.
- **Local Values**: assign values within configuration.

---

## Terraform Workflow

### Standard Workflow

```bash
# 1. Write configuration
vim main.tf

# 2. Format code
terraform fmt

# 3. Initialize working directory
terraform init

# 4. Validate configuration
terraform validate

# 5. Plan changes (dry-run)
terraform plan -out=tfplan

# 6. Apply changes
terraform apply tfplan

# 7. Verify deployment
terraform show

# 8. Get outputs
terraform output

# 9. Destroy when done
terraform destroy
```

### Common Commands

```bash
# Initialize
terraform init                    # Initialize working directory
terraform init -upgrade          # Upgrade providers

# Validation
terraform fmt                     # Format HCL files
terraform fmt -recursive         # Format all files
terraform validate               # Validate configuration syntax

# Planning
terraform plan                   # Generate execution plan
terraform plan -out=tfplan       # Save plan to file
terraform plan -destroy          # Plan destroy

# Execution
terraform apply                  # Apply changes (interactive)
terraform apply tfplan           # Apply saved plan (no questions)
terraform apply -auto-approve    # Auto-approve changes (use carefully!)

# State Management
terraform state list             # List resources in state
terraform state show resource    # Show resource details
terraform state rm resource      # Remove resource from state
terraform state pull             # Download state file
terraform state push             # Upload state file

# Inspection
terraform show                   # Show current state
terraform output                 # List outputs
terraform output -raw var_name   # Get single output value
terraform graph                  # Generate resource graph

# Cleanup
terraform destroy                # Destroy all resources
terraform destroy -auto-approve  # Auto-approve destruction
```

---

## Configuration Structure

### Basic HCL Syntax

```hcl
# Terraform version constraint
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Provider configuration
provider "aws" {
  region = var.aws_region
}

# Variable definition (input)
variable "instance_count" {
  type        = number
  description = "Number of EC2 instances"
  default     = 1
}

# Local value
locals {
  environment = "production"
  name_prefix = "app-${local.environment}"
}

# Resource creation
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  count         = var.instance_count

  tags = {
    Name = "${local.name_prefix}-${count.index}"
  }
}

# Data source (reference existing resource)
data "aws_ami" "ubuntu" {
  owners = ["099720109477"]  # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

# Output (export value)
output "instance_ips" {
  value       = aws_instance.example[*].public_ip
  description = "Public IPs of instances"
  sensitive   = false
}
```

---

## Safety Rules

1. **Never commit real `.tfvars` with secrets**
   ```bash
   # ✅ Add to .gitignore
   terraform.tfvars
   *.tfvars
   
   # ✅ Use environment variables instead
   export TF_VAR_db_password=secret
   ```

2. **Use remote state for team projects**
   ```hcl
   terraform {
     backend "s3" {
       bucket         = "terraform-state"
       key            = "prod/terraform.tfstate"
       region         = "us-east-1"
       dynamodb_table = "terraform-lock"
       encrypt        = true
     }
   }
   ```

3. **Review plans before apply**
   ```bash
   terraform plan -out=tfplan
   # Review tfplan carefully!
   terraform apply tfplan
   ```

4. **Tag resources for ownership and cost**
   ```hcl
   tags = {
     Environment = "production"
     Owner       = "devops-team"
     CostCenter  = "engineering"
     ManagedBy   = "terraform"
   }
   ```

5. **Always document destroy steps**
   ```bash
   # Keep notes on required cleanup steps
   # Some resources may need manual cleanup before terraform destroy
   ```

6. **Use workspaces for environments**
   ```bash
   terraform workspace new prod
   terraform workspace new staging
   terraform workspace select prod
   terraform plan  # Plans for prod workspace
   ```

---

## State Management

### Why State Matters
- Tracks deployed resources
- Maps code to real resources
- Enables updates and cleanup
- Essential for team collaboration

### Local State (Development only)
```bash
# State file stored locally
# terraform.tfstate (main state)
# terraform.tfstate.backup (previous state)
```

### Remote State (Production)

**AWS S3 + DynamoDB** (recommended)
```hcl
terraform {
  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

**Terraform Cloud**
```hcl
terraform {
  cloud {
    organization = "my-company"
    
    workspaces {
      name = "my-workspace"
    }
  }
}
```

### State Lock
```bash
# Prevents concurrent modifications
# Automatically used with remote backends
# Manual lock removal (if needed)
terraform force-unlock LOCK_ID
```

---

## Modules

### Why Use Modules?
- Code reusability
- Consistent configurations
- Team collaboration
- Easier maintenance
- Encapsulation

### Module Structure

```
terraform/
├── main.tf              # Calls modules
├── variables.tf         # Input variables
├── outputs.tf           # Output values
└── modules/
    └── vpc/
        ├── main.tf      # VPC resources
        ├── variables.tf # VPC inputs
        └── outputs.tf   # VPC outputs
    └── ec2/
        ├── main.tf      # EC2 resources
        ├── variables.tf
        └── outputs.tf
```

### Using Modules

```hcl
# Call a module
module "vpc" {
  source = "./modules/vpc"
  
  cidr_block = "10.0.0.0/16"
  name       = "prod-vpc"
  tags       = var.common_tags
}

# Reference module outputs
resource "aws_security_group" "app" {
  vpc_id = module.vpc.vpc_id
  # ...
}

# Using remote modules
module "eks" {
  source = "terraform-aws-modules/eks/aws"
  version = "19.0"
  
  cluster_name    = "prod-cluster"
  cluster_version = "1.28"
}
```

---

## Terraform Cloud/Enterprise

### Benefits
- Remote state management
- Team governance
- Cost estimation
- Policy enforcement
- VCS integration

### Setup
```bash
# Login to Terraform Cloud
terraform login

# Configure cloud backend
terraform {
  cloud {
    organization = "my-organization"
    
    workspaces {
      name = "prod"
    }
  }
}

# Use like normal
terraform plan
terraform apply
```

---

## Best Practices

### Code Organization
```bash
# Separate by environment
terraform/
├── dev/
├── staging/
├── prod/
└── modules/
```

### Naming Conventions
```hcl
# Use descriptive names
resource "aws_security_group" "app_web" {  # ✅ Good
  # vs
resource "aws_security_group" "sg"         # ❌ Not clear
```

### Variable Organization
```hcl
# Group related variables
variable "instance_count" { }
variable "instance_type" { }
variable "instance_tags" { }
```

### Outputs
```hcl
# Export important values
output "load_balancer_dns" {
  value       = aws_lb.main.dns_name
  description = "DNS name of load balancer"
}
```

---

## Interview Questions

1. **Explain why state is important**
   - Maps code to real resources
   - Enables infrastructure updates
   - Tracks resource metadata
   - Essential for team collaboration

2. **Explain drift**
   - Manual changes to resources not in code
   - Terraform plan detects drift
   - Resolved with: refresh, import, or manual sync

3. **Explain module benefits**
   - Code reusability
   - Encapsulation
   - Consistent configurations
   - Easier maintenance

4. **Explain plan vs apply**
   - Plan: dry-run showing proposed changes
   - Apply: actually makes the changes
   - Always review plan before apply!

5. **Explain how secrets should be handled**
   - ❌ Never hardcode secrets
   - ✅ Use environment variables
   - ✅ Use Terraform variables
   - ✅ Use AWS Secrets Manager
   - ✅ Use HashiCorp Vault

6. **Describe the Terraform workflow**
   - init → fmt → validate → plan → apply

7. **How do you manage state for teams?**
   - Remote state (S3, Terraform Cloud)
   - State locking (DynamoDB, Terraform Cloud)
   - Proper access control

8. **What's the difference between count and for_each?**
   - count: indices (0, 1, 2...)
   - for_each: map keys (dev, staging, prod)
   - for_each is better for flexibility

---

## Troubleshooting

### Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Error: resource already exists` | Resource created outside Terraform | Use `terraform import` |
| `Error: state lock` | Another Terraform running | Wait or `terraform force-unlock` |
| `Error: invalid resource type` | Typo in resource type | Check provider docs |
| `Error: module not found` | Path incorrect or not initialized | Check source path, run `terraform init` |

### Debug Mode
```bash
# Enable debug logging
export TF_LOG=DEBUG
terraform plan

# More verbose
export TF_LOG=TRACE
terraform apply
```

---

## Related Tools

- **Checkov**: Scan Terraform for compliance issues
- **tfsec**: Security scanning for Terraform
- **Terragrunt**: Wrapper for managing multiple stacks
- **Terraform Cloud**: Managed Terraform service
- **Atlantis**: GitOps workflow for Terraform


