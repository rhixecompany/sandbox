# Scripts Consolidation & Reference Cleanup: Refactor Context

**Status**: Phase 2 Analysis Complete **Total Scripts Analyzed**: 92 (62 ComicWise + 30 ComicR) **Consolidation Target**: 92 → 22-26 total scripts **Date**: Session: Batch 2 Execution

---

## Executive Summary

A comprehensive analysis of 92 reference scripts across two directories (`.references/comicwise/scripts/` and `.references/comicr/scripts/`) revealed significant consolidation opportunities. Scripts fall into 11 categories with notable duplication in:

- **dev-setup** (23 scripts, many PowerShell/shell pairs)
- **refactoring** (13 scripts with overlapping functionality)
- **utility** (15 helper scripts)
- **database-ops** (8 related scripts)
- **performance** (7 optimization variants)

**Key Finding**: 30% already implemented in project, 28% high-value missing, 20% duplicates, 22% niche-specialized.

**Consolidation Plan**: Merge all scripts in `src/scripts/` into unified super-scripts + standalone specialists, delete all dead code variants, then modify src/scripts/master-setup.ts to orchestrator which execute all unified scripts. Reference `docs/refactor-context.md` for detailed context.

---

## Complete Script Inventory

### ComicWise Scripts (62 total)

| # | Filename | Purpose | Category | Status | Dependencies |
| --- | --- | --- | --- | --- | --- |
| 1 | analyze-project.ts | Project analysis for bottlenecks, vulnerabilities, code quality | performance | duplicate | chalk, ora, glob |
| 2 | build.ps1/build.sh | Build the Next.js project | dev-setup | implemented | next |
| 3 | cacheStats.ts | Redis cache usage statistics | health-checks | implemented | ioredis |
| 4 | camelCaseConverter2025.ts | Convert filenames to camelCase | code-generation | niche | glob, fs-extra, ora, chalk |
| 5 | checkDb.ts | Database connection health check | health-checks | implemented | drizzle-orm |
| 6 | checkRedis.ts | Redis connection health check | health-checks | implemented | ioredis |
| 7 | cleanup-duplicates.ts | Remove duplicate files and dead code | refactoring | duplicate | glob, fs-extra |
| 8 | cleanup-project.ps1/cleanup.sh | Build artifacts and cache cleanup | utility | implemented | none |
| 9 | clearCache.ts | Clear Redis cache with pattern matching | utility | implemented | ioredis |
| 10 | complete-setup\*.ts (4 variants) | Setup task completion runners | dev-setup | niche/duplicate | none |
| 11 | comprehensiveMasterOptimization2025.ts | Master optimization combining phases | performance | duplicate | chalk, ora |
| 12 | cw-aliases\*.ps1/sh | CLI command aliases | utility | high-value-missing | none |
| 13 | cw-enhanced.ps1/cw.sh | CLI wrapper with argument parsing | utility | high-value-missing | none |
| 14 | deploy-vercel.ts | Vercel deployment automation | setup-deployment | high-value-missing | chalk, ora, inquirer |
| 15 | dev.ps1/dev.sh | Start dev server with Turbopack | dev-setup | implemented | none |
| 16 | drizzleSetup.ts | Drizzle ORM configuration and migrations | database-ops | niche | drizzle-kit, drizzle-orm |
| 17 | execute-all-tasks.ts | Execute all project setup tasks | dev-setup | niche | none |
| 18 | fix-line-endings.sh | Fix CRLF/LF line endings | utility | niche | none |
| 19 | format.ps1/format.sh | Run Prettier formatting | dev-setup | implemented | prettier |
| 20 | generateDTOs.ts | Generate DTO interfaces from server actions | code-generation | high-value-missing | glob, ts-morph, zod |
| 21 | git-commit.ts | Conventional commit with message generation | git-ops | high-value-missing | chalk, ora, inquirer, simple-git |
| 22 | git-init.ts | Initialize git repository with hooks | git-ops | high-value-missing | simple-git |
| 23 | healthCheck.ts | Comprehensive health check (DB, Redis, env) | health-checks | implemented | drizzle-orm, ioredis |
| 24 | install-deps.ps1/install-deps.sh | Install project dependencies | dev-setup | implemented | none |
| 25 | install-vscode-extensions.ps1 | Install VS Code extensions | dev-setup | niche | none |
| 26 | lint.ps1/lint.sh | Run ESLint | dev-setup | implemented | eslint |
| 27 | master-setup.ts/master-complete-setup.ts (3 variants) | Master setup orchestration | dev-setup | duplicate | none |
| 28 | masterOptimization.ts | Execute all optimizations | performance | duplicate | chalk |
| 29 | migrateToDto.ts | Migrate API payloads to DTO pattern | refactoring | high-value-missing | glob, ts-morph |
| 30 | ops.ps1/ops.sh | Operations shortcuts | utility | high-value-missing | none |
| 31 | optimize-project.ps1 | Project optimization wrapper | performance | duplicate | none |
| 32 | optimize-vscode-complete-enhanced.ps1 | VS Code optimization | dev-setup | niche | none |
| 33 | prioritySystem.ts/priority-system.bat | Priority queue system | utility | niche/unused | none |
| 34 | projectCleanup\*.ts (3 variants) | Project cleanup with variants | refactoring | duplicate | glob, fs-extra, chalk |
| 35 | queueWorker.ts | Background queue worker | utility | niche/unused | bull, ioredis |
| 36 | replaceImportsEnhanced.ts | Replace relative imports with aliases | refactoring | implemented | glob, ts-morph |
| 37 | run-import-replacement.ps1/sh | Import replacement wrapper | refactoring | duplicate | none |
| 38 | run.ps1/run.sh | Main CLI entry point | utility | high-value-missing | none |
| 39 | scaffold.ts | Generate pages/components/routes | code-generation | implemented | none |
| 40 | seed-dry-run.md | Seed dry-run documentation | documentation | high-value-missing | none |
| 41 | setup-env.ps1 | Configure environment variables | dev-setup | implemented | none |
| 42 | setup.ps1/setup.sh | Main setup script | dev-setup | implemented | none |
| 43 | test.ps1/test.sh | Run Vitest unit tests | dev-setup | implemented | vitest |
| 44 | type-check.ps1/type-check.sh | Run TypeScript type checking | dev-setup | implemented | typescript |
| 45 | uninstall-unused-packages.ts | Uninstall unused npm dependencies | refactoring | high-value-missing | glob |
| 46 | updateAnyTypes.ts | Remove 'any' type annotations | refactoring | implemented | glob, chalk |
| 47 | uploadBulk.ts | Bulk upload to ImageKit/Cloudinary/S3 | utility | high-value-missing | chalk, ora, glob |
| 48 | verify-\* (4 scripts) | VS Code/MCP verification | dev-setup/health-checks | niche | none |

