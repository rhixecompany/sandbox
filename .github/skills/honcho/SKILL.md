---
name: honcho
description: 'MCP gateway service for managing multiple MCP server connections. Provides centralized MCP server orchestration, session management, and gateway status monitoring. Use when you need to manage MCP server connections centrally or query gateway status.'
license: Complete terms in LICENSE.txt
---

# honcho — MCP Gateway Skill

## Overview

honcho is the MCP gateway service that manages multiple MCP server connections centrally. It provides a unified endpoint for MCP server orchestration.

- **Transport:** HTTP
- **Endpoint:** https://mcp.honcho.dev/
- **Auth:** Bearer token

## When to Use This Skill

- You need to query the status of MCP gateway connections
- You are debugging MCP server connectivity issues at the gateway level
- You need to manage session state across multiple MCP servers

## Prerequisites

- Hermès configured with honcho MCP endpoint
- Internet connection to honcho.dev
- Bearer token authentication configured

## Step-by-Step Workflows

1. Verify honcho is enabled: `hermes mcp list` shows honcho as ✓ enabled
2. Query gateway status via the honcho MCP tools
3. If connection fails, check internet connectivity to mcp.honcho.dev

## Gotchas

- Requires online connection to honcho.dev — offline usage is not possible
- Bearer token authentication — token refresh may be needed periodically
- Gateway latency may affect tool response times

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Gateway connection refused | Check internet connectivity to https://mcp.honcho.dev/ |
| Authentication failed | Verify Bearer token is correctly configured in Hermès config |
| Timeout | Gateway may be overloaded — retry with longer timeout |

## Testing

Run `hermes mcp list` to verify honcho is enabled. Use honcho MCP tools directly to query gateway status.
