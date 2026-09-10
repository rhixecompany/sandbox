---
name: context7
description: 'MCP server for context7. Use when you need context7 via MCP.'
license: Complete terms in LICENSE.txt
---

# context7

## Overview
MCP server for context7.

## When to Use
- Debugging context7 MCP issues
- Configuring context7 settings

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
| Issue | Solution |
|-------|----------|
| Server not responding | Run hermes mcp list |

## Testing
Run `hermes mcp list`. For stdio: `bunx -y context7`

## References
- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
