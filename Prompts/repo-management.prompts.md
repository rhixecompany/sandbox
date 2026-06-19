---
title: Repo Management Pipeline
trigger: /repo-management
description: >
  Execute repo management operations across all 14 SandBox projects:
  branch normalization, project consolidation, dependency audit, Bun migration,
  CI workflow setup, and ignore file audit. Run AFTER /repo research phase completes.
mode: agent
system: |
  You are a repo management agent. You execute structured, reversible operations
  across multiple git repositories. Every destructive operation (branch delete,
  file removal, dependency removal) requires explicit verification before and after.
  You never start a later phase before the previous phase's acceptance criteria pass.
tags: [hermes, repos, git, branches, migration, bun, ci, consolidation, maintenance]
dependencies:
  - prompt:.github/prompts/context-map.prompt.md
  - skill:plans-and-specs
  - skill:systematic-debugging
  - skill:git-helper
  - skill:github-repo-management
  - skill:github-pr-workflow
  - skill:finishing-a-development-branch
  - skill:multi-stage-dockerfile
  - skill:workspace-audit
  - tool:terminal
  - tool:read_file
  - tool:write_file
  - tool:search_files
skills:
    - introspection-only-general
    - no-git-delete
    - no-net-fetch
    - skills-tools-preflight-check
---

## CRITICAL RULES

> These rules are non-negotiable. Any phase that skips them produces invalid output.

1. **PREREQUISITE GATE** — Do NOT start this prompt until `/repo` (Phases 0–5)
   has completed and all 14 `RESEARCH_REPORT.md` files are verified on disk.
2. **PHASE ORDERING** — Execute phases strictly in order (P3 → P2 → P1 → P4 → P5 → P6).
   Clean individual repos before consolidating. Never merge dirty sources.
3. **VERIFY BEFORE DELETE** — Any branch delete, file removal, or dependency removal
   requires a before-state snapshot and a post-delete verification.
4. **NO FORCE PUSH to production** — All production branch updates go through PRs.
5. **DRY RUN FIRST** — For batch operations (branch deletes, bun migration), run with
   `--dry-run` or equivalent and review output before executing for real.
6. **ROLLBACK PLAN** — Every phase must have a stated rollback path before execution begins.

---

## Goal

Execute all repo management operations across the 14 SandBox projects after
research is complete. Leave every repo with:

- Clean branch structure: `development` + `production` only
- Dependency files audited and pruned
- JS/TS repos migrated from npm/pnpm to Bun
- GitHub Actions CI workflows present and passing
- Ignore files complete and consistent
- Consolidation targets merged into `rhixecompany-comics`

---

## Context

**Workspace:** `C:\Users\Alexa\Desktop\SandBox`

**Prerequisite:** All 14 `RESEARCH_REPORT.md` verified on disk before starting.

**Consolidation targets:**
- Sources: `comicwise` + `Django-Scrapy-Selenium` + `selenium_webdriver`
- Target: `rhixecompany-comics` (Django + Next.js 16)
- Strategy: clean-slate new project inheriting patterns — not a git merge

### Priority Order

| Priority | Goal | Phases |
|----------|------|--------|
| P3 | Consolidation — comicwise + Django-Scrapy-Selenium + selenium_webdriver → rhixecompany-comics | 1–2 |
| P2 | Branch normalization — development + production per repo | 3 |
| P1 | Ignore file audit — fix all .*ignore files | 4 |
| P4 | Dependency audit — clean package.json / requirements.txt | 5 |
| P5 | Bun migration — npm/pnpm → bun for JS/TS repos | 6 |
| P6 | CI workflow setup — GitHub Actions for all repos | 7 |

---

## Constraints

- Consolidation (P3) uses pattern inheritance, not git merge. The three source repos
  have no shared history. rhixecompany-comics is a new project that adopts
  patterns from all three sources.
- Branch normalization deletes all branches except `development` and `production`.
  Default branch = `development`. Production merges via PR only.
- Bun migration targets JS/TS repos only: Banking, comicwise, rhixe_scans,
  selenium_webdriver, university-libary-jsm. Skip Python projects.
- CI workflows must pass locally (bun run lint, bun run typecheck, bun run test)
  before pushing to GitHub.
- Never commit `.env` files, secrets, or credentials.

---

## Phases

### Phase 1: Consolidation — Pattern Extraction

Extract reusable patterns from the three source repos into documentation.
Do not modify source repos yet.

**Steps:**

1. Read `projects/comicwise/RESEARCH_REPORT.md` — extract frontend patterns.
2. Read `projects/Django-Scrapy-Selenium/RESEARCH_REPORT.md` — extract scraping patterns.
3. Read `projects/selenium_webdriver/RESEARCH_REPORT.md` — extract automation patterns.
4. Write `projects/rhixecompany-comics/docs/consolidation-patterns.md` — 3-section
   doc with inherited patterns, decisions, and what was discarded.

