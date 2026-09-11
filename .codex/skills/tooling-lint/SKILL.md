---
name: tooling-lint
description: "MCP server for tooling-lint. Use when you need tooling-lint via MCP."
license: Complete terms in LICENSE.txt
---

# tooling-lint

## Overview

MCP server for tooling-lint.

## When to Use

- Debugging tooling-lint MCP issues
- Configuring tooling-lint settings

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

Run `hermes mcp list`. For stdio: `bunx -y tooling-lint`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
