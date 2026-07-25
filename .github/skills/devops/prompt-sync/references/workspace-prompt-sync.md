# Workspace Prompt Sync — Reference

Concrete manifest schema and sync checklist for `prompt-sync` operations.

## Triage Manifest Schema

Place at `docs/prompt-sync-manifest.md`. Structure:

```markdown
# Prompt Sync Triage Manifest

> Generated: <ISO_TIMESTAMP> | Updated: <ISO_TIMESTAMP>

## Sync State Summary

| Artifact | Root Count | .github Count | Status |
|----------|-----------|--------------|--------|
| prompts/ | N | N | ❌ Missing / ✅ Synced / ⚠️ Partial |
| plans/ | N | N | ... |
| scripts/ | N | N | ... |
| hooks/ | N dirs (N files) | N dirs (N files) | ... |
| templates/ | N | N | ... |
| skills/ | ... | ... | ... |

## Action Taken

1. **area/** — N files copied to `.github/area/`
2. ...

## Verification

- [ ] Counts match between root and .github for each synced artifact
- [ ] No __pycache__ or .git artifacts included
- [ ] Dangling template/prompt references resolved
```

## Sync Checklist

Before mirroring:

1. ✅ **Inventory current state** — Count files in both root and .github for each artifact category. Record in manifest.
2. ✅ **Identify gaps** — Skip categories already in sync. Only copy missing files/dirs.
3. ✅ **Exclude runtime artifacts** — `__pycache__`, `.git`, `.DS_Store`, `*.pyc`
4. ✅ **Handle templates** — If root `templates/` is empty, check `.github/prompts/templates/` — template content may live there instead.
5. ✅ **Verify after sync** — Confirm destination counts match root. Re-check any prompt references that the orchestrator depends on.

## Common Sync States Found

| State | Meaning | Action |
|-------|---------|--------|
| Root=N, .github=N | Already synced | Skip |
| Root=0, .github=0 | No content exists | Skip (note in manifest) |
| Root>0, .github=0 | Gap — not yet synced | Copy |
| Root=N, .github>N | .github has extras | Check if from prior sync; leave as-is |

## Pitfall: Redundant Overwrite

Mirroring all folders blindly (without triage) can overwrite files in .github that match the root — harmless but wasteful. Worse, it can overwrite .github-only additions that were never in the root (e.g. hand-tuned workflow files). Always triage first.