### ComicR Scripts (30 total)

| # | Filename | Purpose | Category | Status | Dependencies |
| --- | --- | --- | --- | --- | --- |
| 73 | ast-refactor.ts | AST-based refactoring with ts-morph | refactoring | duplicate | ts-morph |
| 74 | autofix-chapter-fields.ts | Auto-fix chapter field values | database-ops | niche | drizzle-orm |
| 75 | cleanup-duplicates.ts | Duplicate code scanner/remover | refactoring | duplicate | glob, fs-extra |
| 76 | complete-plan.ts | Execute plan with progress tracking | utility | niche | none |
| 77 | cw.ts | Main CLI entry point | utility | implemented | none |
| 78 | db-truncate.ts | Safely truncate seeded tables | database-ops | implemented | drizzle-orm |
| 79 | docker-init.sh | Initialize Docker container | dev-setup | high-value-missing | none |
| 80 | enhance-seo.ts | SEO optimizations (metadata, structured data, CWV) | performance | high-value-missing | none |
| 81 | fix-line-endings.sh | Fix CRLF to LF line endings | utility | niche | none |
| 82 | fix-use-directives.ts | Add 'use server'/'use client' automatically | code-generation | high-value-missing | glob |
| 83 | init-db.sql | Database initialization SQL | database-ops | niche | none |
| 84 | install-extensions.ps1 | Install recommended extensions | dev-setup | niche | none |
| 85 | merge-seed-data.ts | Merge data from multiple seed sources | database-ops | niche | glob |
| 86 | optimize-performance.ts | Comprehensive performance optimization | performance | duplicate | none |
| 87 | rename-to-kebab-case.ts | Batch rename files to kebab-case | refactoring | niche | glob, fs-extra |
| 88 | report-missing-chapter-fields.ts | Report chapters with missing fields | utility | niche | drizzle-orm |
| 89 | setup-api.ts | API routes and middleware setup | setup-deployment | niche | none |
| 90 | setup-deployment.ts | Deployment environment configuration | setup-deployment | high-value-missing | none |
| 91 | setup-error-boundaries.ts | Add error boundary components | code-generation | high-value-missing | glob, ts-morph |

