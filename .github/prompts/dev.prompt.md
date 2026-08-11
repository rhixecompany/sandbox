---
name: dev
title: Task1
description: The purpose of the prompt is to get my codebase optimized and refactored.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - configuration
  - debugging
  - performance
  - playwright
  - prompts
  - refactoring
  - testing
  - typescript
trigger: /dev
dependencies: []
metadata:
  hermes: {}
---

## Goal

The purpose of the prompt is to get my codebase optimized and refactored.

## Phase 1

# Task1- list all test in src/backuptests and src/tests then triage- if test already exists, merge intelligently - preserve valuable content while updating outdated sections- Delete src/backuptests and modify playwright.config.mts and vitest.config.mts for this project- modify src/actions/auth.actions.ts to include a custom signOut function- modify src/components/layout/navbar.tsx,src/components/layout/navbar-client.tsx,src/components/layout/nav-user.tsx,src/components/layout/nav-secondary.tsx,src/components/layout/nav-main.tsx,src/components/layout/nav-documents.tsx,src/components/layout/app-sidebar.tsx,src/components/layout/site-header.tsx to handle both authenticated and unauthenticated users with next-auth- list all pages in src/apps and triage- for each page in the list of pages in src/apps modify all of them to use actions in src/actions not dal in src/actions, create a corresponding vitest for all actions and a corresponding playwright test for all pages all test must be basic with valid page navigation and displaying information skip all pages that need authentication in this phase ensure all vitest and playwright test run successfully if a test fails debug by executing the individual failing test# Task2- for each page in the list of pages in src/apps that need authentication create a corresponding playwright test, test must be basic with valid page navigation and displaying information ensure all vitest and playwright test run successfully if a test fails debug by executing the individual failing test

## Template References

Templates in `templates/dev/`:- `phase_1.md`

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

- Return final artifact or findings clearly.
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
|| --- | ------ | ----------- ||
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
