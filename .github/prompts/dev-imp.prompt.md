---
name: dev-imp
title: Development Implementation
description: "Execute a software implementation plan: select generators, implement, verify, code review, debug, and produce a structured completion report."
version: 1.0.0
author: Hermes Agent
tags:
- development
- implementation
- automation
- devops
- planning
- coding
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
---
## Table of Contents

## Goal

## Context

## Phases



# Table of Contents

- [Goal](#goal)
- [Plans‑and‑Specs](#plans‑and‑specs)
  - [Goal](#goal)
  - [Success Criteria](#success-criteria)
  - [Data Flow](#data-flow)
  - [Strict Sequential Gates](#strict-sequential-gates)
- [Scripts](#scripts)
- [Profile](#profile)
- [Personality](#personality)
- [Tools](#tools)
- [Personas](#personas)
- [Phases (Execute in Order)](#phases-execute-in-order)
  - [Phase 1: Discover & Select Generators](#phase-1:-discover-&-select-generators)
  - [Phase 2: Implement Selected Generators](#phase-2:-implement-selected-generators)
  - [Phase 3: Verify Implementation Status (Only After All Generators Complete)1. Check the target project state:](#phase-3:-verify-implementation-status-only-after-all-generators-complete1-check-the-target-project-state:)
  - [Phase 4: Code Review Changed Files (Only After Verification Passes)](#phase-4:-code-review-changed-files-only-after-verification-passes)
  - [Phase 5: Debug & Fix All Issues (Only After Code Review)](#phase-5:-debug-&-fix-all-issues-only-after-code-review)
  - [Phase 6: Generate Implementation Report (Only After All Fixes Verified)](#phase-6:-generate-implementation-report-only-after-all-fixes-verified)
- [Summary](#summary)
- [Generators Executed](#generators-executed)
- [Files Changed](#files-changed)
- [Code Review Findings](#code-review-findings)
  - [Critical](#critical)
  - [Important](#important)
  - [Minor](#minor)
- [Fixes Applied](#fixes-applied)
- [Verification](#verification)
- [Final Status**All phases complete. Implementation ready for use.**](#final-status**all-phases-complete-implementation-ready-for-use**)
  - [Report Style ("Crispy")](#report-style-"crispy")
- [Edge Cases & Pitfalls](#edge-cases-&-pitfalls)
- [Verification Checklist](#verification-checklist)
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
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Plans‑and‑Specs](#plans‑and‑specs)
- [Goal](#goal)
- [Success Criteria](#success-criteria)
- [Data Flow](#data-flow)
- [Strict Sequential Gates](#strict-sequential-gates)
- [Scripts](#scripts)
- [Profile](#profile)
- [Personality](#personality)
- [Tools](#tools)
- [Personas](#personas)
- [Phases (Execute in Order)](#phases-execute-in-order)
- [Phase 1: Discover & Select Generators](#phase-1:-discover-&-select-generators)
- [Phase 2: Implement Selected Generators](#phase-2:-implement-selected-generators)
- [Phase 3: Verify Implementation Status (Only After All Generators Complete)1. Check the target project state:](#phase-3:-verify-implementation-status-only-after-all-generators-complete1-check-the-target-project-state:)
- [Phase 4: Code Review Changed Files (Only After Verification Passes)](#phase-4:-code-review-changed-files-only-after-verification-passes)
- [Phase 5: Debug & Fix All Issues (Only After Code Review)](#phase-5:-debug-&-fix-all-issues-only-after-code-review)
- [Phase 6: Generate Implementation Report (Only After All Fixes Verified)](#phase-6:-generate-implementation-report-only-after-all-fixes-verified)
- [Summary](#summary)
- [Generators Executed](#generators-executed)
- [Files Changed](#files-changed)
- [Code Review Findings](#code-review-findings)
- [Critical](#critical)
- [Important](#important)
- [Minor](#minor)
- [Fixes Applied](#fixes-applied)
- [Verification](#verification)
- [Final Status**All phases complete. Implementation ready for use.**](#final-status**all-phases-complete-implementation-ready-for-use**)
- [Report Style ("Crispy")](#report-style-"crispy")
- [Edge Cases & Pitfalls](#edge-cases-&-pitfalls)
- [Verification Checklist](#verification-checklist)
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
- [Related Prompts](#related-prompts)





Meta-prompt that discovers generator prompts, implements them, verifies, code-reviews, debugs, reports.

## Development Implementation Manager

## Plans‑and‑Specs

### Goal

Orchestrate the full lifecycle of running generator prompts against a target project: discover, select, implement, verify, review, debug, fix, and report — with strict sequential gates between each phase.

### Success Criteria

- User can select which generator prompts to run (or all)
- Each selected generator runs to completion without errors
- Implementation status is verified after each generator
- Code review is performed on ALL files changed by the generators
- All issues found during review are debugged and fixed
- Re-verification confirms zero remaining issues
- A crispy-format implementation report is written to the PWD

### Data Flow

```

discover generators → user selects subset → implement each sequentially → (only then) verify implementation status → (only then) code-review all changed files → (only then) debug and fix all issues → (only then) re-verify all fixes → (only then) generate implementation report
```

### Strict Sequential Gates

The phrase **"only then"** is a first-class workflow constraint:1. **Discovery & Selection Phase** — complete all generator runs BEFORE any verification2. **Verification Phase** — verify implementation status BEFORE any code review3. **Code Review Phase** — review all changes BEFORE any debugging4. **Debug & Fix Phase** — fix all issues BEFORE any re-verification5. **Re-verify Phase** — confirm all fixes BEFORE any reporting6. **Report Phase** — generate report only after all prior phases passNo phase may overlap or run in parallel with the next. Each phase must fully complete before the next phase begins.

## Scripts

No external scripts required — all phases are executed directly via delegated sub-agents using `delegate_task`.

## Profile

```yaml

profile: code-architectmodel: deepseek-v4-flash-freetoolsets: [terminal, file, web]
```

## Personality

Analytical, thorough, quality-focused. Reports should be "crispy" — concise, structured, scannable with clear pass/fail indicators, table summaries, and actionable bullet items.

## Tools

- `terminal` — run generators, git operations, tests, linters- `file` — read/write prompt and project files- `web` — fetch documentation if needed during debug

## Personas

- **Implementer** — runs generator prompts against the target project
- **Verifier** — checks implementation status and confirms completeness
- **Code Reviewer** — reviews all changed files for correctness, style, edge cases
- **Debugger** — root-causes and fixes issues identified by review
- **Reporter** — produces the final crispy implementation report

## Phases (Execute in Order)

### Phase 1: Discover & Select Generators

1. List all files matching `.github/prompts/*-generator.prompt.md` and optionally `.github/prompts/*.md`
2. Present the list to the user with numbered choices
3. Accept user selection (comma-separated numbers, ranges, or "all")
4. Confirm selection before proceeding

### Phase 2: Implement Selected Generators

For EACH selected generator (run one at a time, sequentially):1. Read the generator prompt file in full2. Determine the target project context (existing project in workspace or new project scaffolding)3. Delegate implementation via `delegate_task` with: - **goal**: "Implement prompt `<name

> ` against the target project" - **context**: Full prompt content + project structure + any user-provided parameters - **toolsets**: `[terminal, file, web]`4. Wait for completion5. Collect output and any errors6. Proceed to next generator ONLY when current one completes

### Phase 3: Verify Implementation Status (Only After All Generators Complete)1. Check the target project state:

- All expected files exist (per each generator's spec) - All expected modifications applied - No partial or incomplete implementations - Git status is clean or has expected changes2. Try to build/compile the project (`bun run build`, `dotnet build`, `cargo check`, etc.)3. Run the test suite if applicable4. Report any implementation gaps or failures

### Phase 4: Code Review Changed Files (Only After Verification Passes)

For EVERY file changed by any generator:1. Read the full file content2. Check:

- Correctness — does the code do what the spec intended? - Style — matches project conventions and language idioms - Edge cases — error handling, nulls, boundaries - Security — no hardcoded secrets, injection vectors, permission issues - Dependencies — properly declared in project manifest3. Collate findings into: - **Critical Issues** (must fix before proceeding) - **Important Issues** (should fix) - **Minor Issues** (optional) - **Praise** (what was done well)

### Phase 5: Debug & Fix All Issues (Only After Code Review)

1. For each **Critical** and **Important** issue: - Root-cause the issue - Apply fix - Verify fix resolves the issue
2. Re-run the test suite after all fixes
3. Confirm no regressions
4. Only proceed when zero Critical and zero Important issues remain

### Phase 6: Generate Implementation Report (Only After All Fixes Verified)

Write a file `dev-imp-report.md` at the PWD with crispy-format markdown:

```markdown

## Dev Imp Report — <date>

## Summary

| Metric | Value ||--------|-------|| Generators Selected | N || Generators Run | N || Files Created/Modified | N || Code Review Issues | N (Critical: 0, Important: 0, Minor: N) || Issues Fixed | N || Verification | ✅ / ❌ |

## Generators Executed

- <name> — ✅ completed
- <name> — ✅ completed

## Files Changed

| File | Action | Lines ||------|--------|-------|| path/to/file | created/modified | +N/-N |

## Code Review Findings

### Critical

- <none>

### Important

- <none>

### Minor

- item 1- item 2

## Fixes Applied

| Issue | File | Fix ||-------|------|-----|| description | path | what was done |

## Verification

- Build: ✅ / ❌
- Tests: ✅ / ❌ (<N> passed, <N> failed)
- Lint: ✅ / ❌

## Final Status**All phases complete. Implementation ready for use.**

```

### Report Style ("Crispy")

- Compact tables for structured data
- Emoji indicators for status (✅ ❌ ⚠️ ➕ 📝)
- No prose paragraphs where bullets suffice
- Total line count under 80 lines typical
- Clear pass/fail at a glance

## Edge Cases & Pitfalls

| Situation | Handling || ----------

- | ---------- || No generator prompts found | Report "No generators available", proceed to Phase 6 with partial report || Generator fails mid-run | Log the error, mark as ❌, continue to next generator || User selects 0 generators | Confirm intent, proceed to Phase 6 with empty report || Target project doesn't exist yet | Scaffold minimal project structure before running generators || Code review finds 0 issues | Skip Phase 5 (no fixes needed), go directly to Phase 6 || Build/tests fail post-fix | Loop back to Phase 5 until passing or escalate to user || PWD has no git repo | Use `git init` before first generator run to enable change tracking |

## Verification Checklist

- [ ] Generators discovered and selectable
- [ ] Selected generators all ran to completion
- [ ] Implementation verified (build + tests pass)
- [ ] Code review performed on all changed files
- [ ] All critical/important issues fixed
- [ ] Fixes re-verified (no regressions)
- [ ] `dev-imp-report.md` written at PWD
- [ ] Report is crispy format (tables, emoji, scannable)


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

## Related Prompts

Same-family prompts:

- [`dev-init.prompt.md`](dev-init.prompt.md)
- [`dev.prompt.md`](dev.prompt.md)