---

## Batch 2: Implementation Strategy (HIGH-VALUE NON-DUPLICATES)

**Goal**: Create 9 new/enhanced TypeScript scripts + 4 shell wrappers for daily developer productivity.

**Status**: ✅ Analysis complete | 🔄 Implementation ready

---

### Batch 2.B: Create 5 Core TypeScript Scripts (NEW)

These scripts provide clear value with minimal duplication across references and address daily dev tasks:

#### 1. **fix-line-endings.ts** ⭐ START HERE

- **Lines**: ~120
- **Purpose**: Normalize CRLF → LF across repo (Git standard)
- **Flags**: `--pattern`, `--dry-run`, `--verbose`, `--yes`
- **CLI**: `pnpm fix:line-endings --pattern "src/**/*.{ts,tsx}" --dry-run`
- **Output**: Report count of files changed, pre/post line ending stats
- **Depends on**: fs, logger.ts
- **Priority**: HIGH (cross-platform issue, blocks commits)

#### 2. **cleanup-duplicates.ts**

- **Lines**: ~180
- **Purpose**: Find duplicate files (same content, different names) + prompt deletion
- **Flags**: `--pattern`, `--keep-canonical`, `--dry-run`, `--verbose`, `--yes`, `--json`
- **CLI**: `pnpm cleanup:duplicates --pattern "src/components/**/*.tsx" --dry-run --verbose`
- **Logic**:
  - Compute file hashes (SHA256)
  - Group by hash
  - Flag duplicates, keep canonical (alphabetically first in src/)
  - Delete backups, .old, .copy versions
- **Depends on**: crypto, fs, logger.ts, confirmAction.ts
- **Priority**: HIGH (cleanup technical debt)

#### 3. **validate-env.ts**

- **Lines**: ~200
- **Purpose**: Validate `.env.local` against schema + sync missing keys
- **Flags**: `--sync`, `--dry-run`, `--verbose`
- **CLI**: `pnpm validate:env --sync --dry-run` (preview changes), then `pnpm validate:env --sync --yes`
- **Logic**:
  - Parse `.env.local.example` (source of truth)
  - Extract keys from `src/lib/env.ts` Zod schema
  - Validate `.env.local` has all required keys
  - Suggest missing keys
  - Optional `--sync`: add missing from .example to .local
- **Depends on**: logger.ts, Zod parser
- **Priority**: HIGH (dev experience, onboarding)

#### 4. **project-cleanup.ts**

- **Lines**: ~150
- **Purpose**: Deep project cleanup — remove artifacts, temp files, cache
- **Flags**: `--dry-run`, `--verbose`, `--yes`, `--clear-global` (clear pnpm global cache)
- **CLI**: `pnpm cleanup:project --dry-run --verbose`, then `pnpm cleanup:project --yes`
- **Scope**:
  - Remove: node_modules/.vite, .turbo, .next, dist, build
  - Remove: `*.log`, `*.tmp`, .DS_Store, Thumbs.db, .turbo cache
  - Remove: empty directories
  - Optional: `pnpm cache clean` (local artifact cache)
  - Report: disk space freed
- **Depends on**: fs, path, logger.ts, confirmAction.ts
- **Priority**: HIGH (disk cleanup, slow build fixes)

#### 5. **optimize-performance.ts**

- **Lines**: ~220
- **Purpose**: Bundle analysis + caching audit + optimization suggestions
- **Flags**: `--analyze`, `--cache-audit`, `--dry-run`, `--verbose`, `--json`
- **CLI**: `pnpm optimize:performance --analyze --cache-audit --json > performance-report.json`
- **Output**: JSON report + console summary
  - Bundle size per module
  - Build time trend (if historical data)
  - Cache hit rates (Turbopack file system cache)
  - Top 10 slowest modules
  - Optimization suggestions (code splitting, tree-shaking, lazy loading)
- **Depends on**: logger.ts, fs
- **Priority**: MEDIUM (performance visibility)

---

### Batch 2.C: Create 4 Analysis/DevTools Scripts (ENHANCE/NEW)

#### 6. **analyze-project.ts** (ENHANCE existing)

- **Lines**: ~300 (from ~180 current)
- **New additions**:
  - Security scan: Find hardcoded secrets (patterns: API_KEY, PASSWORD, TOKEN)
  - Dependency analysis: Circular imports, unused deps
  - Code metrics: LOC per file, complexity score
  - Component audit: Count components, identify orphans
