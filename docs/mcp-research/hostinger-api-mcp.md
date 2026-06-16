# Hostinger API MCP Server

**Source:** https://github.com/hostinger/api-mcp-server  
**Package:** `hostinger-api-mcp`  
**Official Docs:** https://www.hostinger.com/support/11079316-hostinger-api-mcp-server/

## Overview

Hostinger's official **API MCP server** that bridges Hostinger's hosting services to AI agents and coding assistants via the Model Context Protocol. Enables AI tools to manage web hosting, VPS, domains, DNS records, billing, and more through natural language.

## Key Features

- Web hosting management (sites, files, databases)
- VPS creation and management
- Domain registration and renewal
- DNS record management
- Billing and subscription queries
- Per-product enable/disable granularity
- Supports stdio, HTTP streaming, and SSE transport

## Authentication

- **API Token** (`HOSTINGER_API_TOKEN`): Primary method
- **OAuth 2.0 with PKCE**: Browser-based sign-in for multi-user scenarios

## Installation

### Requirements

- Node.js 20+ (use nvm for version management)

```bash
nvm install 20
nvm use 20
```

### Global Install

```bash
npm install -g hostinger-api-mcp
# or
yarn global add hostinger-api-mcp
# or
pnpm add -g hostinger-api-mcp
```

### Via npx (no install)

```bash
npx hostinger-api-mcp
```

## Hermes / Claude Desktop Config

```yaml
mcp_servers:
  hostinger-api:
    command: hostinger-api-mcp
    env:
      HOSTINGER_API_TOKEN: "your_api_token_here"
      DEBUG: "false"
```

JSON format (for Claude Desktop):

```json
{
  "mcpServers": {
    "hostinger-api": {
      "command": "hostinger-api-mcp",
      "env": {
        "DEBUG": "false",
        "HOSTINGER_API_TOKEN": "YOUR_API_TOKEN"
      }
    }
  }
}
```

## Transport Modes

| Mode | Command | Use Case |
|------|---------|----------|
| stdio (default) | `hostinger-api-mcp` | Local tool integration |
| HTTP Streaming | `hostinger-api-mcp --http --port 8100` | Remote agent access |
| SSE | `hostinger-api-mcp --sse` | Server-Sent Events stream |

## Available API Products

| Product | Enable/Disable | Description |
|---------|---------------|-------------|
| Web Hosting | ✅ | Manage hosting plans, files, DBs |
| VPS | ✅ | Create and configure VPS instances |
| Domains | ✅ | Register, transfer, renew domains |
| DNS | ✅ | Manage DNS zones and records |
| Billing | ✅ | Queries invoices and subscriptions |
| Reach | ✅ | Marketing and outreach tools |

## Example Agent Prompts

- "List all my active hosting plans"
- "Create a DNS A record for api.example.com pointing to 1.2.3.4"
- "Show upcoming renewal dates for my domains"
- "Get the current status of VPS server #12345"

## Related Resources

- [GitHub: hostinger/api-mcp-server](https://github.com/hostinger/api-mcp-server)
- [Hostinger Developer API](https://developers.hostinger.com/)
- [MCP Servers Directory: Hostinger](https://mcpservers.org/servers/hostinger/api-mcp-server)
