# Batch 2: Scripts Consolidation

> Extracted from `run.prompt.md`.

## Batch 2: Scripts Consolidation

**Goal**: Consolidate 92 reference scripts + 17 existing into unified DRY system.

### Phase 2A: Analyze & Categorize (Reviewer)

Read ALL scripts in `.references/comicwise/scripts/` and `.references/comicr/scripts/`. Categorize: Already Implemented | High-Value Missing | Redundant | Not Applicable. Create `docs/refactor-context.md` with categorized inventory + code samples grouped by Infrastructure, Database, Optimization, DevOps, Quality, Scaffolding.

### Phase 2B: Port New TypeScript Scripts (Implementer)

Create 5 in `src/scripts/` — ALL with `--dry-run`, `--verbose`, `--yes`, `--json`:

1. `project-cleanup.ts` — deep cleanup (duplicates, unused, temp files)
2. `cleanup-duplicates.ts` — pattern-based duplicate detection
3. `optimize-performance.ts` — bundle analysis + caching audit
4. `validate-env.ts` — env validation + `.env.local.example` sync
5. `fix-line-endings.ts` — CRLF→LF normalization

All use `confirmAction.ts` for destructive ops + Logger pattern from seed system.

### Phase 2C: Enhance Existing Scripts (Implementer)

1. `analyze-project.ts` — add security scan patterns
2. `scaffold.ts` — add DAL, schema, action templates
3. Audit ALL scripts for flag consistency (`--dry-run`, `--verbose`, `--yes`, `--json`)

### Phase 2D: Shell Scripts (Implementer)

1. Enhance `setup-dev.sh`/`.ps1` — add `--skip-db`, `--skip-seed`, `--skip-install`
2. Enhance `quality-gate.sh`/`.ps1` — add `tee`/`Tee-Object`, `pnpm build:debug`, timing, JSON summary
3. **NEW**: `dev.sh`/`dev.ps1` — prerequisites + dev server + browser
4. **NEW**: `cleanup.sh`/`cleanup.ps1` — artifact removal with dry-run

### Phase 2E: Update package.json (Implementer)

Add: `cleanup:project`, `cleanup:project:dry`, `cleanup:duplicates`, `cleanup:duplicates:dry`, `optimize:performance`, `optimize:performance:dry`, `validate:env`, `fix:line-endings`, `fix:line-endings:dry`. Verify existing, remove dead entries.

### Batch 2 Verification

```
pnpm type-check → 0 errors
tsx src/scripts/project-cleanup.ts --dry-run --verbose → runs
tsx src/scripts/validate-env.ts --dry-run → runs
docs/refactor-context.md exists with content
All package.json entries resolve
```

---