- **Flags**: `--security`, `--dependencies`, `--metrics`, `--components`, `--json`
- **CLI**: `pnpm analyze:project --security --json`
- **Output**: Markdown report + JSON
- **Priority**: MEDIUM (code insights)

#### 7. **check-db.ts** (NEW)

- **Lines**: ~180
- **Purpose**: Verify database connectivity, schema, data integrity
- **Flags**: `--verbose`, `--turbo` (fast mode, skip counts)
- **CLI**: `pnpm health:db --verbose`
- **Logic**:
  - Test connection via `src/database/db.ts`
  - Verify schema (27 tables exist)
  - Count rows per table (top 5 largest)
  - Check FK integrity
  - Output: Table with row counts, schema validation
- **Depends on**: db.ts, logger.ts
- **Priority**: HIGH (health check integration)

#### 8. **git-init.ts** (NEW)

- **Lines**: ~100
- **Purpose**: Initialize Git hooks (pre-commit, pre-push)
- **Flags**: `--verbose`, `--yes`
- **CLI**: `pnpm git:init --yes`
- **Logic**:
  - Install Husky if not present
  - Create `.husky/pre-commit` → `pnpm lint:fix && pnpm type-check`
  - Create `.husky/pre-push` → `pnpm test`
  - Report: hooks installed
- **Depends on**: child_process, logger.ts
- **Priority**: MEDIUM (team dev hygiene)

#### 9. **scaffold.ts** (ENHANCE existing, ~400 lines total)

- **Subcommands** (NEW capabilities):
  - `scaffold component <name>` → `src/components/<kebab>/<kebab>.tsx`
  - `scaffold dal <Entity>` → `src/dal/<entity>-dal.ts`
  - `scaffold action <name>` → `src/actions/<kebab>.actions.ts`
  - `scaffold page <name>` → `src/app/(root)/<kebab>/page.tsx`
  - `scaffold schema <Entity>` → `src/schemas/<entity>.schema.ts` (NEW)
- **All templates**: Include JSDoc, types, `"use server"`/`"use client"`, proper structure
- **Flags**: `--force` (overwrite), `--dry-run`
- **CLI**:

  ```bash
  pnpm scaffold component ComicCard
  pnpm scaffold dal Comic
  pnpm scaffold action TestAction
  pnpm scaffold page ComicDetail
  pnpm scaffold schema Comic
  ```

- **Depends on**: fs, path, logger.ts, template strings
- **Priority**: HIGH (developer velocity)

---

### Batch 2.D: Create 4 Shell Script Wrappers (NEW)

Created in root directory for cross-platform support:

#### **dev.sh / dev.ps1**

```bash
#!/bin/bash
# Prereq: Node 18+, pnpm 8+, .env.local exists, db connected
# Action: Start pnpm dev + launch browser
# Usage: ./dev.sh [--no-browser]
```

- **Lines**: ~30 (bash) + ~40 (PowerShell)
- **Logic**:
  1. Check Node version: `node --version | grep -E "v(18|19|20|21)"`
  2. Check pnpm version: `pnpm --version`
  3. Check `.env.local` exists
  4. Health check: `pnpm health:db --turbo`
  5. If all pass: `pnpm dev` in background, launch browser to `http://localhost:3000`
  6. Trap SIGINT: Kill pnpm on Ctrl+C

#### **cleanup.sh / cleanup.ps1**

```bash
#!/bin/bash
# Wrapper for pnpm cleanup:project with double-confirm
# Usage: ./cleanup.sh [--force] [--dry-run]
```

- **Lines**: ~25 (bash) + ~35 (PowerShell)
- **Logic**:
  1. Parse args: `--force` skips confirm, `--dry-run` passes through
  2. If not `--force`, prompt: "This will remove artifacts. Continue? [y/N]"
  3. Call: `pnpm cleanup:project --yes`
  4. Report: Disk space freed

---

### Batch 2.E: Update package.json

Add 13 new scripts to `scripts` section:

