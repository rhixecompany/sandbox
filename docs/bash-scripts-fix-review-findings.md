# Bash Scripts Modernization and Consolidation — Review Findings

Generated: 2026-06-12
Prompt: `Prompts/bash-scripts-fix.prompts.md`
Source: live `Bash/` scan, active scripts only

## Summary

Phase 3 review is complete. No destructive fixes were applied in this pass.

| Metric | Value |
| --- | --- |
| Active scripts scanned | 177 |
| Archived/migrated scripts excluded | 55 |
| Fixes applied | 0 |
| Status | Read-only review complete |

## Risk/Diff Assessment

| Risk | Finding |
| --- | --- |
| Highest | Wrapper-parity drift if local dialects are replaced before dry-run comparison |
| Medium | Duplicated logic across platform wrappers without a single TypeScript owner |
| Lowest | Orchestrator scripts should remain untouched in this pass |

## Phase 3 Findings

- PowerShell wrapper families under `Bash/Banking/scripts/*` and `Bash/comicwise/*` are the strongest migration candidates.
- Root utility wrappers with TS counterparts under `Bash/src/*` are second-tier candidates.
- No syntax or formatting fixes were applied; fixes are blocked pending explicit confirmation for migration/rewrite actions.
