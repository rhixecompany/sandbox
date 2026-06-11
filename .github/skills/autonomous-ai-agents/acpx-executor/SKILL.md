---
name: acpx-executor
title: ACPX Universal Executor
description: "Execute a prompt via any ACPX provider (qwen, copilot, opencode) — single unified interface, correct CLI per provider."
version: 1.1.0
author: Alexa
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ACPX, Dispatch, Universal-Executor, Agent-Orchestration]
    related_skills: [qwen-code, copilot-cli, opencode, acpx-agent-routing]
---
## Goal
Execute a prompt via any ACPX provider (qwen, copilot, opencode) — single unified interface, correct CLI per provider.


# ACPX Universal Executor

Dispatch a prompt to any ACPX provider via its correct CLI invocation — one pattern per provider, no flags to remember.

## Workflow
### Phase 1: Preparation

- Understand the context and requirements.
- Gather necessary tools and resources.

### Phase 2: Execution

- Perform the core actions required by the skill.
- Apply the techniques and procedures outlined.

### Phase 3: Verification

- Verify the results against the expected outcomes.
- Confirm that the task has been completed successfully.


## When to Use

- User says "run via qwen" / "use copilot" / "send to opencode"
- You know the target provider and need the correct CLI syntax
- Quick one-shot prompt to an ACPX coding agent

## When NOT to Use

- Need to choose the best agent for a task → use `acpx-agent-routing`
- Need per-provider setup/auth/install → use `qwen-code`, `copilot-cli`, or `opencode`
- Need parallel multi-agent execution → use `dispatching-parallel-agents`

## Provider CLI Reference

**Primary pattern:** `acpx <agent> exec '<prompt>'` — uses the ACPX binary (v0.10.0+) to dispatch prompts.  
**Fallback:** Direct CLI per provider for when `acpx` is unavailable.

| Provider | ACPX Exec (Primary) | Direct CLI (Fallback) | Timeout | Notes |
|----------|--------------------|----------------------|---------|-------|
| qwen | `acpx --approve-all --timeout 30 qwen exec '{prompt}'` | `QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo '{prompt}'` | 30s ACPX / 300s direct | OpenRouter auth. `--yolo` mandatory. 30s OK for smoke tests; increase to 120s+ for real tasks, 300s+ for multi-repo architecture analysis. |
| copilot | `acpx --approve-all --timeout 30 copilot exec '{prompt}'` | `copilot -p '{prompt}'` | 30s ACPX / 60s direct | Auto model (no --model flag needed). GH_TOKEN auth. ~50 premium reqs/week cap. |
| opencode | `acpx --approve-all --timeout 60 opencode exec '{prompt}'` | `opencode run '{prompt}' --model opencode/big-pickle` | 60s ACPX / 300s direct | Provider-agnostic (when working). Cost-guard may block — fall back to qwen. Direct needs `--model opencode/big-pickle`. |

**Prompt quoting:** always single-quote the prompt to prevent shell expansion.

### Verified Examples

```bash
# Qwen via ACPX
acpx --approve-all --timeout 30 qwen exec "whoami, what folder are you currently in, what shell is this"

# OpenCode via ACPX
acpx --approve-all --timeout 60 opencode exec "whoami, what folder are you currently in, what shell is this"

# Copilot via ACPX (auto model)
acpx --approve-all --timeout 30 copilot exec "whoami, what folder are you currently in, what shell is this"
```

### Chaining via `{then}`

Use `&&` to chain follow-up commands after the initial task completes:

```bash
# ACPX chaining
acpx --approve-all --timeout 60 opencode exec 'write tests for auth' && acpx --approve-all --timeout 60 opencode exec 'fix any failures'

# Direct CLI chaining (qwen)
QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo 'write tests for auth' && QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo 'fix any failures'

# Direct CLI chaining (opencode)
opencode run 'write tests for auth' --model opencode/big-pickle && opencode run 'fix any failures' --model opencode/big-pickle

# Direct CLI chaining (copilot)
copilot -p 'write tests for auth' && copilot -p 'fix any failures'
```

