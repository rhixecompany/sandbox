---
name: mcp-codex
title: MCP Codex — OpenAI Codex CLI Integration
description: Exposes all Codex MCP tools for creating and continuing AI coding sessions via OpenAI Codex CLI. Includes test cases per tool.
version: 1.0.0
author: OWL
license: MIT
tags:
  - mcp
  - codex
  - openai
  - coding-agent
---
# MCP Codex

Integrates [OpenAI Codex CLI](https://github.com/openai/codex) as an MCP server. Allows spawning Codex sessions and continuing them programmatically.

## Overview

Automated reasoning and workflow tool for `mcp-codex`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Prerequisites

- MCP server: `codex` must be enabled (`hermes mcp list` → `✓ enabled`)
- Config: `codex mcp-server`
- Codex CLI must be installed and authenticated

## Tools

| Tool | Description |
|------|-------------|
| `codex` | Start a new Codex coding session with configuration parameters |
| `codex_reply` | Continue an existing Codex conversation by thread ID |

## Workflow

### Phase 1: Verify

```
hermes mcp test codex
```

### Phase 2: Use Tools

**Start new session:**
```
codex(
  prompt: "Create a Python function to calculate fibonacci numbers",
  model: "gpt-4o"  # optional, defaults to configured model
)
```

**Continue existing session:**
```
codex_reply(
  thread_id: "abc-123",
  prompt: "Now add memoization"
)
```

### Phase 3: Test Cases

```bash
# 1. Connectivity
hermes mcp test codex

# 2. Quick session (read-only — no file modifications)
# Call: mcp_codex_codex(prompt="Write a one-line bash command to count files", auto_apply=false)

# 3. The session ID from (2) can be used to continue
# Call: mcp_codex_codex_reply(thread_id="<id-from-step-2>", prompt="Add -la flags")
```

## Best Practices

1. **Use `auto_apply=false` for exploration** — preview changes before applying
2. **Keep thread IDs** between `codex` and `codex_reply` for continuity
3. **Set specific goals** in the prompt — Codex works best with well-scoped tasks
4. **Check Codex auth status** first: `hermes auth list | grep codex`
5. **Use with `terminal` tool** for file operations outside the sandbox

## Pitfalls

- Requires active Codex CLI OAuth session — re-auth with `hermes auth` if expired
- Threads are ephemeral in some configurations — save output if you need it
- Long-running sessions may timeout — set explicit scope in the initial prompt
- Codex has its own sandbox — files written by Codex may not be on the host filesystem
- Model selection is constrained by what Codex CLI supports

## Verification Checklist

- [ ] `hermes mcp test codex` passes
- [ ] `codex` starts a session and returns a thread ID
- [ ] `codex_reply` continues the session
- [ ] Codex OAuth is active (`hermes auth list` shows codex credentials)

## When to Use


- When you need to perform MCP Codex — OpenAI Codex CLI Integration operations or tasks
- When managing MCP Codex — OpenAI Codex CLI Integration infrastructure or configurations
- When automating or debugging MCP Codex — OpenAI Codex CLI Integration workflows
- **Triggers**: "mcp codex — openai codex cli integration" required for a project