```json
{
  "scripts": {
    "cleanup:project": "tsx --env-file=.env.local src/scripts/project-cleanup.ts",
    "cleanup:project:dry": "tsx --env-file=.env.local src/scripts/project-cleanup.ts --dry-run",
    "cleanup:duplicates": "tsx --env-file=.env.local src/scripts/cleanup-duplicates.ts",
    "cleanup:duplicates:dry": "tsx --env-file=.env.local src/scripts/cleanup-duplicates.ts --dry-run",
    "validate:env": "tsx --env-file=.env.local src/scripts/validate-env.ts --sync",
    "validate:env:dry": "tsx --env-file=.env.local src/scripts/validate-env.ts --sync --dry-run",
    "fix:line-endings": "tsx --env-file=.env.local src/scripts/fix-line-endings.ts --yes",
    "fix:line-endings:dry": "tsx --env-file=.env.local src/scripts/fix-line-endings.ts --dry-run",
    "optimize:performance": "tsx --env-file=.env.local src/scripts/optimize-performance.ts --analyze --json",
    "git:init": "tsx --env-file=.env.local src/scripts/git-init.ts --yes",
    "analyze:project": "tsx --env-file=.env.local src/scripts/analyze-project.ts --json",
    "health:db": "tsx --env-file=.env.local src/scripts/check-db.ts --verbose",
    "scaffold": "tsx --env-file=.env.local src/scripts/scaffold.ts",
    "dev:sh": "./dev.sh",
    "cleanup:sh": "./cleanup.sh"
  }
}
```

---

### Batch 2 Execution Order (Dependency Chain)

1. **fix-line-endings.ts** (no deps except fs)
2. **cleanup-duplicates.ts** (depends on logger, confirmAction)
3. **validate-env.ts** (depends on logger)
4. **project-cleanup.ts** (depends on logger, confirmAction)
5. **optimize-performance.ts** (depends on logger)
6. **check-db.ts** (depends on db.ts, logger)
7. **git-init.ts** (depends on logger)
8. **analyze-project.ts** (ENHANCE — depends on logger)
9. **scaffold.ts** (ENHANCE — depends on logger)
10. **Shell scripts** (dev.sh, cleanup.sh) — can run after 1-8
11. **package.json** — update after all 9 scripts exist

**Total LOC**: ~1,600 across 9 TypeScript scripts + ~100 LOC shell scripts

---

### Batch 2 Success Criteria

✅ All 9 scripts compile (pnpm type-check → 0 errors) ✅ All scripts have `--help` (Commander.js built-in) ✅ All scripts run with `--dry-run --verbose` without side effects ✅ `pnpm scaffold component TestCard` creates valid component ✅ `pnpm cleanup:project --dry-run` shows what would be deleted ✅ `pnpm health:db` verifies DB connectivity ✅ Shell scripts executable on macOS + Windows (bash + PowerShell parity) ✅ package.json has all 13 new entries

---

## Batch 4: Preview (Source Audit)

**10 Pre-Identified Fixes**:

1. Move `src/actions/auth-db.ts` → `src/dal/auth-db.ts` (does DB queries, not Server Action)
2. Fix `src/dal/search-dal.ts`: extend `BaseDal<T>`, remove 2 `any` types
3. Fix `src/actions/goals.actions.ts` L7: import `./actions-types` → `@/types/actions-types`
4. Delete `src/schemas/comic-schema.ts` (dead, imported nowhere)
5. Delete `src/tests/example.spec.ts` (Playwright placeholder)
6. Rename `src/tests/schemas/comic-schema.spec.ts` → `comic.schema.spec.ts`
7. Investigate merge: `reading-progress.actions.ts` + `reading-progress.ts`
8. Investigate split: `comment-rating-dal.ts` (bundles 2 DALs)
9. **Fix 20 process.env violations** (migrate all to `getEnv()` helper)
10. Add `.references/` to `.vscode/settings.json` search + files excludes

**20 process.env Violations** (across 12 files):

- `src/auth-providers.ts` (3 violations)
- `src/auth-config.ts` (2 violations)
- `src/lib/redis.ts` (3 violations)
- `src/lib/image-kit-uploader.ts` (2 violations)
- `src/database/db.ts` (1 violation)
- `src/lib/query-client.ts` (1 violation)
- `src/lib/performance-metrics.ts` (1 violation)
- `src/components/optimized/performance-monitoring-provider.tsx` (2 violations)
- `src/hooks/use-performance-monitoring.tsx` (1 violation)
- `src/scripts/seed/run.ts` (2 violations)
- `src/app/api/seed/route.ts` (1 violation)
- `src/components/layout/layout-provider.tsx` (2 violations)

**Fix Pattern**:

```typescript
// ❌ BEFORE
const apiKey = process.env.API_KEY;

// ✅ AFTER
import { getEnv } from "@/lib/env";
const apiKey = getEnv("API_KEY");
```

---

## Continuation Plan

After Batch 2.B-E completion:

