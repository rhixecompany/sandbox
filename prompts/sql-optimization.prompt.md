---
toolsets: ["changes", "search/codebase", "edit/editFiles", "problems"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: SQL Performance Optimization Assistant
name: sql-optimization
description: "Universal SQL performance optimization assistant for comprehensive query tuning, indexing strategies, and database performance analysis across all SQL databases (MySQL, PostgreSQL, SQL Server, Oracle). Provides execution plan analysis, pagination optimization, batch operations, and performance monitoring guidance."
tested_with: "GitHub Copilot Chat (GPT-4o) - Validated July 20, 2025"
tags:
  - backend
  - data
  - database
  - frontend
  - performance
  - prompts
  - specification
  - sql
  - typescript
  - database
  - documentation
  - drizzle
  - performance
  - planning
  - specification
  - sql
metadata:
  hermes:
    related_skills: []
    tags:
    - sql-optimization.prompt

trigger: sql-optimization

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - sql-optimization.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - sql-optimization.prompt

## Goal

Universal SQL performance optimization assistant for comprehensive query tuning, indexing strategies, and database performance analysis across all SQL databases (MySQL, PostgreSQL, SQL Server, Oracle). Provides execution plan analysis, pagination optimization, batch operations, and performance monitoring guidance.

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
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


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

## 🎯 Core Optimization Areas

> ### Query Performance Analysis
> -- ❌ BAD: Inefficient query patterns

> **Full content:** `templates/sql-optimization/core_optimization_areas.md`

## 📊 Performance Tuning Techniques

> ### JOIN Optimization
> -- ❌ BAD: Inefficient JOIN order and conditions

> **Full content:** `templates/sql-optimization/performance_tuning_techniques.md`

## 🔍 Query Anti-Patterns

> ### SELECT Performance Issues
> -- ❌ BAD: SELECT * anti-pattern

> **Full content:** `templates/sql-optimization/query_anti-patterns.md`

## 📈 Database-Agnostic Optimization

> -- ❌ BAD: Row-by-row operations
> INSERT INTO products (name, price) VALUES ('Product 1', 10.00);

> **Full content:** `templates/sql-optimization/database-agnostic_optimization.md`

## 🛠️ Index Management

### Index Design Principles

```sql
-- ✅ GOOD: Covering index design
CREATE INDEX idx_orders_covering
ON orders(customer_id, created_at)
INCLUDE (total_amount, status);  -- SQL Server syntax
-- Or: CREATE INDEX idx_orders_covering ON orders(customer_id, created_at, total_amount, status); -- Other databases
```

### Partial Index Strategy

```sql
-- ✅ GOOD: Partial indexes for specific conditions
CREATE INDEX idx_orders_active
ON orders(created_at)
WHERE status IN ('pending', 'processing');
```

## 📊 Performance Monitoring Queries

### Query Performance Analysis

```sql
-- Generic approach to identify slow queries
-- (Specific syntax varies by database)

-- For MySQL:
SELECT query_time, lock_time, rows_sent, rows_examined, sql_text
FROM mysql.slow_log
ORDER BY query_time DESC;

-- For PostgreSQL:
SELECT query, calls, total_time, mean_time
FROM pg_stat_statements
ORDER BY total_time DESC;

-- For SQL Server:
SELECT
    qs.total_elapsed_time/qs.execution_count as avg_elapsed_time,
    qs.execution_count,
    SUBSTRING(qt.text, (qs.statement_start_offset/2)+1,
        ((CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(qt.text)
        ELSE qs.statement_end_offset END - qs.statement_start_offset)/2)+1) as query_text
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) qt
ORDER BY avg_elapsed_time DESC;
```

## 🎯 Universal Optimization Checklist

> - [ ] Avoiding SELECT \* in production queries
> - [ ] Using appropriate JOIN types (INNER vs LEFT/RIGHT)

> **Full content:** `templates/sql-optimization/universal_optimization_checkli.md`

## 📝 Optimization Methodology

1. **Identify**: Use database-specific tools to find slow queries
2. **Analyze**: Examine execution plans and identify bottlenecks
3. **Optimize**: Apply appropriate optimization techniques
4. **Test**: Verify performance improvements
5. **Monitor**: Continuously track performance metrics
6. **Iterate**: Regular performance review and optimization

Focus on measurable performance improvements and always test optimizations with realistic data volumes and query patterns.


## Template References

Detailed templates in `templates/sql-optimization/`:
- `core_optimization_areas.md`
- `database-agnostic_optimization.md`
- `performance_tuning_techniques.md`
- `query_anti-patterns.md`
- `universal_optimization_checkli.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
