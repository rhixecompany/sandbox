---
author: Alexa
description: Catalog of 34 researched MCP servers with source URLs, features, and
  configuration status. Use when evaluating new MCP servers or checking what's available.
license: MIT
name: mcp-server-catalog
tags:
- mcp
- servers
- reference
- catalog
title: MCP Server Catalog
version: 1.0.0

---

# MCP Server Catalog

## Overview
Catalog of 34 MCP servers researched and documented in `docs/mcp-research/`. Each entry includes source URL, key features, and whether it's currently configured.

### Phase 1: Preparation
- Review prerequisites and setup requirements
- Gather necessary tools and dependencies

### Phase 2: Execution
- Follow the step-by-step workflow
- Handle errors and edge cases as they arise

### Phase 3: Verification
- Confirm the output meets requirements
- Run verification checks before completing

## Configured Servers (13)
These are active in `config.yaml`:

| Server | Transport | Purpose | Config Source |
|--------|-----------|---------|---------------|
| ast-grep | stdio | AST code search | `@ast-grep/ast-grep-mcp` |
| code-sandbox | stdio | Node.js sandbox | `node-code-sandbox-mcp` |
| codex | stdio | Codex CLI | `codex mcp-server` |
| copilot-mcp | stdio | GitHub Copilot | Internal Python server |
| fetch | stdio | Web content | `mcp-server-fetch` |
| filesystem | stdio | File access | `@modelcontextprotocol/server-filesystem` |
| github | stdio | GitHub API | `@modelcontextprotocol/server-github` |
| linear | http | Linear issues | `https://mcp.linear.app/mcp` |
| mcp-docker | stdio | Docker | Docker MCP gateway |
| memory | stdio | Persistent memory | `@modelcontextprotocol/server-memory` |
| mindstudio | stdio | MindStudio | `mindstudio mcp` |
| playwright | stdio | Browser | `@playwright/mcp` |
| sequential-thinking | stdio | Reasoning | `@modelcontextprotocol/server-sequential-thinking` |

## Researched Servers Not Configured
Candidates for future setup:

| Server | Source | Language | Purpose |
|--------|--------|----------|---------|
| AWS API Gateway MCP | awslabs/mcp | Python | AWS CLI via natural language |
| Cloud Run MCP | GoogleCloudPlatform | N/A | GCP Cloud Run management |
| Context7 MCP | context7 | N/A | Library documentation |
| Desktop Commander MCP | N/A | N/A | File/terminal/exec |
| Django MCP | N/A | N/A | Django management |
| Gemini API Docs MCP | N/A | N/A | Google AI docs |
| GitMCP | N/A | N/A | Git operations |
| Google Flights MCP | N/A | N/A | Flight search |
| Google Maps MCP | N/A | N/A | Maps/geocoding |
| Hacker News MCP | N/A | N/A | Hacker News API |
| Hostinger API MCP | N/A | N/A | Hosting management |
| Markdownify MCP | N/A | N/A | HTML→Markdown |
| MarkItDown MCP | N/A | N/A | File→Markdown |
| Node Code Sandbox MCP | N/A | N/A | JS sandbox (code-sandbox configured differently) |
| NPM Sentinel MCP | N/A | N/A | NPM security audit |
| Postman MCP | N/A | N/A | API testing |
| Python Refactoring MCP | N/A | Python | Python refactoring |
| Redis MCP | N/A | N/A | Redis operations |
| ScrapeGraph MCP | N/A | N/A | Web scraping |
| Sentry MCP | N/A | N/A | Error monitoring |
| SQLite MCP | N/A | N/A | SQLite database |
| Stripe MCP | N/A | N/A | Payment processing |
| Time MCP | N/A | N/A | Time/timezone |
| uv MCP | N/A | N/A | Python packaging |
| Vitest MCP | N/A | N/A | Test runner |
| YouTube Transcript MCP | N/A | N/A | YouTube captions |

## See Also
- Full extracted research: `.hermes/plans/extracted-content/mcp-research-extracted.md` (42K, 1172 lines)
- MCP config: `config.yaml` → `mcp_servers:` section
- MCP servers index: `docs/mcp-servers/index.md`

## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch

## Verification Checklist

- [ ] Skill has clear purpose and structured workflow
- [ ] Frontmatter is complete and valid
- [ ] All reference files exist and are substantive
- [ ] No placeholder text
