# Repo Normalization Report

> Generated: 2026-05-30 | Refreshed: 2026-06-01 | Phase 7 — Branch normalization verification

## Summary

**12 / 14 repos** are fully normalized to `production`/`development` branch structure. 1 exception (comicwise). 1 repo with naming quirk (profile).

| Repo | Local Branches | Remote Branches | Default Branch | Status |
|------|---------------|----------------|----------------|--------|
| banking | production, development | production, development | production | ✅ |
| comicwise | production, development | main only | main | ⚠️ Exception |
| cookiecutter-django-tailwind | production, development | production, development | production | ✅ |
| Django-Scrapy-Selenium | production, development | production, development | production | ✅ |
| ecom | production, development | production, development | production | ✅ |
| profile | production, development | production, development | production | ✅ |
| Python-projects | production, development | production, development | production | ✅ |
| rhixe_scans | production, development | production, development | production | ✅ |
| rhixecompany-comics | production, development | production, development | production | ✅ |
| selenium_webdriver | production, development | production, development | production | ✅ |
| university-libary-jsm | production, development | production, development | production | ✅ |
| xamehi.tv | production, development | production, development | production | ✅ |
| xamehi | production, development | production, development | production | ✅ |
| youtube-downloader | production, development | production, development | production | ✅ |

### comicwise Exception Detail

- Remote origin has only `main` branch (default = `main`)
- Local has `production` + `development` with divergent history (80 ahead, 69 behind origin/main)
- Per `repo.prompts.md` pitfalls: **skip push** — local is experimental/sandbox testing
- No push or force-push operations should target comicwise's remote

### profile Quirk

- Local directory is `projects/profile` but GitHub remote is `rhixecompany/rhixecompany`
- Branch state is clean and normalized (production + development, default = production)
- No action needed; just note the name mismatch for automation scripts

## Working-Tree Dirtiness

| Repo | Dirty State | Detail |
|------|------------|--------|
| banking | ❌ 60 staged deletions | `.github/agents/`, `.github/instructions/`, `.github/prompts/` files staged for removal — intentional cleanup |
| comicwise | ⚠️ 1 modified, 1 deleted | `QUALITY_GATE_FIX_REPORT.md` modified, `TRIAGE_REPORT.md` deleted |
| cookiecutter-django-tailwind | ⚠️ 1 modified | `AGENTS.md` modified but unstaged |
| selenium_webdriver | ⚠️ 1 untracked | `AGENTS.md` not yet added to git |
| university-libary-jsm | ⚠️ 1 modified | `.vscode/settings.json` modified (local IDE config) |
| xamehi | ⚠️ 1 untracked | `AGENTS.md` not yet added to git |

## Ignore File Status (top-level)

| Repo | .gitignore | .dockerignore | .prettierignore | .eslintignore | Notes |
|------|-----------|--------------|----------------|--------------|-------|
| banking | ✅ | ✅ | ✅ | ✅ | Complete |
| comicwise | ✅ | ✅ | ✅ | — | ESLint not confirmed in toolchain |
| cookiecutter-django-tailwind | ✅ | ✅ | — | — | Template project |
| Django-Scrapy-Selenium | ✅ | ✅ | — | — | Consolidation source |
| ecom | ✅ | — | — | — | Django 3.1 EOL needs upgrade |
| profile | ✅ (+.gcloudignore) | — | — | — | GitHub name mismatch |
| Python-projects | ✅ | — | — | — | Standalone collection |
| rhixe_scans | ✅ | ✅ | ✅ | ✅ | Complete |
| rhixecompany-comics | ✅ | ✅ | ✅ | ✅ | Complete |
| selenium_webdriver | ✅ | ✅ | ✅ | ✅ | Complete |
| university-libary-jsm | ✅ | — | ✅ | ✅ | Missing .dockerignore |
| xamehi.tv | ✅ | — | — | — | Low priority |
| xamehi | ✅ | — | — | — | Low priority |
| youtube-downloader | ✅ | — | — | — | Standalone tool |

## Consolidation Target

| Component | Status | Details |
|-----------|--------|---------|
| GitHub repo | ✅ Created | github.com/Rhixe-company/rhixecompany-comics |
| Default branch | ✅ production | — |
| Branches | ✅ production + development | Both on origin |
| Ignore files | ✅ Complete | .gitignore, .dockerignore, .prettierignore, .eslintignore |
| AGENTS.md | ✅ Present | — |
