# Specification: Hermes Health Sweep

## Functional Requirements

### FR-1: Discovery Engine
- Enumerate all assets across 6 target categories (desktop, desktop-plugins, plugins, hooks, scripts, agents)
- For each asset, identify audit status (file exists, syntax, registration, score)
- Produce structured inventory at `~/.hermes/cache/sweep/<timestamp>/inventory.json`

### FR-2: Audit Pipeline
- Run `hermes doctor` → report status
- Run `hermes hooks doctor` → check allowlist sync
- Run `hooks-judge` → score 0-100 per hook
- Run `plugins-judge` → score 0-100 per plugin manifest
- Run `scripts-judge` → score 0-100 per script
- Run `agents-judge` (custom) → score 0-100 per agent profile
- Run desktop-plugin structural audit (custom, no judge exists) → pass/fail per plugin dir

### FR-3: Remediation Engine
- For each failure, classify: fixable / deprecated / orphan
- Apply targeted fix per remediation class:
  - Hook allowlist drift → re-allowlist
  - Missing CLI surface → add `argparse`/`getopts`
  - Bare `except:` → `except Exception as e:`
  - Missing module docstring → add
  - Duplicate imports → remove redundant
  - Broken plugin dir → quarantine (move, don't delete)
- Preserve rollback capability (no scripted mass-rewrite)

### FR-4: Verification Engine
- Re-run all judges after remediation
- Verify thresholds: hooks ≥95, plugins ≥95, scripts ≥70 (relaxed; baseline), agents ≥95
- Produce final score report at `~/.hermes/cache/sweep/<timestamp>/final.md`
- Update SESSION_REPORT.md with deltas

### FR-5: Reusable Skill Artifact
- Skill: `devops/hermes-health-sweep`
- Provides re-runnable scripts for: `sweep.sh`, `verify.sh`, `remediate.py`
- Documents the entire sweep workflow as a SKILL.md
- References all 6 target categories with judge invocations
- Verification checklist at end of skill

## Non-Functional Requirements

### NFR-1: Idempotency
- Re-running sweep must produce stable output (same delta each time)
- No state corruption on second run

### NFR-2: Performance
- Full sweep completes in ≤10 minutes for current Hermes instance (217 scripts, 12 plugins, 7 hooks)
- Parallel subagent dispatch where independent

### NFR-3: Safety
- No destructive operations without explicit approval (user has granted yolo for this session)
- All deletes go via quarantine directory first
- config.yaml edits use `hermes config set` not direct YAML

### NFR-4: Observability
- Each phase produces log file at `~/.hermes/cache/sweep/<timestamp>/phase-N.log`
- Final report includes: counts, scores, deltas, timestamps, exit codes

### NFR-5: Rollback
- All changes tracked in SandBox git repo
- `git checkout <previous-commit> -- <path>` restores state
- Hook allowlist has built-in revoke command

## Acceptance Criteria

| AC | Description | Verification |
|---|---|---|
| AC-1 | All 6 target categories audited | Inventory complete with counts per category |
| AC-2 | All hook warnings resolved | `hermes hooks doctor` reports 0 warnings |
| AC-3 | Scripts pass rate ≥92% (200/217) | scripts-judge reports passed ≥200 |
| AC-4 | Plugins maintain ≥95 | plugins-judge reports 12/12 ≥95 |
| AC-5 | Desktop-plugins have only runtime-valid plugins | All dirs contain plugin.js or are quarantined |
| AC-6 | All agents ≥95 | agents-audit reports 7/7 ≥95 |
| AC-7 | Skill artifact exists | `~/.hermes/skills/devops/hermes-health-sweep/SKILL.md` readable |
| AC-8 | SESSION_REPORT.md updated | File at SandBox root with session record |

## Out of Scope

- Touching skills/ directory contents (handled by separate skill-judge sweep)
- Updating `.github/prompts/` (handled by separate prompts-judge sweep)
- Modifying Hermes core code
- Network-dependent provider diagnostics