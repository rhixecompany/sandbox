# Batch 1: Stabilize & Clean

> Extracted from `run.prompt.md`.

## Batch 1: Stabilize & Clean

**Goal**: Fix blockers, remove dead weight, establish clean baseline.

### Phase 1A: Fix TypeScript Errors (Debugger)

**File**: `src/components/search/search-results.tsx` (3 errors)

1. Verify bookmark import is `@/components/comics/bookmark-button` (TS2307)
2. Fix `comic.id` string→number mismatch: `Number(comic.id)` or update ComicCard props (TS2322)
3. Fix `comic.synopsis` nullable→optional: `comic.synopsis ?? undefined` (TS2322)
4. **Verify**: `pnpm type-check` → 0 errors

### Phase 1B: Documentation Cleanup (Reviewer)

**DELETE 6 files** (superseded):

- `docs/PHASE_2_COMPLETION.md`, `docs/PHASE_3_COMPLETION.md`
- `docs/PHASE4-3-DAY4-COMPLETE.md`, `docs/PHASE4-3-DAYS4-5-PLAN.md`
- `docs/debugger-context-map.md`, `docs/COMICWISE-PROJECT-STATUS.md`

**KEEP 19 files**: dev.content.md, database-context-map.md, SCRIPTS.md, QUICK_START.md, etc.

### Phase 1C: Components Cleanup (Reviewer)

1. **Resolve reading/reading-progress duplication**: 2 same-named files exist in both dirs (`reading-stats-card.tsx`, `continue-reading-card.tsx`). Grep imports → keep active one → delete duplicate → update imports.
2. **Create barrel exports**: `src/components/bookmarks/index.ts` (4 exports), `src/components/search/index.ts` (5 exports)
3. **Delete**: `src/components/shadcn-studio/` entirely (17 demo files)
4. **Check**: `src/app/admin/data.json` — delete if unused

### Phase 1D: VS Code Config Audit (Reviewer)

1. `settings.json`: Add `.references/` to `files.exclude` + `search.exclude`
2. `tasks.json`: Remove 28 one-time tasks, keep 13 reusable
3. `launch.json`: Verify all 9 configs reference valid scripts
4. `extensions.json`: Verify all 40 extension IDs still valid
5. `mcp.json`: Verify all 5 MCP servers accessible

### Batch 1 Verification

```
pnpm type-check → 0 errors
pnpm test → 241/241 passing
pnpm build → success
grep -r "shadcn-studio" src/ → 0 results
```

---
