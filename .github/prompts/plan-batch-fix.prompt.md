---
name: plan-batch-fix
title: Plan Batch Fix
description: Performs a full scan, batches fixes by priority, verifies per batch with git commits, then re-scans and writes docs/batch-fix-report.md with before/after counts.
trigger: /plan-batch-fix
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
Performs a full scan, batches fixes by priority, verifies per batch with git commits, then re-scans and writes docs/batch-fix-report.md with before/after counts.

## Context

## Phases

# Table of Contents

- [Goal](#goal)
- [Input](#input)
- [Core Rules](#core-rules)
- [Workflow](#workflow)
  - [Phase 1: Full scan](#phase-1:-full-scan)
  - [Phase 2: Batch fixes](#phase-2:-batch-fixes)
  - [Phase 3: Full re-scan](#phase-3:-full-re-scan)
  - [Phase 4: Report](#phase-4:-report)
- [Verification Checklist](#verification-checklist)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Input](#input)
- [Core Rules](#core-rules)
- [Workflow](#workflow)
- [Phase 1: Full scan](#phase-1:-full-scan)
- [Phase 2: Batch fixes](#phase-2:-batch-fixes)
- [Phase 3: Full re-scan](#phase-3:-full-re-scan)
- [Phase 4: Report](#phase-4:-report)
- [Verification Checklist](#verification-checklist)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Scan a codebase for errors, warnings, and deprecations, then fix them systematically in batches. Supports lint issues, TypeScript errors, deprecated API usage, and code quality problems.

> **Shared template references:**>> - [Core rules](templates/_shared/rules-core.md)> - [Skills table](templates/_shared/skills-table-core.md)> - [Verification checklist](templates/_shared/verification-checklist.md)

## Input

- **Target directory** — Codebase root to scan (default: workspace root)
- **Tools to run** — e.g. `tsc --noEmit`, `eslint .`, `pylint`, `cargo check`
- **Batch size** — Files to fix per batch (default: 7)
- **Ignore patterns** — Files/directories to skip

## Core Rules

See [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md).Additional batch-fix rules:1. **Scan before fix** — Always run the full scan first to understand scope.2. **One category at a time** — Fix errors first, then warnings, then deprecations.3. **Verify each batch** — Re-run the tool on the fixed files before moving on.4. **No auto-ignore** — Don't silently skip hard errors; report them as blockers.5. **Git commit per batch** — Every batch gets its own commit for easy rollback.

## Workflow

### Phase 1: Full scan

Run the relevant lint/type-check tool across the entire target:```bash# For TypeScript:tsc --noEmit 2

> &1 | tee docs/batch-fix-scan-results.txt# For Python:pylint **/*.py 2>&1 | tee docs/batch-fix-scan-results.txt# For generalized errors:grep -rn "error\|warning\|deprecated" src/ --include="*.ts" --include="*.tsx"
> docs/batch-fix-scan-results.txt```Categorise issues:- **High:** Compile/type errors (must fix)- **Medium:** Warnings and lint violations (should fix)- **Low:** Deprecation notices (fix when encountered)

### Phase 2: Batch fixes

For each batch (default: 7 files per batch):1. Pick the batch of files with the highest-priority issues.2. Fix each file using `systematic-debugging` approach.3. Re-run the scan on the fixed files to confirm fix.4. `git add -A && git commit -m "fix(batch): <tool

> errors batch <N
> — <files>"`

### Phase 3: Full re-scan

After all batches complete, run the full scan again.

- If zero errors remain → done.
- If errors remain but are pre-existing or out of scope → document in report.

### Phase 4: Report

Write report to `docs/batch-fix-report.md`:- Total issues found: errors / warnings / deprecations- Issues fixed: errors / warnings / deprecations- Issues remaining: errors / warnings / deprecations- Files modified- Git commits

## Verification Checklist

- [ ] Full scan completed and results saved
- [ ] Errors fixed and verified per batch
- [ ] Warnings fixed and verified per batch
- [ ] Full re-scan shows reduction
- [ ] Git commits created per batch
- [ ] Report written with before/after counts
- [ ] No regressions introduced (tests pass if applicable)

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
4. **Report blockers** — State when something fails.


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

- [`plan-audit.prompt.md`](plan-audit.prompt.md)
- [`plan-execute.prompt.md`](plan-execute.prompt.md)
- [`plan-generate.prompt.md`](plan-generate.prompt.md)
```
# Prompt template
Execute the workflow defined in this file.
```
