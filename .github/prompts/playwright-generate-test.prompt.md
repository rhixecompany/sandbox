---
name: playwright-generate-test
title: Playwright Test Generation
description: Generates a Playwright test from a scenario, validates it against the live app, and iterates with @investigator/@author/@runner until the test passes.
trigger: /playwright-generate-test
version: 1.0.0
author: Hermes Agent
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
Generates a Playwright test from a scenario, validates it against the live app, and iterates with @investigator/@author/@runner until the test passes.

## Context

## Phases


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
- [@investigatorA scenario investigator who gathers the facts needed to write a correct test.](#@investigatora-scenario-investigator-who-gathers-the-facts-needed-to-write-a-correct-test)
- [@authorA test author who writes clean Playwright TypeScript.](#@authora-test-author-who-writes-clean-playwright-typescript)
- [@runnerA test runner who fixes issues until the test passes.](#@runnera-test-runner-who-fixes-issues-until-the-test-passes)
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





Generate a Playwright test from a scenario, validate it against the app, and iterate until it passes.


Use when generating Playwright tests from scenarios for the current workspace.

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

Generate a Playwright test from a scenario, validate it against the app, and iterate until it passes.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- `webapp-testing` — use browser automation to validate the scenario in the live app
- `test-driven-development` — translate observed behavior into a reliable test
- `systematic-debugging` — iterate on failures until the test is stable
- `verification-before-completion` — verify the test passes before finishing

## Subagents

| Subagent | Role | Phase || --

- | --- | --- || `@investigator` | Explores the scenario and app behavior | Phase 1 || `@author` | Drafts the Playwright test | Phase 3 || `@runner` | Executes and iterates on the test | Phase 4 |

## Personas

### @investigatorA scenario investigator who gathers the facts needed to write a correct test.

### @authorA test author who writes clean Playwright TypeScript.

### @runnerA test runner who fixes issues until the test passes.

## Steps

- Clarify the scenario.
- Inspect the app with Playwright MCP.
- Write the test file.
- Run and iterate until it passes.

## Tasks

- Capture the scenario.
- Observe the live behavior.
- Draft the Playwright test.
- Execute and stabilize it.

## Subtasks

- Ask for missing scenario details.
- Collect selectors and outcomes.
- Save the test in tests/.
- Repeat until the test passes.

## Actions Summary

1. Gather the scenario.
2. Inspect the app.
3. Generate the test file.
4. Run and refine the test.```

## Template References

Templates in `templates/playwright-generate-test/`:- `phases.md`

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

## Workflow

<content>

Same-family prompts:

- [`playwright-automation-fill-in-form.prompt.md`](playwright-automation-fill-in-form.prompt.md)
- [`playwright-explore-website.prompt.md`](playwright-explore-website.prompt.md)
- [`playwright-typescript.prompt.md`](playwright-typescript.prompt.md)
```
# Prompt template
Execute the workflow defined in this file.
```
