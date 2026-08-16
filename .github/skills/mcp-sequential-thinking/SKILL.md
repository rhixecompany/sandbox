---
name: mcp-sequential-thinking
title: MCP Sequential Thinking — Chain-of-Thought Reasoning
description: Exposes the sequential thinking MCP tool for structured, multi-step problem solving with dynamic thought revision. Includes test cases.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - reasoning
  - chain-of-thought
  - problem-solving
metadata:
  hermes:
    tags: []
---
# MCP Sequential Thinking

Provides structured chain-of-thought reasoning via the standard `@modelcontextprotocol/server-sequential-thinking`. Enables breaking down complex problems into sequential, revisable thoughts that build on each other.

## Overview

Automated reasoning and workflow tool for `mcp-sequential-thinking`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Prerequisites

- MCP server: `sequential-thinking` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `npx -y @modelcontextprotocol/server-sequential-thinking`

## Tools

| Tool | Description |
|------|-------------|
| `sequentialthinking` | Process a thought in a reasoning chain. Supports branching, revision, and dynamic adaptation. |

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thought` | string | The current thought content |
| `nextThoughtNeeded` | boolean | Whether more steps are needed |
| `thoughtNumber` | integer | Current position in the chain (1-indexed) |
| `totalThoughts` | integer | Estimated total steps needed |
| `branchFromThought` | integer (opt) | Branch from a previous thought ID |
| `branchId` | string (opt) | Branch identifier for parallel reasoning |
| `isRevision` | boolean (opt) | Whether this revises a previous thought |
| `revisesThought` | integer (opt) | Which thought ID this revises |

## Workflow

### Phase 1: Verify

```
hermes mcp test sequential-thinking
```

### Phase 2: Linear Chain

```
# Step 1: Define problem
sequentialthinking(
  thought: "We need to design a rate-limited API. Key requirements: 1000 req/min per user, burst up to 100, sliding window algorithm.",
  nextThoughtNeeded: true,
  thoughtNumber: 1,
  totalThoughts: 4
)

# Step 2: Consider approaches
sequentialthinking(
  thought: "Three approaches: token bucket, sliding window (Redis sorted sets), or fixed window. Sliding window is most accurate for our use case but costs more in Redis memory.",
  nextThoughtNeeded: true,
  thoughtNumber: 2,
  totalThoughts: 4
)

# Step 3: Make decision
sequentialthinking(
  thought: "Go with token bucket for simplicity — it handles bursts naturally and uses less Redis memory than sliding window log. Implement with Redis INCR + TTL per user key.",
  nextThoughtNeeded: true,
  thoughtNumber: 3,
  totalThoughts: 4
)

# Step 4: Implementation plan
sequentialthinking(
  thought: "Implementation: 1) Redis middleware checks token count, 2) Configurable rate limits per endpoint, 3) Return 429 with Retry-After header, 4) Add monitoring via rate limit metrics.",
  nextThoughtNeeded: false,
  thoughtNumber: 4,
  totalThoughts: 4
)
```

### Phase 3: Revision & Branching

```
# Revise a previous thought
sequentialthinking(
  thought: "Actually, re-evaluating: Redis sorted sets give us more precision per-user costs. For 10K users the memory is ~2MB, acceptable.",
  nextThoughtNeeded: false,
  thoughtNumber: 5,
  totalThoughts: 5,
  isRevision: true,
  revisesThought: 2
)

# Branch for alternative analysis
sequentialthinking(
  thought: "Alternative: What if we use local rate limiting with a shared Redis counter for distributed systems?",
  nextThoughtNeeded: false,
  thoughtNumber: 1,
  totalThoughts: 2,
  branchId: "alt-approach",
  branchFromThought: 1
)
```

### Phase 4: Test Cases

```bash
# 1. Connectivity
hermes mcp test sequential-thinking

# 2. Simple 2-step reasoning chain
# Call: mcp__sequential_thinking__sequentialthinking(
#   thought="The user wants to calculate 145 * 237. I'll break this down: 145 * 200 = 29000, 145 * 37 = 5365, total = 34365",
#   nextThoughtNeeded=true, thoughtNumber=1, totalThoughts=2
# )
# Call: mcp__sequential_thinking__sequentialthinking(
#   thought="Double-checking: 145 * 237 = 145 * (200 + 37) = 29000 + 5365 = 34365. Result is 34365.",
#   nextThoughtNeeded=false, thoughtNumber=2, totalThoughts=2
# )
```

## Best Practices

1. **Use `totalThoughts` as an estimate** — it's flexible, not fixed; revise as reasoning evolves
2. **Use `isRevision` + `revisesThought`** when correcting or refining — preserves full reasoning trace
3. **Use `branchId` + `branchFromThought`** for exploring alternatives — keeps the main chain clean
4. **One idea per thought** — atomic thoughts are easier to revise and branch from
5. **Set `nextThoughtNeeded: false`** on the final thought to signal completion
6. **Prefer this tool over verbose internal reasoning** when the reasoning itself is the deliverable

## Pitfalls

- No natural language understanding of context — must provide complete information each call
- `thoughtNumber` increments within a chain but resets for branches
- `branchId` must be unique per branch within a session
- Long chains with frequent revisions may exceed tool output limits
- The tool does NOT remember previous calls — it returns the full chain state each time for the agent to process

## Verification Checklist

- [ ] `hermes mcp test sequential-thinking` passes
- [ ] 2-step simple chain completes without errors
- [ ] `nextThoughtNeeded: false` correctly signals completion

## When to Use


- When you need to perform MCP Sequential Thinking — Chain-of-Thought Reasoning operations or tasks
- When managing MCP Sequential Thinking — Chain-of-Thought Reasoning infrastructure or configurations
- When automating or debugging MCP Sequential Thinking — Chain-of-Thought Reasoning workflows
- **Triggers**: "mcp sequential thinking — chain-of-thought reasoning" required for a project
