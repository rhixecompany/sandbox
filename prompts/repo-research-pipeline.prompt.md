---
trigger: /repo-research-pipeline
name: repo-research-pipeline
title: "Repo Research Pipeline (MCP-Enhanced)"
description: >
  Structured workflow for executing web research across multiple projects
  and writing actionable RESEARCH_REPORT.md files. Delegates to the
  repo-research-pipeline skill and web-research-pipeline skill.
version: 2.0.0
tags: [hermes, research, repo, github, mcp]
dependencies:
  - skill:repo-research-pipeline
  - skill:web-research-pipeline
  - skill:mcp-github
  - skill:mcp-fetch
  - skill:domain-intel
skills:
  - repo-research-pipeline — Core multi-project research workflow
  - web-research-pipeline — Per-project web search and extraction
  - mcp-github — GitHub repo/code/issue search
  - mcp-fetch — Documentation extraction
  - domain-intel — Passive domain recon
---

## Goal

Run research across all project repos and produce RESEARCH_REPORT.md files
with verified sources. MCP-first: use mcp-github → mcp-fetch before built-in tools.

## Workflow

Load the `repo-research-pipeline` skill (primary implementation) plus
`web-research-pipeline` for per-project research:

1. **Phase 1: Inventory** — Find existing RESEARCH_REPORT.md files
2. **Phase 2: Per-Project Discovery** — Extract tech stack and generate queries
3. **Phase 3: Parallel Research** — Delegate to subagents via web-research-pipeline
4. **Phase 4: Report Writing** — Write/update RESEARCH_REPORT.md per project
5. **Phase 5: Index & Cross-Reference** — Verify cross-ref symmetry
6. **Phase 6: Verification** — Count, size gate, URL spot-checks

## Rules

1. **NO FABRICATION** — Every finding must trace to real search or extraction.
2. **VERIFY BEFORE CLAIMING** — Never report without running the command.
3. **SIZE GATE** — Reports 1KB–5KB. Trim over 5KB, expand under 1KB.
4. **SYMMETRIC CROSS-REFS** — If project A references B, B must reference A.
5. **MCP-FIRST** — mcp-github → mcp-fetch → mcp-smithery before built-in tools.
6. **MULTI-BACKEND** — If mcp-fetch fails, try firecrawl_scrape before giving up.
