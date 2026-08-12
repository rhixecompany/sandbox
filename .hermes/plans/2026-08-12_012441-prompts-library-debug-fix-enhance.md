---
name: prompts-library-debug-fix-enhance
title: "Debug, Fix, Verify, Enhance .github/prompts/*.md (Full Library)"
description: "Systemic repair of all 228 prompt files: fix doubled-pipe tables (651 rows, 219 files), glued headings (105, 42 files), fence artifacts (57, 11 files), plan:'None' strings (203 files); normalize frontmatter; add Hooks/Scripts/Tools/MCP/Related sections; clear analyzer findings."
version: 1.0.0
author: Hermes Agent (OWL)
license: MIT
tags: [plan, prompts, library, repair, normalize, DRY]
---

# Plan: Debug, Fix, Verify, Enhance `.github/prompts/*.md`

## Goal

Repair and enhance ALL prompt files under `.github/prompts/` (228 `.md` files
at root, plus subdirs `docs/`, `templates/`) to a consistent, lint-clean,
dependency-accurate state:

1. Fix the systemic markdown corruption (same class already repaired in the 6
   `repo*.md` files in the previous plan execution).
2. Normalize frontmatter (`plan: 'None'` string → `null`, consistent versioning).
3. Add missing structural sections (Skills/Scripts/Hooks/Tools/MCP/Related
   Prompts) per file, reference-only — pointing at assets that exist.
4. Clear analyzer findings (`.enhance/analyze_prompts.py`).

## Current Context (verified by inspection 2026-08-12)

### Library inventory

- 228 root `.md` files (226 with frontmatter, 2 without: `generator-orchestrator-runbook.md`, `index.md` — decide: index.md is likely a landing doc, runbook is likely a standalone doc; may legitimately lack frontmatter).
- Subdirs: `docs/` (2+ files), `templates/` (14 files in `_shared/` + `repo-tooling-implementation/README.md`).
- Version spread: 1.0.0 (209), 2.0.0 (7), 1.1.0 (5), 2.2.0 (4), 2.1.0 (1).

### Corruption sweep results (all real, regex-verified)

