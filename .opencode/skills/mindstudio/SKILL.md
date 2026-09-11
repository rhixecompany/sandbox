---
name: mindstudio
description: "MindStudio CLI MCP server. Use when you need mindstudio via MCP."
license: Complete terms in LICENSE.txt
---

# mindstudio

## Overview

MindStudio CLI MCP server.

## When to Use

- Debugging mindstudio MCP issues
- Configuring mindstudio settings

## Prerequisites

- MindStudio installed

## Configuration

**Transport:** N/A | **Command:** `mindstudio` | **Enabled:** yes

**Arguments:**

- (none)

## Workflows

- Pre-configured

## Gotchas

- No known gotchas

## Troubleshooting

| Issue                 | Solution            |
| --------------------- | ------------------- |
| Server not responding | Run hermes mcp list |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y mindstudio`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
