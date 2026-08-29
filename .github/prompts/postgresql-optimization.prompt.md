---
name: postgresql-optimization
title: PostgreSQL Optimization
description: PostgreSQL-specific development assistant covering JSONB operations, array types, custom types, range/geometric types, full-text search, window functions, and the extensions ecosystem.
trigger: /postgresql-optimization
version: 1.0.0
author: Hermes Agent
tags:
  - postgresql
  - performance
  - optimization
  - database
  - sql
  - tuning
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
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [PostgreSQL-Specific Features](#postgresql-specific-features)
- [� PostgreSQL Performance Tuning>](#�-postgresql-performance-tuning>)
  - [Query Optimization](#query-optimization)
- [�️ PostgreSQL Advanced Data Types>](#�️-postgresql-advanced-data-types>)
  - [Custom Types & Domains](#custom-types-&-domains)
- [📊 PostgreSQL Extensions & Tools](#📊-postgresql-extensions-&-tools)
  - [Useful Extensions](#useful-extensions)
- [📊 Monitoring and Maintenance](#📊-monitoring-and-maintenance)
  - [Query Performance Monitoring](#query-performance-monitoring)
  - [Database Maintenance](#database-maintenance)
- [🛠️ Common Query Patterns](#🛠️-common-query-patterns)
- [📋 Optimization Checklist](#📋-optimization-checklist)
- [🎯 Optimization Output Format](#🎯-optimization-output-format)
  - [Query Analysis Results](#query-analysis-results)
- [Query Performance Analysis](#query-performance-analysis)
- [🚀 Advanced PostgreSQL Features](#🚀-advanced-postgresql-features)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand off](#phase-4:-hand-off)
- [PostgreSQL-Specific Features](#postgresql-specific-features)
- [� PostgreSQL Performance Tuning)](#�-postgresql-performance-tuning)
- [� PostgreSQL Performance Tuning>](#�-postgresql-performance-tuning>)
- [Query Optimization](#query-optimization)
- [�️ PostgreSQL Advanced Data Types)](#�️-postgresql-advanced-data-types)
- [�️ PostgreSQL Advanced Data Types>](#�️-postgresql-advanced-data-types>)
- [Custom Types & Domains](#custom-types-&-domains)
- [📊 PostgreSQL Extensions & Tools](#📊-postgresql-extensions-&-tools)
- [Useful Extensions](#useful-extensions)
- [📊 Monitoring and Maintenance](#📊-monitoring-and-maintenance)
- [Query Performance Monitoring](#query-performance-monitoring)
- [Database Maintenance](#database-maintenance)
- [🛠️ Common Query Patterns](#🛠️-common-query-patterns)
- [📋 Optimization Checklist](#📋-optimization-checklist)
- [🎯 Optimization Output Format](#🎯-optimization-output-format)
- [Query Analysis Results](#query-analysis-results)
- [Query Performance Analysis](#query-performance-analysis)
- [🚀 Advanced PostgreSQL Features](#🚀-advanced-postgresql-features)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





PostgreSQL-specific development assistant focusing on unique PostgreSQL features, advanced data types, and PostgreSQL-exclusive capabilities. Covers JSONB operations, array types, custom types, range/geometric types, full-text search, window functions, and PostgreSQL extensions ecosystem.


Use when optimizing PostgreSQL queries, data types, and database performance.

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

- Return the final artifact or findings .
- Stop once the requested result is delivered.

## PostgreSQL-Specific Features

> -- Advanced JSONB queries
> CREATE TABLE events (
>   id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
>   event_data JSONB NOT NULL,
>   created_at TIMESTAMP DEFAULT NOW()
> );

## � PostgreSQL Performance Tuning

### Query Optimization

> -
>
- EXPLAIN ANALYZE for performance analysis

## �️ PostgreSQL Advanced Data Types

### Custom Types & Domains

> -
>
- Create custom types

## 📊 PostgreSQL Extensions & Tools

### Useful Extensions

> -
>
- Enable commonly used extensions

## 📊 Monitoring and Maintenance

### Query Performance Monitoring

```
sql-- Identify slow queriesSELECT query, calls, total_time, mean_time, rowsFROM pg_stat_statementsORDER BY total_time DESCLIMIT 10;-- Check index usageSELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetchFROM pg_stat_user_indexesWHERE idx_scan = 0;
```

### Database Maintenance

- **VACUUM and ANALYZE**: Regular maintenance for performance
- **Index Maintenance**: Monitor and rebuild fragmented indexes
- **Statistics Updates**: Keep query planner statistics current
- **Log Analysis**: Regular review of PostgreSQL logs

## 🛠️ Common Query Patterns

> -- ❌ BAD: OFFSET for large datasets
> SELECT * FROM products ORDER BY id OFFSET 10000 LIMIT 20;
>
> -- ✅ GOOD: Keyset pagination
> SELECT * FROM products WHERE id > 10000 ORDER BY id LIMIT 20;
>
> -- ❌ BAD: SELECT in loop
> -- ✅ GOOD: Bulk operations with arrays/CTEs
> SELECT * FROM products WHERE id = ANY(ARRAY[1,2,3]);

## 📋 Optimization Checklist

> - [ ] Run EXPLAIN ANALYZE for expensive queries
> - [ ] Check for sequential scans on large tables
> - [ ] Review index usage with pg_stat_all_indexes
> - [ ] Monitor query performance with pg_stat_statements
> - [ ] Verify VACUUM and ANALYZE run on schedule

## 🎯 Optimization Output Format

### Query Analysis Results

````

## Query Performance Analysis

**Original Query**:
[Original SQL with performance issues]

**Issues Identified**:
- Sequential scan on large table (Cost: 15000.00)
- Missing index on frequently queried column
- Inefficient join order

**Optimized Query**:
[Improved SQL with explanations]

**Recommended Indexes**:
```sql
CREATE INDEX idx_table_column ON table(column);
````

**Performance Impact**: Expected 80% improvement in execution time

## 🚀 Advanced PostgreSQL Features

> -- Running totals and rankings
> SUM(amount) OVER (PARTITION BY product_id ORDER BY order_date) as running_total,
> -- Window functions for analytics
> ROW_NUMBER() OVER (PARTITION BY category ORDER BY score DESC) as rank_by_category,
> -- CTEs for readable complex queries
> WITH RECURSIVE org_tree AS (
>   SELECT id, name, manager_id FROM employees WHERE manager_id IS NULL
>   UNION ALL
>   SELECT e.id, e.name, e.manager_id FROM employees e JOIN org_tree ot ON e.manager_id = ot.id
> )

## Template References

Detailed templates in `templates/postgresql-optimization/`:- `advanced_postgresql_features.md`- `common_query_patterns.md`- `optimization_checklist.md`- `postgresql-specific_features.md`- `postgresql_advanced_data_types.md`- `postgresql_extensions__tools.md`- `postgresql_performance_tuning.md`

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

- [`postgresql-code-review.prompt.md`](postgresql-code-review.prompt.md)