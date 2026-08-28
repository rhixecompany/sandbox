---
name: seed-review-and-create
title: Seed System Review and Create
description: Reviews existing TypeScript seed scripts, fixes issues with image linking and fallback handling, updates documentation, and creates new seeders for the codebase.
version: 1.0.0
author: Hermes Agent
tags:
- tool
- automation
- backend
- typescript
- seeding
- documentation
- refactor
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
# Table of Contents

- [Goal](#goal)
- [Context Files (Read First)](#context-files-read-first)
- [Architecture](#architecture)
- [Tasks](#tasks)
  - [1. Review Existing Seeders](#1-review-existing-seeders)
- [Quality Gate](#quality-gate)
- [Reference](#reference)
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
- [Related Prompts](#related-prompts)


## Table of Contents

- [Goal](#goal)
- [Context Files (Read First)](#context-files-read-first)
- [Architecture](#architecture)
- [Tasks](#tasks)
- [1. Review Existing Seeders](#1-review-existing-seeders)
- [Quality Gate](#quality-gate)
- [Reference](#reference)
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
- [Related Prompts](#related-prompts)




## Goal

Review seed system files, create new seeders, fix issues, and implement improvements.

## Seed System Review & EnhancementAs **Reviewer persona**, research the codebase for additional context and dependencies, research the seeding system and identify how images are being managed and linked to their respective entities. Update seeding system images management to ensure proper linking, set a default callback image for all failed entities to the default image or the placeholder image or the image url, update documentation, and seeders accordingly.As **Reviewer persona**, review all `src/scripts/seed/**/*.ts` files. Understand the architecture, identify issues, and implement improvements.

## Context Files (Read First)

1. `src/database/schema.ts` — All table definitions, relations, and enums2. `src/scripts/seed/types.ts` — Core types: `SeedConfig`, `SeedOptions`, `LookupCache`, `EntityResult`, `SeedReport`3. `src/scripts/seed/seeders/base-seed.ts` — Abstract `BaseSeeder<T

> ` template method pattern4. `src/scripts/seed/seed-orchestrator.ts` — Entity ordering, cache management, seeder dispatch5. `src/scripts/seed/index.ts` — Central exports6. `src/schemas/seed/` — Zod validation schemas for each entity

## Architecture

The seed system uses the **Template Method Pattern**:

```
BaseSeeder<T>.seed() → loadData() → validateData() → processBatches() → insertBatch()
```

- **Abstract methods** each seeder must implement: `getDataSources()`, `getUniqueField()`, `transformData()`, `insertBatch()`
- **LookupCache** is shared across all seeders for deduplication (entity name → ID maps)
- **SeedOrchestrator** manages dependency order and coordinates seeding
- **Entity order**: users → types → authors → artists → genres → comics → comic-images → chapters → chapter-images

## Tasks

### 1. Review Existing Seeders

>
> Review all files in `src/scripts/seed/seeders/` for:
> **Full content:**

## Quality Gate

After all changes, run:```bashpnpm type-check # Must be 0 TypeScript errorspnpm lint:strict # Must be 0 Lint errors```

## Reference

- **Password hashing**: `bcryptjs` with 10 salt rounds (project standard)- **DB driver**: Drizzle ORM with `db.query.*` and `db.insert()` patterns- **Schema location**: `src/database/schema.ts` (27 tables, 4 enums)- **Zod schemas**: `src/schemas/seed/*.seed.ts`

## Template References

Templates in `templates/seed-review-and-create/`:- `tasks.md`

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

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State when something fails.

## Phases

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

## Related Prompts

Same-family prompts:

- [`code-review.prompt.md`](code-review.prompt.md)