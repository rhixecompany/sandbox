---
name: twilio-docs
description: "MCP server for twilio-docs. Use when you need twilio-docs via MCP."
license: Complete terms in LICENSE.txt
---

# twilio-docs

## Overview

MCP server for twilio-docs.

## When to Use

- Debugging twilio-docs MCP issues
- Configuring twilio-docs settings

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

Run `hermes mcp list`. For stdio: `bunx -y twilio-docs`

## References

- [MCP Catalog](../mcp-servers/references/mcp-server-catalog.json)
- [Management Tool](../scripts/hermes-mcp-manager.py)
