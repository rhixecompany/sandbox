# ComicWise Phase Master Plan

**Generated:** March 13, 2026  
**Status:** Complete (All 5 Batches Implemented)

---

## Overview

This document provides a comprehensive inventory of all phases from Phase 1 through Phase 4.3+, with detailed tasks, dependencies, checkpoints, and recovery points.

---

## Batch Summary

| Batch | Status | Description |
| --- | --- | --- |
| **Batch 1** | ✅ Complete | Stabilize & Clean — TS errors, docs cleanup, component cleanup, VS Code config |
| **Batch 2** | ✅ Complete | Scripts Consolidation — All scripts created/enhanced, shell scripts ready |
| **Batch 3** | ✅ Complete | Seeds + Quality Gate — Enhanced seeders, quality gate scripts, triage system |
| **Batch 4** | ✅ Complete | Full Source Audit — All pre-identified issues fixed, process.env violations resolved |
| **Batch 5** | ✅ Complete | CI/CD + Phase Master Plan — Workflows updated, this document created |

---

## Phase Inventory

### Phase 1: Foundation (COMPLETE ✅)

#### Phase 1A: TypeScript Errors

- **Status:** ✅ Complete
- **Verification:** `pnpm type-check` → 0 errors

#### Phase 1B: Documentation Cleanup

- **Status:** ✅ Complete
- **Action:** Deleted 6 superseded docs
- **Files Deleted:** PHASE_2_COMPLETION.md, PHASE_3_COMPLETION.md, PHASE4-3-DAY4-COMPLETE.md, etc.

#### Phase 1C: Components Cleanup

- **Status:** ✅ Complete
- **Actions:**
  - Created barrel exports for `bookmarks/` and `search/`
  - Deleted `shadcn-studio/` directory
  - Deleted `admin/data.json`

#### Phase 1D: VS Code Config Audit

- **Status:** ✅ Complete
- **Actions:**
  - Hidden `.references/` in explorer
  - Removed duplicate Type Check task
  - Verified launch.json, extensions.json, mcp.json

---

### Phase 2: Scripts & Tools (COMPLETE ✅)

#### Phase 2A: Script Analysis

- **Status:** ✅ Complete
- **Output:** `docs/refactor-context.md` (769 lines)
- **Analyzed:** 92 scripts across `.references/comicwise` and `.references/comicr`

#### Phase 2B: Core Scripts Created

- **Status:** ✅ Complete
- **Scripts:**
  - `project-cleanup.ts` — Deep cleanup with dry-run
  - `cleanup-duplicates.ts` — Pattern-based duplicate detection
  - `optimize-performance.ts` — Bundle analysis
  - `validate-env.ts` — Env validation + sync
  - `fix-line-endings.ts` — CRLF→LF normalization

#### Phase 2C: Enhanced Scripts

- **Status:** ✅ Complete
- **Enhanced:**
  - `analyze-project.ts` — Added security scan, dependency analysis, metrics
  - `scaffold.ts` — Added DAL, schema templates

#### Phase 2D: Shell Scripts

- **Status:** ✅ Complete
- **Created/Enhanced:**
  - `dev.sh` / `dev.ps1` — Prerequisites + dev server + browser
  - `cleanup.sh` / `cleanup.ps1` — Artifact removal
  - `setup-dev.sh` / `setup-dev.ps1` — Added --skip-db, --skip-seed, --skip-install
  - `quality-gate.sh` / `quality-gate.ps1` — tee logging, timing, JSON summary

#### Phase 2E: Package.json Updates

- **Status:** ✅ Complete
- **Added:** 30+ script entries

---

### Phase 3: Seeds & Quality Gate (COMPLETE ✅)

#### Phase 3A: Seed Enhancement

- **Status:** ✅ Complete
- **Features:**
  - User seeder: 10 users default (3 admin, 3 mod, 4 user)
  - Comic/Chapter image seeders: multi-strategy (URL/local/ImageKit)
  - Chunked processing with `--chunk-size` flag
  - Checkpoint/resume via `.seed-checkpoints/` directory
  - `--resume` flag to continue from checkpoint

#### Phase 3B: Quality Gate Scripts

- **Status:** ✅ Complete
- **Features:**
  - `quality-gate.sh` / `quality-gate.ps1` with tee logging
  - Per-gate timing
  - `--continue-on-error` flag
  - JSON summary output
  - Skip flags for individual gates

#### Phase 3C: Triage System

- **Status:** ✅ Complete
- **Script:** `src/scripts/triage-quality-gate.ts`
- **Command:** `pnpm triage`
- **Output:** `quality-gate-triage.json`

---

### Phase 4: Full Source Audit (COMPLETE ✅)

#### Phase 4A: Pre-Identified Issues (10 fixes)

- **Status:** ✅ Complete

