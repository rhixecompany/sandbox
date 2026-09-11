---
name: atlassian
description: "MCP server for atlassian. Use when you need atlassian via MCP."
license: Complete terms in LICENSE.txt
---

# atlassian

## Overview

MCP server for atlassian.

## When to Use

- Debugging atlassian MCP issues
- Configuring atlassian settings

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

Run `hermes mcp list`. For stdio: `bunx -y atlassian`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
