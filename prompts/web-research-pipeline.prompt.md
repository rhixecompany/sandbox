---
trigger: web-research-pipeline
name: web-research-pipeline
title: "Web Research Pipeline (MCP-Enhanced)"
description: >
  Search the web, extract full content from discovered pages, and save crisply
  formatted markdown files — one per source. Delegates to the
  web-research-pipeline skill for implementation.
version: 2.0.0
author: Hermes Agent
license: MIT
tags: [hermes, research, web, scraping, mcp]
dependencies:
  - skill:web-research-pipeline
  - skill:mcp-fetch
  - skill:firecrawl-scrape
  - skill:domain-intel
skills:
  - web-research-pipeline — Core implementation (search → extract → save)
  - mcp-fetch — Primary URL content extraction (MCP-first)
  - firecrawl-scrape — JS-rendered page fallback
  - domain-intel — Optional passive domain recon
metadata:
  hermes:
    related_skills:
      - web-research-pipeline
      - mcp-fetch
      - firecrawl-scrape
      - domain-intel
---

## Goal

Web search → extract full content → save as formatted markdown. MCP-first approach:
prefer `mcp_fetch_get_markdown`, fall back to `firecrawl_scrape`, then `web_extract`.

## Workflow

Load the `web-research-pipeline` skill (this is a delegation prompt):

1. **Phase 1: Preflight** — Verify MCP servers healthy
2. **Phase 2: Search** — `firecrawl_search` or `web_search` with bounded queries
3. **Phase 3: Extract** — mcp-fetch → firecrawl → web_extract → scrapling → playwright
4. **Phase 4: Save** — Markdown files with metadata header
5. **Phase 5: Domain Intel (optional)** — Passive recon
6. **Phase 6: Report** — Summary table

## Rules

1. **MCP-first** — Prefer `mcp_fetch_get_markdown` over `web_extract`.
2. **Multi-backend fallback** — Try all backends before declaring a URL failed.
3. **Never fabricate** — Every finding must trace to a real search or extraction.
4. **Preserve content** — Extract as-is; never summarize or truncate.
5. **Verify before saving** — Confirm extracted content is non-empty (>100 chars).

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