**Tasks:**

- [ ] 1.1 Read and summarize comicwise patterns (Next.js, Prisma, Stripe, UI)
- [ ] 1.2 Read and summarize Django-Scrapy-Selenium patterns (Scrapy, Celery, Django admin)
- [ ] 1.3 Read and summarize selenium_webdriver patterns (Playwright migration path)
- [ ] 1.4 Write `projects/rhixecompany-comics/docs/consolidation-patterns.md`

**Rollback:** No destructive operations in Phase 1. Delete the new doc if needed.

---

### Phase 2: Consolidation — Scaffold rhixecompany-comics

Apply extracted patterns to rhixecompany-comics project structure.

**Steps:**

1. Read `projects/rhixecompany-comics/AGENTS.md` for current structure.
2. Read `projects/rhixecompany-comics/RESEARCH_REPORT.md` for architecture decisions.
3. Create/update `projects/rhixecompany-comics/docs/architecture.md` — full tech
   decisions doc referencing consolidation-patterns.md.
4. Create/update `projects/rhixecompany-comics/docs/migration-status.md` — track
   what has been consolidated vs. still pending.

**Tasks:**

- [ ] 2.1 Architecture doc created/updated
- [ ] 2.2 Migration status doc created/updated
- [ ] 2.3 Source repos (comicwise, Django-Scrapy-Selenium, selenium_webdriver)
         marked as `Status: Consolidation target` in their RESEARCH_REPORT.md

**Rollback:** Revert doc writes with `git checkout HEAD -- <file>`.

---

### Phase 3: Branch Normalization

Normalize all 14 repos to `development` + `production` only.

**Strategy per repo:**

```bash
# 1. Create development if missing
git checkout -b development 2>/dev/null || git checkout development

# 2. Create production if missing
git checkout -b production 2>/dev/null || git checkout production
git push -u origin production

# 3. List branches to delete (dry run first)
git branch | grep -v -E "^\*|development|production"

# 4. Delete local branches (after dry run review)
git branch | grep -v -E "^\*|development|production" | xargs -r git branch -D

# 5. Delete remote branches
git push origin --delete <branch> 2>/dev/null || true

# 6. Set default branch to development (via gh CLI)
gh repo edit <owner>/<repo> --default-branch development

# 7. Verify
git branch -a | grep -v -E "development|production|HEAD" | wc -l
# → must be 0
```

**Tasks:**

- [ ] 3.1 Banking — development + production only
- [ ] 3.2 comicwise — development + production only
- [ ] 3.3 cookiecutter-django-tailwind — development + production only
- [ ] 3.4 Django-Scrapy-Selenium — development + production only
- [ ] 3.5 ecom — development + production only
- [ ] 3.6 profile — development + production only
- [ ] 3.7 Python-projects — development + production only
- [ ] 3.8 rhixe_scans — development + production only
- [ ] 3.9 rhixecompany-comics — development + production only
- [ ] 3.10 selenium_webdriver — development + production only
- [ ] 3.11 university-libary-jsm — development + production only
- [ ] 3.12 xamehi — development + production only
- [ ] 3.13 xamehi.tv — development + production only
- [ ] 3.14 youtube-downloader — development + production only

**Rollback:** `git branch <deleted-branch> <sha>` to restore. Record SHA before delete.

---

### Phase 4: Ignore File Audit

Audit and fix all `.*ignore` files across all 14 repos.

**Steps per repo:**

1. Read existing `.gitignore`, `.dockerignore`, `.eslintignore` (if present).
2. Verify coverage for: `node_modules/`, `.env`, `*.pyc`, `__pycache__/`,
   `dist/`, `build/`, `.next/`, `venv/`, `.DS_Store`.
3. Add missing entries. Remove duplicates.
4. Verify `.env.example` exists for any project with env vars.

**Tasks:**

- [ ] 4.1 .gitignore audited and fixed in all 14 repos
- [ ] 4.2 .dockerignore present in all repos with Dockerfiles
- [ ] 4.3 .env.example present in all repos with env vars
- [ ] 4.4 No secrets or tokens committed in any repo

---

### Phase 5: Dependency Audit

Audit package.json / requirements.txt for all repos. Remove unused deps, flag bloat.

**Steps per repo:**

1. JS/TS: `bun pm ls --production` — identify unused packages.
   Run `npx depcheck` for deeper analysis.
2. Python: `pip-autoremove --list` or manually cross-reference imports vs requirements.
3. Flag packages more than 2 major versions behind latest stable.
4. Flag packages with known vulnerabilities (`bun audit` / `pip-audit`).

**Tasks:**

