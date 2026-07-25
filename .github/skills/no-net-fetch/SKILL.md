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
title: No Net Fetch
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

## When to Use

- Offline or air-gapped environments
- When network access could introduce security risks
- During deterministic local-only operations
- When reproducibility requires fixed local state
- Combined with `introspection-only-general` for fully offline read-only mode

## When NOT to Use

- When you need to download packages, fetch APIs, or update dependencies
- When web search or extraction is required for the task

## Workflow

### Phase 1: Activate

Load this skill before any task that must not make network calls.

### Phase 2: Execute

Perform local operations only. No fetch, download, or API calls.

### Phase 3: Verify

Confirm all operations completed offline with no network access.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Foundational skill workflow |
| `validate-memories` | Memory validation (local only) |

## Verification

- [ ] No network calls made during execution
- [ ] Only local files and commands used
- [ ] All operations succeed offline

## Pitfalls

- Intent is advisory — the LLM can still call web tools; rely on disabling web toolsets for enforcement
- Some tools cache or log network metadata even without explicit fetch calls
- Combine with `introspection-only-general` for fully offline, read-only mode
- Not a security boundary — it's a behavioral constraint on the agent

## Verification Checklist

- [ ] All tasks completed
- [ ] Output verified
- [ ] Edge cases handled
- [ ] No network operations occurred