| # | Issue | Status |
| --- | --- | --- |
| 1 | Move `auth-db.ts` → `src/dal/auth-db.ts` | ✅ Already there |
| 2 | SearchDAL extends BaseDal | ✅ Already fixed |
| 3 | Fix `any` types in SearchDAL | ✅ Already fixed |
| 4 | Fix `goals.actions.ts` import | ✅ Already fixed |
| 5 | Delete `comic-schema.ts` | ✅ Already deleted |
| 6 | Delete `example.spec.ts` | ✅ Already deleted |
| 7 | Rename `comic-schema.spec.ts` → `comic.schema.spec.ts` | ✅ Already done |
| 8 | Reading-progress duplicates | ✅ No duplicates found |
| 9 | Comment-rating bundling | ✅ Acceptable as-is |

#### Phase 4B: process.env Violations

- **Status:** ✅ Complete
- **Remaining:** Only `process.env.NODE_ENV` in client components (standard Next.js pattern)

#### Phase 4C: Directory Audits

- **Status:** ✅ Complete
- **Verified:**
  - `src/hooks/` — Clean ✅
  - `src/types/` — Clean ✅
  - `src/dal/` — Extends BaseDal ✅
  - `src/actions/` — Server Actions pattern ✅

---

### Phase 5: CI/CD (COMPLETE ✅)

#### Phase 5A: Workflow Updates

- **Status:** ✅ Complete

| Workflow                  | Updates                        |
| ------------------------- | ------------------------------ |
| `test.yml`                | Node 18→20, actions v4         |
| `playwright.yml`          | Already Node 20, pnpm cache ✅ |
| `deploy.yml`              | Docker actions v3 ✅           |
| `copilot-setup-steps.yml` | Fixed checkout@v5→v4           |

#### Phase 5B: Phase Master Plan

- **Status:** ✅ Complete
- **Output:** This document (`docs/PHASE-MASTER-PLAN.md`)

---

## Quality Gates

All quality gates must pass before any commit:

```bash
# Required: All must pass with 0 errors
pnpm type-check    # TypeScript strict mode
pnpm lint:fix      # ESLint + Prettier
pnpm test          # Vitest unit tests (241/241)
pnpm build         # Production build
```

### Verification Commands

```bash
# Full quality gate
./quality-gate.sh

# Individual gates
pnpm type-check
pnpm lint:fix
pnpm test
pnpm build

# Triage (after quality gate)
pnpm triage
```

---

## Recovery Points

### Git-based Recovery

```bash
# Stash uncommitted changes
git stash

# Discard all local changes
git checkout .

# Reset to last commit
git reset --hard HEAD

# Specific file recovery
git checkout HEAD -- path/to/file
```

### Database Rollback

```bash
# Drop all tables
pnpm db:drop

# Reset database
pnpm db:reset
```

### Checkpoint Recovery (Seeding)

```bash
# Resume from last checkpoint
pnpm seed:all --resume --chunk-size=500

# Check checkpoint status
ls -la .seed-checkpoints/
```

---

## Dependency Graph

```
Batch 1 (Foundation)
    ↓
Batch 2 (Scripts) ← Depends on Batch 1
    ↓
Batch 3 (Seeds) ← Depends on Batch 2
    ↓
Batch 4 (Audit) ← Depends on Batch 1-3
    ↓
Batch 5 (CI/CD) ← Depends on Batch 4
```

---

## Checkpoints

| Batch | Command | Expected Result |
| --- | --- | --- |
| 1 | `pnpm type-check` | 0 errors |
| 1 | `pnpm test` | 241/241 passing |
| 2 | `tsx src/scripts/validate-env.ts --dry-run` | Runs successfully |
| 2 | `pnpm scaffold component Test` | Creates valid component |
| 3 | `pnpm seed:validate` | All validations pass |
| 3 | `./quality-gate.sh --json` | Generates JSON report |
| 4 | `grep -r "process\.env\." src/ --include="\*.ts" | Minimal results (NODE_ENV only) |
| 5 | All workflows | Valid YAML, no deprecated actions |

---

## Code Samples

### Example: Running Quality Gate

```bash
# Full quality gate with all checks
./quality-gate.sh

# Continue on error, generate JSON
./quality-gate.sh --continue-on-error --json

# Skip individual gates
./quality-gate.sh --skip-build
```

### Example: Seeding with Checkpoints

```bash
# Seed all entities with chunking
pnpm seed:all --chunk-size=500

# Resume from checkpoint
pnpm seed:all --resume --chunk-size=500

# Dry run validation
pnpm seed:validate
```

### Example: Scaffold Commands

```bash
# Create component
pnpm scaffold component ComicCard

# Create DAL
pnpm scaffold dal Comic

# Create action
pnpm scaffold action updateProfile

# Create page
pnpm scaffold page comics/browse

# Create schema
pnpm scaffold schema User
```

---

## References

- **AGENTS.md** — Developer conventions and patterns
- **docs/BATCH-IMPLEMENTATION-PLAN.md** — Detailed batch plan (873 lines)
- **docs/BATCH-IMPLEMENTATION-SUMMARY.md** — Summary document (464 lines)
- **docs/refactor-context.md** — Script analysis (769 lines)
- **docs/database-context-map.md** — Entity relationships

---

**Document Status:** Complete  
**Last Updated:** March 13, 2026  
**Next Action:** None (All batches complete)
