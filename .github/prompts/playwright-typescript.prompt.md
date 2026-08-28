---
name: playwright-typescript
title: Playwright TypeScript Test Authoring
description: Designs scenarios, implements stable @playwright/test suites with role/label-based locators and web-first assertions, then runs and stabilizes them.
version: 1.0.0
author: Hermes Agent
tags:
  - playwright
  - typescript
  - testing
  - tdd
  - qa
  - frontend
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
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Scenario and Test Design](#phase-1:-scenario-and-test-design)
- [Phase 2: Test Implementation](#phase-2:-test-implementation)
- [Steps](#steps)
- [Tasks](#tasks)
- [Subtasks](#subtasks)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Author and refine Playwright TypeScript tests with role/label-based locators and web-first assertions.

## Description

Author and refine Playwright TypeScript tests that are resilient, readable, and aligned with accessibility-first locator and assertion practices.


Use when creating or updating Playwright TypeScript tests with accessibility-first locators and web-first assertions.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Playwright test design and isolation
- Accessibility-first locator strategy
- Deterministic assertion and flake reduction

## Subagents

| Subagent | Role | When to Use || --

- | --- | --- || Test Author | Writes structured Playwright tests | Always || Locator Auditor | Ensures strong user-facing locator choices | Locator-heavy tests || Stability Checker | Identifies flake and timing anti-patterns | Failing or intermittent tests |

## Personas

- Test Author: Writes behavior-focused tests with clear steps.
- Locator Auditor: Prefers role and label-based locators over brittle selectors.
- Stability Checker: Eliminates fixed waits and unstable timing assumptions.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Use @playwright/test with clear test.describe and test.step grouping.
- Prefer getByRole, getByLabel, and user-visible locators.
- Use web-first auto-retrying assertions and avoid hard-coded waits.
- Keep tests feature-focused and stored under tests/ with clear names.
- Verify navigation with URL assertions and structure with accessibility snapshots when applicable.


### Phase 1: Scenario and Test Design

### Phase 2: Test Implementation

## Steps

1. Define scenario and expected outcomes.
2. Choose strong, accessible locators.
3. Implement tests with explicit action/assertion steps.
4. Run tests and inspect failures.
5. Iterate to stable green execution.

## Tasks

- Task 1.1 — Convert scenario requirements into explicit user-facing test outcomes.
- Task 1.2 — Implement tests with role/label/text-based locators.
- Task 1.3 — Add meaningful web-first assertions for content and navigation.
- Task 1.4 — Execute and fix instability without hard waits.
- Task 1.5 — Confirm stable pass and summarize coverage.

## Subtasks

- Subtask 1.1.1 — Capture setup and prerequisite state assumptions.
- Subtask 1.2.1 — Replace brittle CSS/XPath selectors when possible.
- Subtask 1.3.1 — Use toHaveText, toContainText, toHaveURL, and toHaveCount appropriately.
- Subtask 1.4.1 — Resolve strict-mode violations and flaky transitions.
- Subtask 1.5.1 — Document remaining gaps or deferred scenarios.

## Actions Summary

1. Design behavior-driven scenarios.
2. Implement strong Playwright tests.
3. Run and stabilize.
4. Deliver passing tests with clear intent.

## Template References

Templates in `templates/playwright-typescript/`:- `phases.md`

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`playwright-automation-fill-in-form.prompt.md`](playwright-automation-fill-in-form.prompt.md)
- [`playwright-explore-website.prompt.md`](playwright-explore-website.prompt.md)
- [`playwright-generate-test.prompt.md`](playwright-generate-test.prompt.md)