---
name: playwright
description: "MCP server for playwright. Use when you need playwright via MCP."
license: Complete terms in LICENSE.txt
---

# playwright

## Overview

MCP server for playwright.

## When to Use

- Debugging playwright MCP issues
- Configuring playwright settings

## Prerequisites

- Hermès or MCP-compatible agent

## Configuration

**Transport:** N/A | **Command:** `npx` | **Enabled:** yes

**Arguments:**

- (none)

## Workflows

- Pre-configured

## Gotchas

- - Install: npx playwright install chromium

## Troubleshooting

| Issue                 | Solution            |
| --------------------- | ------------------- |
| Server not responding | Run hermes mcp list |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y playwright`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