1. **Batch 4.1** — Fix 10 pre-identified issues
2. **Batch 4.2** — Migrate 20 `process.env` violations
3. **Batch 4.3** — Directory audit + consistency checks
4. **Batch 3.5** (Final) — Batch-fix remaining seeders, quality gates, registration

**Timeline**: Batch 2 = 3-4 hours (9 scripts + 4 shell), Batch 4 = 2-3 hours (fixes + migrations) | 92 | setup-eslint.ts | ESLint configuration setup | dev-setup | niche | none | | 93 | setup-logging.ts | Centralized logging infrastructure | dev-setup | niche | none | | 94 | validate-env.ts | Environment variables validation | dev-setup | implemented | zod | | 95 | verify-dal-usage.ts | Scan for direct DB queries outside DAL | refactoring | high-value-missing | glob | | 96 | verify-links.ts | Validate internal/external links | testing | high-value-missing | glob | | 97-101 | verify-\* (5 scripts) | MCP/provider/config verification | health-checks/dev-setup | niche | none |

---

## Category Breakdown

### By Category

| Category | Count | Key Scripts |
| --- | --- | --- |
| **dev-setup** | 23 | build, dev, test, lint, setup, install, verify extensions |
| **refactoring** | 13 | updateAnyTypes, replaceImports, cleanup, ast-refactor, DAL verify |
| **utility** | 15 | cw.sh/ps1, ops, cache, plan execution, queue (unused) |
| **health-checks** | 6 | checkDb, checkRedis, healthCheck, MCP verify |
| **database-ops** | 8 | db-truncate, drizzleSetup, autofix fields, merge seed |
| **performance** | 7 | optimize variants (3), analyze, enhance-seo |
| **code-generation** | 6 | scaffold, generateDTOs, fix-use-directives, setup-error-boundaries |
| **git-ops** | 2 | git-commit, git-init |
| **setup-deployment** | 4 | deploy-vercel, setup-deployment, setup-api, setup-logging |
| **testing** | 1 | verify-links |
| **documentation** | 2 | seed-dry-run.md, UPLOAD_BULK_README.md |

### By Status

| Status | Count | % | Action |
| --- | --- | --- | --- |
| already-implemented-in-project | 28 | 30% | Document version differences, consider consolidation |
| high-value-missing | 26 | 28% | **Implement as new unified scripts** |
| duplicate-of-existing | 18 | 20% | **Consolidate into unified scripts** |
| niche-specialized | 20 | 22% | Keep if actively used, delete if unused |

---

## Consolidation Plan

### 5 Unified Super-Scripts

#### 1. **unified-project-health.ts** (Replaces 6 scripts)

- `checkDb.ts` — Database connection status
- `checkRedis.ts` — Redis connection status
- `healthCheck.ts` — Comprehensive health check
- `cacheStats.ts` — Cache statistics reporting
- `verify-mcp-servers.ps1` → MCP server health
- `verify-mcp-packages.ts` → MCP packages health

**Command**: `pnpm health [--all|--db|--redis|--mcp|--cache]`

**Features**:

- Non-blocking health checks with clear status indicators
- Parallel health checks for speed
- Supports selective checking (--db only, --redis only, etc.)
- JSON output for CI/CD integration
- Retries with exponential backoff for transient failures

---

#### 2. **unified-schema-refactor.ts** (Replaces 7 scripts)

- `updateAnyTypes.ts` — Remove 'any' type annotations
- `ast-refactor.ts` — AST-based code refactoring
- `replaceImportsEnhanced.ts` — Replace relative imports with aliases
- `migrateToDto.ts` — Migrate API payloads to DTO pattern
- `verify-dal-usage.ts` — Verify DAL compliance
- `setup-error-boundaries.ts` — Add error boundary components
- `fix-use-directives.ts` — Add 'use server'/'use client' directives

**Command**: `pnpm refactor [--types|--imports|--dto|--boundaries|--directives|--dal-verify] [--dry-run]`

**Features**:

- Multi-step refactoring with dry-run preview
- Before/after file diffs
- Rollback support via git
- Selective execution (--types only, --imports only, etc.)
- Type safety validation

---

#### 3. **unified-db-operations.ts** (Replaces 6 scripts)

- `db-truncate.ts` — Safely truncate seeded tables
- `drizzleSetup.ts` — Drizzle ORM setup
- `autofix-chapter-fields.ts` — Auto-fix field values
- `report-missing-chapter-fields.ts` — Report missing fields
- `merge-seed-data.ts` — Merge seed from multiple sources
- `verify-seed-storage.ts` — Verify seed data integrity

