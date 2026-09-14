---
name: coderabbit-cli-mcp
description: 'MCP server for coderabbit-cli-mcp. Use when you need coderabbit-cli-mcp via MCP.'
license: Complete terms in LICENSE.txt
---

# coderabbit-cli-mcp

## Overview
MCP server for coderabbit-cli-mcp.

## When to Use
- Debugging coderabbit-cli-mcp MCP issues
- Configuring coderabbit-cli-mcp settings

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
Run `hermes mcp list`. For stdio: `bunx -y coderabbit-cli-mcp`

## References
- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