## Procedure

1. **Identify provider** — qwen, copilot, or opencode
2. **Prefer ACPX exec** — use `acpx --approve-all --timeout <N> <agent> exec '{prompt}'`
3. **Fallback to direct CLI** — if `acpx` unavailable, use provider-specific direct command
4. **Substitute prompt** — wrap in single quotes
5. **Set timeout** per table defaults; increase to 120s+ for deep file analysis, 300s+ for multi-repo architecture synthesis
6. **Execute** via `terminal(command=..., timeout=...)`
7. **Verify** — check output for expected results or error signals; match known failure signatures in `references/acpx-failure-modes.md`
8. **Fallback provider** — if provider rate-limited/fails, retry with another
9. **All-agents failure** — if every agent fails, skip fallback chaining and switch to direct tools immediately (see All-Agents-Failed Recovery below)

## Fallback Chain

| Primary | Fallback 1 | Fallback 2 |
|---------|-----------|------------|
| copilot | qwen | opencode |
| opencode | qwen | copilot |
| qwen | opencode | copilot |

### User's Preferred Dispatch Order

When no task-type-specific routing guidance exists (i.e. the user says "use ACPX" without naming a specific agent), dispatch in this order:

1. **copilot** — fastest for prompts under 3 files, read-only verification, quick explanations
2. **opencode** — architecture, design, code generation, code review (when not blocked by cost-guard)
3. **qwen** — deep file analysis, cross-repo synthesis, fallback when others are unavailable/rate-limited

This differs from the per-provider fallback chain above (which shows what happens when a specific primary agent fails). The dispatch order is the sequence to try when starting from scratch with no designated primary.

### Copilot Dispatch Tips

- Copilot CLI's `-p` mode scans files in the background before responding. For prompts referencing 3+ repos or 100+ files, it will likely timeout at the 60s default — the I/O scan delays the actual reasoning.
- **Keep copilot prompts narrow**: one repo, one file, or one specific question. Avoid multi-repo analysis or bulk enumeration.
- For multi-repo work, skip copilot and go direct to qwen with a 300s timeout, or break into one-repo-at-a-time prompts.
- **Partial output recovery**: When copilot times out (exit 124), its stdout/buffer still contains the file-scanning reconnaissance it performed before the clock ran out — `search_files` results, `read_file` contents, settings inspection, and environment probing. **Do not discard this output.** Review it for gathered data and use it to write the deliverable manually. The agent's exploration phase completes before the reasoning phase — the data it found is valid even though it didn't finish analyzing it. This is especially useful for Django settings inspection, requirements review, and code structure surveys where copilot's grep/glob exploration is the expensive part but the analysis you can do yourself.

## Per-Provider Pitfalls

- **copilot** — rate limited ~50/week. When exhausted, CLI returns rate-limit errors. Fall back immediately. Always uses `auto` model.
- **copilot** — ACPX agent context can resolve the wrong file path (drive letter mismatch: `SandBox/` vs `Sandbox/`, or finds a docs copy instead of the real project). Always verify the path an ACPX agent resolves against the actual worktree before trusting its findings.
- **qwen** — direct CLI requires `--yolo` headless flag + `QWEN_CODE_SUPPRESS_YOLO_WARNING=1`. ACPX exec handles this automatically.
- **opencode** — direct CLI model names require `opencode/` prefix (`opencode/big-pickle`, not `big-pickle`). ACPX uses default model.
- **opencode** — can fail with `[cost-guard]` JSON parse errors when provider enforces spend limits. The non-JSON status line breaks the NDJSON parser. No recovery from the agent side — fall back to another provider or direct execution.
- All — timeouts too short cause silent failures. Use table defaults. There are TWO distinct timeout scenarios:
  - **Deep file analysis** (globbing 500+ files): increase to 120s+. The agent reads every file before responding, so the file count drives the timeout. Switch to `search_files`/`read_file` directly if >500 files.
  - **Complex architecture reasoning** (multi-project synthesis, cross-repo planning): increase to 300s+. Even 180s can be insufficient when the agent analyzes 3+ repos and synthesizes an architecture plan. Break into smaller focused prompts (one repo at a time) if timeout persists — the agent's reasoning depth, not file I/O, is the bottleneck.
