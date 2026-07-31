---

name: playwright-explore-website

title: Playwright Explore Website

description: 'Explore a website with Playwright MCP, document core flows, and propose tests from the findings.'

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

plan: None

tags:

  - mcp

  - ml

  - playwright

  - prompts

  - specification

  - testing

  - typescript

trigger: /playwright-explore-website

compatibility: None

created: 2026-05-25 10:50:21.952313+00:00

mcp_generator: None

skill_stub: 'True'

dependencies: []

metadata:

  hermes: {}

---

## Goal

Explore a website with Playwright MCP, document core flows, and propose tests from the findings.

## Context

Use when you need to playwright website exploration for the current workspace or task.

## Input

s

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Output

s

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

Explore a website with Playwright MCP, document core flows, and propose tests from the findings.

## Context

- Use the provided URL; if none is provided, ask the user for one.
- Focus on the main user journeys rather than exhaustive coverage.
- Record locators and observed outcomes while exploring.

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

## Rules

1. Navigate to the provided URL before exploring.
2. If no URL is provided, ask for one instead of guessing.
3. Inspect 3 to 5 core flows only.
4. Capture useful locators and expected outcomes.
5. Close the browser context when finished.
6. Provide a concise summary and test ideas.

## Phases

### Phase 1: Start and orient

> **Goal:** load the site and identify the main areas worth exploring.

## Steps

- Open the URL.
- Explore 3 to 5 core flows.
- Document locators and outcomes.
- Propose tests and close the browser.

## Tasks

- Confirm the URL.- Exercise the main user journeys.- Record evidence.- Summarize and suggest tests.

## Subtasks

- Ask for a URL if missing.- Capture locators for key controls.- Note observed outcomes.- Close the browser context.

## Actions Summary

1. Navigate to the site.
2. Interact with the core flows.
3. Document locators and outcomes.
4. Generate test ideas.```

## Template References

Templates in `templates/playwright-explore-website/`:- `phases.md`

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
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Goal

Explore a website with Playwright MCP, document core flows, and propose tests from the findings.

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
