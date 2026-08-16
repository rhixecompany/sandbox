---
name: SandBox-root
title: "SandBox-root — Plan"
description: "Plan for SandBox-root — AI-ready Bun monorepo: MCP sync, bunfig.toml, SPEC/PLAN for all repos, git push"
version: 3.0.0
status: in_progress
created: 2026-08-16
tags: [plan, repo, ai-ready, bun, mcp, bunfig, git]
---

# SandBox-root — Plan (v3)

## Overview

Complete the AI-readiness of the SandBox workspace and all 17 subrepos by:
1. Fixing Hermes MCP config (npx→bunx, enable disabled servers)
2. Creating bunfig.toml for all 18 repos
3. Updating root SPEC.md and PLAN.md
4. Validating and git pushing everything

## Stack
- Root: Bun 1.3.14 + TypeScript
- All subrepos: Bun (bun@1.3.14) as packageManager
- MCP: 25 servers across 5 config formats → Hermes config
- Hermes: C:\Users\Alexa\AppData\Local\hermes\config.yaml

## Phases

### Phase 1: Hermes MCP config fix (COMPLETE)
- [x] Identify 8 MCP servers in Hermes config using `npx` instead of `bunx`
- [x] Replace `npx` with `bunx` for: ast-grep, code-sandbox, fetch, filesystem, github, memory, playwright, sequential-thinking
- [x] Enable 4 disabled MCP servers: docs, postgres, pytest, django
- [x] Verify: `hermes mcp list` shows all 25 servers with correct commands

### Phase 2: Bunfig.toml creation (COMPLETE)
- [x] Create root `bunfig.toml` with best practices ([install], [test], [build], smol, logLevel)
- [x] Update Banking/bunfig.toml (was missing [test], [install], had wrong smol=true)
- [x] Update Bash/bunfig.toml (was missing [test], [install])
- [x] Create bunfig.toml for all 15 subrepos missing it:
  - comicwise, cookiecutter-django-tailwind, Django-Scrapy-Selenium, docs, ecom,
  - mcp-servers, mcp-server-typescript, profile, Python-projects, Resume_maker,
  - rhixe_scans, rhixecompany-comics, selenium_webdriver, university-libary-jsm,
  - xamehi.tv, xamehi, youtube-downloader
- [x] Verify: all 20 bunfig.toml files parse as valid TOML

### Phase 3: Root SPEC/PLAN update (COMPLETE)
- [x] Update SPEC.md to v3 with MCP sync requirements (R9-R12), bunfig requirements
- [x] Update PLAN.md to v3 with all phases, mark completed items

### Phase 4: Validation (COMPLETE)
- [x] Validate all bunfig.toml files parse as valid TOML — 20/20 OK
- [x] Verify Hermes config.yaml has 0 remaining npx commands for MCP servers
- [x] Verify `hermes mcp list` shows all servers enabled — 25/25 enabled
- [x] Run `bun run check` at root (pre-existing issues only, untracked files)

### Phase 5: Git operations — root (COMPLETE)
- [x] `git add` all changed files (bunfig.toml, SPEC.md, PLAN.md, + subrepo bunfig.toml)
- [x] `git commit` with conventional message (77fabd81)
- [x] `git push` to origin/development (a25479fb)

### Phase 6: Git operations — submodules (COMPLETE)
- [x] For each submodule with new/changed bunfig.toml: `cd`, `git add`, `git commit`, `git push`
- [x] Banking: 454a99d2
- [x] All 16 other subrepos: committed + pushed

### Phase 7: Final verification (IN PROGRESS)
- [ ] Re-run `bun run check` at root
- [ ] Verify `git status` clean at root and all submodules
- [ ] Confirm all SPEC.md/PLAN.md statuses are in_progress or done
- [ ] Report completion summary

## Acceptance
- [x] Root SPEC.md v3: status in_progress, all requirements listed (R1-R12)
- [x] Root PLAN.md v3: status in_progress, all phases actionable
- [x] All 18 repos have bunfig.toml with best practices (20/20 TOML valid)
- [x] Hermes config: 0 npx commands, all 25 MCP servers enabled
- [x] Git add/commit/push succeeds at root with zero errors
- [x] Git add/commit/push succeeds in every submodule with zero errors
- [x] `bun run check` at root passes or failures are documented
- [x] `hermes mcp list` shows all 25 servers enabled and healthy

## Risks
- Hermes config.yaml is outside the repo — changes won't be committed (intentional, it's a user config)
- Some subrepo bunfig.toml files are minimal (Python-only repos)
- Root push may hit GitHub secret-scanning on pre-existing commits
