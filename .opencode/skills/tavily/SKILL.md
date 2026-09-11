---
name: tavily
description: "MCP server for tavily. Use when you need tavily via MCP."
license: Complete terms in LICENSE.txt
---

# tavily

## Overview

MCP server for tavily.

## When to Use

- Debugging tavily MCP issues
- Configuring tavily settings

## Prerequisites

- Hermès or MCP-compatible agent

## Configuration

**Transport:** N/A | **Command:** `N/A` | **Enabled:** yes

**Arguments:**

- (none)

## Workflows

- Pre-configured

## Gotchas

- - TAVILY_API_KEY must be set
- - Rate limits

## Troubleshooting

| Issue                 | Solution            |
| --------------------- | ------------------- |
| Server not responding | Run hermes mcp list |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y tavily`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
