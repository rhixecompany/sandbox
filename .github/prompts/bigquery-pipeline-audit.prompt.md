---
name: bigquery-pipeline-audit
title: BigQuery Pipeline Audit
description: Audit Python + BigQuery pipelines for cost exposure, dry-run safety, idempotency, backfill design, and observability — and report exact patch locations.
trigger: /bigquery-pipeline-audit
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
Audit Python + BigQuery pipelines for cost exposure, dry-run safety, idempotency, backfill design, and observability — and report exact patch locations.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [A) COST EXPOSURE: What will actually get billed?](#a-cost-exposure:-what-will-actually-get-billed?)
- [B) DRY RUN AND EXECUTION MODES](#b-dry-run-and-execution-modes)
- [C) BACKFILL AND LOOP DESIGN](#c-backfill-and-loop-design)
- [D) QUERY SAFETY AND SCAN SIZEFor each query, check:](#d-query-safety-and-scan-sizefor-each-query-check:)
- [E) SAFE WRITES AND IDEMPOTENCY](#e-safe-writes-and-idempotency)
- [F) OBSERVABILITY: Can you debug a failure?Verify:](#f-observability:-can-you-debug-a-failure?verify:)
- [Final](#final)
- [Template References](#template-references)
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
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)



- [Goal](#goal)
- [A) COST EXPOSURE: What will actually get billed?](#a-cost-exposure:-what-will-actually-get-billed?)
- [B) DRY RUN AND EXECUTION MODES](#b-dry-run-and-execution-modes)
- [C) BACKFILL AND LOOP DESIGN](#c-backfill-and-loop-design)
- [D) QUERY SAFETY AND SCAN SIZEFor each query, check:](#d-query-safety-and-scan-sizefor-each-query-check:)
- [E) SAFE WRITES AND IDEMPOTENCY](#e-safe-writes-and-idempotency)
- [F) OBSERVABILITY: Can you debug a failure?Verify:](#f-observability:-can-you-debug-a-failure?verify:)
- [Final](#final)
- [Template References](#template-references)
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
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)





Audits Python + BigQuery pipelines for cost safety, idempotency, and production readiness. Returns a structured report with exact patch locations.

## A) COST EXPOSURE: What will actually get billed?

Locate every BigQuery job trigger (`client.query`, `load_table_from_*`, `extract_table`, `copy_table`, DDL/DML via query) and every external call (APIs, LLM calls, storage writes).For each, answer:

- Is this inside a loop, retry block, or async gather?- What is the realistic worst-case call count?- For each `client.query`, is `QueryJobConfig.maximum_bytes_billed` set? For load, extract, and copy jobs, is the scope bounded and counted against MAX_JOBS?- Is the same SQL and params being executed more than once in a single run? Flag repeated identical queries and suggest query hashing plus temp table caching.**Flag immediately if:**- Any BQ query runs once per date or once per entity in a loop- Worst-case BQ job count exceeds 20- `maximum_bytes_billed` is missing on any `client.query` call---

## B) DRY RUN AND EXECUTION MODES

Verify a `--mode` flag exists with at least `dry_run` and `execute` options.

- `dry_run` must print the plan and estimated scope with zero billed BQ execution (BigQuery dry-run estimation via job config is allowed) and zero external API or LLM calls- `execute` requires explicit confirmation for prod (`--env=prod --confirm`)- Prod must not be the default environmentIf missing, propose a minimal `argparse` patch with safe defaults.---

## C) BACKFILL AND LOOP DESIGN

**Hard fail if:** the script runs one BQ query per date or per entity in a loop.Check that date-range backfills use one of:1. A single set-based query with `GENERATE_DATE_ARRAY`2. A staging table loaded with all dates then one join query3. Explicit chunks with a hard `MAX_CHUNKS` capAlso check:- Is the date range bounded by default (suggest 14 days max without `--override`)?- If the script crashes mid-run, is it safe to re-run without double-writing?- For backdated simulations, verify data is read from time-consistent snapshots (`FOR SYSTEM_TIME AS OF`, partitioned as-of tables, or dated snapshot tables). Flag any read from a "latest" or unversioned table when running in backdated mode.Suggest a concrete rewrite if the current approach is row-by-row.---

## D) QUERY SAFETY AND SCAN SIZEFor each query, check:

- **Partition filter** is on the raw column, not `DATE(ts)`, `CAST(...)`, or any function that prevents pruning- **No `SELECT *`**: only columns actually used downstream- **Joins will not explode**: verify join keys are unique or appropriately scoped and flag any potential many-to-many- **Expensive operations** (`REGEXP`, `JSON_EXTRACT`, UDFs) only run after partition filtering, not on full table scansProvide a specific SQL fix for any query that fails these checks.---

## E) SAFE WRITES AND IDEMPOTENCY

Identify every write operation. Flag plain `INSERT`/append with no dedup logic.

> ) = 1`Also check:- Will a re-run create duplicate rows?- Is the write disposition (`WRITE_TRUNCATE` vs `WRITE_APPEND`) intentional and documented?- Is`run_id` being used as part of the merge or dedupe key? If so, flag it. `run_id` should be stored as a metadata column, not as part of the uniqueness key, unless you explicitly want multi-run history.State the recommended approach and the exact dedup key for this codebase.---

## F) OBSERVABILITY: Can you debug a failure?Verify:

- Failures raise exceptions and abort with no silent `except: pass` or warn-only- Each BQ job logs: job ID, bytes processed or billed when available, slot milliseconds, and duration- A run summary is logged or written at the end containing: `run_id, env, mode, date_range, tables written, total BQ jobs, total bytes`- `run_id` is present and consistent across all log linesIf `run_id` is missing, propose a one-line fix: `run_id = run_id or datetime.utcnow().strftime('%Y%m%dT%H%M%S')`---

## Final

**1. PASS / FAIL** with specific reasons per section (A to F). **2. Patch list** ordered by risk, referencing exact functions to change. **3. If FAIL: Top 3 cost risks** with a rough worst-case estimate (e.g., "loop over 90 dates x 3 retries = 270 BQ jobs").

## Template References

Templates in `templates/bigquery-pipeline-audit/`:- `a_cost_exposure_what_will.md`- `c_backfill_and_loop_desig.md`- `e_safe_writes_and_idempot.md`

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

## Workflow

<content>

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section
```
# Prompt template
Execute the workflow defined in this file.
```
