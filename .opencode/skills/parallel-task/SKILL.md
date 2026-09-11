---
name: parallel-task
description: "MCP server for parallel-task. Use when you need parallel-task via MCP."
license: Complete terms in LICENSE.txt
---

# parallel-task

## Overview

MCP server for parallel-task.

## When to Use

- Debugging parallel-task MCP issues
- Configuring parallel-task settings

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

| Issue                 | Solution            |
| --------------------- | ------------------- |
| Server not responding | Run hermes mcp list |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y parallel-task`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