**Command**: `pnpm db [--truncate|--setup|--autofix|--report|--merge|--verify] [--dry-run]`

**Features**:

- Database operations with safety checks
- Transaction rollback on errors
- Detailed operation logging
- Seed data migration and merging
- Field validation and auto-repair

---

#### 4. **unified-performance-ops.ts** (Replaces 5 scripts)

- `masterOptimization.ts` → Master optimization
- `comprehensiveMasterOptimization2025.ts` → Comprehensive optimization
- `analyze-project.ts` — Project analysis report
- `enhance-seo.ts` — SEO optimization
- `optimize-performance.ts` — Performance optimization

**Command**: `pnpm optimize [--analysis|--seo|--performance|--all] [--report]`

**Features**:

- Bundle analysis and recommendations
- SEO metadata and structured data generation
- Performance profiling and bottleneck identification
- Caching strategy recommendations
- HTML report generation

---

#### 5. **unified-dev-setup.ts** (Replaces 15+ scripts)

Consolidates setup, installation, and verification:

- All PowerShell/shell pairs (setup, dev, build, lint, format, test, type-check)
- `complete-setup.ts` (all 4 variants)
- `install-deps.ps1/install-deps.sh`
- `verify-and-install-vscode-extensions.ps1`
- `setup-env.ps1`
- `docker-init.sh`
- `setup-eslint.ts`, `setup-logging.ts`

**Command**: `pnpm setup [--deps|--env|--extensions|--eslint|--logging|--docker|--all]`

**Features**:

- Interactive setup wizard
- Dependency validation before installation
- Environment variable template creation
- VS Code extensions installation
- ESLint and logging setup
- Docker container initialization
- Rollback on failure

---

### 7 Standalone Specialist Scripts (Keep As-Is)

1. **git-commit.ts** — Conventional commit messaging with semantic analysis
2. **scaffold.ts** — Code generation for pages, components, API routes
3. **uploadBulk.ts** — Bulk image upload to CDNs (ImageKit, Cloudinary, S3)
4. **deploy-vercel.ts** — Vercel deployment automation (preview + production)
5. **uninstall-unused-packages.ts** — Dependency cleanup and removal
6. **verify-links.ts** — Link validation (internal + external)
7. **fix-line-endings.sh** — Universal line ending fixes (CRLF ↔ LF)

---

### Scripts to DELETE

These are dead code with TODOs or no active usage:

1. **queueWorker.ts** — Incomplete email queue system with TODOs
2. **prioritySystem.ts** + **priority-system.bat** — Unused priority queue (never integrated)
3. **camelCaseConverter2025.ts** — Not used (project uses kebab-case)
4. **projectCleanup2025.ts** + **projectCleanup2026.ts** — Replace with unified-project-health.ts
5. **complete-setup-tasks.ps1** — Dead variant, superseded
6. **completeImplementation.ts** — Duplicate of complete-setup.ts
7. **all PowerShell/shell setup pairs** — Replace with run.ps1/sh → unified-dev-setup.ts

---

### PowerShell/Shell Deduplication

**Current**: 28 PowerShell + shell pairs (56 files) **Proposed**: 2 universal runners + 1 TypeScript implementation

```bash
# Before (56 files)
dev.ps1 / dev.sh
build.ps1 / build.sh
test.ps1 / test.sh
lint.ps1 / lint.sh
format.ps1 / format.sh
type-check.ps1 / type-check.sh
setup.ps1 / setup.sh
install-deps.ps1 / install-deps.sh
... (8 pairs)

# After (2 runners + 1 implementation)
run.ps1 → unified-dev-setup.ts
run.sh → unified-dev-setup.ts
unified-dev-setup.ts (200-300 lines)
```

---

## Post-Consolidation CLI Structure

### New CLI (22-26 total scripts)

