# Hermes vs OpenCode Platform Mapping Guide

**Session Reference:** May 2026 enhance-markdown execution on Hermes. Clarifies how to translate OpenCode-centric skill specs to Hermes `delegate_task` equivalents.

## Platform Differences

| Aspect | OpenCode | Hermes |
| --- | --- | --- |
| **Subagents** | Named agents in `.opencode/agents/*/*.md` | `delegate_task(goal="...")` with toolsets |
| **Planning System** | Plugin API: `createPlan()`, `readPlan()`, `appendSpec()` | `plans-and-specs` skill + companion markdown (optional CLI: `hermes plans`) |
| **Environment Check** | Agent readiness probes built into spec | Manual check: `hermes skills list` or try-catch on tool calls |
| **Parallel Execution** | Up to N concurrent agents via platform | `delegate_task` with `tasks=[...]` array; limited by `delegation.max_concurrent_children` config |
| **Tool Invocation** | Direct API calls, no shell | `terminal`, `patch`, `search_files`, `read_file`, `write_file` tools |

## Subagent Mapping Examples

### Phase 1 — Catalog & Audit

**OpenCode:**
```
delegate codebase-locator → forward/reverse scan
delegate codebase-analyzer → batch read & analyze
```

**Hermes equivalent:**
```
delegate_task(goal="Phase 1 Step 1.2: Dependency scan for {file}",
  toolsets=["file","search_files"])

delegate_task(tasks=[
  {"goal":"Audit files {file1-7} for formatting/content/structural issues", 
   "toolsets":["file","search_files","terminal"]},
  {"goal":"Audit files {file8-14} for issues",
   "toolsets":["file","search_files","terminal"]},
  {"goal":"Audit files {file15-21} for issues",
   "toolsets":["file","search_files","terminal"]}
])
```

### Phase 2 — Plan & Fix

**OpenCode:**
```
opencoder → plan authoring + fix application via `createPlan()`, `appendSpec()`, `editFile()`
```

**Hermes equivalent:**
```
# Plan authoring:
write_file(path="thoughts/plans/{purpose}-debug.md", content="...")

# Fix application:
patch(mode="replace", path="{file}", old_string="...", new_string="...")

# Batch execution (optional — can also apply fixes directly):
delegate_task(goal="Apply fixes to batch 1 (Critical items) from {purpose}-debug.md",
  toolsets=["file","patch","terminal"])
```

### Phase 3 — Execute Remaining

**OpenCode:**
```
openagent → execute pending plan items
```

**Hermes equivalent:**
```
# Direct execution (simple cases):
patch(mode="replace", path="{file}", old_string="...", new_string="...")

# Batch execution (for ≤7 files):
delegate_task(goal="Execute {N} pending fixes from {purpose}-debug.md, verify each",
  toolsets=["file","patch","terminal"])
```

### Phase 4 — Verify

**OpenCode:**
```
openagent → independent re-read verification
```

**Hermes equivalent:**
```
# Direct re-read via read_file + analysis:
read_file(path="{file}")

# Batch verification (optional):
delegate_task(goal="Re-read & verify {N} files against original issues list from {purpose}-issues-context.md",
  toolsets=["file","terminal"])
```

## Hermes Environment Readiness

### Check for plans-and-specs Skill

```bash
hermes skills list | grep -E "plans-and-specs|planning"
```

If output contains `plans-and-specs`, the skill is available. Companion markdown (`thoughts/plans/{purpose}-debug.md`) is always safe to use regardless.

### Check for Plugin Planning CLI

```bash
hermes plans help 2>&1 || echo "Plugin CLI not available"
```

If this returns usage text, plugin CLI is available. If not, use companion markdown only.

### Verify Patch Tool

```bash
# No direct check needed — patch tool is built-in.
# Verify by attempting a small patch (will error if not available).
```

## Toolset Capabilities by Phase

### Phase 1 — Catalog & Audit (read-only)

| Toolset | Use | Phase 1? |
| --- | --- | --- |
| `file` | Read file contents | ✅ Yes |
| `search_files` | Find files by pattern, grep contents | ✅ Yes |
| `terminal` | Run bash commands (grep, find, wc) | ✅ Optional |
| `patch` | Edit files | ❌ No |

**Minimum for Phase 1:** `file`, `search_files`

### Phase 2 — Plan & Fix (write-allowed)

