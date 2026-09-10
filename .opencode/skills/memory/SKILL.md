---
name: memory
description: 'MCP server for memory. Use when you need memory via MCP.'
license: Complete terms in LICENSE.txt
---

# memory

## Overview
MCP server for memory.

## When to Use
- Debugging memory MCP issues
- Configuring memory settings

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
Run `hermes mcp list`. For stdio: `bunx -y memory`

## References
- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
