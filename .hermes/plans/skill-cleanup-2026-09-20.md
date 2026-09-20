# Plan: Skill registry cleanup and duplicate consolidation

**Feature**: Skill registry cleanup and duplicate consolidation (scope: docs/scope/skill-cleanup.md; spec: docs/specs/skill-cleanup.md).
**Pipeline**: scope (created) → architect (spec created) → audit (inspection evidence) → develop (confirm installations) → cleanup (duplicate delete) → verify (gate check).

## Phases (sequential, with gates)

### Phase A: Inspect remaining skills (gate: all inspected or skipped with reason)
- Inspect timeout skills: `architect`, `audit` (jsmastery-pro); `vercel-composition-patterns`, `vercel-deploy`, `vercel-optimize` (vercel-labs)
- Gate: inspection results saved; timeouts preserved honestly

### Phase B: Confirm install per identifier (gate: user confirms each batch)
- Non-timeout batch 1: `check`, `debug`, `develop` (jsmastery-pro); `deploy-to-vercel`, `vercel-cli-with-tokens` (vercel-labs)
- Ask per-identifier: confirm install of each (use clarify tool; ≤5 q/turn)
- Gate: at least one confirmed or explicitly skipped

### Phase C: Install confirmed skills (gate: exit 0 from each install)
- `hermes skills install -y --force --category CATEGORY <identifier>` for each confirmed
- Record exit code (real, not fabricated)

### Phase D: Duplicate triage and delete (gate: profile-dir only best versions)
- Compare names at `$HERMES_HOME/skills/` (162 installed) vs new installs
- Best = profile-dir match; profile-dir currently empty; best = hub-installed match with same identifier
- Confirm best version per duplicate group; delete extras
- Gate: `find` or `ls` shows no duplicate names; real exit codes

### Phase E: Verify and document (gate: evidence complete; 0 synthetic)
- Audit: `hermes skills audit` or manual comparison
- Scope/plans/specs verified (docs/scope/skill-cleanup.md, docs/specs/skill-cleanup.md, .hermes/plans/skill-cleanup-<ts>.md)
- Memory: context saved
- `.env` untouched; identity DRY preserved
- No synthetic session IDs / capabilities / rankings
