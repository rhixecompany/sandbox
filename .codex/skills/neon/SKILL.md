---
name: neon
description: "MCP server for neon. Use when you need neon via MCP."
license: Complete terms in LICENSE.txt
---

# neon

## Overview

MCP server for neon.

## When to Use

- Debugging neon MCP issues
- Configuring neon settings

## Prerequisites

- Hermès or MCP-compatible agent

## Configuration

**Transport:** N/A | **Command:** `N/A` | **Enabled:** yes

**Arguments:**

- (none)

## Workflows

- Pre-configured

## Gotchas

- - Neon branch architecture

## Troubleshooting

| Issue                 | Solution            |
| --------------------- | ------------------- |
| Server not responding | Run hermes mcp list |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y neon`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
