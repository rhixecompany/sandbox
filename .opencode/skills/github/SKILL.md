---
name: github
description: "MCP server for github. Use when you need github via MCP."
license: Complete terms in LICENSE.txt
---

# github

## Overview

MCP server for github.

## When to Use

- Debugging github MCP issues
- Configuring github settings

## Prerequisites

- Hermès or MCP-compatible agent

## Configuration

**Transport:** N/A | **Command:** `npx` | **Enabled:** yes

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

Run `hermes mcp list`. For stdio: `bunx -y github`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
