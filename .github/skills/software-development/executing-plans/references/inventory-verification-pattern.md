# Inventory Verification Pattern

> Reusable pattern for verifying live system state before executing any implementation plan. Captured from 2026-06-16 unified ecosystem master plan execution.

## The Problem

Plan artifacts (`.hermes/plans/*.md`, audit reports, status tables) become stale. They describe *assumed* state, not *actual* state. Executing against stale assumptions leads to:
- "Fixing" things that already work (wasted effort)
- Missing things that silently broke since the plan was written
- Config mismatches (e.g., plan says hooks unregistered; reality says 4 active)

## The Pattern: Phase 0 — Inventory Verification

Before Phase 1 (Prepare Plan), insert a mandatory **Phase 0: Verify Live Inventory**.

### Standard Inventory Commands

| Domain | Command | Artifact Output | What It Verifies |
|--------|---------|-----------------|------------------|
| Hooks | `hermes hooks list` | `.hermes/plans/verification/hooks-list-<date>.txt` | Hook registration, approval status, event bindings |
| Plugins | `hermes plugins list` | `.hermes/plans/verification/plugins-list-<date>.txt` | Enabled/disabled plugins, versions, sources |
| MCP Servers | `hermes mcp list` | `.hermes/plans/verification/mcp-list-<date>.txt` | Server connectivity, tool discovery, transport |
| Skills | `hermes skills audit` | `.hermes/plans/verification/skills-audit-<date>.txt` | Skill health, blocking findings, verdicts |
| Files | `search_files`, `read_file` | Per-artifact verification | File existence, sizes, content freshness |

### Verification Artifact Naming

```
.hermes/plans/verification/
  hooks-list-YYYY-MM-DD.txt
  plugins-list-YYYY-MM-DD.txt
  mcp-list-YYYY-MM-DD.txt
  skills-audit-YYYY-MM-DD.txt
```

### Comparison Protocol

1. **Read plan assumptions** — Extract claimed state from the plan (e.g., "hooks unregistered")
2. **Run inventory command** — Capture live output to artifact
3. **Compare** — diff or manual review: does live match claimed?
4. **Document discrepancies** — Update plan with `✅ Verified`, `⚠️ Discrepancy: ...`, or `❌ Plan Stale`
5. **Decision** — Proceed, adjust plan, or halt for investigation

### Example: Hooks Verification (2026-06-16)

**Plan claimed:** "hooks scripts present; config registration unclear; `hermes hooks list` reports no shell hooks"

**Live inventory (`hermes hooks list`):**
```
Configured shell hooks (4 total):
  [on_session_end]    - session-auto-commit (approved 2026-06-16)
  [on_session_end]    - session-logger (approved 2026-06-16)
  [on_session_start]  - session-logger (approved 2026-06-16)
  [pre_llm_call]      - governance-audit (approved 2026-06-16)
```

**Resolution:** Plan was stale. Updated plan status: `Hooks → ✅ Complete — config mismatch resolved`

### When to Skip Phase 0

- **Never** for destructive/irreversible plans
- **Optional** for pure documentation/read-only plans (but still recommended)
- **Conditional** if a prior Phase 0 in the same session already verified the same domain and no mutations occurred since

## Integration with executing-plans Workflow

```
Phase 0: Verify Live Inventory First  ← NEW (this pattern)
Phase 1: Prepare Plan
Phase 2: Execute Phase 1
Phase 3: Review & Checkpoint (incl. Approval Gates)
Phase 4: Execute Remaining Phases
Phase 5: Verification (cross-reference pattern)
```

## Anti-Patterns to Avoid

| Anti-Pattern | Consequence | Fix |
|--------------|-------------|-----|
| Trust plan without verification | Fix non-issues, miss real issues | Always run Phase 0 |
| Verify only one domain | Blind spots in other domains | Run full inventory suite |
| Don't capture artifacts | No audit trail, can't diff later | Write to `.hermes/plans/verification/` |
| Compare from memory | Confirmation bias | Read plan claim, run command, diff explicitly |
| Proceed on "probably fine" | Silent failures | Require explicit `✅ Verified` or documented acceptance |