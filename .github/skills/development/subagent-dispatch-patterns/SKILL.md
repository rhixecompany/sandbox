---
name: subagent-dispatch-patterns
title: "Subagent Dispatch Patterns"
description: "Patterns for dispatching delegate_task subagents: path resolution, context injection, file-writing discipline, and common pitfalls."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [delegation, subagent, dispatch, patterns, pitfall]
metadata:
  hermes:
    tags: [delegation, subagent, dispatch, patterns, pitfall]
    related_skills: [dispatching-parallel-agents, subagent-driven-development]
---

# Subagent Dispatch Patterns

Complements `dispatching-parallel-agents` and `subagent-driven-development` with cross-cutting patterns that apply to both.

## Key Patterns

### 1. Absolute Paths for File Writes

**Problem:** Subagents inherit their CWD from the project directory they're dispatched for. A relative path like `docs/build/` in context resolves to `projects/X/docs/build/`, not the workspace root.

**Fix:** Always pass fully-qualified absolute paths for write targets:

```
Instead of: docs/Project_Architecture/X.md
Use:        /c/Users/me/SandBox/docs/Project_Architecture/X.md
```

**Verification:** After the subagent completes, stat the expected absolute path. Subagent self-report of "wrote file.md" may mean the wrong location.

### 2. Inject Everything, Don't Reference Files

Subagents cannot read your loaded skills, plan files, or conversation history. Paste every detail inline in `context`.

### 3. Verify on Disk, Don't Trust Self-Reports

Subagents report success but may have written to wrong paths or created empty files. Always stat expected outputs before advancing.

### 4. Batched Dispatch Discipline

- Respect concurrency cap (max 3 per user)
- Drain a batch before starting the next
- Never dispatch two subagents writing to the same file

## Reference Files

- `references/dispatch-path-pitfall.md` — Detailed reproduction, root cause, detection, and recovery steps for the subagent relative-path trap observed during a multi-project blueprint generation run (2026-07-24)
