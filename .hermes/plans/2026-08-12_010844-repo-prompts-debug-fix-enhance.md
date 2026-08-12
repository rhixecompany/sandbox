---
name: repo-prompts-debug-fix-enhance
title: "Debug, Fix, Verify, Enhance .github/prompts/repo*.md"
description: "Repair markdown corruption, normalize frontmatter, add Hooks/Scripts/Tools/MCP sections, and add destructive-op consent gates to the 6 repo prompt files."
version: 1.0.0
author: Hermes Agent (OWL)
license: MIT
tags: [plan, prompts, repo, debug, fix, enhance]
---

# Plan: Debug, Fix, Verify, Enhance `.github/prompts/repo*.md`

## Goal

Bring all 6 `repo*.md` prompt files under `.github/prompts/` to a consistent,
lint-clean, dependency-accurate state: fix markdown corruption, normalize
frontmatter, populate the **Skills / Scripts / Hooks / Tools / MCP / Related
Prompts** sections with entries that actually resolve, and add explicit
consent gates for destructive operations.

## Current Context (verified by inspection 2026-08-12)

### Files in scope

| File | Size | Version | State |
|------|------|---------|-------|
| `repo.prompt.md` | 22,662 B | 2.1.0 | **Heavy corruption** |
| `repo-management.prompt.md` | 6,812 B | 2.1.0 | Destructive ops w/o consent gate; MCP table mismatch |
| `repo-research-pipeline.prompt.md` | 5,779 B | 2.1.0 | Frontmatter/plan quoting; MCP table mismatch |
| `repo-story-time.prompt.md` | 5,781 B | 2.1.0 | Frontmatter/plan quoting; MCP table mismatch |
| `repo-init.prompt.md` | 3,828 B | 1.0.0 | Core sound; missing sections |
| `repo-tooling-implementation.prompt.md` | 4,553 B | 1.0.0 | Stub; empty skills/deps/scripts |

### Defects found (debug output)

1. **repo.prompt.md markdown corruption** (worst offender):
   - Glued/concatenated headings (`### Phase 0: PrerequisitesVerify tools...`).
   - Collapsed table rows: entire tables flattened to one line with `||` separators
     (Repo Inventory line ~106, Skills Required ~253, Secondary Goals ~289).
   - Mangled code fences: `read_file("projects/<name` + `> /RESEARCH_REPORT.md")`
     with `>` blockquote continuation artifacts inside fences (lines ~131-153,
     ~159-173, Report Template ~179-240).
   - `__name__` mangled to `**name**` (line ~159).
   - Report Template section corrupted — placeholders split across lines.
2. **Stale reference**: line 297 references
   `.hermes/archived-prompt-templates/repo.prompts/` — directory does NOT exist.
   Must be removed or repointed.
3. **Phase-number inconsistency**: `system:` says "Stop at Phase 4 (verification)"
   but `## Secondary Goals` says "Execute ONLY after Phase 5 verification passes".
   The file has exactly 4 phases (0-4). Fix to Phase 4.
4. **repo-management Phase 1** (`## Phase 1: Branch Normalization`) runs
   `git branch | grep -v -E "development|production" | xargs -r git branch -D`
   and `git push origin --delete <branch>` with NO approval gate. Violates
   standing rule: destructive ops need explicit consent. Must add a confirmation
   step (dry-run → list deletions → user approval → execute).
5. **MCP Servers & Tools section** lists only 6 servers
   (ast-grep/filesystem/sequential-thinking/fetch/playwright/github) while
   `dependencies:` frontmatter references tavily, memory, honcho, context7 etc.
   Section must match actual dependencies.
6. **Missing Hooks section**: prompts never mention the live hooks at
   `.github/hooks/` (session-logger, governance-audit, session-auto-commit,
   pre-exec-validate.sh, post-exec-state-log.py) or hook docs README.
