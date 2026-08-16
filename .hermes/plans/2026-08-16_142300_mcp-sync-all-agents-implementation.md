# MCP Server Sync — All Agents & Subrepos Implementation Plan

**Date:** 2026-08-16
**Status:** in_progress
**Goal:** Sync all MCP servers across Hermes, VS Code, OpenCode, Codex, Copilot configs + all project subrepos. Migrate npx→bunx/uvx. Push to development + production across root and all subrepos. Implement /hermes-networkchuck-course.

---

## Current State (Root Level — DONE)

| Config | Path | Servers | Bunx | Uxv | Http | Docker | Status |
|--------|------|---------|------|-----|------|--------|--------|
| Hermes (root) | `.mcp.json` | 25 | 11 | 1 | 8 | 1 | DONE |
| VS Code | `.vscode/mcp.json` | 25 | 11 | 1 | 8 | 1 | DONE |
| OpenCode | `opencode.json` | 25 | 11 | 1 | 8 | 1 | DONE |
| Codex | `.codex/mcp.json` | 25 | 11 | 1 | 8 | 1 | DONE |
| Copilot | `.copilot/mcp.json` | 25 | 11 | 1 | 8 | 1 | DONE |

**Servers (canonical 25):** ast-grep, code-sandbox, context7, fetch, filesystem, github, mcp-docker, memory, neon, playwright, sentry, sequential-thinking, smithery, tavily, honcho, mindstudio, python-quality, tooling-lint, tooling-config, parallel-search, parallel-task, django, docs, postgres, pytest

## Remaining Work

### Phase 1: Project-Level MCP Sync (PENDING)
16 project subrepos with `.vscode/mcp.json` — all have only 8 bunx servers. Need to add remaining 17 servers (honcho, mindstudio, python-quality, tooling-*, parallel-*, django, docs, postgres, pytest) while keeping existing 8.

**Modified subrepos (have M .vscode/mcp.json):**
- `projects/profile` — M .vscode/mcp.json (needs full sync)
- `projects/selenium_webdriver` — M .vscode/mcp.json (needs full sync)
- `projects/university-libary-jsm` — M .vscode/mcp.json (needs full sync)
- `projects/xamehi` — M .vscode/mcp.json (needs full sync)

**Unmodified subrepos (stale — only 8 servers, need full sync):**
- projects/Banking, comicwise, cookiecutter-django-tailwind, Django-Scrapy-Selenium, ecom
- projects/Python-projects, Resume_maker, rhixecompany-comics, rhixe_scans
- xamehi.tv, youtube-downloader

**Total: 15 project subrepos need MCP sync.**

### Phase 2: Git Push (BLOCKED)
GitHub push protection is blocking pushes to `development` on both root and subrepos due to a pre-existing commit (`8d2f9668`) containing what GitHub flags as Alibaba Cloud credentials in `credential-file-formats.md:43-44`.

**Root push status:** Commit `cf233417` ready locally with 32 files changed. Blocked by GH013.
**Subrepo pushes:** 4 done (profile, selenium_webdriver, university-libary-jsm, xamehi). 11 remaining.

**Resolution options:**
1. Sanitize the credential file in the old commit and force-push (risky — rewrites history)
2. Ask GitHub admin to unblock the secret via UI
3. Push to a different branch and merge

### Phase 3: Production Branch
Push to `production` branch on root + all subrepos after development succeeds.

### Phase 4: /hermes-networkchuck-course (PENDING)
Full implementation of the Hermes NetworkChuck course — needs investigation of what exists and what's needed.

---

## Execution Order

1. Sync all 15 project `.vscode/mcp.json` files (bunx/uvx, add missing servers)
2. Validate all JSON configs
3. Attempt git push (root → handle push protection)
4. Push all subrepos
5. Push production branches
6. Implement /hermes-networkchuck-course
