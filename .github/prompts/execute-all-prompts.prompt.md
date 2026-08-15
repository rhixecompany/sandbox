---
name: execute-all-prompts
title: execute all prompts
description: Prompt for execute-all-prompts
version: "1.0.0"
tags: []
trigger: execute-all-prompts
metadata:
  hermes:
    profile: default
    priority: medium
    categories: []
  copilot:
    model_required: claude-opus
    context_length: medium
  opencode:
    enabled: true
    compatibility: compatible
  codex:
    enabled: false
    model_preferred: text-davinci-003
---

---
name: execute-all-prompts
title: Execute All Prompts Orchestrator
description: 'Orchestrates sequential execution of 4 workspace prompt workflows: audit-skills-judge-fix,
  agents-system-prompt-context-fix, sync-hermes-opencode, and test-providers-models.
  Each prompt runs to completion before the next begins.'
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
- agents
- ai-assistant
- audit
- data
- execution
- fix
- prompts
- skills
- testing
- typescript
- workflow
trigger: /execute-all-prompts
formatter: default
dependencies:
- skill:using-superpowers
- skill:user-communication-preferences
- skill:verification-before-completion
- skill:subagent-driven-development
metadata:
  hermes: {}
toolsets: null
scripts: []
skills: null
plan: null
---

## Goal

Orchestrates sequential execution of 4 workspace prompt workflows: audit-skills-judge-fix, agents-system-prompt-context-fix, sync-hermes-copilot-codex, and test-providers-models. Each prompt runs to completion before the next begins.

# Execute All Prompts Orchestrator

> Strict sequential execution. Phase N+1 begins only after Phase N is fully verified complete.

## Context

- **Workspace root:** `C:\Users\Alexa\Desktop\SandBox`
- **Hermes prompts root:** `C:\Users\Alexa\AppData\Local\hermes\prompts`
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`

## Execution Rule

- This workflow is intended to be run through the available Hermes task interface.
- If a dedicated `hermes prompt run ...` command is unavailable, execute this workflow by processing the referenced prompt files in sequence, preserving strict ordering and phase gates.
- Only advance after the current phase passes its gate.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. Execute prompts in order. Do not reorder.
2. Each prompt must pass its own verification before advancing.
3. All Python scripts/outputs go under the Hermes scripts path unless the prompt states otherwise.
4. Append progress after each phase; append evidence to verification after each phase.
5. If a prompt file is missing, pause and report the exact missing path instead of fabricating work.

## Phase Contents

Full phase instructions live in `templates/execute-all-prompts/phases.md`.

| Order | Phase | Prompt File |
| ------ | ------- | ----------- |
| 1 | Audit Skills Judge Fix | `audit-skills-judge-fix.prompt.md` |
| 2 | Agents System Prompt Context Fix | `agents-system-prompt-context-fix.prompt.md` |
| 3 | Sync Hermes OpenCode | `sync-hermes-opencode.prompt.md` |
| 4 | Test Providers & Models | `test-providers-models.prompt.md` |

## Verification Checklist (Orchestrator Level)

- [ ] Phase 1 completed and verified
- [ ] Phase 2 completed and verified
- [ ] Phase 3 completed and verified
- [ ] Phase 4 completed and verified
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`

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

- [`execute-plan.prompt.md`](execute-plan.prompt.md)