| Toolset | Use | Phase 2? |
| --- | --- | --- |
| `file` | Read/write files | ✅ Yes |
| `patch` | Apply targeted fixes | ✅ Yes (primary) |
| `terminal` | Verify fixes via grep/diff | ✅ Yes (verify) |
| `search_files` | Find related files | ✅ Optional |

**Minimum for Phase 2:** `file`, `patch`

### Phase 3 — Execute (write-allowed)

Same as Phase 2 — fixes continue via `patch` + verification via `terminal`.

### Phase 4 — Verify (read-only)

| Toolset | Use | Phase 4? |
| --- | --- | --- |
| `file` | Re-read current file state | ✅ Yes |
| `search_files` | Cross-check references | ✅ Optional |
| `terminal` | Run verification commands | ✅ Optional |
| `patch` | Edit files | ❌ No |

**Minimum for Phase 4:** `file`

## Companion Markdown Plan Format

When plugin system is unavailable, write fix plan to `thoughts/plans/{purpose}-debug.md`:

```markdown
# {purpose} — Fix Plan

Generated: {date}

## Objective

{1-2 sentence description}

## Fix Items

### Batch 1 — Proof of Concept

- [ ] {issue-id}: {file} — {description} [Priority: Critical]
- [ ] {issue-id}: {file} — {description} [Priority: Major]

### Batch 2

- [ ] {issue-id}: {file} — {description} [Priority: Major]

## Progress

### Batch 1 ✅ Passed

Applied 3 critical fixes to convert-plaintext-to-md.prompt.md
- [x] CNT-001: Added --header to Inputs
- [x] STR-001: Updated Phase 2 Step 3 with all parameters
- [x] CNT-003: Clarified idempotent behavior rule
```

Track completion by marking items `[x]` as fixes are applied. This is the authoritative progress log when plugin system is unavailable.

## Batch Sizing Conventions

**Phase 1 (analysis):** Batch = 7 files per concurrent task (up to 3 concurrent batches)
- Rationale: Balance parallelism vs context window usage

**Phase 2 (fixes):** Batch = 7 files per `delegate_task` call
- Rationale: Batch 1 is proof-of-concept gate; Batch 2+ continue in sequence
- Batch 1 must complete fully before Batch 2 starts (no parallelism for fixes to avoid cascading failures)

**Phase 3 (execute remaining):** Continue in sequence with batch size ≤7 (sync not required)

**Phase 4 (verify):** Up to 3 concurrent verification batches if batch size ≤7

## Common Pitfalls

### Pitfall: Assuming Plugin CLI Always Available

**Problem:** Skill spec uses `createPlan()` API without fallback.

**Solution:** Check `hermes skills list` first. If `plans-and-specs` is present, try the plugin CLI; if not, use companion markdown only. Always write companion markdown as well to avoid losing the plan state.

### Pitfall: Trying to Use OpenCode Agent Names in Hermes

**Problem:** Copying agent names like `codebase-analyzer` directly into Hermes without mapping.

**Solution:** Use the mapping table (Subagent Mapping Examples above) to translate OpenCode agent names to Hermes `delegate_task` calls with appropriate toolsets.

### Pitfall: Batch Size > 7 in Phase 2 Fixes

**Problem:** Applying too many fixes in a single batch, making it hard to isolate failures.

**Solution:** Respect the 7-file batch limit. Batch 1 is proof-of-concept (verify before continuing). Batch 2+ can proceed on failure, but batch size should never exceed 7.

### Pitfall: Verifying Against Phase 2/3 Artifacts in Phase 4

**Problem:** Reading the fix plan before re-reading the original issues — introduces confirmation bias.

**Solution:** In Phase 4 Step 4.1, read ONLY Phase 1 outputs (`docs/{purpose}-context.md`, `docs/{purpose}-issues-context.md`) before verifying. Read Phase 2/3 artifacts only after the independent re-read check is complete.

## Session Reference

**Executed:** May 2026, claude-haiku-4.5 via GitHub Copilot.

**Session outcome:**
- All 6 `.github/prompts/*.prompt.md` files audited (20 issues)
- 14/20 issues fixed in Phases 2-3
- 6/20 minor issues remaining (non-blocking, accepted as partial)
- Phase 4 verification complete, production-ready recommendation

**Key decision:** Fell back to companion markdown when Hermes CLI didn't expose `hermes plans` command despite skill being available. Companion markdown proved sufficient for tracking batch progress and fix completion.
