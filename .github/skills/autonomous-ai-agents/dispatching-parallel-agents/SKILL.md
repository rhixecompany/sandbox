---
name: dispatching-parallel-agents
title: Dispatching Parallel Agents
description: Use when coordinating parallel subagents for concurrent tasks and orchestration.
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags:
      - imported
      - priority
    related_skills: []
---## Goal
coordinating parallel subagents for concurrent tasks and orchestration. to accomplish the associated tasks and objectives.


# Dispatching Parallel Agents

## Description

Use when coordinating parallel subagents for concurrent tasks and orchestration.

## When to Use

Use in **SandBox/Bash/ scripts** for parallel task orchestration when:

- Multiple independent tasks that can run simultaneously
- Tasks with no shared state or dependencies
- Parallel exploration or analysis
- Batch processing independent items
- Concurrent implementation of separate features
- **Multi-phase workflows requiring different specialized profiles** (e.g., code-architect for implementation, research-analyst for analysis, default for coordination)

Example: Delegate parallel audits of multiple projects, script validation across Bash/ subdirectories, or concurrent GitHub workflow updates.

## When NOT to Use

- Tasks with sequential dependencies
- Shared state between tasks
- Single task that needs focus
- Tasks requiring coordination

## Workflow

### Phase 1: Identify Independent Tasks

- List all tasks to be executed
- Verify no dependencies between tasks
- Confirm no shared state needed

### Phase 2: Plan Parallelization

- Group tasks by type
- Assign resources to each task
- Set up communication channels

### Phase 3: Dispatch Agents

- Create agent for each task
- Provide complete context to each
- Start all agents simultaneously
- **Profile-based dispatch** (when phases require specialized expertise):
  - Assign profile= parameter in delegate_task for each subagent
  - Example: `{"goal": "Phase 1: Catalog scripts", "context": "...", "profile": "research-analyst"}`
  - Profiles available: code-architect, research-analyst, exec-assistant, patient-tutor, creative-director, default

### Phase 4: Collect Results

- Wait for all agents to complete
- Aggregate results
- Handle any failures

## Tools & References

- **Related Skills**: subagent-driven-development
- **Parallelization**: spawn_agent tool
- **Coordination**: Minimal, tasks are independent
- **Profile Orchestration**: See `references/profile-orchestration-pattern.md` for multi-phase workflows requiring specialized profiles (code-architect, research-analyst, etc.)

## Best Practices

- Verify true independence before parallelizing
- Provide complete context to each agent
- Set reasonable timeouts
- Aggregate results clearly
- Log all agent activities
- Handle partial failures gracefully
- **Profile-specific orchestration**: When phases require different expertise (code vs analysis vs coordination), delegate each phase to the best-suited profile. Example: code-architect for TypeScript design, research-analyst for safety audits, default for final integration. Each subagent runs with its profile's specialized tools and SOUL.md preferences.

## Pitfalls & Recovery Patterns

### Subagent Timeout → Direct Implementation

**Problem**: Subagent delegation can timeout on large analysis/cataloging tasks (5+ min expected runtime). The default per-subagent timeout is 600s — reached when a subagent has too many projects/files to process.

**Symptom**: `delegate_task` returns `{"status": "timeout", "error": "Subagent timed out after 600.0s"}`.

**Recovery Pattern**:
1. Switch from delegation to direct implementation for remaining phases
2. Use `execute_code` for multi-step workflows with mechanical operations
3. Reserve delegation for true reasoning-heavy subtasks (not file enumeration)
4. Keep todo tracking active across both approaches

**When to Prefer Direct Implementation**:
- File enumeration, search, catalog tasks (deterministic, tool-heavy)
- Multi-file writes with templates (mechanical, no complex reasoning)
- Integration/verification steps (straightforward validation)
- **Bulk documentation generation** — 14+ projects × 15 files = 210 files is too much for delegation; use a standalone script via `terminal()` instead
- **Any operation touching 100+ files** — beyond that volume, the 50-tool-call ceiling inside `execute_code` makes per-file reads/writes unreliable; write a standalone Python script and run it via `terminal()`

**When to Keep Delegation**:
- Complex architectural design decisions
- Safety audits requiring judgment
- Code review with nuanced feedback
- Tasks benefiting from specialized profile perspective

**Example**: Repository migration with 14 projects — Phase 2 delegation timed out on the 8-project batch. Switched to `execute_code` for bulk documentation generation, completing all 210 files in ~120s vs 10+ minutes of delegation time.

