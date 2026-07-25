---
name: repo-research-pipeline
title: Repo Research Pipeline (MCP-Enhanced)
description: Structured workflow for executing web research across multiple projects and writing
  actionable RESEARCH_REPORT.md files. Delegates to the repo-research-pipeline skill
  and web-research-pipeline skill.
version: 2.1.0
license: MIT
author: Hermes Agent
toolsets:
  - browser
  - code_execution
  - file
  - mcp
  - terminal
  - web
scripts: []
skills:
  - domain-intel
  - gh-cli
  - web-research-pipeline
  - subagent-driven-development
formatter: default
plan: ''
dependencies:
  - prompt:web-research-pipeline
  - skill:domain-intel
  - skill:gh-cli
  - tool:mcp-tavily
  - tool:mcp-fetch
  - tool:mcp-filesystem
  - tool:mcp-github
  - tool:mcp-memory
  - tool:mcp-playwright
  - tool:mcp-sequential-thinking
  - skill:subagent-driven-development
  - skill:web-research-pipeline
tags:
  - frontend
  - generator
  - git
  - mcp
  - prompts
  - skills
  - typescript
  - vscode
  - workflow
trigger: /repo-research-pipeline
metadata:
  hermes:
    related_skills:
      - domain-intel
      - gh-cli
      - web-research-pipeline
      - tool:mcp-fetch
      - tool:mcp-filesystem
      - tool:mcp-github
      - tool:mcp-memory
      - tool:mcp-playwright
      - tool:mcp-sequential-thinking
---

## Goal

Run research across all project repos and produce RESEARCH_REPORT.md files
with verified sources. **Tavily-first:** use `mcp__tavily__tavily_search` → `mcp__tavily__tavily_extract` before other backends.

## Workflow

Load the `repo-research-pipeline` skill (primary implementation) plus
`web-research-pipeline` for per-project research:

1. **Phase 1: Inventory** — Find existing RESEARCH_REPORT.md files
2. **Phase 2: Per-Project Discovery** — Extract tech stack and generate queries
3. **Phase 3: Parallel Research** — Delegate to subagents via web-research-pipeline
4. **Phase 4: Report Writing** — Write/update RESEARCH_REPORT.md per project
5. **Phase 5: Index & Cross-Reference** — Verify cross-ref symmetry
6. **Phase 6: Verification** — Count, size gate, URL spot-checks
7. **Phase 7: Quick Onboarding** — For ad-hoc questions, delegate to `repo.prompt.md`'s
   **Quick Repo Onboarding** section (Q1–Q4: summarize, entrypoint, PR workflow, disk usage).

## Rules

1. **NO FABRICATION** — Every finding must trace to real search or extraction.
2. **VERIFY BEFORE CLAIMING** — Never report without running the command.
3. **SIZE GATE** — Reports 1KB–5KB. Trim over 5KB, expand under 1KB.
4. **SYMMETRIC CROSS-REFS** — If project A references B, B must reference A.
5. **TAVILY-FIRST** — `mcp__tavily__tavily_search` → `mcp__tavily__tavily_extract` → `mcp__fetch__get_markdown` → firecrawl_scrape → `web_extract`.
6. **MULTI-BACKEND** — Try all backends before declaring a URL failed.