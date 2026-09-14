---
name: python-quality
description: 'MCP server for python-quality. Use when you need python-quality via MCP.'
license: Complete terms in LICENSE.txt
---

# python-quality

## Overview
MCP server for python-quality.

## When to Use
- Debugging python-quality MCP issues
- Configuring python-quality settings

## Prerequisites
- Hermès or MCP-compatible agent

## Configuration
**Transport:** N/A | **Command:** `` | **Enabled:** yes

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
Run `hermes mcp list`. For stdio: `bunx -y python-quality`

## References
- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
