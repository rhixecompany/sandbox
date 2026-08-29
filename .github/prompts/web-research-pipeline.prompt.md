---
name: web-research-pipeline
title: Web Research Pipeline
description: Run a web search → extract full content → save as formatted markdown pipeline using a Tavily-first approach with fetch MCP fallback for robust research capture.
trigger: /web-research-pipeline
version: 1.0.0
author: Hermes Agent
tags:
  - research
  - web
  - tavily
  - pipeline
  - automation
  - search
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---
## Table of Contents

## Goal

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Workflow](#workflow)
- [Rules](#rules)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Workflow](#workflow)
- [Rules](#rules)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`repo-research-pipeline.prompt.md`](repo-research-pipeline.prompt.md)