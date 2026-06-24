---
title: "Bash Scripts Implementation Plan"
source: "docs/bash-scripts-implementation-plan.md"
---

# Bash Scripts Implementation Plan

**Date:** 2026-05-29  
**Source:** `docs/bash-scripts-list-context.md`

## Goal

Consolidate operational scripts into `Bash/**` with safe wrappers in project folders until migration parity is reached.

## Phase 1 - Path Integrity (Complete)

1. Fix broken script entrypoints in package scripts.
2. Align docs with real executable locations.

**Completed**

- `projects/Banking/package.json` CI helper paths corrected to `bin/utils/ci-helpers/*`.
- CI helper docs updated in:
  - `projects/Banking/bin/utils/ci-helpers/README.md`
  - `projects/Banking/docs/scripts.md`

## Phase 2 - Consolidation Prep

1. Define Bash canonical location for Banking CI helpers (recommended: `Bash/scripts/banking/ci-helpers/`).
2. Add thin compatibility wrappers in `projects/Banking/bin/utils/ci-helpers/*` that call Bash-owned scripts.
3. Keep argument parity and exit code parity.

## Phase 3 - Migration

1. Move shared operational logic from `projects/Banking/scripts/**` into `Bash/**`.
2. Preserve seed/runtime scripts in-place when project framework requires locality.
3. Update `package.json` and workflow references to Bash canonical paths via wrappers.

## Phase 4 - Verification and Cleanup

1. Validate wrappers and direct entrypoints.
2. Remove duplicate project-local operational implementations once parity is confirmed.
3. Retain only:
   - Bash canonical scripts
   - required seed scripts
   - thin local wrappers (if still needed)

## Validation Commands

Run from `Bash/`:

1. `bun run format`
2. `bun run typecheck`
3. `bun run lint:strict`
