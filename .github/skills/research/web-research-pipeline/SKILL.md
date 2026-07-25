---
author: Alexa
description: 'Web search -> extract links -> scrape full content -> save as formatted markdown. MCP-first. Triggers: research, gather info, web scraping, content collection.'
license: MIT
name: web-research-pipeline
tags:
- research
- web
- scraping
- content
- markdown
- mcp
title: Web Research Pipeline (MCP-Enhanced)
version: 2.0.0
---

# Web Research Pipeline (MCP-Enhanced)

Search the web, extract full content from discovered pages, and save crisply formatted markdown files — one per source — using MCP tools first. Integrates multiple extraction backends for maximum coverage.

## When to Use

- Researching a topic from multiple web sources
- Building a knowledge base / reference collection
- Gathering documentation / tutorial content
- Competitive/market research from published content
- Any task that needs "search the web and save everything"

## When NOT to Use

- Single-page extraction (use web_extract or mcp_fetch_get_markdown directly)
- Real-time/live data (use web_search directly)
- Internal/private URLs (use browser tool or mcp_playwright)

## Skills Required

| Skill | Purpose |
|-------|---------|
| mcp-fetch | Primary URL content extraction (MCP-first) |
| mcp-filesystem | File/directory operations (MCP-first) |
| mcp-playwright | JS-heavy page rendering fallback |
| firecrawl-scrape | JS-rendered page extraction |
| firecrawl-search | Web search with full content |
| firecrawl-crawl | Bulk site extraction |
| domain-intel | Passive domain recon enrichment |
| dispatching-parallel-agents | Dispatch 3-4 projects concurrently via subagents |

## MCP Tool Precedence

| Task | MCP First | Fallback |
|------|-----------|----------|
| Fetch URL | mcp_fetch_get_markdown | firecrawl_scrape |
| Search | firecrawl_search | web_search |
| File ops | mcp_filesystem_* | terminal/write_file |
| JS-rendered | mcp_playwright | firecrawl_scrape |
| Bulk crawl | firecrawl_crawl | scrapling |
| Domain recon | domain_intel | — |

## Workflow

### Phase 1: Preflight
Verify MCP servers are healthy. If down, fall back to built-in equivalents.

### Phase 2: Search
Preference: firecrawl_search (full content) > web_search (built-in). Default limit=10.

### Phase 3: Extract Content
Backend chain: mcp_fetch_get_markdown > firecrawl_scrape > web_extract > scrapling > mcp_playwright. Try each on failure before skipping the URL.

### Phase 4: Save as Markdown
Format: Title header, metadata block (source, timestamp, backend), content, footer.

### Phase 5: Enrich (Optional)
Layer domain_intel or osint_investigation for deeper research.

### Phase 6: Report Summary
Source/saved/failed counts, backends used, output directory.

## Automated Execution

For a fully automated pipeline, use scripts/pipeline-execute.py:
python3 SKILL_DIR/scripts/pipeline-execute.py

This handles search to extraction to save to summary in one pass.

## Reference Files

- references/pipeline-architecture.md — Search strategies and pipeline patterns
- references/multi-query-pattern.md — Pattern for multi-query research from structured query docs
- references/comprehensive-tech-stack-research.md — Worked example of per-technology deep-dive format (used for rhixe_scans: Next.js 15 + Prisma 6 + PostgreSQL + Stripe + PayPal + Docker + Tailwind)
- references/profile-project-research-2026.md — Detailed findings for profile project (Django 4.x, GCS, CKEditor 5, Docker, GCP)
- references/python-security-pyscg-2026.md — OpenSSF Secure Coding Guide for Python (50+ rules, May 2026)
- references/synthesize-to-report.md — Workflow: synthesize web-research-*.md + local project docs into a standardized RESEARCH_REPORT.md (from Bash project experience)
- templates/research-report.md — Structured research report template (two variants: minimal thematic for single-topic, comprehensive per-tech for multi-stack projects)
- scripts/pipeline-execute.py — Full automated pipeline script

## Pitfalls

- **Output format choice:** For single-topic research, use the minimal thematic template (sections by theme). For multi-technology stack research (4+ technologies), use the comprehensive per-tech format (one subsection per technology, each with Best Practices / Pitfalls / Performance / Security) — see `references/comprehensive-tech-stack-research.md` for a worked example.
- Backend fallback chain: always try each backend before giving up on a URL
- JS-rendered pages need firecrawl_scrape or mcp_playwright
- Rate limiting: spread requests 1-2s apart
- Duplicate titles get slug-dedup suffix
- Empty content under 200 chars likely means paywall or login wall
- Keep slugs under 80 chars for Windows path safety
- firecrawl requires FIRECRAWL_API_KEY in .env
- **Tech-stack research tip:** When researching a specific stack, run 7+ searches — include queries for adjacent tools (package manager, linter, test framework, security scanner) not just the core language. This uncovers integrated workflows and full-toolchain recommendations that single-topic searches miss.

## Verification Checklist

- [ ] mcp-fetch, mcp-filesystem servers enabled and tested
- [ ] Backend fallback chain working through all tiers
- [ ] slugify handles special chars, collisions, max length
- [ ] Summary report includes backend column
- [ ] Pipeline script exercises all extraction backends
