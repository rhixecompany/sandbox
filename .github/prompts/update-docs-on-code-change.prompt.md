---

name: update-docs-on-code-change

title: Update Docs on Code Change

description: 'Comprehensive prompt for synchronizing documentation whenever code changes modify behavior, APIs, or workflows.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

scripts: []

skills: []

formatter: default

plan: None

tags:

  - api

  - configuration

  - documentation

  - frontend

  - maintenance

  - ml

  - prompts

  - skills

  - typescript

  - workflow

trigger: /update-docs-on-code-change

dependencies: []

metadata:

  hermes: {}

---

## Goal

Use when "Comprehensive prompt for synchronizing documentation whenever code changes modify behavior, APIs, or workflows." to accomplish the associated tasks and objectives.

## Description

Detect when code changes require documentation updates and ensure README, API docs, config docs, changelogs, and examples remain synchronized.

## Context

Use this prompt whenever application code, scripts, APIs, configuration, or public interfaces are changed.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Change-impact analysis across code and documentation
- Documentation synchronization and migration guide authoring
- Example and reference validation

## Subagents

| Subagent | Role | When to Use || --

- | --- | --- || Impact Analyzer | Maps code changes to required documentation updates | Always || Docs Updater | Executes README/API/config/changelog updates | Always || Verification Reviewer | Confirms docs and examples remain accurate | Final validation |

## Personas

- Impact Analyzer: Finds every doc affected by behavior or interface changes.
- Docs Updater: Produces precise updates in standard documentation locations.
- Verification Reviewer: Ensures no stale references or broken examples remain.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Update docs in the same change as code whenever behavior or interfaces change.
- Always evaluate README impact for new features, setup, config, and CLI changes.
- Sync API docs for endpoint/signature/auth changes.
- Update examples and migration guidance for breaking or deprecated behavior.
- Keep changelog entries structured and user-focused.

## Phases

### Phase 1: Trigger and Scope Detection

### Phase 2: Documentation Synchronization

## Steps

1. Evaluate code changes against documentation trigger conditions.
2. Build a file-level list of required doc updates.
3. Update README, API docs, configuration docs, and examples.
4. Add changelog and migration notes where applicable.
5. Verify links, snippet correctness, and public-facing clarity.

## Tasks

- Task 1.1 — Detect documentation-triggering code changes and classify impact.- Task 1.2 — Update required documentation files and sections.- Task 1.3 — Synchronize code examples, API references, and configuration docs.- Task 1.4 — Add changelog and migration guidance for breaking changes.- Task 1.5 — Validate documentation completeness and consistency.

## Subtasks

- Subtask 1.1.1 — Map each changed public symbol or behavior to a doc target.- Subtask 1.2.1 — Update README features, setup, CLI, and configuration sections as needed.- Subtask 1.3.1 — Confirm snippets match current signatures and imports.- Subtask 1.4.1 — Mark deprecated behavior and provide migration steps.- Subtask 1.5.1 — Check links and note any deferred documentation debt.

## Actions Summary

1. Detect doc-impacting code changes.
2. Synchronize all affected docs in the same change.
3. Validate examples and references.
4. Deliver release-ready documentation alignment.

## Template References

Templates in `templates/update-docs-on-code-change/`:- `phases.md`

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

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

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

Comprehensive prompt for synchronizing documentation whenever code changes modify behavior, APIs, or workflows.

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
