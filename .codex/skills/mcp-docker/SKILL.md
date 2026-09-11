---
name: mcp-docker
description: "Docker MCP server. Use when you need mcp-docker via MCP."
license: Complete terms in LICENSE.txt
---

# mcp-docker

## Overview

Docker MCP server.

## When to Use

- Debugging mcp-docker MCP issues
- Configuring mcp-docker settings

## Prerequisites

- Docker installed
- Docker gateway configured

## Configuration

**Transport:** N/A | **Command:** `docker` | **Enabled:** yes

**Arguments:**

- (none)

## Workflows

- Pre-configured

## Gotchas

- No known gotchas

## Troubleshooting

| Issue                 | Solution            |
| --------------------- | ------------------- |
| Server not responding | Run hermes mcp list |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y mcp-docker`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
