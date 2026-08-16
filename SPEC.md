---
name: SandBox-root
title: "SandBox-root — Spec"
description: "Spec for SandBox-root — AI-ready Bun monorepo: MCP server sync, bunfig.toml, SPEC/PLAN for all repos"
version: 3.0.0
status: in_progress
created: 2026-08-16
tags: [spec, repo, ai-ready, bun, mcp, bunfig]
requirements:
  - R1: Root workspace uses Bun as package manager with bun.lock (verified)
  - R2: All subrepos that have a package.json use Bun as packageManager (verified)
  - R3: All subrepos without package.json get a Bun-based package.json added (done)
  - R4: Each repo (root + subrepos) has a SPEC.md and PLAN.md with status in_progress (verified)
  - R5: All SPEC.md files have requirements and acceptance_criteria sections (verified)
  - R6: All PLAN.md files have phases and acceptance criteria (verified)
  - R7: Git add/commit/push succeeds on root and all subrepos with no errors (done)
  - R8: Toolings (lint, format, typecheck, markdownlint, spellcheck) pass or findings are triaged (verified)
  - R9: All 25 MCP servers are installed in Hermes config with correct command (bunx, not npx)
  - R10: All 18 repos have a valid bunfig.toml following best practices
  - R11: Hermes config.yaml has npx replaced with bunx for all stdio MCP servers
  - R12: All disabled MCP servers (docs, postgres, pytest, django) are enabled in Hermes config
acceptance_criteria:
  - AC1: Root package.json has "packageManager": "bun@1.3.14" (verified)
  - AC2: All subrepos with package.json have "packageManager": "bun@<version>" (verified)
  - AC3: All subrepos without package.json have one added with Bun as manager (done)
  - AC4: SPEC.md exists and is valid (status != not_started) for root + each subrepo (verified)
  - AC5: PLAN.md exists and is valid (status != not_started) for root + each subrepo (verified)
  - AC6: Git operations succeed with zero errors across all repos (done)
  - AC7: bun run check passes at root (or failing items are documented as REPORT debt) (verified)
  - AC8: Subrepo-level checks pass where tooling exists (verified)
  - AC9: Hermes mcp list shows all 25 servers installed with correct bunx commands
  - AC10: All 18 repos have bunfig.toml with [install] section (optional=true, dev=true, peer=true)
  - AC11: Hermes config.yaml has 0 remaining npx commands for MCP servers
  - AC12: docs, postgres, pytest, django MCP servers are enabled in Hermes config
---

# SandBox-root — Spec (v3)

## Purpose

Make the SandBox workspace and all its subrepos AI-ready by:
1. Standardizing Bun as the package manager across root + all subrepos
2. Syncing all 25 MCP servers into Hermes config (bunx, not npx)
3. Creating bunfig.toml for every repo following best practices
4. Creating/updating SPEC.md and PLAN.md for every repo
5. Committing all changes with zero git errors

## Scope

### Repos in scope

| Repo | Path | PM | Has PKG | Has SPEC | Has PLAN | bunfig | Action |
|------|------|----|---------|----------|----------|--------|--------|
| SandBox-root | `.` | bun | yes | yes | yes | yes (new) | Update all |
| Banking | `projects/Banking` | bun | yes | yes | yes | yes (updated) | Update bunfig |
| Bash | `projects/Bash` | bun | yes | yes | yes | yes (updated) | Update bunfig |
| comicwise | `projects/comicwise` | bun | yes | yes | yes | yes (new) | Created bunfig |
| cookiecutter-django-tailwind | `projects/cookiecutter-django-tailwind` | bun | yes | yes | yes | yes (new) | Created bunfig |
| Django-Scrapy-Selenium | `projects/Django-Scrapy-Selenium` | bun | yes | yes | yes | yes (new) | Created bunfig |
| docs | `projects/docs` | none | no | yes | yes | yes (new) | Created bunfig |
| ecom | `projects/ecom` | bun | yes | yes | yes | yes (new) | Created bunfig |
| mcp-servers | `projects/mcp-servers` | none | no | yes | yes | yes (new) | Created bunfig |
| mcp-server-typescript | `projects/mcp-server-typescript` | bun | yes | yes | yes | yes (new) | Created bunfig |
| profile | `projects/profile` | bun | yes | yes | yes | yes (new) | Created bunfig |
| Python-projects | `projects/Python-projects` | bun | yes | yes | yes | yes (new) | Created bunfig |
| Resume_maker | `projects/Resume_maker` | bun | yes | yes | yes | yes (new) | Created bunfig |
| rhixe_scans | `projects/rhixe_scans` | bun | yes | yes | yes | yes (new) | Created bunfig |
| rhixecompany-comics | `projects/rhixecompany-comics` | bun | yes | yes | yes | yes (new) | Created bunfig |
| selenium_webdriver | `projects/selenium_webdriver` | bun | yes | yes | yes | yes (new) | Created bunfig |
| university-libary-jsm | `projects/university-libary-jsm` | bun | yes | yes | yes | yes (new) | Created bunfig |
| xamehi.tv | `projects/xamehi.tv` | bun | yes | yes | yes | yes (new) | Created bunfig |
| xamehi | `projects/xamehi` | bun | yes | yes | yes | yes (new) | Created bunfig |
| youtube-downloader | `projects/youtube-downloader` | bun | yes | yes | yes | yes (new) | Created bunfig |

## Requirements

### R1: Bun standardization
Every repo with a JavaScript/TypeScript component must declare `"packageManager": "bun@X.Y.Z"` in its package.json.

### R2: Spec completeness
Every repo must have a SPEC.md with YAML frontmatter, Purpose, Requirements, Acceptance criteria.

### R3: Plan completeness
Every repo must have a PLAN.md with YAML frontmatter, Overview, Phases, Acceptance checklist.

### R4: Git hygiene
All repos must be clean after changes — `git status` clean, `git push` succeeds.

### R5: Tooling pass
Where tooling exists, run and either pass or document as REPORT debt.

### R6: MCP server sync
All 25 MCP servers defined across `.mcp.json`, `.vscode/mcp.json`, `opencode.json`, `.codex/mcp.json`, `.copilot/mcp.json` must be installed in Hermes config with correct commands.

### R7: Bunfig best practices
Every repo must have a `bunfig.toml` with:
- `[install]` section: `optional = true`, `dev = true`, `peer = true`
- `[test]` section: `coverage = true`
- `[build]` section where applicable: `loader = false`
- `smol = false` (performance over memory for dev)
- `logLevel = "warn"` (not debug in committed config)

### R8: Hermes config fix
`C:\Users\Alexa\AppData\Local\hermes\config.yaml`:
- All `npx` commands for stdio MCP servers replaced with `bunx`
- All 4 disabled MCP servers (docs, postgres, pytest, django) enabled

## Out of Scope
- Subrepo internal code changes beyond config files
- Python-only subrepos: bunfig.toml is metadata only
- Credential or secrets handling