7. **Missing Scripts section**: `scripts: []` everywhere; workspace has real
   scripts (`scripts/repo-init.py`, `.enhance/analyze_prompts.py`,
   `.github/hooks/*.py`) that should be referenced where relevant.
8. **Frontmatter inconsistency**: `plan: 'None'` (string) vs `plan: None` (null);
   repo.prompt.md has `mode: agent` + `system:` — other files omit them;
   repo-tooling-implementation has `plan: ''`.
9. **repo-tooling-implementation is a stub**: `skills: []`, `dependencies: []`,
   `scripts: []` — but `templates/repo-tooling-implementation/README.md` EXISTS
   (verified) and should be referenced with real execution steps + skill list.

### Verified assets (all exist — no new artifacts needed)

- Scripts: `scripts/repo-init.py` (12,226 B), `docs/ai-agents-inventory.md`
- Templates: `templates/_shared/` (14 files incl. skills-table-core, rules-core,
  personas, personality, section-skeleton, deps-core), `templates/repo-tooling-implementation/README.md`
- Hooks: `.github/hooks/` (session-logger, governance-audit, session-auto-commit, pre-exec-validate.sh, post-exec-state-log.py, README.md)
- Prompt deps: context-map, repo-management, repo-research-pipeline, repo-story-time, update-implementation-plan, web-research-pipeline, workspace-consolidate, bash-scripts-fix — **all resolve** ✓
- Skills (9 core): repo-research-pipeline, web-research-pipeline, repo-init, repo-management, github-repo-management, subagent-driven-development, dispatching-parallel-agents, firecrawl-search, firecrawl-scrape — **all exist** ✓
- Analyzer tooling: `.github/prompts/.enhance/analyze_prompts.py`, `classify_fences.py`, fixers (LF-only, proven against the 2026-07-31 heading-glue campaign)

## Proposed Approach

Targeted patching, not full rewrites (preserve prompt intent; fix the class of
corruption). Work in order of dependency: repo.prompt.md first (the orchestrator),
then the 5 satellite prompts. Every write is LF-only. No script/hook/template
content changes — only prompt files.

## Step-by-Step Plan

### Phase 0: Inventory & Backup (read-only + git)

- [ ] `git status` — confirm clean baseline for `.github/prompts/`
- [ ] Copy the 6 files to `.hermes/plans/docs/repo-prompts-backup-<ts>/` (or rely on git; do NOT create `.bak` files in repo)
- [ ] Run `.enhance/analyze_prompts.py` + `classify_fences.py` on the 6 files → save baseline report

### Phase 1: Audit (verification gates)

- [ ] markdownlint the 6 files (`npx markdownlint-cli2 .github/prompts/repo*.md` or repo-local equivalent) → record failures
- [ ] Frontmatter parse check on all 6 (YAML valid, known keys)
- [ ] Reference-resolution check: every `prompt:`, `skill:`, `tool:` in frontmatter resolves (script it)

### Phase 2: Fix repo.prompt.md (the big one)

- [ ] Rebuild corrupted table rows (Repo Inventory, Skills Required, Secondary Goals, Acceptance Criteria) as proper multi-line markdown tables
- [ ] Repair mangled code fences — remove `>` blockquote artifacts, close `<name>` placeholders correctly
- [ ] Fix `__name__` → back to `__name__`
- [ ] Rebuild the Report Template block cleanly (it is copied into every RESEARCH_REPORT.md)
- [ ] Fix phase numbering: Secondary Goals → "after Phase 4 verification passes"
- [ ] Remove stale `.hermes/archived-prompt-templates/repo.prompts/` reference (or repoint to `templates/_shared/`)
- [ ] Bump version → 2.2.0

### Phase 3: Normalize the 5 satellite prompts

- [ ] repo-management.prompt.md:
  - [ ] Add **consent gate** to Phase 1 branch normalization (dry-run list → explicit user approval → execute; never `xargs -r git branch -D` without it)
  - [ ] Align MCP section with actual deps; add Hooks/Scripts sections
  - [ ] Version → 2.2.0
