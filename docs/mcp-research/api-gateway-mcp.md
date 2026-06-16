# AWS API Gateway / AWS API MCP Server

**Source:** https://github.com/awslabs/mcp  
**AWS Announcement:** https://aws.amazon.com/about-aws/whats-new/2025/07/aws-api-mcp-server-available/

## Overview

The **AWS API MCP Server** (from AWS Labs) allows LLMs and AI agents to interact with AWS APIs using natural language by translating requests into syntactically valid AWS CLI commands. It acts as a bridge between MCP-compatible clients and the full AWS API surface.

A related project covers deploying MCP servers **behind** AWS API Gateway for secure, scalable hosting.

## Key Features

- Translate natural language to valid AWS CLI commands
- Execute AWS API calls on behalf of AI agents
- Scoped IAM-based execution for least-privilege access
- Supports Lambda, ECS, Fargate deployment patterns behind API Gateway
- OAuth / Cognito integration for client auth

## Tools Exposed

Varies by configured AWS API surface. Examples:

| Tool | Description |
|------|-------------|
| `aws_api_call` | Execute an AWS CLI command |
| `list_resources` | List resources in a service/region |
| `describe_resource` | Get details about a specific resource |
| `create_resource` | Create a new AWS resource |

## Installation

### From awslabs/mcp

```bash
git clone https://github.com/awslabs/mcp.git
cd mcp/src/aws-api-mcp-server
pip install -r requirements.txt
python main.py
```

### Serverless Deployment (Lambda + API Gateway)

```bash
# Using AWS SAM from the sample repo
git clone https://github.com/aws-samples/sample-serverless-mcp-servers
cd sample-serverless-mcp-servers/stateless-mcp-on-lambda-python
sam build
sam deploy --guided
```

## Hermes / Claude Desktop Config

```yaml
mcp_servers:
  aws-api:
    command: python
    args: ["/path/to/aws-api-mcp-server/main.py"]
    env:
      AWS_PROFILE: "default"
      AWS_REGION: "us-east-1"
```

## API Gateway Deployment Pattern

Deploy any MCP server behind API Gateway for:
- OAuth / IAM authentication
- Rate limiting and throttling
- Centralized logging via CloudWatch
- VPC integration for private MCP endpoints

```bash
# Architecture: Client → API Gateway → Lambda → MCP Server Logic
gcloud run deploy mcp-server \
  --image my-mcp-image \
  --allow-unauthenticated
```

## Related Resources

- [awslabs/mcp — AWS Labs MCP Hub](https://github.com/awslabs/mcp)
- [AWS API MCP Server announcement](https://aws.amazon.com/about-aws/whats-new/2025/07/aws-api-mcp-server-available/)
- [Serverless MCP on Lambda](https://github.com/aws-samples/sample-serverless-mcp-servers)
- [Guidance: Deploying MCP on AWS](https://github.com/aws-solutions-library-samples/guidance-for-deploying-model-context-protocol-servers-on-aws)
