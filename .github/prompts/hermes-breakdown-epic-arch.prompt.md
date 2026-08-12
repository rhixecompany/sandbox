---
name: hermes-breakdown-epic-arch
title: Hermes Breakdown Epic Arch
description: 'Hermes-equivalent: create a high-level Epic Architecture Specification
  from an Epic PRD.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
- file
- terminal
scripts: []
skills: []
formatter: default
plan: null
tags:
- ai-assistant
- architecture
- data
- frontend
- ml
- prompts
- specification
- typescript
- ai-assistant
- architecture
- data
- frontend
- ml
- prompts
- specification
- typescript
trigger: /hermes-breakdown-epic-arch
dependencies: []
metadata:
  hermes: {}
---

## Goal

Turn an Epic PRD into a high-level architecture specification with layers, enablers, and technology guidance.

## Context

- Use when an epic already exists and needs architecture direction.
- Keep the plan high-level and architecture-focused.
- Use Mermaid diagrams for system layering and data flow.
- Do not write implementation code.

## Inputs

- Epic PRD path: `/docs/ways-of-work/plan/{epic-name}/epic.md`
- Optional architecture notes or constraints

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/arch.md`

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. Include an architecture overview.
2. Show User, Application, Service, Data, and Infrastructure layers.
3. List features and technical enablers.
4. Recommend a technology stack with short justification.
5. Include a value assessment and t-shirt estimate.
6. Prefer labeled Mermaid subgraphs for clarity.

## Phases

### Phase 1: Analyze the epic

> **Goal:** extract the architectural implications of the epic.

## Actions Summary

1. Read the Epic PRD.
2. Draft the architecture overview and diagram.
3. Add enablers, stack guidance, and estimates.
4. Verify completeness and path correctness.

## Template References

Templates in `templates/hermes-breakdown-epic-arch/`:- `phases.md`

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

- [`hermes-breakdown-epic-pm.prompt.md`](hermes-breakdown-epic-pm.prompt.md)
- [`hermes-breakdown-feature-implementation.prompt.md`](hermes-breakdown-feature-implementation.prompt.md)
- [`hermes-breakdown-feature-prd.prompt.md`](hermes-breakdown-feature-prd.prompt.md)
- [`hermes-breakdown-plan.prompt.md`](hermes-breakdown-plan.prompt.md)
- [`hermes-breakdown-test.prompt.md`](hermes-breakdown-test.prompt.md)
- [`hermes-comprehensive-setup.prompt.md`](hermes-comprehensive-setup.prompt.md)
- [`hermes-doctor-systematic-debugging.prompt.md`](hermes-doctor-systematic-debugging.prompt.md)
