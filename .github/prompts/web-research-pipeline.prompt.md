---
name: web-research-pipeline
title: Web Research Pipeline (Tavily-First)
description: "Search the web, extract full content from discovered pages, and save crisply formatted\
  \ markdown files \u2014 one per source. Uses Tavily MCP as primary search/extract backend."
version: 2.1.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
  - web
  - mcp
scripts: []
skills:
  - domain-intel
formatter: default
plan: ''
dependencies:
  - tool:mcp-tavily
  - tool:mcp-fetch
  - skill:domain-intel
tags:
  - backend
  - markdown
  - mcp
  - tavily
  - workflows
trigger: /web-research-pipeline
metadata:
  hermes:
    related_skills:
      - tool:mcp-tavily
      - tool:mcp-fetch
      - domain-intel
---

## Goal
Web search → extract full content → save as formatted markdown. **Tavily-first approach:** prefer `mcp__tavily__tavily_search` + `mcp__tavily__tavily_extract`, fall back to `mcp__fetch__get_markdown`, then `web_extract`.

## Workflow
Load the `web-research-pipeline` skill (this is a delegation prompt):
1. **Phase 1: Preflight** — Verify Tavily MCP server healthy
2. **Phase 2: Search** — `mcp__tavily__tavily_search` with bounded queries; use `search_depth: advanced` for thorough results, `time_range: year` for recency
3. **Phase 3: Extract** — `mcp__tavily__tavily_extract` → `mcp__fetch__get_markdown` → `web_extract`
4. **Phase 4: Save** — Markdown files with metadata header
5. **Phase 5: Domain Intel (optional)** — Passive recon
6. **Phase 6: Report** — Summary table

## Rules
1. **Tavily-first** — Prefer `mcp__tavily__tavily_search` over other backends.
2. **Multi-backend fallback** — Try all backends before declaring a URL failed.
3. **Never fabricate** — Every finding must trace to a real search or extraction.
4. **Preserve content** — Extract as-is; never summarize or truncate.
5. **Verify before saving** — Confirm extracted content is non-empty (>100 chars).
