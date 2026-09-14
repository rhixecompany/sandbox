---
name: telegram
description: 'MCP server for telegram. Use when you need telegram via MCP.'
license: Complete terms in LICENSE.txt
---

# telegram

## Overview
MCP server for telegram.

## When to Use
- Debugging telegram MCP issues
- Configuring telegram settings

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
Run `hermes mcp list`. For stdio: `bunx -y telegram`

## References
- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
