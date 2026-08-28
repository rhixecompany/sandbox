---
name: repo-tooling-implementation
title: Repo Tooling Implementation
description: Execute the repo-tooling-implementation workflow, which scaffolds AI-agent context files (AGENTS.md, copilot-instructions, hooks, etc.) and verifies per-repo tooling.
version: 1.0.0
author: Hermes Agent
tags: [repo, tooling, agent-context, scaffolding, setup]
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
date: '2026-08-25'
---
## Table of Contents

## Goal

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Template Reference](#template-reference)
- [Execution](#execution)
- [Steps](#steps)
- [Rules](#rules)
- [Subgoals](#subgoals)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Tasks](#tasks)
- [Dependencies](#dependencies)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Template Reference](#template-reference)
- [Execution](#execution)
- [Steps](#steps)
- [Rules](#rules)
- [Subgoals](#subgoals)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Tasks](#tasks)
- [Dependencies](#dependencies)
- [Related Prompts](#related-prompts)





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

| Persona | When to Use |
| ------------- | -------------------------------------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes


Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.


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

- Return final artifact or findings .
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| - | ---------- | ----------------------------------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| -------------------------------- | ----------------------------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| Server | Purpose |
| --------------------- | ----------------------------------------- |
| `filesystem` | File read/write operations |
| `github` | GitHub API operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `ast-grep` | AST-based code search and replace |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `tavily` | Web search + URL extraction |

## Hooks

The following workspace hooks run around this prompt's execution (see `.github/hooks/README.md`):

| Hook | When | Behavior |
| ------------------------ | ----------------- | ---------------------------- |
| `session-logger` | session start/end | Logs session metadata |
| `governance-audit` | session events | Audits governance compliance |
| `session-auto-commit` | session end | Auto-commits session state |
| `pre-exec-validate.sh` | before commands | Validates command execution |
| `post-exec-state-log.py` | after commands | Appends state log |

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