---
name: web-research-pipeline
title: Web Research Pipeline (Tavily-First)
description: 'Search the web, extract full content from discovered pages, and save crisply formatted markdown files — one per source. Uses Tavily MCP as primary search/extract backend.'
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
plan: None
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
  hermes: {}
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
>
> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. **Tavily-first** — Prefer `mcp__tavily__tavily_search` over other backends.
2. **Multi-backend fallback** — Try all backends before declaring a URL failed.
3. **Never fabricate** — Every finding must trace to a real search or extraction.
4. **Preserve content** — Extract as-is; never summarize or truncate.
5. **Verify before saving** — Confirm extracted content is non-empty (>100 chars).

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when researching topics or synthesizing findings. Start with broad discovery, then narrow to specific sources.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions
