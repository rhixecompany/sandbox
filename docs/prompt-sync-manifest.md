# Prompt Sync Triage Manifest

> Generated: 2026-07-24T07:15+00:00 | Updated: 2026-07-24T07:18+00:00

## Sync State Summary

| Artifact | Root Count | .github Count | Status |
| ---------- | ----------- | -------------- | -------- |
| prompts/ | 211 | 211 | ✅ Synced |
| plans/ | 22 | 22 | ✅ Synced |
| scripts/ | ~106 | ~109 | ✅ Synced (+3 extra in .github) |
| hooks/ | 3 dirs (34 files) | 3 dirs (24 files) | ✅ Synced (excl __pycache__) |
| templates/ | 0 | 0 | ✅ N/A |
| skills/ | Partial | 3 dirs | ⚠️ Partial (not full mirror) |

## Action Taken

1. __plans/__ — 22 plan files copied to `.github/plans/`
2. __hooks/__ — 3 hook directories (governance-audit, session-auto-commit, session-logger) + lib.py/lib.sh copied to `.github/hooks/`
3. `__pycache__` dirs excluded (runtime artifacts)

## Verification

- [x] Plans: 22 files in `.github/plans/` match root count
- [x] Hooks: 24 files in `.github/hooks/` (3 dirs + lib files)
- [x] All prompts present and matching root
- [x] No __pycache__ artifacts included
