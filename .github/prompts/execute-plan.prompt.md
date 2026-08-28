---
name: execute-plan
title: Execute Plan
description: Executes a specified implementation plan from `.hermes/plans/`, taking the plan filename as a parameter.
version: 1.0.0
author: Hermes Agent
date: '2026-08-25'
tags:
  - planning
  - execution
  - hermes
  - automation
  - implementation
metadata:
  hermes:
    profile: code-architect
    priority: high
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---

# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Load Plan](#phase-1:-load-plan)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Report](#phase-4:-report)
- [Verification Checklist](#verification-checklist)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)


## Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Load Plan](#phase-1:-load-plan)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Report](#phase-4:-report)
- [Verification Checklist](#verification-checklist)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)




## Goal

Execute the specified plan from `.hermes/plans/`.**Parameter** — set `plan` to the plan filename (e.g., `acpx-agents-feature-specs.md`).

## Context

Loads a target plan document and follows its phases, steps, and requirementssequentially. Use when a written plan already exists and needs driven to completion.

## Inputs

- `plan` — plan filename under `.hermes/plans/` (required).

## Outputs

- Plan phases executed in order.
- Completion report with key outcomes.
- Blockers surfaced honestly if encountered.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow the plan literally — do not skip or reorder.
- Verify each phase's output before advancing.
- If a phase references a file that does not exist, stop and report the gap.
- Keep the response structured, deterministic, and easy to act on.

## Phases

### Phase 1: Load Plan

1. Read `.hermes/plans/{plan}`.
2. Parse the plan's phases, rules, and verification steps.
3. Report the plan title and total number of phases.

### Phase 2: Execute

1. Walk through each phase in order.
2. Perform the requested work with the smallest safe change set.
3. Keep the steps explicit and reproducible.

### Phase 3: Verify

1. Run each verification step listed in the plan.
2. Confirm outputs match the plan's acceptance criteria.

### Phase 4: Report

Summarise what was done, what was verified, and any deviations from the plan.

## Verification Checklist

- [ ] `plan` parameter is provided and points to an existing file under `.hermes/plans/`.
- [ ] Plan loaded and understood before execution.
- [ ] Every phase completed before advancing to the next.
- [ ] Blockers reported honestly (never fabricated).
- [ ] Final report includes verification results.

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

- [`execute-all-prompts.prompt.md`](execute-all-prompts.prompt.md)