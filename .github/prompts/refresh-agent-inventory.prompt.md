---

name: refresh-agent-inventory

title: Refresh Agent Inventory

description: Refresh workspace customization inventory and patch stale AGENTS or copilot instruction references.

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

  - agents

  - ai-assistant

  - ml

  - prompts

  - skills

  - typescript

trigger: /refresh-agent-inventory

mode: ask

dependencies: []

metadata:

  hermes: {}

---

## Goal

Use when

## Description to accomplish the associated tasks and objectives.

## Description

Refresh the workspace customization inventory by reconciling discovered assetsagainst the canonical report, then propose precise edits for stale AGENTS andcopilot instruction references.

## Context

- Workspace is monorepo-style with root and subproject overrides.
- Canonical report path:  - reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
- Primary customization files:  - AGENTS.md  - .github/copilot-instructions.md

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)- customization-audit- context-map

## Subagents

- Explore (optional): read-only discovery of inventory, duplicates, and stale  references.

## Personas

- Maintainer persona: prioritize deterministic, low-risk edits.
- Auditor persona: prioritize verifiable findings with file evidence.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow nearest-file precedence for AGENTS and instructions.
- Link to existing documents instead of embedding long copied content.
- Keep edits minimal and scoped to customization files.
- If no changes are needed, output a no-op report with evidence.

## Phases

### Phase 1: Discover and compare

| Field      | Details                                                                    || ---------

- | -------------------------------------------------------------------------- || Goal       | Build a current inventory snapshot and compare it to the canonical report. || Inputs     | Workspace files, report file, AGENTS.md, .github/copilot-instructions.md.  || Outputs    | Drift list with concrete path-level evidence.                              || Validation | Every drift item cites at least one path and one mismatch type.            |

### Phase 2: Propose and apply scoped updates

| Field      | Details                                                                  || ---------

- | ------------------------------------------------------------------------ || Goal       | Produce minimal customization-file updates that remove drift.            || Inputs     | Phase 1 drift list and current customization file contents.              || Outputs    | Patch-ready update plan and optional applied edits.                      || Validation | Updated references are path-valid and do not introduce duplicate assets. |

## Steps

1. Discover AGENTS.md files and customization assets under .github.
2. Read the canonical inventory report and compare counts and references.
3. Identify stale lists, missing paths, and duplicate-purpose customizations.
4. Prepare minimal edits for AGENTS.md and .github/copilot-instructions.md if   needed.
5. Summarize outcomes as a remediation report.

## Tasks

- Task 1.1 — Discover AGENTS and customization asset files.- Task 1.2 — Compare discovered inventory with report-backed counts and  references.- Task 2.1 — Draft minimal updates for stale customization references.- Task 2.2 — Validate paths and precedence logic after updates.- Task 2.3 — Publish remediation summary with risk notes.

## Subtasks

- Subtask 1.1.1 — Enumerate AGENTS files by workspace path.- Subtask 1.2.1 — Record count deltas for instructions, prompts, and skills.- Subtask 2.1.1 — Patch stale override lists and refresh commands.- Subtask 2.2.1 — Verify no broken links or invalid paths in changed files.- Subtask 2.3.1 — Report fixed items, remaining risks, and next actions.

## Actions Summary

- Discover current customization inventory.
- Compare against canonical report and precedence rules.
- Apply or propose minimal customization-file fixes.
- Deliver a concise remediation report with evidence.

## Template References

Templates in `templates/refresh-agent-inventory/`:- `phases.md`

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

Refresh workspace customization inventory and patch stale AGENTS or copilot instruction references.

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
