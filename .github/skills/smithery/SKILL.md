---
name: smithery
description: 'MCP server for smithery. Use when you need smithery via MCP.'
license: Complete terms in LICENSE.txt
---

# smithery

## Overview
MCP server for smithery.

## When to Use
- Debugging smithery MCP issues
- Configuring smithery settings

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
Run `hermes mcp list`. For stdio: `bunx -y smithery`

## References
- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
