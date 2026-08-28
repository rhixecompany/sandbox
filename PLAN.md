---
name: SandBox-root
title: "SandBox-root — Plan: MCP Server Install & Skills Creation"
description: "Plan for installing all 23 MCP servers globally via bunx, creating SKILL.md for each, syncing profiles, and integrating references"
version: 1.0.0
status: in_progress
created: 2026-08-16
tags: [plan, mcp, skills, bunx, profiles, instructions, tools, git]
---

# MCP Server Install + Skills — Plan

## Overview

Install all 23 MCP server npm dependencies globally, create SKILL.md for each server, sync all 7 profile identity files, triage references, and create management tools/hooks/quick commands.

## Phase 1: Install Global Bunx Dependencies

### 1.1 Already-installed packages (skip)

- [x] @notprolands/ast-grep-mcp (installed, works via npx)
- [x] mcp-server-fetch-typescript
- [x] @modelcontextprotocol/server-github
- [x] @playwright/mcp@0.0.78

### 1.2 Install remaining npm packages

- [ ] @modelcontextprotocol/server-memory (installed, works via npx)
- [ ] @modelcontextprotocol/server-sequential-thinking (installed, works via npx)
- [ ] @modelcontextprotocol/server-filesystem (fails — investigate)
- [ ] node-code-sandbox-mcp (fails — investigate)
- [ ] @mamounalzyoud/django-mcp-server@2.0.0 (correct name for django-mcp)
- [ ] @speakeasy-api/docs-mcp-core@0.17.1 (correct name for docs-mcp)
- [ ] pytest-mcp-server@1.1.6 (correct name for pytest-mcp)
- [ ] @yawlabs/postgres-mcp@0.10.0 (correct name for postgres-mcp)

### 1.3 Verify all installations

- [ ] Run `bunx -y <pkg>` for each, verify no errors
- [ ] For servers that fail, document as REPORT items

## Phase 2: Create MCP Skills (23 SKILL.md files)

### 2.1 Code/Development MCP Servers (6 skills)

- [ ] ast-grep — code search/replace, AST pattern matching
- [ ] code-sandbox — isolated Node.js execution sandbox
- [ ] playwright — browser automation, screenshots, console logs
- [ ] sequential-thinking — structured reasoning, chain-of-thought
- [ ] tooling-lint — ESLint + Prettier + Markdownlint + CSpell
- [ ] tooling-config — pre-commit + git-cliff + .gitignore validation

### 2.2 Data/Infrastructure MCP Servers (4 skills)

- [ ] filesystem — file read/write/search, directory ops
- [ ] memory — persistent memory storage CRUD
- [ ] postgres — PostgreSQL query, schema, connection management
- [ ] mcp-docker — Docker container management via MCP gateway

### 2.3 Search/Discovery MCP Servers (4 skills)

- [ ] context7 — authoritative external docs, API references
- [ ] tavily — web search with API key
- [ ] parallel-search — parallel web search
- [ ] parallel-task — parallel task execution

### 2.4 Platform/Integration MCP Servers (5 skills)

- [ ] github — GitHub API, PRs, issues, repos, code search
- [ ] fetch — web content extraction, HTTP requests
- [ ] smithery — MCP toolbox registry, tool discovery
- [ ] honcho — MCP gateway, session management (✅ DONE)
- [ ] mindstudio — MindStudio CLI, project management

### 2.5 Testing/Quality/Other MCP Servers (4 skills)

- [ ] python-quality — ruff linting + pyright type checking
- [ ] docs — documentation generation/management
- [ ] pytest — Python test execution
- [ ] django — Django ORM, settings, migrations
- [ ] neon — PostgreSQL cloud database (Neon)
- [ ] sentry — error tracking, issue management

## Phase 3: Profile Identity Sync

### 3.1 Audit profiles

- [ ] Check each of 7 profiles for SOUL.md, USER.md, MEMORY.md
- [ ] Identify missing/incomplete files

### 3.2 Create/complete profile files

- [ ] Create SOUL.md/USER.md/MEMORY.md for any missing
- [ ] Complete any stubs

### 3.3 Profile sync scripts

- [ ] Create scripts/profile-audit.py — audit all profiles
- [ ] Create scripts/profile-sync.py — sync common content

## Phase 4: Reference Triage

### 4.1 Categorize instruction files

- [ ] Group 189 ~/Desktop/instructions/*.instructions.md by domain
- [ ] Group 407 ~/Desktop/SandBox/**/*.instructions.md by domain
- [ ] Map instruction files to MCP servers where relevant

### 4.2 Create reference catalog

- [ ] Create docs/mcp-server-reference-catalog.md

## Phase 5: Tools, Hooks, Quick Commands

### 5.1 MCP Management Tool

- [x] hermes-mcp-manager.py: list, test, install, skills commands ✅ DONE
- [ ] Fix any bugs in the tool

### 5.2 Health Check Hook

- [x] mcp-health-check.sh created ✅ DONE
- [ ] Fix bash syntax error in case statement
- [ ] Register in config.yaml hooks section

### 5.3 Quick Commands

- [ ] config.yaml: add mcp:list, mcp:test, mcp:install, mcp:skills

## Phase 6: Git Operations

### 6.1 Root

- [ ] git add, commit, push

### 6.2 Subrepos

- [ ] For each affected subrepo: git add, commit, push

## Acceptance

- All bunx packages installed and working
- 23 SKILL.md files with complete content
- All 7 profiles complete
- Reference catalog created
- Tools/hooks/quick-commands working
- Git clean + pushed
