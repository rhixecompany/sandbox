---
name: code-docs-terraform_style
description: "Terraform Documentation Style"
version: 1.0.0
author: Alexa
---
     1|# Terraform Documentation Style
     2|
     3|Complete reference for documenting Terraform code, following HashiCorp best practices and terraform-docs standards.
     4|
     5|## Basic Principles
     6|
     7|- Every variable and output must have a `description`
     8|- Descriptions should be clear, concise, and actionable
     9|- Use comments for complex resource logic
    10|- Module README should explain purpose and usage
    11|- Follow consistent formatting and naming
    12|
    13|## Variable Documentation
    14|
    15|### Basic Variable
    16|
    17|```hcl
    18|variable "instance_type" {
    19|  description = "EC2 instance type for the application servers."
    20|  type        = string
    21|  default     = "t3.medium"
    22|}
    23|```
    24|
    25|### Variable with Validation
    26|
    27|```hcl
    28|variable "environment" {
    29|  description = "Deployment environment (dev, staging, prod). Determines resource naming and sizing."
    30|  type        = string
    31|
    32|  validation {
    33|    condition     = contains(["dev", "staging", "prod"], var.environment)
    34|    error_message = "Environment must be dev, staging, or prod."
    35|  }
    36|}
    37|```
    38|
    39|### Complex Variable Types
    40|
    41|```hcl
    42|variable "vpc_config" {
    43|  description = "VPC configuration including CIDR blocks and subnet configuration."
    44|  type = object({
    45|    cidr_block           = string
    46|    enable_dns_hostnames = bool
    47|    enable_dns_support   = bool
    48|    public_subnets       = list(string)
    49|    private_subnets      = list(string)
    50|  })
    51|
    52|  default = {
    53|    cidr_block           = "10.0.0.0/16"
    54|    enable_dns_hostnames = true
    55|    enable_dns_support   = true
    56|    public_subnets       = ["10.0.1.0/24", "10.0.2.0/24"]
    57|    private_subnets      = ["10.0.10.0/24", "10.0.11.0/24"]
    58|  }
    59|}
    60|```
    61|
    62|### Sensitive Variable
    63|
    64|```hcl
    65|variable "database_password" {
    66|  description = "Master password for the RDS database. Must be at least 16 characters."
    67|  type        = string
    68|  sensitive   = true
    69|
    70|  validation {
    71|    condition     = length(var.database_password) >= 16
    72|    error_message = "Database password must be at least 16 characters."
    73|  }
    74|}
    75|```
    76|
    77|### Variable with Example
    78|
    79|```hcl
    80|variable "tags" {
    81|  description = <<-EOT
    82|    Common tags to apply to all resources.
    83|
    84|    Example:
    85|      tags = {
    86|        Environment = "production"
    87|        Project     = "myapp"
    88|        ManagedBy   = "terraform"
    89|      }
    90|  EOT
    91|  type        = map(string)
    92|  default     = {}
    93|}
    94|```
    95|
    96|### List Variable
    97|
    98|```hcl
    99|variable "allowed_cidr_blocks" {
   100|  description = "List of CIDR blocks allowed to access the application. Use 0.0.0.0/0 for public access (not recommended for production)."
   101|  type        = list(string)
   102|  default     = []
   103|}
   104|```
   105|
   106|### Map Variable
   107|
   108|```hcl
   109|variable "instance_types_by_env" {
   110|  description = "Map of environment names to EC2 instance types. Allows different instance sizes per environment."
   111|  type        = map(string)
   112|
   113|  default = {
   114|    dev     = "t3.small"
   115|    staging = "t3.medium"
   116|    prod    = "t3.large"
   117|  }
   118|}
   119|```
   120|
   121|## Output Documentation
   122|
   123|### Basic Output
   124|
   125|```hcl
   126|output "vpc_id" {
   127|  description = "ID of the created VPC."
   128|  value       = aws_vpc.main.id
   129|}
   130|```
   131|
   132|### Output with Sensitive Data
   133|
   134|```hcl
   135|output "database_endpoint" {
   136|  description = "Connection endpoint for the RDS database."
   137|  value       = aws_db_instance.main.endpoint
   138|  sensitive   = true
   139|}
   140|```
   141|
   142|### Complex Output
   143|
   144|```hcl
   145|output "load_balancer_details" {
   146|  description = "Load balancer configuration including DNS name, ARN, and zone ID."
   147|  value = {
   148|    dns_name = aws_lb.main.dns_name
   149|    arn      = aws_lb.main.arn
   150|    zone_id  = aws_lb.main.zone_id
   151|  }
   152|}
   153|```
   154|
   155|### Output with Usage Instructions
   156|
   157|```hcl
   158|output "ssh_command" {
   159|  description = <<-EOT
   160|    SSH command to connect to the bastion host.
   161|
   162|    Usage:
   163|      $(terraform output -raw ssh_command)
   164|  EOT
   165|  value = "ssh -i ${var.key_name}.pem ec2-user@${aws_instance.bastion.public_ip}"
   166|}
   167|```
   168|
   169|## Resource Comments
   170|
   171|### Simple Resource
   172|
   173|```hcl
   174|# VPC for the application infrastructure
   175|resource "aws_vpc" "main" {
   176|  cidr_block           = var.vpc_cidr
   177|  enable_dns_hostnames = true
   178|  enable_dns_support   = true
   179|
   180|  tags = merge(var.common_tags, {
   181|    Name = "${var.project_name}-vpc"
   182|  })
   183|}
   184|```
   185|
   186|### Complex Resource with Inline Comments
   187|
   188|```hcl
   189|resource "aws_instance" "app_server" {
   190|  ami           = data.aws_ami.ubuntu.id
   191|  instance_type = var.instance_type
   192|
   193|  # Use the first available private subnet
   194|  subnet_id = var.private_subnet_ids[0]
   195|
   196|  # Security group for application traffic
   197|  vpc_security_group_ids = [aws_security_group.app.id]
   198|
   199|  # IAM role for CloudWatch logs and S3 access
   200|  iam_instance_profile = aws_iam_instance_profile.app.name
   201|
   202|  # User data script runs on first boot
   203|  user_data = templatefile("${path.module}/scripts/init.sh", {
   204|    environment = var.environment
   205|    region      = var.aws_region
   206|  })
   207|
   208|  # Ensure the instance is replaced before destroying
   209|  # to maintain availability during updates
   210|  lifecycle {
   211|    create_before_destroy = true
   212|  }
   213|
   214|  tags = merge(var.common_tags, {
   215|    Name = "${var.project_name}-app-${var.environment}"
   216|    Role = "application-server"
   217|  })
   218|}
   219|```
   220|
   221|### Conditional Resource
   222|
   223|```hcl
   224|# Create NAT gateway only for production environments
   225|# to reduce costs in dev/staging
   226|resource "aws_nat_gateway" "main" {
   227|  count = var.environment == "prod" ? length(var.public_subnet_ids) : 0
   228|
   229|  allocation_id = aws_eip.nat[count.index].id
   230|  subnet_id     = var.public_subnet_ids[count.index]
   231|
   232|  tags = merge(var.common_tags, {
   233|    Name = "${var.project_name}-nat-${count.index + 1}"
   234|  })
   235|
   236|  depends_on = [aws_internet_gateway.main]
   237|}
   238|```
   239|
   240|### Dynamic Block
   241|
   242|```hcl
   243|resource "aws_security_group" "app" {
   244|  name        = "${var.project_name}-app-sg"
   245|  description = "Security group for application servers"
   246|  vpc_id      = aws_vpc.main.id
   247|
   248|  # Create ingress rules from variable list
   249|  dynamic "ingress" {
   250|    for_each = var.ingress_rules
   251|    content {
   252|      description = ingress.value.description
   253|      from_port   = ingress.value.from_port
   254|      to_port     = ingress.value.to_port
   255|      protocol    = ingress.value.protocol
   256|      cidr_blocks = ingress.value.cidr_blocks
   257|    }
   258|  }
   259|
   260|  # Allow all outbound traffic
   261|  egress {
   262|    description = "Allow all outbound traffic"
   263|    from_port   = 0
   264|    to_port     = 0
   265|    protocol    = "-1"
   266|    cidr_blocks = ["0.0.0.0/0"]
   267|  }
   268|
   269|  tags = var.common_tags
   270|}
   271|```
   272|
   273|## Data Source Comments
   274|
   275|```hcl
   276|# Get the latest Ubuntu 22.04 LTS AMI
   277|data "aws_ami" "ubuntu" {
   278|  most_recent = true
   279|  owners      = ["099720109477"] # Canonical
   280|
   281|  filter {
   282|    name   = "name"
   283|    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
   284|  }
   285|
   286|  filter {
   287|    name   = "virtualization-type"
   288|    values = ["hvm"]
   289|  }
   290|}
   291|
   292|# Retrieve current AWS region
   293|data "aws_region" "current" {}
   294|
   295|# Get availability zones in current region
   296|data "aws_availability_zones" "available" {
   297|  state = "available"
   298|}
   299|```
   300|
   301|## Module Documentation
   302|
   303|### Module Block with Comments
   304|
   305|```hcl
   306|# VPC module creates networking infrastructure
   307|# including subnets, route tables, and internet gateway
   308|module "vpc" {
   309|  source  = "terraform-aws-modules/vpc/aws"
   310|  version = "5.1.0"
   311|
   312|  name = "${var.project_name}-vpc"
   313|  cidr = var.vpc_cidr
   314|
   315|  # Create subnets across multiple availability zones
   316|  # for high availability
   317|  azs             = data.aws_availability_zones.available.names
   318|  private_subnets = var.private_subnet_cidrs
   319|  public_subnets  = var.public_subnet_cidrs
   320|
   321|  # Enable NAT gateway for private subnet internet access
   322|  enable_nat_gateway = var.environment == "prod"
   323|  single_nat_gateway = var.environment != "prod"
   324|
   325|  # Enable DNS for service discovery
   326|  enable_dns_hostnames = true
   327|  enable_dns_support   = true
   328|
   329|  tags = var.common_tags
   330|}
   331|```
   332|
   333|## Local Values
   334|
   335|```hcl
   336|locals {
   337|  # Common name prefix for all resources
   338|  name_prefix = "${var.project_name}-${var.environment}"
   339|
   340|  # Map of AZ names to subnet indices
   341|  # Used for distributing resources across AZs
   342|  az_to_subnet_index = {
   343|    for idx, az in data.aws_availability_zones.available.names :
   344|    az => idx
   345|  }
   346|
   347|  # Merged tags combining common tags with resource-specific ones
   348|  common_tags = merge(
   349|    var.tags,
   350|    {
   351|      Environment = var.environment
   352|      ManagedBy   = "terraform"
   353|      Project     = var.project_name
   354|    }
   355|  )
   356|}
   357|```
   358|
   359|## File Headers
   360|
   361|### variables.tf
   362|
   363|```hcl
   364|# Variables for the VPC module
   365|#
   366|# This file defines all configurable parameters for the VPC,
   367|# including CIDR blocks, subnet configuration, and feature flags.
   368|
   369|variable "vpc_cidr" {
   370|  description = "CIDR block for the VPC."
   371|  type        = string
   372|  default     = "10.0.0.0/16"
   373|}
   374|
   375|# ... more variables
   376|```
   377|
   378|### outputs.tf
   379|
   380|```hcl
   381|# Outputs from the VPC module
   382|#
   383|# These outputs expose VPC resources for use by other modules
   384|# or for displaying important information to users.
   385|
   386|output "vpc_id" {
   387|  description = "ID of the created VPC."
   388|  value       = aws_vpc.main.id
   389|}
   390|
   391|# ... more outputs
   392|```
   393|
   394|### main.tf
   395|
   396|```hcl
   397|# Main VPC infrastructure
   398|#
   399|# This file creates the core VPC resources including:
   400|# - VPC with DNS support
   401|# - Internet Gateway
   402|# - Public and private subnets
   403|# - Route tables and associations
   404|# - NAT Gateway (production only)
   405|
   406|terraform {
   407|  required_version = ">= 1.5.0"
   408|
   409|  required_providers {
   410|    aws = {
   411|      source  = "hashicorp/aws"
   412|      version = "~> 5.0"
   413|    }
   414|  }
   415|}
   416|
   417|# ... resources
   418|```
   419|
   420|## Module README.md Template
   421|
   422|````markdown
   423|# VPC Module
   424|
   425|Terraform module for creating a VPC with public and private subnets.
   426|
   427|## Features
   428|
   429|- Multi-AZ subnet creation
   430|- Optional NAT Gateway
   431|- DNS support enabled
   432|- Customizable CIDR blocks
   433|- Flexible tagging
   434|
   435|## Usage
   436|
   437|```hcl
   438|module "vpc" {
   439|  source = "./modules/vpc"
   440|
   441|  project_name = "myapp"
   442|  environment  = "production"
   443|  vpc_cidr     = "10.0.0.0/16"
   444|
   445|  private_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24"]
   446|  public_subnet_cidrs  = ["10.0.10.0/24", "10.0.11.0/24"]
   447|
   448|  tags = {
   449|    Owner = "platform-team"
   450|  }
   451|}
   452|```
   453|````
   454|
   455|## Requirements
   456|
   457|| Name      | Version  |
   458|| --------- | -------- |
   459|| terraform | >= 1.5.0 |
   460|| aws       | ~> 5.0   |
   461|
   462|## Providers
   463|
   464|| Name | Version |
   465|| ---- | ------- |
   466|| aws  | ~> 5.0  |
   467|
   468|## Inputs
   469|
   470|| Name | Description | Type | Default | Required |
   471|| --- | --- | --- | --- | :-: |
   472|| project_name | Name of the project | `string` | n/a | yes |
   473|| environment | Deployment environment | `string` | n/a | yes |
   474|| vpc_cidr | VPC CIDR block | `string` | `"10.0.0.0/16"` | no |
   475|
   476|## Outputs
   477|
   478|| Name               | Description                |
   479|| ------------------ | -------------------------- |
   480|| vpc_id             | ID of the created VPC      |
   481|| private_subnet_ids | List of private subnet IDs |
   482|| public_subnet_ids  | List of public subnet IDs  |
   483|
   484|## Examples
   485|
   486|See the `examples/` directory for complete usage examples.
   487|
   488|````
   489|
   490|## Best Practices
   491|
   492|### Variable Descriptions
   493|
   494|**DO** ✅
   495|
   496|```hcl
   497|variable "instance_count" {
   498|  description = "Number of EC2 instances to create. Set to 0 to disable."
   499|  type        = number
   500|  default     = 1
   501|