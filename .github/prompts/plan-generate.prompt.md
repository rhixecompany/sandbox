---
name: plan-generate
title: Generate Implementation Plan
description: 'Generate a detailed, structured implementation plan from a goal or specification. Produces a phased plan with dependencies, references, and verification gates. Replaces ad-hoc plan-* prompts (debugger, features-seed, updateAiAgentSetupPrompt, etc.) with a single reusable generator.'
version: 1.0.0
license: MIT
author: Hermes Agent (consolidated)
toolsets:
  - file
  - terminal
scripts: []
skills:
  - plans-and-specs
  - writing-plans
  - simplify
  - brainstorming
  - systematic-debugging
  - verification-before-completion
formatter: default
plan: 'None'
dependencies:
  - "skill:plans-and-specs"
  - "skill:writing-plans"
  - "skill:simplify"
  - "skill:brainstorming"
  - "skill:systematic-debugging"
  - "skill:verification-before-completion"
  - "prompt:context-map.prompt.md"
tags:
  - ai-assistant
  - generator
  - ml
  - planning
  - prompts
  - specification
  - typescript
trigger: /plan-generate
metadata:
  hermes: {}
---

## Goal

Generate a detailed, structured implementation plan from a goal or specification. Produces a phased plan with dependencies, references, and verification gates. Replaces ad-hoc plan-* prompts (debugger, features-seed, updateAiAgentSetupPrompt, etc.) with a single reusable generator.

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

## Phases

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
|| ------- | ----------- ||
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
4. **Report blockers** — State clearly when something fails.

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
|| ------- | --------- ||
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
