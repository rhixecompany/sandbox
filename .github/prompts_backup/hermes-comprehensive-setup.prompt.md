---
name: hermes-comprehensive-setup
title: Comprehensive Hermes and OpenCode Setup, Migration, and Validation
description: 'Configure Hermes and OpenCode using best practices: load all prompts, plans, markdown files,
  skills, MCP servers, hooks, and templates. Run enhancement, validation, and dry-run verification end
  to end.'
version: 1.0.0
license: MIT
author: Hermes Agent
trigger: /hermes-comprehensive-setup
toolsets:
- file
- terminal
skills: []
dependencies: []
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
    command: opencode /hermes-comprehensive-setup
    flags: {}
    help: 'Configure Hermes and OpenCode using best practices: load all prompts, plans, ...'
  codex:
    model_override: null
    system_prompt_id: null
    temperature: null
    max_tokens: null
tags:
- agent-type:hermes
- ai-assistant
- backend
- configuration
- documentation
- markdown
- mcp
- ml
- prompts
- skills
- typescript
- workflow
scripts: []
## Goal

Execute the `hermes-comprehensive-setup` workflow. Full details: `templates/hermes-comprehensive-setup/README.md`.

## Template Reference

Detailed template in `templates/hermes-comprehensive-setup/`:

- `README.md`

## Execution

See `templates/hermes-comprehensive-setup/README.md` for phases/steps/workflow.

## Steps

1. Read `templates/hermes-comprehensive-setup/README.md`.
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


## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `test-driven-development` | TDD workflow enforcement |
| `code-review` | Code quality assurance |
| `systematic-debugging` | Debugging and root cause analysis |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |


## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `code-sandbox` | Isolated code execution and testing |
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



## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`hermes-breakdown-epic-arch.prompt.md`](hermes-breakdown-epic-arch.prompt.md)
- [`hermes-breakdown-epic-pm.prompt.md`](hermes-breakdown-epic-pm.prompt.md)
- [`hermes-breakdown-feature-implementation.prompt.md`](hermes-breakdown-feature-implementation.prompt.md)
- [`hermes-breakdown-feature-prd.prompt.md`](hermes-breakdown-feature-prd.prompt.md)
- [`hermes-breakdown-plan.prompt.md`](hermes-breakdown-plan.prompt.md)
- [`hermes-breakdown-test.prompt.md`](hermes-breakdown-test.prompt.md)
- [`hermes-doctor-systematic-debugging.prompt.md`](hermes-doctor-systematic-debugging.prompt.md)