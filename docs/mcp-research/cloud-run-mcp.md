# Cloud Run MCP Server

**Source:** https://github.com/GoogleCloudPlatform/cloud-run-mcp

## Overview

Google's official **Cloud Run MCP server** and Gemini CLI extension. Enables MCP-compatible AI agents to deploy applications to Google Cloud Run, retrieve logs, and manage Cloud Run services via natural language or programmatic tool calls.

## Key Features

- Deploy containerized applications to Cloud Run
- Retrieve service logs and status
- Manage environment variables and secrets
- Scale services and adjust concurrency settings
- Integrate with Gemini CLI for natural language deployments

## Tools Exposed

| Tool | Description |
|------|-------------|
| `deploy` | Deploy a container image to Cloud Run |
| `get_logs` | Retrieve logs from a Cloud Run service |
| `list_services` | List all Cloud Run services in a project |
| `describe_service` | Get details about a specific service |
| `delete_service` | Remove a Cloud Run service |

## Installation

### Prerequisites

- Google Cloud CLI (`gcloud`) installed and authenticated
- A GCP project with Cloud Run API enabled
- Node.js 18+

### Via npx (Development/Testing)

```bash
npx @google-cloud/cloud-run-mcp
```

### Via Cloud Run (Production)

```bash
gcloud run deploy cloud-run-mcp \
  --image gcr.io/google.com/cloudsdktool/cloud-sdk \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## Hermes / Claude Desktop Config

```yaml
mcp_servers:
  cloud-run:
    command: npx
    args: ["@google-cloud/cloud-run-mcp"]
    env:
      GOOGLE_CLOUD_PROJECT: "your-project-id"
```

## Authentication

Uses `gcloud` Application Default Credentials (ADC). Run:

```bash
gcloud auth application-default login
```

## Related Resources

- [GoogleCloudPlatform/cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp)
- [google/mcp — Google MCP Hub](https://github.com/google/mcp)
- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [MCP on Cloud Run (community)](https://github.com/jackwotherspoon/mcp-on-cloudrun)
