---
name: playwright-automation-fill-in-form
title: Playwright Form Fill Automation
description: Fills a form field by field using Playwright MCP, uploads an image if requested, then stops before submit and asks for human review.
trigger: /playwright-automation-fill-in-form
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
Fills a form field by field using Playwright MCP, uploads an image if requested, then stops before submit and asks for human review.

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
- [@browserA careful browser operator who fills the form field by field.](#@browsera-careful-browser-operator-who-fills-the-form-field-by-field)
- [@checkerA reviewer who verifies the form is ready but not submitted.](#@checkera-reviewer-who-verifies-the-form-is-ready-but-not-submitted)
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





Fill a form with Playwright MCP, stop before submission, and ask for a human review.


Use when filling web forms field by field with Playwright, stopping before submission for human review.

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

- [`playwright-explore-website.prompt.md`](playwright-explore-website.prompt.md)
- [`playwright-generate-test.prompt.md`](playwright-generate-test.prompt.md)
- [`playwright-typescript.prompt.md`](playwright-typescript.prompt.md)
```
# Prompt template
Execute the workflow defined in this file.
```
