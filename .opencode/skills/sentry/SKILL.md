---
name: sentry
description: "MCP server for sentry. Use when you need sentry via MCP."
license: Complete terms in LICENSE.txt
---

# sentry

## Overview

MCP server for sentry.

## When to Use

- Debugging sentry MCP issues
- Configuring sentry settings

## Prerequisites

- Hermès or MCP-compatible agent

## Configuration

**Transport:** N/A | **Command:** `N/A` | **Enabled:** yes

**Arguments:**

- (none)

## Workflows

- Pre-configured

## Gotchas

- - Sentry auth token

## Troubleshooting

| Issue                 | Solution            |
| --------------------- | ------------------- |
| Server not responding | Run hermes mcp list |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y sentry`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
