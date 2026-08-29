---
name: testing
title: Comprehensive Testing Prompt
description: Create, update, and validate unit and E2E tests that provide deterministic coverage for public behavior and critical flows such as authentication, payments, and reconciliation.
trigger: /testing
version: 1.0.0
author: Hermes Agent
tags:
  - testing
  - unit-tests
  - e2e
  - coverage
  - quality
  - automation
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


# Table of Contents

- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Coverage Planning](#phase-1:-coverage-planning)
  - [Phase 2: Test Authoring](#phase-2:-test-authoring)
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



- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Coverage Planning](#phase-1:-coverage-planning)
- [Phase 2: Test Authoring](#phase-2:-test-authoring)
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





Use when "Comprehensive testing prompt aligned to repository unit and E2E guidance." to accomplish the associated tasks and objectives.

## Description

Create, update, and validate tests that provide deterministic coverage for public behavior and critical flows such as authentication, payments, and reconciliation.


Use this prompt for tests under tests/ and for planning or reviewing validation strategy for changed behavior.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Unit and integration test design
- E2E flow verification with environment constraints
- Deterministic test isolation and mocking

## Subagents

| Subagent | Role | When to Use || --

- | --- | --- || Unit Test Author | Builds focused deterministic unit tests | Business logic changes || E2E Test Author | Builds realistic end-to-end scenarios | User flow changes || Test Reliability Reviewer | Removes flakes and env coupling | Intermittent failures |

## Personas

- Unit Test Author: Maximizes signal-to-noise with small focused tests.
- E2E Test Author: Validates critical user journeys in realistic conditions.
- Test Reliability Reviewer: Eliminates nondeterminism and fragile assumptions.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Prefer fast deterministic unit tests with mocked external dependencies.
- Cover critical paths and public behavior changes.
- Run Playwright E2E against expected local test server conditions.
- Keep test files focused and readable.
- Ensure CI-relevant commands and prerequisites are respected.


### Phase 1: Coverage Planning

### Phase 2: Test Authoring

## Steps

1. Identify changed behavior and risk-critical paths.
2. Design unit and E2E test cases for required coverage.
3. Implement deterministic tests and mocks.
4. Run tests and resolve failures or instability.
5. Summarize coverage and remaining gaps.

## Tasks

- Task 1.1 — Define coverage requirements for changed and critical behavior.
- Task 1.2 — Implement unit tests for logic and edge cases.
- Task 1.3 — Implement or update E2E tests for key user flows.
- Task 1.4 — Execute tests and stabilize failures.
- Task 1.5 — Record coverage outcomes and residual testing risk.

## Subtasks

- Subtask 1.1.1 — Map tests to public surface and risk areas.
- Subtask 1.2.1 — Mock external services and keep assertions deterministic.
- Subtask 1.3.1 — Ensure environment assumptions are explicit and reproducible.
- Subtask 1.4.1 — Eliminate brittle timing and order dependencies.
- Subtask 1.5.1 — Flag any deferred tests with rationale.

## Actions Summary

1. Plan risk-based coverage.
2. Write deterministic tests.
3. Execute and stabilize.
4. Deliver clear test confidence and gap reporting.

## Template References

Templates in `templates/testing/`:- `phases.md`

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