```bash
# Interactive menu
pnpm run                        # Show main menu

# Health checks (unified-project-health.ts)
pnpm health                     # Check all systems
pnpm health --db               # Database only
pnpm health --redis            # Redis only
pnpm health --mcp              # MCP servers only
pnpm health --cache            # Cache stats only

# Schema refactoring (unified-schema-refactor.ts)
pnpm refactor                   # Show options
pnpm refactor --types          # Fix 'any' types
pnpm refactor --imports        # Alias imports
pnpm refactor --dto            # DTO pattern migration
pnpm refactor --boundaries     # Add error boundaries
pnpm refactor --directives     # Fix use directives
pnpm refactor --dal-verify     # Check DAL compliance
pnpm refactor --dry-run        # Preview changes

# Database operations (unified-db-operations.ts)
pnpm db                         # Show options
pnpm db --truncate             # Truncate tables
pnpm db --setup                # Drizzle setup
pnpm db --autofix              # Auto-fix fields
pnpm db --report               # Report issues
pnpm db --merge                # Merge seed data
pnpm db --verify               # Verify seed storage
pnpm db --dry-run              # Preview changes

# Performance optimization (unified-performance-ops.ts)
pnpm optimize                   # Show options
pnpm optimize --analysis       # Analyze project
pnpm optimize --seo            # SEO optimization
pnpm optimize --performance    # Performance optimization
pnpm optimize --all            # All optimizations
pnpm optimize --report         # Generate report

# Development setup (unified-dev-setup.ts)
pnpm setup                      # Interactive wizard
pnpm setup --deps              # Install dependencies
pnpm setup --env               # Setup environment
pnpm setup --extensions        # Install VS Code extensions
pnpm setup --eslint            # Setup ESLint
pnpm setup --logging           # Setup logging
pnpm setup --docker            # Initialize Docker
pnpm setup --all               # Complete setup

# Standalone specialists (keep as commands)
pnpm scaffold <type> <name>    # Generate code
pnpm commit "<message>"        # Conventional commit
pnpm upload-bulk <src> <dst>   # Bulk image upload
pnpm deploy [--preview|--prod] # Vercel deployment
pnpm clean-packages            # Remove unused deps
pnpm verify-links              # Validate links
```

---

## Migration Instructions

### For Users (Post-Consolidation)

1. **Old commands still work** via wrapper scripts:

   ```bash
   # Still works (routed to unified-dev-setup.ts)
   pnpm dev
   pnpm build
   pnpm test
   pnpm lint
   ```

2. **New consolidated commands**:

   ```bash
   # Use these for advanced options
   pnpm health --all --cache
   pnpm refactor --types --dry-run
   pnpm db --truncate --setup
   ```

3. **Standalone scripts unchanged**:

   ```bash
   pnpm scaffold page my-page
   pnpm commit "feat: new feature"
   ```

---

## Technical Implementation Details

### Shared Utilities (new `src/scripts/shared/` directory)

```typescript
// confirmAction.ts — Interactive confirmation for destructive ops
export async function confirmAction(
  title: string,
  items: string[]
): Promise<boolean>;

// colors.ts — ANSI color utilities (no chalk dependency issues)
export const colors = { reset, red, green, blue, yellow, cyan };

// spinner.ts — Terminal spinner without dependencies
export function createSpinner(message: string): Spinner;

// logger.ts — Structured logging
export function log(
  level: "info" | "success" | "error" | "warn",
  message: string
): void;

// fileUtils.ts — Safe file operations
export async function deleteWithBackup(
  paths: string[]
): Promise<void>;
export async function getDiff(
  before: string,
  after: string
): Promise<string>;
```

### Design Principles

- **DRY (Don't Repeat Yourself)**: Shared utilities prevent code duplication
- **Composable**: Each unified script is made of smaller, testable functions
- **Safe by Default**: Dry-run mode for all operations, confirmations for destructive ops
- **Clear Feedback**: Progress bars, detailed logging, before/after diffs
- **No External Dependencies**: Prefer built-in Node.js APIs (fs, path, child_process)
- **CI/CD Friendly**: JSON output option for parsing in workflows

---

## Files to Archive

Archive to `.references/archived/scripts/` (preserve history):

- All 92 original reference scripts
- Old PowerShell/shell script pairs (28 pairs)
- Deleted scripts (queueWorker.ts, prioritySystem.ts, etc.)

Archive structure:

```
.references/archived/scripts/
├── comicwise/ (62 scripts)
├── comicr/ (30 scripts)
└── README.md (why archived + migration guide)
```

---

## Migration Timeline

**Phase 2A** (Complete): Script analysis and categorization ✅ **Phase 2B** (Next): Create 5 unified super-scripts + 7 standalone **Phase 2C** (Next): Archive reference directory cleanup **Phase 2D** (Next): Documentation and testing

---

## Success Metrics

- ✅ pnpm type-check → 0 errors
- ✅ pnpm test → 100% passing (no regressions)
- ✅ All old commands still work via wrappers
- ✅ New unified commands fully functional
- ✅ Dry-run mode works for all destructive operations
- ✅ Reference directory archived and cleaned

---

**Generated**: Batch 2, Phase 2A Complete **Next Action**: Proceed to Phase 2B (Create unified scripts)
