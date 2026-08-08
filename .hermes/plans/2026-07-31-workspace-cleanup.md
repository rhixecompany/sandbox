---
status: completed
---

# Workspace Cleanup Plan — 2026-07-31

> cwd: `C:\Users\Alexa\Desktop\SandBox` | baseline: 201 modified, 7 untracked (git)

## Scope

Clean inventory of 11,451 files (excluding node_modules + hermes-profiles mirror + .git).

## Findings

### A. Root-level clutter (~55 loose files)

- **30 tracked analysis scripts/JSONs at root** — `analyze_slice1.py`, `classify.py`, `build_registry.py`, `report.2026*.json`, `prompts_combined.txt` (4.27MB), `slice3.txt`, `uncle-eze.txt` (59B), `1614584020.txt` (10B), `cleanup.txt`, etc. — one-off pipeline artifacts from skills-audit runs
- **Report .md files** — FINAL_REPORT.md, SESSION_AUDIT_227.md, REPOSITORY_SUMMARY.md, PRESTATE_SandBox.md, THE_STORY_OF_THIS_REPO.md, GENERATOR_ORCHESTRATOR.md, hermes-hooks-audit.md
- **Duplicate script check needed**: root `audit_prompts.py` vs `scripts/audit_prompts.py`, root `build_registry.py` vs `scripts/build_registry.py`

### B. Duplicate directories

- `earnings-kit/` (5 files, 20KB) vs `uk-earnings-kit/` (38 files, 250KB) — earnings-kit is older superseded draft
- `plan/` (1 file) vs `plans/` (24 files) vs `.hermes/plans/` (4 files) — three plan stores
- `judge_results/` (18 files) + `results/` (3 files) — stale pipeline outputs from 2026-07-16

### C. Duplicate markdown (45 groups, ~712KB reclaimable)

- `docs/folder-structure/*` == `docs/Project_Architecture/*` copies (exact MD5)
- `docs/Project_Architecture/projects/*_techstack.md` == `projects/*/TECHNOLOGY_STACK.md` (per-project canonical)
- `docs/tech-stack/*` == `docs/Project_Architecture/projects/*_techstack.md` copies
- **DO NOT TOUCH**: `projects/profile/base/static/ckeditor` vs `projects/profile/static/ckeditor` (vendor trees), Python-projects vs youtube-downloader (separate real repos)

### D. scripts/ hygiene

- `MEMORY_precompact.md`, `USER_precompact.md` — pre-compact dumps (backup artifacts, delete)
- `audit-227.js` AND `audit-227.cjs` — duplicate (keep .cjs, it's the canonical per memory)
- `benchmark_results.json`, `benchmark_run_20260710.log` — stale pipeline artifacts
- `batch_remediate.py` — known 14-line no-op stub (memory)

### E. Stale/empty dirs

- Empty: `.firecrawl`, `.hermes/scripts`, `docs/archive`, `docs/audit`, `docs/catalog`, `docs/mcp`, `docs/references`
- `docs/` has 30+ loose report .md/.json/.txt — move to `docs/reports/`

### F. Large junk

- `prompts_combined.txt` (4.27MB) — combined dump, regenerable
- `.copilot/session-state/` (3.85MB, 15 files) — gitignored Copilot state, leave or delete
- `.hermes/archived-prompt-templates/` (771 md, 941KB) — pre-migration archive, already organized

## Plan (ordered by safety)

### Phase 1 — Consolidate plan stores (safe)

- `plan/repair-github-prompts.md` → `plans/` (merge, delete `plan/` dir)
- Keep root `plans/` (24 files) as legacy store; `.hermes/plans/` (4 files) as active

### Phase 2 — Root scripts/reports → organized dirs (safe, git-tracked)

- Analysis scripts (`.py`, `.cjs`) → `scripts/` (dedupe against existing first)
- Report .md/.json/.txt → `docs/reports/`
- Delete junk txt: `uncle-eze.txt`, `1614584020.txt`, `cleanup.txt`
- `prompts_combined.txt` → delete (regenerable)

### Phase 3 — scripts/ hygiene (safe)

- Delete `MEMORY_precompact.md`, `USER_precompact.md`, `benchmark_results.json`, `benchmark_run_20260710.log`
- Dedupe `audit-227.js` → delete (keep `.cjs`)

### Phase 4 — Dedupe markdown (reference-checked)

- Delete exact duplicates where one copy is unreferenced (keep `docs/Project_Architecture` copies; delete `docs/folder-structure`/`docs/tech-stack` dupes)
- Verify references before each delete

### Phase 5 — Earnings kit consolidation

- Merge unique content from `earnings-kit/` → `uk-earnings-kit/`
- Delete superseded `earnings-kit/`

### Phase 6 — Stale pipeline outputs

- Delete `judge_results/` (18 files), `results/` (3 files)

### Phase 7 — Empty dirs

- Remove 7 empty dirs

### Phase 8 — Verify

- Re-run duplicate scan (expect ~0 groups)
- `git status` diff vs baseline
- Confirm no broken references (grep key paths)

## COMPLETED — 2026-07-31 23:20

- Phase 1 ✅ plan/ merged into plans/
- Phase 2 ✅ 13 root scripts → scripts/archive/, 3 colliding → root_ prefixed, 17 reports → docs/reports/, 4 junk txt deleted
- Phase 3 ✅ scripts/ hygiene (precompact dumps, benchmark artifacts, audit-227.js dup, batch_remediate.py stub)
- Phase 4 ✅ 22 duplicate md deleted (315KB) — per-project TECHNOLOGY_STACK.md + docs/Project_Architecture kept
- Phase 5 ✅ earnings-kit/ 5 unique files → uk-earnings-kit/legacy-earnings-kit/, dir removed
- Phase 6 ✅ judge_results/ + results/ removed
- Phase 7 ✅ 7 empty dirs removed + docs/ loose artifacts → docs/reports/
- Phase 8 ✅ verified: all deletions gone, keepers present, no broken references, md dupes down to 14 cross-repo/vendor groups (untouched by design)

Final root: docs/ hermes-profiles/ node_modules/ plans/ projects/ research/ scripts/ uk-earnings-kit/ + config files
