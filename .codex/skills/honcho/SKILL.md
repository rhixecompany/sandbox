---
name: honcho
description: "MCP server for honcho. Use when you need honcho via MCP."
license: Complete terms in LICENSE.txt
---

# honcho

## Overview

MCP server for honcho.

## When to Use

- Debugging honcho MCP issues
- Configuring honcho settings

## Prerequisites

- Hermès or MCP-compatible agent

## Configuration

**Transport:** http | **Command:** `N/A` | **Enabled:** yes

**Arguments:**

- (none)

## Workflows

1. Verify API key
2. HTTP endpoint
3. Tools available

## Gotchas

- No known gotchas

## Troubleshooting

| Issue            | Solution         |
| ---------------- | ---------------- |
| 401 Unauthorized | Verify API key   |
| 404 Not Found    | Check URL        |
| Timeout          | Retry with delay |

## Testing

Run `hermes mcp list`. For stdio: `bunx -y honcho`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
