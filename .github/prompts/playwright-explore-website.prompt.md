---
name: playwright-explore-website
title: Playwright Website Exploration
description: Explores a website with Playwright MCP, documents core flows, locators, and outcomes, then proposes test cases from the findings.
version: 1.0.0
author: Hermes Agent
tags:
  - playwright
  - browser-automation
  - testing
  - webapp
  - exploration
  - qa
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
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [Description](#description)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
  - [@explorer](#@explorer)
  - [@scribeA recorder who writes down locators, outcomes, and noteworthy UI behavior.](#@scribea-recorder-who-writes-down-locators-outcomes-and-noteworthy-ui-behavior)
  - [@tester](#@tester)
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


## Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand off](#phase-4:-hand-off)
- [Description](#description)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [@explorer](#@explorer)
- [@scribeA recorder who writes down locators, outcomes, and noteworthy UI behavior.](#@scribea-recorder-who-writes-down-locators-outcomes-and-noteworthy-ui-behavior)
- [@tester](#@tester)
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




## Goal

Explore a website with Playwright MCP, document core flows, and propose tests from the findings.

## Context

Use when you need to playwright website exploration for the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake

- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute

- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify

- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off

- Return the final artifact or findings .
- Stop once the requested result is delivered.

## Description

Explore a website with Playwright MCP, document core flows, and propose tests from the findings.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- `webapp-testing` — navigate and exercise the live site with browser automation
- `verification-before-completion` — confirm the exploration evidence before summarizing
- `systematic-debugging` — trace UI behavior and interaction issues cleanly

## Subagents

| Subagent | Role | Phase || --

- | --- | --- || `@explorer` | Navigates and exercises the site | Phase 2 || `@scribe` | Records locators, flows, and outcomes | Phase 3 || `@tester` | Turns exploration findings into test ideas | Phase 4 |

## Personas

### @explorer

A careful site explorer who finds the main flows without over-driving the app.

### @scribeA recorder who writes down locators, outcomes, and noteworthy UI behavior.

### @tester

A test-minded reviewer who turns exploration notes into concrete test cases.

## Steps

- Open the URL.
- Explore 3 to 5 core flows.
- Document locators and outcomes.
- Propose tests and close the browser.

## Tasks

- Confirm the URL.
- Exercise the main user journeys.
- Record evidence.
- Summarize and suggest tests.

## Subtasks

- Ask for a URL if missing.
- Capture locators for key controls.
- Note observed outcomes.
- Close the browser context.

## Actions Summary

1. Navigate to the site.
2. Interact with the core flows.
3. Document locators and outcomes.
4. Generate test ideas.```

## Template References

Templates in `templates/playwright-explore-website/`:- `phases.md`

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
- [`playwright-generate-test.prompt.md`](playwright-generate-test.prompt.md)
- [`playwright-typescript.prompt.md`](playwright-typescript.prompt.md)