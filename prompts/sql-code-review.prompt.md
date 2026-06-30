---
toolsets: ["changes", "search/codebase", "edit/editFiles", "problems"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: SQL Code Review
name: sql-code-review
description: "Universal SQL code review assistant that performs comprehensive security, maintainability, and code quality analysis across all SQL databases (MySQL, PostgreSQL, SQL Server, Oracle). Focuses on SQL injection prevention, access control, code standards, and anti-pattern detection. Complements SQL optimization prompt for complete development coverage."
tested_with: "GitHub Copilot Chat (GPT-4o) - Validated July 20, 2025"
tags:
  - audit
  - backend
  - data
  - database
  - ml
  - prompts
  - security
  - sql
  - typescript
  - code-quality
  - code-review
  - database
  - documentation
  - drizzle
  - linting
  - performance
  - security
  - sql
metadata:
  hermes:
    related_skills: []
    tags:
    - sql-code-review.prompt

trigger: sql-code-review

---
metadata:
  hermes:
    related_skills: []
    tags:
    - sql-code-review.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - sql-code-review.prompt

## Goal

Universal SQL code review assistant that performs comprehensive security, maintainability, and code quality analysis across all SQL databases (MySQL, PostgreSQL, SQL Server, Oracle). Focuses on SQL injection prevention, access control, code standards, and anti-pattern detection. Complements SQL optimization prompt for complete development coverage.

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

## 🔒 Security Analysis

> ### SQL Injection Prevention
> -- ❌ CRITICAL: SQL Injection vulnerability

> **Full content:** `templates/sql-code-review/security_analysis.md`

## ⚡ Performance Optimization

> ### Query Structure Analysis
> -- ❌ BAD: Inefficient query patterns

> **Full content:** `templates/sql-code-review/performance_optimization.md`

## 🛠️ Code Quality & Maintainability

> ### SQL Style & Formatting
> -- ❌ BAD: Poor formatting and style

> **Full content:** `templates/sql-code-review/code_quality__maintainability.md`

## 🗄️ Database-Specific Best Practices

> -- Use JSONB for JSON data
> CREATE TABLE events (

> **Full content:** `templates/sql-code-review/database-specific_best_practic.md`

## 🧪 Testing & Validation

### Data Integrity Checks

```sql
-- Verify referential integrity
SELECT o.user_id
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;

-- Check for data consistency
SELECT COUNT(*) as inconsistent_records
FROM products
WHERE price < 0 OR stock_quantity < 0;
```

### Performance Testing

- **Execution Plans**: Review query execution plans
- **Load Testing**: Test queries with realistic data volumes
- **Stress Testing**: Verify performance under concurrent load
- **Regression Testing**: Ensure optimizations don't break functionality

## 📊 Common Anti-Patterns

> ### N+1 Query Problem
> -- ❌ BAD: N+1 queries in application code

> **Full content:** `templates/sql-code-review/common_anti-patterns.md`

## 📋 SQL Review Checklist

> - [ ] All user inputs are parameterized
> - [ ] No dynamic SQL construction with string concatenation

> **Full content:** `templates/sql-code-review/sql_review_checklist.md`

## 🎯 Review Output Format

### Issue Template

````
## [PRIORITY] [CATEGORY]: [Brief Description]

> **Location**: [Table/View/Procedure name and line number if applicable]
> **Issue**: [Detailed explanation of the problem]

> **Full content:** `templates/sql-code-review/priority_category_brief_descri.md`

## Template References

Detailed templates in `templates/sql-code-review/`:
- `code_quality__maintainability.md`
- `common_anti-patterns.md`
- `database-specific_best_practic.md`
- `performance_optimization.md`
- `priority_category_brief_descri.md`
- `security_analysis.md`
- `sql_review_checklist.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
