---
name: tooling-config
description: "MCP server for tooling-config. Use when you need tooling-config via MCP."
license: Complete terms in LICENSE.txt
---

# tooling-config

## Overview

MCP server for tooling-config.

## When to Use

- Debugging tooling-config MCP issues
- Configuring tooling-config settings

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

| Issue                 | Solution            |
| --------------------- | ------------------- |
| Server not responding | Run hermes mcp list |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y tooling-config`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
