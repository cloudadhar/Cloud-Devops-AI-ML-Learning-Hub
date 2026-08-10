# Terraform for Beginners - Infrastructure as Code

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Basic Concepts](#basic-concepts)
4. [AWS Example](#aws-example)
5. [State Management](#state-management)
6. [Modules & Reusability](#modules--reusability)
7. [Best Practices](#best-practices)

---

## Introduction

### What is Terraform?
Terraform is an Infrastructure as Code (IaC) tool that:
- Defines infrastructure in configuration files
- Provisions and manages resources
- Supports multiple cloud providers (AWS, Azure, GCP, etc.)
- Enables version control of infrastructure
- Facilitates team collaboration
- Provides reproducible deployments

**Official Documentation**: https://www.terraform.io/docs

**HCL** (HashiCorp Configuration Language):
- Declarative language
- Readable and intuitive
- Human-friendly syntax

### Benefits
✅ Version control for infrastructure
✅ Code review before deployment
✅ Reproducible environments
✅ Multi-cloud support
✅ Easy scaling
✅ Disaster recovery

---

## Installation

### macOS
```bash
brew install terraform

terraform version
```

### Ubuntu/Debian
```bash
sudo apt-get install -y gnupg software-properties-common curl
curl https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install terraform

terraform version
```

### Windows
```powershell
choco install terraform
# or download from https://www.terraform.io/downloads.html
```

### Verify Installation
```bash
terraform version
terraform help
```

---

## Basic Concepts

### Providers
Plugins that interact with cloud platforms (AWS, Azure, GCP, etc.)

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}
```

### Resources
Infrastructure objects (instances, databases, networks, etc.)

```hcl
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "example-instance"
  }
}
```

### Variables
Input values for reusability

```hcl
variable "instance_type" {
  type        = string
  default     = "t2.micro"
  description = "EC2 instance type"
}

variable "environment" {
  type = string
}

variable "tags" {
  type = map(string)
  default = {
    Environment = "dev"
    Team        = "devops"
  }
}
```

### Outputs
Export values for reference

```hcl
output "instance_id" {
  value       = aws_instance.example.id
  description = "ID of the EC2 instance"
}

output "instance_ip" {
  value = aws_instance.example.public_ip
}
```

### Data Sources
Reference existing resources

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "example" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
}
```

---

## AWS Example

### Simple EC2 Deployment

Create `main.tf`:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Create VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "${var.environment}-vpc"
  }
}

# Create public subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = true

  tags = {
    Name = "${var.environment}-public-subnet"
  }
}

# Create security group
resource "aws_security_group" "allow_http" {
  name_prefix = "allow-http-"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.allowed_ssh_cidr
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.environment}-sg"
  }
}

# Create EC2 instance
resource "aws_instance" "web" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.allow_http.id]

  user_data = base64encode(templatefile("${path.module}/init-script.sh", {
    environment = var.environment
  }))

  tags = {
    Name = "${var.environment}-web-server"
  }
}

# Create Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.environment}-igw"
  }
}

# Create route table
resource "aws_route_table" "main" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block      = "0.0.0.0/0"
    gateway_id      = aws_internet_gateway.main.id
  }

  tags = {
    Name = "${var.environment}-rt"
  }
}

# Associate route table with subnet
resource "aws_route_table_association" "main" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.main.id
}
```

Create `variables.tf`:

```hcl
variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "AWS region"
}

variable "environment" {
  type        = string
  default     = "dev"
  description = "Environment name"
}

variable "instance_type" {
  type        = string
  default     = "t2.micro"
  description = "EC2 instance type"
}

variable "allowed_ssh_cidr" {
  type        = list(string)
  default     = ["0.0.0.0/0"]
  description = "CIDR blocks allowed for SSH"
}
```

Create `outputs.tf`:

```hcl
output "instance_id" {
  value       = aws_instance.web.id
  description = "Instance ID"
}

output "instance_public_ip" {
  value       = aws_instance.web.public_ip
  description = "Public IP address"
}

output "vpc_id" {
  value       = aws_vpc.main.id
  description = "VPC ID"
}
```

### Deploy

```bash
# Initialize Terraform
terraform init

# Validate configuration
terraform validate

# Format code
terraform fmt

# Plan deployment
terraform plan -out=tfplan

# Apply deployment
terraform apply tfplan

# View outputs
terraform output

# Destroy resources
terraform destroy
```

---

## State Management

### State File
Terraform tracks resource state in `terraform.tfstate`:

```bash
# View state
terraform state list
terraform state show aws_instance.web

