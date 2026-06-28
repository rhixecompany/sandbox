---
name: no-net-fetch
description: "Constraint flag: never make network fetch calls or web requests. Prevents all outbound HTTP/HTTPS requests during execution. Use as network safety constraint."
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - constraint
  - network
  - safety
  - offline
---

# No Net Fetch

**Constraint flag**: never make network fetch calls or web requests.

When this skill is active, the agent may NOT:
- Make HTTP/HTTPS requests
- Fetch remote URLs
- Download packages or dependencies
- Call external APIs
- Use web search or extraction tools

The agent MAY:
- Work with local files and data
- Run local commands
- Process existing downloaded content

## When to use

- Offline or air-gapped environments
- When network access could introduce security risks
- During deterministic local-only operations
- When reproducibility requires fixed local state

## Verification

- [ ] No network calls made during execution
- [ ] Only local files and commands used
- [ ] All operations succeed offline
