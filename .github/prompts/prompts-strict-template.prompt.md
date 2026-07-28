---
name: prompts-strict-template
title: Prompts Strict Template
description: Comprehensive prompt for enforcing strict .prompt.md template structure and formatting rules.
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
  - audit
  - fix
  - frontend
  - markdown
  - ml
  - prompts
  - skills
  - typescript
trigger: /prompts-strict-template
dependencies: []
metadata:
  hermes: {}
---
## GoalUse when "Comprehensive prompt for enforcing strict .prompt.md template structure and formatting rules." to accomplish the associated tasks and objectives.

## DescriptionNormalize and validate prompt markdown files so they follow the repository's strict required structure, section order, phase table format, and task numbering conventions.

## ContextUse this prompt when creating, editing, reviewing, or repairing files that match .prompt.md naming conventions.

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)- Markdown structure and lint-aware formatting- Template compliance verification- Controlled normalization without intent loss

## Subagents| Subagent | Role | When to Use || --- | --- | --- || Template Enforcer | Applies required section order and presence checks | Always || Structure Validator | Validates phase tables and numbering syntax | Always || Intent Preserver | Prevents semantic drift during normalization | Existing prompt migrations |

## Personas- Template Enforcer: Treats required section order as non-negotiable.- Structure Validator: Rejects malformed phases, tables, and numbering patterns.- Intent Preserver: Keeps original prompt purpose and guidance intact.

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Ensure all required top-level sections exist and are non-empty.- Keep required section order exact.- Include at least one phase with required Field/Details table and mandatory rows.- Enforce Task N.x and Subtask N.x.y numbering patterns.- Preserve source intent and wording as much as possible.

## Phases

### Phase 1: Structural IntakeInventory the target `.prompt.md` before editing: parse its frontmatter (name/trigger/description/dependencies), list its top-level `##` sections in order, and compare against the 11 required sections — flagging any that are missing, extra, or out of order. Also inspect each Phase block for a Field/Details table with the mandatory `Phase`/`Input`/`Output`/`Validation` rows and check `Task N.x` / `Subtask N.x.y` numbering. Emits a drift report; mutates nothing.

### Phase 2: Template NormalizationApply the Phase 1 findings: insert missing sections in exact required order, reorder out-of-order ones, give every Phase a Field/Details table with the four mandatory rows, and rewrite list items to strict `Task N.x` / `Subtask N.x.y` numbering. Then run `enhance-markdown`-style checks, preserve the source's intent and wording, and emit a compliance report. Safe to re-run (idempotent).> **Full content:** `templates/prompts-strict-template/phases.md`

## Steps1. Parse prompt content and compare with strict template requirements.2. Add missing sections in exact required order.3. Normalize phase formatting and table rows.4. Correct Tasks and Subtasks numbering syntax.5. Validate final structure and preserve original intent.

## Tasks- Task 1.1 — Detect missing or out-of-order top-level sections.- Task 1.2 — Ensure Phase sections include required table schema and rows.- Task 1.3 — Normalize Tasks and Subtasks numbering patterns.- Task 1.4 — Preserve source intent while restructuring content.- Task 1.5 — Produce final compliance validation output.

## Subtasks- Subtask 1.1.1 — Check exact sequence of all 11 required sections.- Subtask 1.2.1 — Verify Goal, Inputs, Outputs, and Validation rows exist.- Subtask 1.3.1 — Rewrite list entries to Task N.x and Subtask N.x.y format.- Subtask 1.4.1 — Retain meaningful prompt semantics and role guidance.- Subtask 1.5.1 — Confirm no new markdown diagnostics were introduced.

## Actions Summary1. Detect structural drift.2. Normalize to strict template.3. Validate numbering and phase tables.4. Deliver compliance-preserving updates.

## Template ReferencesTemplates in `templates/prompts-strict-template/`:- `phases.md`

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
|---|------|-----------|
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |


## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Goal

Comprehensive prompt for enforcing strict .prompt.md template structure and formatting rules.


## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.


## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
|-------|---------|
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