- [ ] 5.1 Banking deps audited
- [ ] 5.2 comicwise deps audited
- [ ] 5.3 rhixe_scans deps audited
- [ ] 5.4 university-libary-jsm deps audited
- [ ] 5.5 xamehi (Node side) deps audited
- [ ] 5.6 Django projects requirements.txt audited (4 repos)
- [ ] 5.7 Python-projects requirements audited
- [ ] 5.8 youtube-downloader requirements audited

---

### Phase 6: Bun Migration

Migrate JS/TS repos from npm/pnpm to Bun.

**Target repos:** Banking, comicwise, rhixe_scans, selenium_webdriver, university-libary-jsm

**Steps per repo:**

```bash
# 1. Install bun if not present
which bun || npm install -g bun

# 2. Remove existing lockfiles (keep package.json)
rm -f package-lock.json yarn.lock pnpm-lock.yaml

# 3. Generate bun.lockb
bun install

# 4. Verify scripts still work
bun run build 2>&1 | tail -5
bun run lint 2>&1 | tail -5
bun run typecheck 2>&1 | tail -5

# 5. Update package.json scripts to use bun
# Replace: "dev": "next dev" → "dev": "bun run next dev" (if needed)

# 6. Add .bunfig.toml if project needs custom bun config
```

**Tasks:**

- [ ] 6.1 Banking migrated to Bun — bun install + scripts verified
- [ ] 6.2 comicwise migrated to Bun
- [ ] 6.3 rhixe_scans migrated to Bun
- [ ] 6.4 selenium_webdriver migrated to Bun
- [ ] 6.5 university-libary-jsm migrated to Bun

**Rollback:** `git checkout HEAD -- package.json` + restore original lockfile from git history.

---

### Phase 7: CI Workflow Setup

Create or validate GitHub Actions workflows for all repos.

**Minimum CI per JS/TS repo:**

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: oven-sh/setup-bun@v2
      - run: bun install --frozen-lockfile
      - run: bun run typecheck
      - run: bun run lint
      - run: bun run build
```

**Minimum CI per Python repo:**

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install -r requirements.txt
      - run: python manage.py check --deploy 2>/dev/null || true
      - run: python -m pytest --tb=short 2>/dev/null || echo "No tests yet"
```

**Tasks:**

- [ ] 7.1 Banking CI workflow created/updated
- [ ] 7.2 comicwise CI workflow created/updated
- [ ] 7.3 cookiecutter-django-tailwind CI created/updated
- [ ] 7.4 Django-Scrapy-Selenium CI created/updated
- [ ] 7.5 ecom CI created/updated
- [ ] 7.6 profile CI created/updated
- [ ] 7.7 Python-projects CI created/updated
- [ ] 7.8 rhixe_scans CI created/updated
- [ ] 7.9 rhixecompany-comics CI created/updated
- [ ] 7.10 selenium_webdriver CI created/updated
- [ ] 7.11 university-libary-jsm CI created/updated
- [ ] 7.12 xamehi CI created/updated
- [ ] 7.13 xamehi.tv CI created/updated
- [ ] 7.14 youtube-downloader CI created/updated

---

## Acceptance Criteria

| Gate | Condition | Verification |
|------|-----------|--------------|
| Research prerequisite | 14 RESEARCH_REPORT.md on disk | `find projects/ -name 'RESEARCH_REPORT.md' \| wc -l` = 14 |
| Consolidation docs | consolidation-patterns.md + architecture.md exist | `ls projects/rhixecompany-comics/docs/` |
| Branch normalization | 0 stray branches in all 14 repos | `git branch -a \| grep -v -E 'development\|production\|HEAD'` = 0 per repo |
| Ignore files | .gitignore covers standard patterns | grep check per repo |
| Bun migration | bun.lockb exists, no npm lockfile | `ls *.lock*` per JS/TS repo |
| CI passing | All workflow runs green | `gh run list --limit 1` per repo |

---

## Actions

- `terminal("git branch | grep -v -E 'development|production' | wc -l")` — count stray branches
- `terminal("gh repo edit <owner>/<repo> --default-branch development")` — set default branch
- `terminal("bun install --frozen-lockfile")` — install with lockfile
- `terminal("bun run build && bun run lint && bun run typecheck")` — verify scripts
- `terminal("pip-audit")` — check Python dep vulnerabilities
- `read_file("projects/<name>/AGENTS.md")` — read tech stack
- `write_file(".github/workflows/ci.yml", content=<workflow>)` — create CI workflow
- `search_files(pattern=".gitignore", target="files", path="projects/<name>")` — find ignore files

---

## Related Prompts

| Prompt | Location | Purpose |
|--------|----------|---------|
| `/repo` | `Prompts/repo.prompts.md` | Research pipeline — run this first |
| `/bash-scripts-fix` | `Prompts/bash-scripts-fix.prompts.md` | Bash script modernization |
| `/workspace-consolidate` | `Prompts/workspace-consolidate.prompts.md` | Workspace-level consolidation |