# Manually modify state (use with caution)
terraform state mv aws_instance.old aws_instance.new
terraform state rm aws_instance.web
```

### Remote State (Recommended for Teams)

**AWS S3 Backend**:

Create `backend.tf`:

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

Setup S3 bucket:

```hcl
# Create in separate Terraform configuration
resource "aws_s3_bucket" "terraform_state" {
  bucket = "my-terraform-state"
}

resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# State locking table
resource "aws_dynamodb_table" "terraform_locks" {
  name           = "terraform-locks"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

**Terraform Cloud Backend**:

```hcl
terraform {
  cloud {
    organization = "my-org"

    workspaces {
      name = "my-workspace"
    }
  }
}
```

### State Locking
Prevents concurrent modifications:

```bash
# Automatically locked with S3 + DynamoDB backend
# Manually unlock (if needed):
terraform force-unlock LOCK_ID
```

---

## Modules & Reusability

### Create a Module

Directory structure:

```
modules/
├── vpc/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── security_group/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
└── ec2_instance/
    ├── main.tf
    ├── variables.tf
    └── outputs.tf
```

### Module Example: VPC

`modules/vpc/main.tf`:

```hcl
resource "aws_vpc" "main" {
  cidr_block = var.cidr_block

  tags = {
    Name = var.name
  }
}

resource "aws_subnet" "main" {
  count             = length(var.subnet_cidr_blocks)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.subnet_cidr_blocks[count.index]
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "${var.name}-subnet-${count.index + 1}"
  }
}
```

`modules/vpc/variables.tf`:

```hcl
variable "name" {
  type = string
}

variable "cidr_block" {
  type = string
}

variable "subnet_cidr_blocks" {
  type = list(string)
}
```

`modules/vpc/outputs.tf`:

```hcl
output "vpc_id" {
  value = aws_vpc.main.id
}

output "subnet_ids" {
  value = aws_subnet.main[*].id
}
```

### Use Module

`main.tf`:

```hcl
module "vpc" {
  source = "./modules/vpc"

  name               = "production"
  cidr_block         = "10.0.0.0/16"
  subnet_cidr_blocks = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

module "security_group" {
  source = "./modules/security_group"

  name   = "app-sg"
  vpc_id = module.vpc.vpc_id
}
```

---

## Best Practices

### File Organization

```
project/
├── main.tf              # Primary configuration
├── variables.tf         # Input variables
├── outputs.tf           # Output values
├── terraform.tfvars     # Variable values
├── backend.tf           # Remote state config
├── providers.tf         # Provider config
├── locals.tf            # Local values
├── modules/
│   ├── vpc/
│   ├── security/
│   └── compute/
├── environments/
│   ├── dev/
│   ├── staging/
│   └── prod/
└── .gitignore
```

### .gitignore

```
# Local .terraform directories
**/.terraform/*

# .tfstate files
*.tfstate
*.tfstate.*

# Crash log files
crash.log
crash.*.log

# Exclude all .tfvars files
*.tfvars
*.tfvars.json

# Ignore override files
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Include override files as they are usually used to override resources locally
!example_override.tf

# IDE
.idea/
.vscode/
*.swp
*.swo
*~
```

### Naming Conventions

✅ Use descriptive names:
- `aws_instance` resources: "web", "database", "cache"
- Variables: `instance_type`, `environment`, `vpc_cidr_block`
- Outputs: Clear, descriptive names

### Code Quality

```bash
# Format code
terraform fmt -recursive

# Validate syntax
terraform validate

# Security scanning (TFLint)
brew install tflint
tflint

# Policy as Code (Sentinel)
# Enterprise feature for policy enforcement
```

### Workspace Management

```bash
# Create workspace for multiple environments
terraform workspace new prod
terraform workspace new staging
terraform workspace new dev

# Switch workspace
terraform workspace select prod

# List workspaces
terraform workspace list

# Use workspace in configuration
resource "aws_instance" "web" {
  tags = {
    Environment = terraform.workspace
  }
}
```

---

## Common Patterns

### Loop Through Resources

```hcl
# For loop
resource "aws_subnet" "main" {
  for_each          = var.subnets
  cidr_block        = each.value.cidr
  availability_zone = each.value.az
}

# Count loop
resource "aws_instance" "web" {
  count         = var.instance_count
  instance_type = "t2.micro"

  tags = {
    Name = "web-${count.index + 1}"
  }
}
```

### Conditional Resources

```hcl
resource "aws_instance" "web" {
  count         = var.create_instance ? 1 : 0
  instance_type = "t2.micro"
}
```

---

## Official Resources

- **Terraform Documentation**: https://www.terraform.io/docs
- **Provider Documentation**: https://registry.terraform.io/
- **Community Modules**: https://registry.terraform.io/modules
- **Best Practices**: https://www.terraform.io/docs/cloud/guides

---

**Last Updated**: August 2026
**Version**: 1.0
