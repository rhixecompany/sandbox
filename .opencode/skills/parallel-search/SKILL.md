---
name: parallel-search
description: "MCP server for parallel-search. Use when you need parallel-search via MCP."
license: Complete terms in LICENSE.txt
---

# parallel-search

## Overview

MCP server for parallel-search.

## When to Use

- Debugging parallel-search MCP issues
- Configuring parallel-search settings

## Prerequisites

- Hermès or MCP-compatible agent

## Configuration

**Transport:** N/A | **Command:** `N/A` | **Enabled:** yes

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

Run `hermes mcp list`. For stdio: `bunx -y parallel-search`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
