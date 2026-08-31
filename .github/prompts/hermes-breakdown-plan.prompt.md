---
name: hermes-breakdown-plan
title: Hermes Breakdown — Project Plan
description: Generates an execution-ready project plan that consolidates feature and epic inputs into a planning package.
trigger: /hermes-breakdown-plan
version: 1.0.0
author: Hermes Agent
date: 2026-08-25
tags: 
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Generates an execution-ready project plan that consolidates feature and epic inputs into a planning package.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Parse the source artifacts](#phase-1:-parse-the-source-artifacts)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
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
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Parse the source artifacts](#phase-1:-parse-the-source-artifacts)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
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





Generate a project plan that turns feature and epic inputs into an execution-ready planning package.


- Use when the user needs a Project Plan plus issue-creation support.
- Prefer concise, actionable language.
- Keep the plan aligned with the provided PRD, technical breakdown, implementation plan, and test strategy.
- Do not invent scope that is not supported by the source artifacts.

## Inputs

- Epic PRD path: `/docs/ways-of-work/plan/{epic-name}/epic.md`
- Feature PRD path: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`
- Optional: `technical-breakdown.md`, `implementation-plan.md`, `test-strategy.md`

## Outputs

- Project Plan markdown at `/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`
- Issue Creation Checklist at `/docs/ways-of-work/plan/{epic-name}/{feature-name}/issues-checklist.md`
- GitHub issue templates for Epic, Feature, Story, Enabler, and Test work items
- A minimal GitHub Actions snippet for issue creation

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. Use the provided artifacts as the only source of scope.
2. Keep outputs concise and directly usable.
3. Use Mermaid diagrams for hierarchy and dependency views.
4. Include practical issue templates, not generic prose.
5. Create backup copies before overwriting existing outputs.
6. Split large outputs into companion files if a single file would exceed the size limit.


### Phase 1: Parse the source artifacts

> **Goal:** identify the epic, feature, and supporting planning inputs.

## Actions Summary

1. Read the source planning artifacts.
2. Derive the project scope and hierarchy.
3. Write the project plan and issue checklist.
4. Add the minimal automation snippet.
5. Verify the outputs and backup state.

## Template References

Templates in `templates/hermes-breakdown-plan/`:- `phases.md`

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

## Workflow

<content>

Same-family prompts:

- [`hermes-breakdown-epic-arch.prompt.md`](hermes-breakdown-epic-arch.prompt.md)
- [`hermes-breakdown-epic-pm.prompt.md`](hermes-breakdown-epic-pm.prompt.md)
- [`hermes-breakdown-feature-implementation.prompt.md`](hermes-breakdown-feature-implementation.prompt.md)
- [`hermes-breakdown-feature-prd.prompt.md`](hermes-breakdown-feature-prd.prompt.md)
- [`hermes-breakdown-test.prompt.md`](hermes-breakdown-test.prompt.md)
- [`hermes-comprehensive-setup.prompt.md`](hermes-comprehensive-setup.prompt.md)
- [`hermes-doctor-systematic-debugging.prompt.md`](hermes-doctor-systematic-debugging.prompt.md)
```
# Prompt template
Execute the workflow defined in this file.
```
