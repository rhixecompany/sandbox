# Agent / Provider Matrix Runner Implementation Plan

**Date:** 2026-08-28  
**Status:** in-progress  
**Primary goal:** Build a noninteractive runner that executes the same request across every installed Hermes profile and every authorized provider, while reading `packages/**/*` to derive package capability context and emitting normalized result artifacts.

---

## Why this exists

We already have provider-audit skills and provider workflow research. What is missing is a concrete, reusable runner that:

- enumerates live provider auth from `hermes auth list`
- enumerates installed agents/profiles from `hermes profile list`
- scans the package tree for capability context
- runs requests without TTY interaction
- captures results in a machine-readable, repeatable format

This plan extends the existing provider workflow work instead of duplicating it.

---

## Planned Artifacts

| Artifact | Purpose |
|----------|---------|
| `.hermes/plans/specs/agent-provider-matrix-spec.md` | Detailed functional spec and output contract |
| `.hermes/plans/agent-provider-matrix.md` | Implementation checklist and status tracker |
| `prompts/agent-provider-matrix.prompt.md` | Reusable noninteractive prompt template |
| `scripts/agent_provider_matrix.py` | Main runner for inventory, execution, and reporting |
| `scripts/agent-provider-matrix-smokecheck.sh` | One-cell live validation helper |
| `docs/agent-provider-matrix.md` | User-facing usage + output schema |
| Hermes skill `agent-provider-matrix-runner` | Reusable workflow wrapper for future sessions |

---

## Execution Phases

### Phase 1 — Inventory and design

- [x] Verify existing overlap with provider workflow plans and skills
- [x] Read `packages/**/*` and inventory the two package families
- [x] Collect `hermes auth list` output
- [x] Collect `hermes profile list` output
- [x] Draft spec and plan files
- [ ] Confirm the output contract for result rows

### Phase 2 — Prompt and runner

- [x] Create `prompts/agent-provider-matrix.prompt.md`
- [x] Implement `scripts/agent_provider_matrix.py`
- [x] Add dry-run mode and stable ordering
- [x] Add package capability extraction heuristics
- [x] Add report generation (JSON + Markdown)
- [x] One-cell live validation (`scripts/agent-provider-matrix-smokecheck.sh`)

### Phase 3 — Skill packaging

- [ ] Create Hermes skill `agent-provider-matrix-runner`
- [ ] Add reference material for output schema and heuristics
- [ ] Link the skill to the repo prompt and runner script

### Phase 4 — Verification

- [ ] `python -m py_compile scripts/agent_provider_matrix.py`
- [ ] `scripts/agent_provider_matrix.py --dry-run` succeeds
- [ ] Inventory counts match the live Hermes CLI output
- [ ] Result artifacts are written to `.hermes/plans/results/`
- [ ] Skill loads successfully and references the script correctly

---

## Implementation Notes

- Use Hermes CLI as the source of truth for live auth and profile inventory.
- Treat `packages/**/*` as capability context, not as credentials or secrets.
- Prefer one Python runner over separate TS/Python runners; the job is orchestration, not SDK showcase.
- Keep live provider calls optional behind a flag so validation can run safely in dry-run mode.
- The prompt file should be the only place that defines the user-facing response shape.

---

## Dependencies and Constraints

- Hermes CLI must be available on PATH.
- The runner must work on Windows Git Bash/MSYS paths.
- Result files must avoid secrets and redact any accidental token-like strings.
- Provider defaults may differ, so the effective model must be captured per run.

---

## Verification Gates

### Gate A — Inventory correctness

- `hermes auth list` parsed successfully
- `hermes profile list` parsed successfully
- package capability summaries generated for both packages

### Gate B — Runner correctness

- prompt file loads cleanly
- dry-run prints commands and context without calling providers
- live mode executes a single pair without interactivity

### Gate C — Output correctness

- every result row includes provider, context, max-output, and capabilities
- markdown summary and JSON artifact are both written
- per-cell outputs are stable and repeatable

### Gate D — Skill correctness

- skill loads via `skill_view`
- skill references the repo prompt and runner script
- skill stays concise and defers details to references

---

## Open Questions

1. Should the default live matrix include the `default` profile, or should it only use named profiles?
2. Should live runs target every provider by default or require an explicit allow-list?
3. Do we want one combined summary report or one report per profile/provider pair plus a summary index?
4. Should package capability extraction be strictly heuristic, or should it also compare against source exports when possible?

---

## Status Tracker

- [x] Discovery complete
- [x] Live Hermes inventory captured
- [x] Spec drafted
- [x] Plan drafted
- [ ] Prompt created
- [ ] Runner implemented
- [ ] Skill created
- [ ] Verification passed