### `hermes_tools` API Pitfalls in `execute_code`

**Problem**: The `terminal()` function from `hermes_tools` (used inside `execute_code` blocks) has a different return API than the root-level `terminal()` tool. When a command fails, the dict may not have an `output` key.

**Symptom**: `KeyError: 'output'` when accessing `result["output"]` after a command that errored or had shell substitution issues.

**Root Cause**: Failed commands (non-zero exit, shell parsing errors) can return a structurally different dict. The root-level `terminal()` tool always returns `{"output": ..., "exit_code": ...}`, but `hermes_tools` may omit the key on error.

**Prevention**:
```python
result = terminal("ls /nonexistent 2>/dev/null")
output = result.get("output", "")  # Use .get() not [] access
# OR: wrap in try/except
try:
    output = result["output"]
except (KeyError, TypeError):
    output = ""
```

**Also**: Complex shell-pipe chains (`cd X && for d in Y; do ...; done`) can fail inside `execute_code` when they'd work in a direct `terminal()` call. Prefer simple commands in `execute_code` and reserve complex shell pipelines for the direct `terminal()` tool.

### The 50-Tool-Call Ceiling in `execute_code`

**Problem**: Every `execute_code` block is capped at ~50 tool calls (`read_file`, `write_file`, `terminal`, `search_files`, `patch` — all count). After that threshold, subsequent calls fail silently — no error, just missing data. This makes bulk operations over 100+ files fundamentally unreliable inside `execute_code`.

**Symptom**: An `execute_code` block reports success with no errors, but output files are missing, truncated, or stale (reads return empty). Non-obvious because half the data may be present — the first ~50 calls work, the rest don't.

**Prevention**: For any operation touching more than ~40 files, skip `execute_code` entirely. Instead, write a standalone Python script to disk and run it via `terminal()`:

```python
# DON'T (unreliable beyond ~50 tool calls):
# execute_code with loops calling read_file/write_file for 176 files

# DO (no tool-call limit):
# 1. Write script to disk:
write_file("/tmp/fix_all.py", content)
# 2. Run it via terminal — no tool-call ceiling:
terminal("python3 /tmp/fix_all.py")
```

The standalone script reads/writes filesystem directly (`open()`/`os.walk()`). This bypasses the hermes_tools abstraction entirely and has no artificial ceiling.

**Path normalization on Windows**: When writing standalone Python scripts for a `terminal()` run, use `C:/path/to/file` (forward-slash Windows path) — `os.walk` on Windows returns backslash paths that must be normalized with `path.replace("\\\\", "/")` before building report filenames. The `/c/...` MSYS path format used in shell commands does NOT work with Python `os` functions.

**Recovery**: If you suspect a silent write failure inside `execute_code`, verify with a `terminal("ls | wc -l")` call immediately after. If counts are short, re-create files with the root-level `write_file` tool (outside execute_code) or switch to a standalone script.

### `write_file` Batch Limits in `execute_code`

**Problem**: `write_file` from `hermes_tools` can silently fail on some paths when called many times in a single `execute_code` block — especially with dotted directory names (e.g., `xamehi.tv/`) or after ~50+ cumulative tool calls.

**Symptom**: The `execute_code` block reports success with no errors, but some files are missing when verified afterward.

**Prevention**:
- **Always verify file writes** after an `execute_code` block with a check: `terminal("ls -la output/dir/ | grep '^-' | wc -l")`
- For projects with dots in names (`xamehi.tv`), verify files were created
- Batch writes into smaller `execute_code` blocks (under 50 writes per block)
- For critical writes, use the root-level `write_file` tool instead of `hermes_tools.write_file`
- Document expected file counts per project and verify against actuals

**Recovery**: When missing files are detected, re-create them with the root-level `write_file` tool (not `hermes_tools.write_file`). This tool reliably writes to any path.

## Overview

Parallel agent dispatching skill for coordinating concurrent subagent execution. Ensures task independence, provides complete context to each agent, and aggregates results with failure handling.

## Verification Checklist

- [ ] All parallel tasks are verified to be truly independent
- [ ] Each subagent receives complete, self-contained context
- [ ] Timeouts are set appropriately for each task
- [ ] Partial failures are handled gracefully without blocking other tasks
- [ ] Results are aggregated and clearly presented
