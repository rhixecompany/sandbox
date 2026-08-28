---
name: repo-research-pipeline
title: Repo Research Pipeline
description: Run research across all project repos and produce RESEARCH_REPORT.md files with verified sources using the Tavily-first research pipeline and symmetric cross-references.
version: 1.0.0
author: Hermes Agent
tags: [research, web-search, tavily, report, pipeline, automation]
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
date: '2026-08-25'
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
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Tasks](#tasks)
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
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Tasks](#tasks)
- [Related Prompts](#related-prompts)





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

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. **NO FABRICATION** — Every finding must trace to real search or extraction.
2. **VERIFY BEFORE CLAIMING** — Never report without running the command.
3. **SIZE GATE** — Reports 1KB–5KB. Trim over 5KB, expand under 1KB.
4. **SYMMETRIC CROSS-REFS** — If project A references B, B must reference A.
5. **TAVILY-FIRST** — `mcp__tavily__tavily_search` → `mcp__tavily__tavily_extract` → `mcp__fetch__get_markdown` → firecrawl_scrape → `web_extract`.
6. **MULTI-BACKEND** — Try all backends before declaring a URL failed.

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------------- | -------------------------------------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes


Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| - | ---------- | ----------------------------------- |
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
| -------------------------------- | ----------------------------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| Server | Purpose |
| --------------------- | ------------------------------------------------------ |
| `tavily` | Web search + URL extraction (primary research backend) |
| `fetch` | Web page content extraction fallback |
| `filesystem` | File read/write operations |
| `github` | GitHub API operations |
| `memory` | Persistent memory operations |
| `playwright` | Browser automation for interactive pages |
| `sequential-thinking` | Structured reasoning for complex problems |
| `ast-grep` | AST-based code search and replace |

## Hooks

The following workspace hooks run around this prompt's execution (see `.github/hooks/README.md`):

| Hook | When | Behavior |
| ------------------------ | ----------------- | ---------------------------- |
| `session-logger` | session start/end | Logs session metadata |
| `governance-audit` | session events | Audits governance compliance |
| `session-auto-commit` | session end | Auto-commits session state |
| `pre-exec-validate.sh` | before commands | Validates command execution |
| `post-exec-state-log.py` | after commands | Appends state log |

## Scripts

- `.github/prompts/.enhance/analyze_prompts.py` — Prompt-library analyzer (audit/verify)
- `.github/hooks/*` — Hook implementations listed in the Hooks section

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Related Prompts

Same-family prompts:

- [`repo-init.prompt.md`](repo-init.prompt.md)
- [`repo-management.prompt.md`](repo-management.prompt.md)
- [`repo-story-time.prompt.md`](repo-story-time.prompt.md)
- [`repo-tooling-implementation.prompt.md`](repo-tooling-implementation.prompt.md)
- [`repo.prompt.md`](repo.prompt.md)