| Class | Pattern | Hits | Files | Severity |
|-------|---------|------|-------|----------|
| A. Doubled leading pipes | `^\|\|` | **651** | **219** | Critical (breaks tables) |
| B. Glued headings | `^#{2,4} <80+ chars inline>` | **105** | 42 | High |
| C. Fence/blockquote artifacts | ```` ``` ```` or `> /` | **57** | 11 | Medium |
| D. `plan: 'None'` string | frontmatter `plan == 'None'` | **203** | 203 | Low (frontmatter hygiene) |
| E. Analyzer findings | `.enhance/analyze_prompts.py` | 8 | 8 | Medium/Info (RULES_INLINE_NOT_SHARED ×7, MISSING_RULES_SECTION + MISSING_EXECUTION_SECTION on test-providers-models) |

- Deep-corruption files (all 3 of A+B+C): 5 — `create-tldr-page.prompt.md`,
  `prompt-management.prompt.md`, `skills-fix.prompt.md`,
  `swift-mcp-server-generator.prompt.md`, `workspace-consolidate.prompt.md`.
- Worst single files (score ≥ 5): 38 files, led by `setup-groq-cloud.prompt.md`
  (50), `workspace-consolidate.prompt.md` (20), `dev-init.prompt.md` (19),
  `generator-orchestrator-runbook.md` (18), `dev-imp.prompt.md` (16).
- markdownlint: **0 errors** across all 228 files (structural lint passes; the
  corruption is invisible to markdownlint because doubled pipes still parse as
  tables/rows). Confirmed the same blind spot as repo.prompt.md before repair.

### Proven asset inventory (all verified to exist)

- Analyzer tooling: `.enhance/analyze_prompts.py`, `classify_fences.py`, LF-only fixers.
- Scripts: `scripts/repo-init.py`, `.github/hooks/*.py` + `*.sh` + `README.md`.
- Templates: `templates/_shared/` (skills-table-core, rules-core, personas, personality, section-skeleton, deps-core, best-practices, etc.).
- Hook set (5): session-logger, governance-audit, session-auto-commit, pre-exec-validate.sh, post-exec-state-log.py.
- MCP servers (config.yaml, live): tavily, fetch, filesystem, github, memory, sequential-thinking, context7, ast-grep, playwright, honcho, neon, docker, parallel-search, etc.

### Lessons carried from previous plan execution (repo*.md, completed 2026-08-12 01:0x)

- The corruption class is identical: a prior botched glue-repair pass doubled
  leading `|` on table rows and flattened headings onto body text.
- Fix pattern proven: strip doubled leading pipes → align tables via script →
  patch glued headings → fix fences → verify with markdownlint + analyzer.
- markdownlint `MD060` wants tables with consistent column alignment
  (re-enable after repair; it currently passes only because corrupted tables
  are structurally "consistent").
- Writing must stay LF-only; `.env`-style secrets never touched; never fabricate
  content — reconstruct from the visible remainder of each corrupted line.
- After every batch: re-run markdownlint + analyzer + ref-resolution script.

## Proposed Approach

Script-assisted repair, then targeted manual patches. Order of operations:

1. **Class A fix (651 rows, 219 files)** — deterministic, script-only: strip
   the doubled leading `|` (and `|||` → `|`) on table rows, then run the
   proven table-align routine. Low risk, high yield.
2. **Class B fix (105 glued headings)** — script to split `### Phase X: ...body`
   onto heading + body lines where the 80+ char inline run is a heading glued to
   following text; verify each split manually (sampling) because some long
   headings are legitimately long single lines.
3. **Class C fix (57 fence artifacts)** — remove empty fence pairs (```` ``` ````)
   and `> /` blockquote artifacts inside code blocks.
4. **Class D fix (203 plan:'None')** — frontmatter rewrite via python
   (yaml round-trip), exactly as proven on the repo files.
5. **Class E fix (8 analyzer findings)** — 7 RULES_INLINE_NOT_SHARED: add the
   `templates/_shared/rules-core.md` reference line above inline domain rules
   (repo-init pattern). test-providers-models: add Rules + Phases/Steps/Workflow
   sections.
6. **Enhancement pass** — add/verify MCP Servers & Tools, Hooks, Scripts,
   Related Prompts sections to files that lack them (reference-only; batch by
   file family).
7. **Verify** — full sweep: markdownlint, analyzer, ref-resolution, LF check,
   git diff scope.

## Step-by-Step Plan

### Phase 0: Inventory & Baseline (read-only + git)

- [ ] `git status` — confirm clean baseline (unrelated university-libary-jsm change expected)
- [ ] Run `.enhance/analyze_prompts.py` → capture `analysis_report.json` baseline (restore after)
- [ ] Run corruption-marker sweep script → save per-file scores to `.hermes/plans/docs/prompts-baseline-<ts>.json` (the exact regex set used above)
- [ ] Record markdownlint 0-error baseline

### Phase 1: Class A — Doubled Pipe Repair (script, batch ≤ 40 files)

- [ ] Write `repair_doubled_pipes.py` (temp, in scripts/ or .enhance/): for each `.md`, replace `^||` → `|` and `^|||` → `|` on table rows only (lines starting with `|`), leave non-table lines
- [ ] Re-run table-align routine on affected files
- [ ] After each batch of ≤ 40 files: markdownlint + spot-read 2 files
- [ ] Verify no data loss: diff shows only `|`-prefix changes

### Phase 2: Class B — Glued Headings (script + manual sampling)

- [ ] Write `split_glued_headings.py`: find `^#{2,4} <run>`, split at the first
   2+ spaces or `**` boundary where a body sentence begins; only split when the
   run > 120 chars OR contains code-fence markers
- [ ] Manual review list: every file whose split is ambiguous (long legitimate headings) → patch by hand
- [ ] Re-verify markdownlint

### Phase 3: Class C — Fence Artifacts

- [ ] Remove empty ```` ``` ```` pairs (adjacent open+close with nothing between)
- [ ] Remove `> /` blockquote artifacts inside code fences (context-aware: only where inside a fence)
- [ ] Verify fences balanced per file (count ``` parity)

### Phase 4: Class D — Frontmatter Normalization

- [ ] For all 226 files with frontmatter: yaml round-trip (sort_keys=False,
     allow_unicode), set `plan: null` when currently `'None'`, LF-only write
- [ ] Do NOT touch `mode: agent`/`system:` semantics; only fix `plan` type
- [ ] Version strategy decision (OQ3): keep existing versions; bump only files
     that get meaningful section additions

### Phase 5: Class E — Analyzer Findings

- [ ] 7 RULES_INLINE_NOT_SHARED files: add rules-core reference line + `### Domain Rules` heading
- [ ] test-providers-models.prompt.md: add `## Rules` + `## Phases` (or `## Workflow`) sections with ≥ 3 steps
- [ ] Re-run analyzer → expect 0 repo-family findings; remaining = 0 critical/high, 0 medium, 0 info

### Phase 6: Enhancement Pass (reference-only additions)

- [ ] For files lacking them (script scan: grep for `## MCP Servers & Tools`, `## Hooks`, `## Scripts`, `## Related Prompts`): add standard sections with verified asset lists (from Proven Asset Inventory)
- [ ] Batch by family (setup-*, create-*, csharp-*, java-*, etc.) to keep diffs reviewable
- [ ] Verify every new reference resolves (script)

### Phase 7: Verify (full gate)

- [ ] markdownlint: 0 errors on `.github/prompts/**/*.md`
- [ ] `.enhance/analyze_prompts.py`: 0 critical/high/medium/info
- [ ] Ref-resolution script: 100% (all prompt:/skill:/tool: resolve)
- [ ] LF check: 0 CRLF bytes across all files
- [ ] Fence parity: balanced ``` in every file
- [ ] `git diff --stat` — scope = prompt files + plan artifacts only; analyzer json restored
- [ ] Idempotency: re-run repair script → no further changes

