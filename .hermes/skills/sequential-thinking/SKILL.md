---
name: sequential-thinking
description: 'MCP server for sequential-thinking. Use when you need sequential-thinking via MCP.'
license: Complete terms in LICENSE.txt
---

# sequential-thinking

## Overview
MCP server for sequential-thinking.

## When to Use
- Debugging sequential-thinking MCP issues
- Configuring sequential-thinking settings

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
Run `hermes mcp list`. For stdio: `bunx -y sequential-thinking`

## References
- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
