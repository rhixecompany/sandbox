---
name: SandBox-root
title: "SandBox-root — Spec: MCP Server Install & Skills Creation"
description: "Spec for installing all 23 MCP servers globally via bunx, creating SKILL.md for each, syncing profiles, and integrating ~/Desktop/instructions/*.instructions.md references"
version: 1.0.0
status: in_progress
created: 2026-08-16
tags: [spec, mcp, skills, bunx, profiles, instructions, tools, hooks, quick-commands]

requirements:
  - R1: All 23 MCP servers are installed globally and resolvable via bunx without errors
  - R2: Each MCP server has a SKILL.md in .github/skills/<server>/ with proper frontmatter, description, workflows, gotchas, references
  - R3: Skills follow best practices from agent-skills.instructions.md, agent-safety.instructions.md, context7.instructions.md
  - R4: All 7 profiles have complete SOUL.md, USER.md, MEMORY.md
  - R5: Profile sync scripts created and tested in scripts/
  - R6: MCP management tool (hermes-mcp-manager.py) works: list, test, install, skills
  - R7: MCP health check hook (mcp-health-check.sh) works and registered in config
  - R8: Quick commands for MCP management added to config.yaml
  - R9: Reference triage complete: all 189 + 407 instruction files categorized by domain
  - R10: All changes committed to root + subrepos with zero git errors

acceptance_criteria:
  - AC1: `bunx -y <package>` succeeds for all installable npm packages
  - AC2: 23 SKILL.md files exist with YAML frontmatter, description (WHAT/WHEN/KEYWORDS), workflows, gotchas
  - AC3: Skills reference agent-skills, agent-safety, context7, context-engineering, code-review instructions
  - AC4: All 7 profiles have SOUL.md, USER.md, MEMORY.md — full content
  - AC5: Profile audit script runs, reports status for all profiles
  - AC6: `python scripts/hermes-mcp-manager.py list` shows all 23 servers
  - AC7: `bash hooks/mcp-health-check.sh` runs without errors
  - AC8: config.yaml has mcp:list, mcp:test, mcp:install, mcp:skills quick commands
  - AC9: Reference catalog created documenting instruction file categories
  - AC10: Git status clean at root and all submodules after commit
---

# MCP Server Install + Skills — Spec

## Purpose

Make all 23 Hermes MCP servers fully operational with global bunx dependencies, wrap each in a proper SKILL.md that exposes/uses/tests it, sync all profile identity files, and integrate the large reference library.

## Scope

### MCP Servers (23 total)

**npm/bunx-based (12):**

1. ast-grep — @notprolands/ast-grep-mcp ✅
2. code-sandbox — node-code-sandbox-mcp ⚠ (fails npx too — needs investigation)
3. fetch — mcp-server-fetch-typescript ✅
4. filesystem — @modelcontextprotocol/server-filesystem ⚠ (fails npx too)
5. github — @modelcontextprotocol/server-github ✅
6. memory — @modelcontextprotocol/server-memory ✅
7. playwright — @playwright/mcp@0.0.78 ✅
8. sequential-thinking — @modelcontextprotocol/server-sequential-thinking ✅
9. django — @mamounalzyoud/django-mcp-server@2.0.0 (correct name)
10. docs — @speakeasy-api/docs-mcp-core@0.17.1 (correct name)
11. postgres — @yawlabs/postgres-mcp@0.10.0 (correct name)
12. pytest — pytest-mcp-server@1.1.6 (correct name)

**HTTP-based (8 — no npm install needed):** 13. honcho — https://mcp.honcho.dev/ 14. neon — https://mcp.neon.tech/mcp 15. context7 — https://mcp.context7.com/mcp 16. sentry — https://mcp.sentry.dev/mcp 17. tavily — https://mcp.tavily.com/mcp/ 18. parallel-search — https://search.parallel.ai/mcp 19. parallel-task — https://task-mcp.parallel.ai/mcp 20. smithery — https://mcp.smithery.ai/alexanderrhixe30

**Binary/executable (3 — no npm install needed):** 21. mcp-docker — docker mcp gateway 22. mindstudio — .mindstudio/bin/mindstudio.exe mcp 23. python-quality/tooling-lint/tooling-config — Python scripts

### Reference Files

- ~/Desktop/instructions/: 189 *.instructions.md
- ~/Desktop/docs/: documentation dir
- ~/Desktop/SandBox/**/*.instructions.md: 407 files

### Profiles (7)

default, alexa, code-architect, creative-director, exec-assistant, patient-tutor, research-analyst

## Requirements

### R1: Global bunx installation

Install all npm packages globally. For packages not on npm under expected names, use correct names found via npm search.

### R2: MCP Skills

Each MCP server gets SKILL.md with agent-skills.instructions.md format.

### R3: Best Practice Integration

Skills incorporate agent-skills, agent-safety, context7, context-engineering, code-review guidance.

### R4: Profile Sync

All 7 profiles have complete SOUL.md/USER.md/MEMORY.md.

### R5: Tools/Hooks/Quick Commands

MCP management tool, health check hook, quick commands in config.yaml.

### R6: Reference Triage

Categorize all instruction files by domain.

## Acceptance Criteria

- AC1-10 as listed in frontmatter
