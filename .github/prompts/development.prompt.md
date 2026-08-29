---
name: development
title: Comprehensive Setup Guide
description: Comprehensive development setup guide — prerequisites and end-to-end project bootstrap (e.g. ComicWise-style full-stack projects).
trigger: /development
version: 1.0.0
author: Hermes Agent
tags:
- development
- setup
- bootstrap
- tutorial
- beginner
- full-stack
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
toolsets:
  - file
  - terminal
skills:
  - skill:using-superpowers
dependencies: []
formatter: markdown
license: MIT
---
## Table of Contents

## Goal

## Context

## Phases



# Table of Contents

- [Goal](#goal)
- [Comprehensive setup guide for ComicWise](#comprehensive-setup-guide-for-comicwise)
- [Prerequisites](#prerequisites)
- [**Comprehensive setup guide for ComicWise](#**comprehensive-setup-guide-for-comicwise)
- [Tasks](#tasks)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)



- [Goal](#goal)
- [Comprehensive setup guide for ComicWise](#comprehensive-setup-guide-for-comicwise)
- [Prerequisites](#prerequisites)
- [**Comprehensive setup guide for ComicWise](#**comprehensive-setup-guide-for-comicwise)
- [Tasks](#tasks)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)





🚀 ComicWise - Complete Project Setup & Scaffolding Guide.

## Comprehensive setup guide for ComicWise

- a modern web comic platform built with Next.js 16, PostgreSQL, Redis, and AI-powered features

> Personality: Expert Software Engineer, DevOps Specialist, Technical Writer
> Project: ComicWise - Web Comic Platform
> **Full content:** `templates/development/comprehensive_setup_guide_for_.md`

## Prerequisites

1. Node.js 20+2. pnpm 9+
2. PostgreSQL 16+
3. Redis 7+ (optional)

## **Comprehensive setup guide for ComicWise

- a modern web comic platform built with Next.js 16, PostgreSQL, Redis, and AI-powered features.**Read And understand the following files before proceeding with the tasks and also to get context on how the project is structured and works:- `**/*.ts` ,- `**/*.tsx`,- `**/*.mjs`,- `**/*.json`,- `**/*.mts`,- `**/*.json`,- `**/*.md`,- `**/*.txt`,- `**/*.yml`,- `**/*.ps1`,- `**/*.sh`,- `**/*/Dockerfile`,- `src/**`,- `scripts/**`Complete all Tasks

## Tasks

> 1 - Setup the project by installing all dependencies using pnpm, setting up the
> 2 - Create, Optimize and Validate if exists copy file to end with .backup and Cr
> **Full content:** `templates/development/tasks.md`

## Template References

Detailed templates in `templates/development/`:- `comprehensive_setup_guide_for_.md`- `tasks.md`- `tasks_.md`

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


Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State when something fails.


### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings .
- Stop once the requested result is delivered.

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section