- [ ] repo-research-pipeline.prompt.md: frontmatter `plan: None`, add Hooks/Scripts/MCP accuracy; version → 2.2.0
- [ ] repo-story-time.prompt.md: same normalization; version → 2.2.0
- [ ] repo-init.prompt.md: add Hooks/Scripts sections (repo-init.py, hooks README), add MCP table; version → 1.1.0
- [ ] repo-tooling-implementation.prompt.md: flesh out stub — reference the verified template README, populate skills (using-superpowers, systematic-debugging, verification-before-completion, executing-plans), deps, scripts; version → 1.1.0

### Phase 4: Add Required / Optional / Recommended sections (consistent across all 6)

- [ ] **Skills Required** — per-domain table (core: using-superpowers, systematic-debugging, verification-before-completion, executing-plans; domain-specific per file), pointing at `templates/_shared/skills-table-core.md` + inline table
- [ ] **Scripts** — list actual workspace scripts used by the workflow
- [ ] **Hooks** — reference `.github/hooks/README.md` + the 3 shared hooks; note pre-exec-validate / post-exec-state-log behavior
- [ ] **Tools / MCP Servers** — match `dependencies:` exactly (tavily, fetch, filesystem, github, memory, sequential-thinking, playwright, honcho, context7, ast-grep as applicable)
- [ ] **Related Prompts** — verify all cross-refs resolve (already verified: 8/8)

### Phase 5: Verify

- [ ] markdownlint clean on all 6 (LF only)
- [ ] `.enhance/analyze_prompts.py` re-run → no new MISSING/glue/corruption findings
- [ ] Frontmatter YAML parses; `plan:` null consistent
- [ ] Reference-resolution script → 100% resolve
- [ ] `git diff --stat` — only the 6 prompt files changed
- [ ] Idempotency: re-run analyzer, expect clean

### Phase 6: Deliver

- [ ] Concise summary: per-file fix list, verification results, any open questions

## Files Likely to Change

- `.github/prompts/repo.prompt.md` — major repair
- `.github/prompts/repo-management.prompt.md` — consent gate + sections
- `.github/prompts/repo-research-pipeline.prompt.md` — normalization
- `.github/prompts/repo-story-time.prompt.md` — normalization
- `.github/prompts/repo-init.prompt.md` — sections
- `.github/prompts/repo-tooling-implementation.prompt.md` — flesh out stub
- (No changes to scripts/, hooks/, templates/ — references only)

## Tests / Validation

- markdownlint (LF, all 6 files)
- `.enhance/analyze_prompts.py` + `classify_fences.py` before/after
- Frontmatter YAML parse (python `yaml.safe_load` on each frontmatter block)
- Reference-resolution script (prompt:/skill:/tool: existence)
- Manual diff review for repo.prompt.md report template integrity

## Risks, Tradeoffs, Open Questions

- **R1 — repo.prompt.md corruption is deep**: 383 lines with embedded artifacts.
  Mitigation: targeted patches per section; if a section is unrecoverable,
  rewrite that section from the Report Template + Related Prompts semantics.
  Never fabricate content — preserve existing findings/steps.
- **R2 — Destructive ops**: repo-management Phase 1 will be gated, but a user
  may still approve a bulk branch deletion. The gate must show the exact branch
  list and require a typed confirmation, not just "y".
- **R3 — Scope creep**: user asked for "all needed/required/optional/recommended"
  — keep additions reference-only; do not invent new hooks/scripts/skills that
  don't exist.
- **OQ1**: Should the 6 prompts consolidate to fewer files? Current design keeps
  them separate by trigger; leave structure as-is unless user asks.
- **OQ2**: repo.prompt.md mentions 17 projects with mcp-servers flagged CREATE —
  verify the project inventory still matches disk during execution.
- **OQ3**: Should `mode: agent` + `system:` fields be added to all prompts for
  consistency, or only kept where semantically needed (orchestrator vs leaf)?
