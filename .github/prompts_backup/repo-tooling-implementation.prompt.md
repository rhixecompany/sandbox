---
name: repo-tooling-implementation
title: Repo Tooling Implementation
description: Fully implement the repo-tooling master plan with verification, fixes, and artifact delivery
  across the SandBox workspace.
version: 1.1.0
license: MIT
author: Hermes Agent
trigger: /repo-tooling-implementation
toolsets:
- file
- terminal
skills: []
dependencies:
- prompt:repo
- skill:executing-plans
- skill:systematic-debugging
- skill:verification-before-completion
- skill:using-superpowers
- tool:mcp-filesystem
- tool:mcp-github
- tool:mcp-sequential-thinking
- tool:mcp-tavily
formatter: default
metadata:
  hermes:
    profile: code-architect
    mcp_servers: []
    context_size: large
  copilot:
    context_size: large
    extensions: []
    keybinding: null
  opencode:
    command: opencode /repo-tooling-implementation
    flags: {}
    help: Fully implement the repo-tooling master plan with verification, fixes, and ar...
  codex:
    model_override: null
    system_prompt_id: null
    temperature: null
    max_tokens: null
tags:
- agent-type:hermes
- documentation
- fix
- ml
- prompts
- typescript
- workflow
scripts: []
## Goal

Execute the `repo-tooling-implementation` workflow. Full details: `templates/repo-tooling-implementation/README.md`.

## Template Reference

Detailed template in `templates/repo-tooling-implementation/`:

- `README.md`

## Execution

See `templates/repo-tooling-implementation/README.md` for phases/steps/workflow.

## Steps

1. Read `templates/repo-tooling-implementation/README.md`.
2. Execute the workflow.
3. Verify outputs.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.


## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona       | When to Use                            |
| ------------- | -------------------------------------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer**  | Code review, quality assurance         |
| **User**      | General purpose, operations            |


## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes


## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.


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

| # | Gate       | Criterion                           |
| - | ---------- | ----------------------------------- |
| 1 | Scope      | Change matches the original request |
| 2 | Quality    | Meets project standards             |
| 3 | Tests      | Tests pass (if applicable)          |
| 4 | Regression | No unintended side effects          |
| 5 | Docs       | Changes documented if needed        |


## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill                            | Purpose                       |
| -------------------------------- | ----------------------------- |
| `using-superpowers`              | Foundational skill workflow   |
| `systematic-debugging`           | Root cause analysis and fix   |
| `git-patch-management`           | Patch creation and management |
| `executing-plans`                | Execute plans step by step    |
| `verification-before-completion` | Validate before claiming done |


## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| Server                | Purpose                                   |
| --------------------- | ----------------------------------------- |
| `filesystem`          | File read/write operations                |
| `github`              | GitHub API operations                     |
| `sequential-thinking` | Structured reasoning for complex problems |
| `ast-grep`            | AST-based code search and replace         |
| `fetch`               | Web page content extraction               |
| `playwright`          | Browser automation for interactive pages  |
| `tavily`              | Web search + URL extraction               |

## Hooks

The following workspace hooks run around this prompt's execution (see `.github/hooks/README.md`):

| Hook                     | When              | Behavior                     |
| ------------------------ | ----------------- | ---------------------------- |
| `session-logger`         | session start/end | Logs session metadata        |
| `governance-audit`       | session events    | Audits governance compliance |
| `session-auto-commit`    | session end       | Auto-commits session state   |
| `pre-exec-validate.sh`   | before commands   | Validates command execution  |
| `post-exec-state-log.py` | after commands    | Appends state log            |

## Scripts

- `.github/prompts/.enhance/analyze_prompts.py` — Prompt-library analyzer (audit/verify)
- `.github/hooks/*` — Hook implementations listed in the Hooks section

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions



## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Related Prompts

Same-family prompts:

- [`repo-init.prompt.md`](repo-init.prompt.md)
- [`repo-management.prompt.md`](repo-management.prompt.md)
- [`repo-research-pipeline.prompt.md`](repo-research-pipeline.prompt.md)
- [`repo-story-time.prompt.md`](repo-story-time.prompt.md)
- [`repo.prompt.md`](repo.prompt.md)