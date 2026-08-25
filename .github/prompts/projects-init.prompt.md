---
title: Goal
description: Prompt for goal
date: '2026-08-25'
tags:
- prompt
version: 1.0.0
author: Hermes Agent
---
# Table of Contents

- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Triage Documentation](#phase-1:-triage-documentation)
- [Phase 2: Migrate Prompts](#phase-2:-migrate-prompts)
- [Phase 3: Create Skills & Update](#phase-3:-create-skills-&-update)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)


## Table of Contents

- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Triage Documentation](#phase-1:-triage-documentation)
- [Phase 2: Migrate Prompts](#phase-2:-migrate-prompts)
- [Phase 3: Create Skills & Update](#phase-3:-create-skills-&-update)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)




## Goal

Three-phase workspace initialization: triage MD documentation files, migrate prompt files to prompts/, then create skills/scripts and update prompts. Eliminates duplicates and consolidates documentation.

## Projects Init> Initialize a workspace: triage docs, migrate prompts, create skills. Three sequential phases — each must finish before the next begins.

## Description

This prompt initialises a new or stale workspace by running a three-phase cleanup and consolidation pipeline. Phase 1 discovers and deduplicates all markdown documentation files. Phase 2 discovers prompt files, migrates them to `.github/prompts/`, and consolidates. Phase 3 indexes the new prompt directory, creates any needed skills and helper scripts, and updates all prompts to reference the skills they need.**Critical rules (must appear within the first 15% of execution):**- **Only then constraint** — Each phase completes fully before the next begins. No overlapping phases.

- **Delete only after verification** — Before deleting any file, confirm the canonical copy exists in the target location.
- **Count before and after** — Record file counts at each phase start and end; report deltas.

## Context

- **Source reference:** `projects-init.prompt.txt` (raw specification)
- **Target scope:** `pwd` (workspace root), `docs/`, `.github/prompts/`
- **Phase 1 outputs:** Consolidated markdown documentation inventory + deleted duplicates
- **Phase 2 outputs:** Prompt files migrated to `.github/prompts/` + deleted originals
- **Phase 3 outputs:** New skills/scripts in `~/AppData/Local/hermes/skills/` + updated prompt frontmatter
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill | Purpose |
| ------------------ | ------------------------------------------------------- |
| `enhance-markdown` | Audit, enhance, convert, and consolidate markdown files |
| `hermes-skills` | List, create, install, and manage skills |
| `skill-creator` | Scaffold new skills with validated frontmatter |

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. **Strict sequential execution** — Phase 1 → Phase 2 → Phase 3. Each phase must complete (including verification) before the next starts.
2. **Verify before delete** — Always confirm the canonical copy exists at the target path before removing a source file.
3. **Count and report** — Log file counts before and after each phase. Report deltas in the phase summary.
4. **No destructive operations without confirmation** — For `rm` operations over 3+ files, show the list and ask before executing.

## Phases

## Phase 1: Triage Documentation

> **Goal:** Inventory all markdown documentation files, identify duplicates, conso
> **Inputs:** `pwd`, `docs/**` (and subdirectories)
> **Full content:**

## Phase 2: Migrate Prompts

> **Goal:** Discover all markdown prompt files, migrate them to `.github/prompts/`
> **Inputs:** `pwd`, `.github/prompts/` (if exists)
> **Full content:**

## Phase 3: Create Skills & Update

> **Goal:** Scan `.github/prompts/`, identify needed skills and scripts, create th
> **Inputs:** `.github/prompts/**`
> **Full content:**

## Actions Summary

1. List and triage all markdown documentation files in `pwd` and `docs/**`; consolidate and delete duplicates
2. List and triage all markdown prompt files in `pwd` and `.github/prompts/`; migrate prompts to `.github/prompts/`; consolidate; delete originals
3. List and triage the migrated `.github/prompts/` collection; create all needed skills and scripts; update all prompts with accurate skill references

## Template References

Detailed templates in `templates/projects-init/`:

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

- [`dev-init.prompt.md`](dev-init.prompt.md)
- [`repo-init.prompt.md`](repo-init.prompt.md)