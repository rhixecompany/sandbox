---
name: plan-generate
title: Plan Generate
description: Generates a structured implementation plan (inputs, outputs, phases with verification gates) at .github/prompts/<name>.prompt.md or .hermes/plans/<name>.md.
trigger: /plan-generate
version: 1.0.0
author: Hermes Agent
tags:
  - planning
  - documentation
  - spec
  - workflow
  - writing
  - meta
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


- [Goal](#goal)
- [Core Rules](#core-rules)
- [Workflow](#workflow)
- [Phase 1: Context gathering](#phase-1:-context-gathering)
- [Phase 2: Plan structure](#phase-2:-plan-structure)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Phases](#phases)
- [Phase N: <Name](#phase-n:-<name)
- [Verification Checklist](#verification-checklist)
- [Phase 3: Write](#phase-3:-write)
- [Phase 4: Verify](#phase-4:-verify)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Best Practices](#best-practices)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Generate a structured implementation plan from a goal or specification. The plan includes phased execution, dependencies, and verification gates.

> **Shared template references:**>> - [Frontmatter patterns](templates/_shared/frontmatter.md)> - [Core rules](templates/_shared/rules-core.md)> - [Section skeleton](templates/_shared/section-skeleton.md)> - [Verification checklist](templates/_shared/verification-checklist.md)

## Core Rules

See [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md).Additional plan-specific rules:1. **Phases must be sequential** — Each phase must complete before the next begins.2. **Each phase has a verification gate** — Explicit checks that phase is done.3. **Dependencies are explicit** — Every skill, prompt, and tool referenced must exist.4. **DRY output** — Generated plans reference shared templates where possible.5. **One plan = one goal** — Never combine unrelated goals into a single plan.

## Workflow

### Phase 1: Context gathering

1. Read the user's goal/specification.
2. Run `context-map` (prompt) to identify impacted files, dependencies, and scope.
3. Use `brainstorming` to explore approach options.
4. Use `systematic-debugging` to identify edge cases and risks.

### Phase 2: Plan structure

Generate a plan with these sections:```markdown

## Inputs

- Files, APIs, data sources the plan consumes

## Outputs

- Files, reports, artifacts the plan produces


### Phase N: <Name

> **Gate:** <condition that confirms completion>**Dependencies:** <prior phases or external deps>**Steps:**1. <action>2. <action>3. Verify: <validation step>

## Verification Checklist

- [ ] All phases completed
- [ ] All outputs verified
- [ ] No orphaned references```

### Phase 3: Write

1. Create the plan file at `.github/prompts/<name>.prompt.md` or `.hermes/plans/<name>.md`.
2. Use `writing-plans` skill for structured plan writing.
3. Apply `simplify` to remove redundancy.

### Phase 4: Verify

1. Run the verification checklist below.
2. Confirm all referenced skills/prompts/tools exist.
3. If the plan targets `.github/prompts/*.prompt.md`, validate frontmatter.
4. Run the plan through `dry_run_prompts.py` for smoke-testing.

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


Use when creating an implementation plan from a goal, specification, or feature request.

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

- [`plan-audit.prompt.md`](plan-audit.prompt.md)
- [`plan-batch-fix.prompt.md`](plan-batch-fix.prompt.md)
- [`plan-execute.prompt.md`](plan-execute.prompt.md)