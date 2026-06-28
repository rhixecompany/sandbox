---
name: dispatching-parallel-agents
description: Scan, dispatch, and process work across multiple agent platforms in parallel batches. Use when coordinating work across Hermes, Copilot, and Codex agents simultaneously.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - parallel
  - agents
  - orchestration
  - workflow
---

# Dispatching Parallel Agents

Scan, dispatch, and process work across multiple agent platforms in parallel batches. Use when coordinating agents across Hermes, Copilot, and Codex simultaneously.

## Workflow

1. **Inventory** — Discover agent files across all platforms
2. **Map** — Build cross-reference table of equivalent agents
3. **Dispatch** — Delegate work to parallel sub-agents
4. **Collect** — Gather results from each agent
5. **Verify** — Validate consistency across platforms

## Usage

```bash
# Dispatch parallel agent tasks
dispatching-parallel-agents --platforms hermes,copilot,codex

# Scan agents in parallel
dispatching-parallel-agents scan --all
```

## Verification

- [ ] All platforms discovered and reachable
- [ ] Parallel execution completes within timeout
- [ ] Results collected and cross-referenced
- [ ] No platform drift after sync
