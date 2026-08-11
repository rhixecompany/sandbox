---
name: playwright-automation-fill-in-form
title: Playwright Automation Fill In Form
description: 'Fill a form with Playwright MCP, stop before submission, and ask for a human review.'
version: 1.0.0
license: MIT
author: Alexa
toolsets:
  - file
  - terminal
  - web
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - audit
  - mcp
  - ml
  - playwright
  - prompts
  - specification
  - typescript
trigger: /playwright-automation-fill-in-form
compatibility: 'None'
created: 2026-05-25 10:50:21.952313+00:00
mcp_generator: 'None'
skill_stub: 'True'
dependencies: []
metadata:
  hermes: {}
---

## Goal

Fill a form with Playwright MCP, stop before submission, and ask for a human review.

## Context

Use when you need to playwright form fill automation for the current workspace or task.

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

- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Description

Fill a form with Playwright MCP, stop before submission, and ask for a human review.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- `webapp-testing` — use browser automation to interact with the live form
- `systematic-debugging` — resolve selector and filling issues methodically
- `verification-before-completion` — confirm the form is ready for review before stopping

## Subagents

| Subagent | Role | Phase || --

- | --- | --- || `@browser` | Performs the form interaction steps | Phase 2 || `@checker` | Confirms the filled state and captures issues | Phase 3 |

## Personas

### @browserA careful browser operator who fills the form field by field.

### @checkerA reviewer who verifies the form is ready but not submitted.

## Steps

- Confirm input values.
- Open the form.
- Fill all fields carefully.
- Stop and request review.

## Tasks

- Validate inputs.
- Fill the form fields.
- Upload the image if valid.
- Pause before submit.

## Subtasks

- Check the URL.
- Verify each field label.
- Confirm the upload path exists.
- Report the ready-to-review state.

## Actions Summary

1. Open the form URL.
2. Fill the requested fields.
3. Upload the image if available.
4. Stop before submission.```

## Template References

Templates in `templates/playwright-automation-fill-in-form/`:- `phases.md`

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

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |
