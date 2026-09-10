---
name: filesystem
description: 'MCP server for filesystem. Use when you need filesystem via MCP.'
license: Complete terms in LICENSE.txt
---

# filesystem

## Overview
MCP server for filesystem.

## When to Use
- Debugging filesystem MCP issues
- Configuring filesystem settings

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
| Issue | Solution |
|-------|----------|
| Server not responding | Run hermes mcp list |

## Testing
Run `hermes mcp list`. For stdio: `bunx -y filesystem`

## References
- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