### Phase 8: Deliver

- [ ] Per-class fix summary with counts, verification results, open questions

## Files Likely to Change

- All 228 `.github/prompts/*.md` (Class A touches 219; D touches 203; enhancements touch most)
- `.github/prompts/.enhance/analysis_report.json` (regenerated; restore via git after)
- `.hermes/plans/docs/prompts-baseline-<ts>.json` (new artifact, tracked or gitignored)
- No changes to scripts/, hooks/, templates/ (references only)

## Tests / Validation

- markdownlint-cli2 across `.github/prompts/**/*.md` (0 errors required)
- `.enhance/analyze_prompts.py` (0 findings required)
- Corruption-marker sweep re-run (0 hits for classes A/B/C)
- Fence-parity count per file
- Frontmatter YAML parse on all 226
- Ref-resolution script (all prompt:/skill:/tool: resolve)
- Git diff review: repair is lossless (only pipe-prefix/heading-split changes)

## Risks, Tradeoffs, Open Questions

- **R1 — Lossless repair ambiguity**: Class A is mechanical (safe). Class B
  splitting risks breaking legitimately long headings. Mitigation: split only
  where a clear body sentence follows (2+ spaces + lowercase start), manual
  review of every ambiguous case. Never fabricate content — if a line is
  unrecoverable, keep it as-is and flag it.
- **R2 — Bulk enhancement could inflate diffs**: 200+ files each gaining
  sections is a huge diff. Mitigation: batch by family, keep additions minimal
  and reference-only, and consider doing enhancements only where the file lacks
  the section entirely (not re-adding everywhere).
- **R3 — Scope**: "all needed/required/optional/recommended" — reference-only
  additions; do not invent hooks/scripts/skills/MCP servers that don't exist.
- **OQ1**: `generator-orchestrator-runbook.md` and `index.md` have no
  frontmatter — are they prompts or docs? (Plan: treat as docs, exclude from
  prompt-class repairs unless user says otherwise.)
- **OQ2**: Should `mode: agent` + `system:` be added to all prompts for
  consistency, or only where semantically needed? (Previous plan left this open.)
- **OQ3**: Version bump policy — bump only files with meaningful additions, or
  uniform bump to 2.2.0? Recommend: bump only changed files.
- **OQ4**: Should the enhancement pass run for all 228 or only the 38
  severe-corruption files + analyzer-flagged files? (Recommend: all files
  missing sections, batched.)