- All — file-scoped context: qwen uses `@path`, opencode uses `-f path`, copilot doesn't support file scoping.
- All — **ACPX agents are unreliable for file I/O.** Qwen Code may degrade existing files (wrapping content in code blocks instead of proper conversion). OpenCode may analyze fully but fail to write output. **Workaround:** use ACPX agents only for analysis, review, and verification. Handle file writes/edits yourself with patch/write_file. Copilot CLI is safest for read-only verification since it can't write files.

## All-Agents-Failed Recovery

When every ACPX agent fails in a single session (e.g. qwen timeout, opencode cost-guard parse error, copilot wrong path), do NOT cycle the fallback chain — all providers share the same fundamental limitations:

1. **Switch to direct implementation** immediately — use `search_files`, `read_file`, `write_file`, `patch`, and `terminal` directly
2. **Do the file analysis yourself** — ACPX agents can't handle 500+ file globs without timeout
3. **Document gaps** — note what the ACPX agents failed to do so the user knows what they missed
4. **Reserve delegation** for reasoning-heavy subtasks (architecture decisions, code review of specific files) — never for bulk file enumeration

This pattern is also documented in `dispatching-parallel-agents` (Subagent Timeout → Direct Implementation section).

## Read-Only vs Read-Write Guidance

| Task Type | ACPX Agent OK? | Recommended Tool | Timeout Hint |
|-----------|---------------|------------------|-------------|
| Quick explanation (<3 files) | ✅ Yes | Copilot CLI (fastest) | 30s |
| Prompt analysis | ✅ Yes | OpenCode | 60s |
| Shallow code review (single file) | ✅ Yes | Copilot CLI | 30s |
| Deep codebase analysis (500+ files) | ❌ No — agents glob all files pre-analysis, timeout guaranteed >60s | Use search_files/read_file/terminal directly | — |
| File writing / editing | ❌ No — degrades content | Use patch/write_file directly | — |
| Bulk text conversion | ❌ No — wraps in code blocks | Use execute_code or direct tools | — |
| Report generation | ⚠️ May fail silently | Write report yourself after analysis | — |
| Verification / smoke test (<5 files) | ✅ Yes | Copilot CLI | 30s |
| **Multi-repo architecture synthesis** (3+ repos) | ⚠️ Edge — timeout risk high | Use qwen with 300s+ timeout, OR break into one-repo-at-a-time prompts with 120s each | 300s+ or split |
| **Cross-file analysis** (10-50 files) | ✅ Yes | Qwen Code | 120-180s |

## Verification

Smoke test per provider (ACPX exec method):

```bash
acpx --approve-all --timeout 30 qwen exec 'Reply: QWEN_OK'           → exit 0, contains QWEN_OK
acpx --approve-all --timeout 30 copilot exec 'Reply: COPILOT_OK'     → exit 0, contains COPILOT_OK (or rate-limit msg)
acpx --approve-all --timeout 60 opencode exec 'Reply: OPENCODE_OK'   → exit 0, contains OPENCODE_OK
```

Direct CLI equivalents:

```bash
QWEN_CODE_SUPPRESS_YOLO_WARNING=1 qwen --yolo 'Reply: QWEN_OK'      → exit 0, contains QWEN_OK
copilot -p 'Reply: COPILOT_OK'                                       → exit 0, premium req counted
opencode run 'Reply: OPENCODE_OK' --model opencode/big-pickle       → exit 0, contains OPENCODE_OK
```
