---
name: ast-grep
description: "MCP server for ast-grep. Use when you need ast-grep via MCP."
license: Complete terms in LICENSE.txt
---

# ast-grep

## Overview

MCP server for ast-grep.

## When to Use

- Debugging ast-grep MCP issues
- Configuring ast-grep settings

## Prerequisites

- Hermès or MCP-compatible agent

## Configuration

**Transport:** N/A | **Command:** `npx` | **Enabled:** yes

**Arguments:**

- (none)

## Workflows

- Pre-configured

## Gotchas

- - AST-based queries

## Troubleshooting

| Issue                 | Solution            |
| --------------------- | ------------------- |
| Server not responding | Run hermes mcp list |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y ast-grep`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
