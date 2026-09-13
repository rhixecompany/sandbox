---
name: create-readme
title: Create Readme
description: Create a README.md file for the project.
version: 1.0.0
license: MIT
author: Hermes Agent
trigger: /create-readme
toolsets:
- file
- terminal
- web
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
    command: opencode /create-readme
    flags: {}
    help: Create a README.md file for the project.
  codex:
    model_override: null
    system_prompt_id: null
    temperature: null
    max_tokens: null
tags:
- agent-type:hermes
- documentation
- generator
- ml
- prompts
- specification
- typescript
scripts: []
---

## Goal

Create a README.md file for the project.

## Context

Use when you need to work on the current workspace or task.

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

## Role

You're a senior expert software engineer with extensive experience in open source projects. You always make sure the README files you write are appealing, informative, and easy to read.

## Task

1. Take a deep breath, and review the entire project and workspace, then create a comprehensive and well-structured README.md file for the project.2. Take inspiration from these readme files for the structure, tone and content:   - <https://raw.githubusercontent.com/Azure-Samples/serverless-chat-langchainjs/refs/heads/main/README.md>   - <https://raw.githubusercontent.com/Azure-Samples/serverless-recipes-javascript/refs/heads/main/README.md>   - <https://raw.githubusercontent.com/sinedied/run-on-output/refs/heads/main/README.md>   - <<https://raw.githubusercontent.com/sinedied/smoke/refs/heads/main/README.md>

> 1. Do not overuse emojis, and keep the readme concise and to the point.4. Do not include sections like "LICENSE", "CONTRIBUTING", "CHANGELOG", etc. There are dedicated files for those sections.5. Use GFM (GitHub Flavored Markdown) for formatting, and GitHub admonition syntax (<https://github.com/orgs/community/discussions/16925>) where appropriate.6. If you find a logo or icon for the project, use it in the readme's header.

## Template References

Templates in `templates/create-readme/`:- `phases.md`

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`create-agentsmd.prompt.md`](create-agentsmd.prompt.md)
- [`create-architectural-decision-record.prompt.md`](create-architectural-decision-record.prompt.md)
- [`create-github-action-workflow-specification.prompt.md`](create-github-action-workflow-specification.prompt.md)
- [`create-github-issue-feature-from-specification.prompt.md`](create-github-issue-feature-from-specification.prompt.md)
- [`create-github-issues-feature-from-implementation-plan.prompt.md`](create-github-issues-feature-from-implementation-plan.prompt.md)
- [`create-github-issues-for-unmet-specification-requirements.prompt.md`](create-github-issues-for-unmet-specification-requirements.prompt.md)
- [`create-github-pull-request-from-specification.prompt.md`](create-github-pull-request-from-specification.prompt.md)
- [`create-implementation-plan.prompt.md`](create-implementation-plan.prompt.md)
- [`create-llms.prompt.md`](create-llms.prompt.md)
- [`create-oo-component-documentation.prompt.md`](create-oo-component-documentation.prompt.md)
- [`create-specification.prompt.md`](create-specification.prompt.md)
- [`create-spring-boot-java-project.prompt.md`](create-spring-boot-java-project.prompt.md)
- [`create-spring-boot-kotlin-project.prompt.md`](create-spring-boot-kotlin-project.prompt.md)
- [`create-technical-spike.prompt.md`](create-technical-spike.prompt.md)
- [`create-tldr-page.prompt.md`](create-tldr-page.prompt.md)