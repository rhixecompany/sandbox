# Direct Execution Pattern vs Subagent Delegation

Captured from dev-init pipeline execution (2026-05-27).

## When to Use Direct Execution Over Delegation

| Task Type | Approach | Rationale |
|-----------|----------|-----------|
| File enumeration, search, catalog | `execute_code` | Deterministic, no reasoning needed |
| Multi-file find/replace | `patch` or `execute_code` sweep | Surgical, idempotent |
| Phase tracking across 3+ phases | `todo` tool | Persistent progress display |
| Architecture design | `delegate_task` (code-architect) | Needs specialized reasoning |
| Safety audit | `delegate_task` (research-analyst) | Judgment calls, nuanced |
| Code review | `delegate_task` | Fresh perspective needed |

## Pipeline Execution Structure

```python
from hermes_tools import todo

todo([
    {"id": "p1", "content": "Phase 1: Analysis", "status": "in_progress"},
    {"id": "p2", "content": "Phase 2: Implementation", "status": "pending"},
    {"id": "p3", "content": "Phase 3: Validation", "status": "pending"},
])

for phase in phases:
    # Use execute_code for bulk analysis + patch for edits
    # Write phase report
    todo([{"id": phase["id"], "content": "...", "status": "completed"}], merge=True)
```

## Phase Documents

Each phase produces:
- `docs/dev-init-reports/phase{N}-{name}.md` — phase-specific results
- `.context.json` in `artifacts/context-maps/` — structured metadata

## Real-World Example 1: Dev-Init Pipeline

7 .txt files → 7 enhanced .md files in 6 phases:
- ~80 tool calls total (execute_code bulk + patch edits + report writes)
- ~15 min execution time for all 6 phases
- 0 constraint violations, 100% validation pass rate

## Real-World Example 2: Repo Migration (14 Projects)

Full multi-phase migration: inventory → docs generation → patch mapping → apply → verify

### Strategy: Delegate First, Execute Directly on Timeout

Phase 1 (inventory) → delegate_task (success, smaller scope)
Phase 2 (documentation generation for 14 projects) → delegate_task (first batch of 4 succeeds, 2nd batch of 8 times out after 600s each)
Timeout fallback → execute_code with loops generating all 210 files in ~120s

### Key Lessons

1. **Batch delegate_task into groups of 2-3** when each task involves 4+ projects. The 600s timeout is hit when a single subagent has too much to do.
2. **For bulk generation, skip delegation entirely** — `execute_code` with Python loops is faster and deterministic for mechanical multi-file writes.
3. **Always verify file counts** after `execute_code` blocks — `write_file` can silently fail on some paths (especially dotted dir names like `xamehi.tv/`).
4. **Recover missing files** using the root-level `write_file` tool, not `hermes_tools.write_file`.

### Phase Structure for Repo Migration

```python
from hermes_tools import todo, write_file, terminal

todo([
    {"id": "p1", "content": "Phase 1: Inventory", "status": "in_progress"},
    {"id": "p2", "content": "Phase 2: Documentation", "status": "pending"},
    {"id": "p3", "content": "Phase 3: Patch Plan", "status": "pending"},
    {"id": "p4", "content": "Phase 4: Apply Patches", "status": "pending"},
    {"id": "p5", "content": "Phase 5: Verify", "status": "pending"},
])

# Phase 1 — Use terminal directly for fast inventory
inv = terminal("ls -d projects/*/ && find . -name '*.patch'")
# Analysis in execute_code
# Report via write_file

# Phase 2 — execute_code for bulk generation
# (faster than delegation for deterministic work)

# Phase 3-5 — Direct terminal/file tools
# With todo progress tracking throughout
```

### API Pitfalls in execute_code

The `hermes_tools` wrapper functions have subtle differences from the root-level tools:

| Function | `hermes_tools` behavior | Root-level behavior |
|----------|------------------------|---------------------|
| `terminal()` | May omit `output` key on error; `.get("output", "")` safe | Always has `output` + `exit_code` |
| `write_file()` | May silently fail on dotted paths or near 50+ calls | Always succeeds |
| `search_files()` | Returns `{"matches": [...]}` | Same format |
| `read_file()` | Returns `{"content": "...", "total_lines": N}` | Same format |

**Rule**: In `execute_code` blocks, use `.get("output", "")` instead of `["output"]` for terminal results. Verify file writes afterward.

### Batch Size Limits

- **`delegate_task`**: max_concurrent_children=3 (for this user). Tasks beyond this must be queued in a second call.
- **`execute_code` write_file calls**: ~50 writes per block before risk of silent failure. Split large batches.
- **Root-level `write_file`**: No practical limit — use for critical paths, verify-heavy writes.
