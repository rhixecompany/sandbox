---
name: fetch
description: "MCP server for fetch. Use when you need fetch via MCP."
license: Complete terms in LICENSE.txt
---

# fetch

## Overview

MCP server for fetch.

## When to Use

- Debugging fetch MCP issues
- Configuring fetch settings

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

Run `hermes mcp list`. For stdio: `bunx -y fetch`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
