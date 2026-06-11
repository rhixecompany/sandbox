# Bash Scripts Catalog Context

**Generated:** 2026-05-29  
**Workspace:** `C:\Users\Alexa\Desktop\SandBox`  
**Scope:** `Bash/**`, `projects/Banking/**`, `projects/comicwise/**`

## Critical Rules

1. All operational scripts should converge under `Bash/**` over time.
2. Framework-required seed scripts may stay in project-local locations.
3. Wrapper scripts are acceptable while migration is in progress.
4. Archive content and infrastructure scripts are not migration targets.

## Inventory Summary (Operational Script Areas)

| Location | Total | .sh | .ps1 | .bat | .ts | Status |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `Bash/scripts` | 27 | 6 | 21 | 0 | 0 | Keep (canonical) |
| `projects/Banking/scripts` | 103 | 9 | 8 | 5 | 81 | Migrate candidates (except seeds) |
| `projects/Banking/bin` | 71 | 17 | 17 | 17 | 20 | Keep as wrappers/compat layer, then consolidate |
| `projects/comicwise/scripts` | 0 | 0 | 0 | 0 | 0 | No action |

## Classification

### Keep

- `Bash/scripts/**` (canonical orchestrator and phase tooling)
- Seed and schema bootstrap scripts required by project runtime conventions
- Archived one-shot artifacts and infra-only scripts

### Migrate

- Operational automation scripts in `projects/Banking/scripts/**` that duplicate Bash-owned tooling patterns
- Cross-project wrappers that should point to Bash-managed entrypoints after parity

### Delete (after parity)

- Duplicate legacy wrappers in project folders once Bash-hosted equivalents are verified
- Stale references to moved script paths in docs and package script entries

## Findings Implemented in This Pass

1. Fixed broken `projects/Banking/package.json` CI helper script paths:
   - `scripts/utils/ci-helpers/*` -> `bin/utils/ci-helpers/*`
2. Updated Banking CI helper docs to match real paths:
   - `projects/Banking/bin/utils/ci-helpers/README.md`
   - `projects/Banking/docs/scripts.md`

## Notes for Phase Execution

- Immediate risk was command breakage from stale paths, now corrected.
- Next migration batch should move shared CI helper logic to `Bash/**` and leave project wrappers thin.
