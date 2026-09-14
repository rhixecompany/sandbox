---
name: codemap-codemap
description: "src/skills/codemap/"
version: 1.0.0
author: Alexa
---
     1|# src/skills/codemap/
     2|
     3|## Responsibility
     4|
     5|- Provide a command-style skill package that standardizes repository mapping workflows for unfamiliar codebases.
     6|- Define the task contract used by Orchestrator/fixer agents via `SKILL.md` and operational guidance via `README.md`.
     7|- Generate and evolve change-aware codemap state artifacts (`.slim/codemap.json`) and scaffold placeholders (`codemap.md`).
     8|
     9|## Design
    10|
    11|- Contract layer: `SKILL.md` (machine prompt contract) + `README.md` (human-facing operation notes).
    12|- Execution layer: `scripts/codemap.mjs` exports deterministic helper functions:
    13|  - `parseArgs(argv)`
    14|  - `cmdInit`, `cmdChanges`, `cmdUpdate`
    15|  - `selectFiles`, `computeFileHash`, `computeFolderHash`, `createEmptyCodemap`
    16|  - `loadState`, `saveState`, `migrateLegacyState`
    17|- Persistence model: JSON state at `.slim/codemap.json` with `metadata`, `file_hashes`, and `folder_hashes`.
    18|- Testing layer: `scripts/codemap.test.ts` validates pattern matching, hash determinism, and migration behavior.
    19|- The script intentionally avoids network and mutates only filesystem-local state and codemap templates.
    20|
    21|## Flow
    22|
    23|- Entry point `main(argv)` parses command and arguments (`init|changes|update`, `--root`, `--include`, `--exclude`, `--exception`) and dispatches via strict branches.
    24|- `cmdInit()` computes include/exclude candidate sets using `selectFiles()` and writes:
    25|  1. `.slim/codemap.json` via `saveState()`
    26|  2. one `codemap.md` per discovered folder via `createEmptyCodemap()`.
    27|- `cmdChanges()` reloads state (`loadState()` + `migrateLegacyState()`), recomputes current hashes, emits added/removed/modified diffs and affected folder list, and exits non-zero if state is absent.
    28|- `cmdUpdate()` recomputes full state from existing metadata and persists it, used after targeted fixers finish updates.
    29|- `codemap` skill invocation path in SKILL workflow is explicit: Step 1 checks `.slim/codemap.json` or `.slim/cartography.json`, then Step 2/3 selects init or incremental path.
    30|
    31|## Integration
    32|
    33|- Installed under OpenCode through `src/cli/custom-skills.ts` as `name: 'codemap'`, `sourcePath: 'src/skills/codemap'`.
    34|- `src/cli/install.ts` copies this directory into the user skill directory; OpenCode executes `scripts/codemap.mjs` from that context.
    35|- `src/hooks/filter-available-skills/index.ts` applies agent-level skill gating via names from `getSkillPermissionsForAgent()`.
    36|- `scripts/verify-release-artifact.ts` includes codemap skill metadata and runtime checks as required packaged files.
    37|