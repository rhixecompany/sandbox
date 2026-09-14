---
name: code-sandbox
description: 'MCP server for code-sandbox. Use when you need code-sandbox via MCP.'
license: Complete terms in LICENSE.txt
---

# code-sandbox

## Overview
MCP server for code-sandbox.

## When to Use
- Debugging code-sandbox MCP issues
- Configuring code-sandbox settings

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
Run `hermes mcp list`. For stdio: `bunx -y code-sandbox`

## References
- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
