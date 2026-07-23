# Final Verification Report — `.github` Prompt Normalization

**Date:** 2026-07-23  
**Plan:** `.hermes/plans/2026-07-23-comprehensive-github-prompts-plan.md`  
**Status:** Approved and executed  

## Summary

All prompt-family assets are now canonical under `.github/prompts/`. Legacy roots `.github/agents/`, `.github/instructions/`, and `.github/skills/` no longer exist. Active cross-references in root docs and workflows have been normalized to canonical paths. Exact-dedupe scan found 0 duplicate bodies in the active prompt set.

## Canonical Structure

| Directory | Files | Notes |
|-----------|-------|-------|
| `.github/prompts/agents/` | 174 | `*.agent.md` |
| `.github/prompts/instructions/` | 186 | `*.instructions.md` |
| `.github/prompts/skills/` | 1 | `**/SKILL.md` |
| `.github/prompts/archived/` | 771 | Archived templates |
| **Total** | **1133** | Active + archived |

## Exact-Duplicate Body Scan

- **Scanned:** 361 active files (`agents/`, `instructions/`, `skills/**/SKILL.md`)
- **Unique hashes:** 361
- **Duplicate groups:** 0
- **Action taken:** None required; no duplicates to archive

## Cross-Reference Normalization

### Updated Files
- `README.md` — `.github/prompts/` as canonical prompt library
- `AGENTS.md` — canonical prompt paths in project table and stale-ref tracker
- `.github/copilot-instructions.md` — inventory snapshot updated
- `.github/workflows/deploy-website.yml` — prompt path filter updated
- `.github/workflows/validate-readme.yml` — prompt path filter updated
- `.github/workflows/resource-staleness-report.md` — prompt reference paths updated

### Canonical Prompt Files Verified Clean
- `.github/prompts/agents/*.agent.md` — 0 legacy stale refs
- `.github/prompts/instructions/*.instructions.md` — 0 legacy stale refs

## Legacy Directory Status

| Legacy Path | Status |
|-------------|--------|
| `.github/agents/` | Removed |
| `.github/instructions/` | Removed |
| `.github/skills/` | Removed |

## Verification Artifacts

- `.hermes/audits/2026-07-23-parent-baseline.json` — baseline counts and duplicate scan
- `.hermes/audits/2026-07-23-phase2-canonical-patches.md` — canonical path normalization audit
- `.hermes/audits/2026-07-23-phase3-dedupe-report.md` — exact-dedupe verification report

## Conclusion

The `.github` prompt normalization is complete and verified. All active assets live under `.github/prompts/`, no exact-duplicate bodies remain, and legacy directories have been removed.
