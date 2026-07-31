---

name: sql-code-review

title: SQL Code Review

description: 'Universal SQL code review assistant that performs comprehensive security, maintainability, and code quality analysis across all SQL databases (MySQL, PostgreSQL, SQL Server, Oracle). Focuses on SQL injection prevention, access control, code standards, and anti-pattern detection. Complements SQL optimization prompt for complete development coverage.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - terminal

  - file

scripts: []

skills: []

formatter: default

plan: None

tags:

  - audit

  - backend

  - data

  - database

  - ml

  - prompts

  - security

  - specification

  - sql

  - typescript

trigger: /sql-code-review

tested_with: 'GitHub Copilot Chat (GPT-4o) - Validated July 20, 2025'

dependencies: []

metadata:

  hermes: {}

---

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

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

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

### SQL Injection Prevention

> -- ❌ CRITICAL: SQL Injection vulnerability

## ⚡ Performance Optimization

### Query Structure Analysis

> -- ❌ BAD: Inefficient query patterns

## 🛠️ Code Quality & Maintainability

### SQL Style & Formatting

> -- ❌ BAD: Poor formatting and style

## 🗄️ Database-Specific Best Practices

> -- Use JSONB for JSON data
> CREATE TABLE events (
> **Full content:**

## 🧪 Testing & Validation

### Data Integrity Checks

```
sql-- Verify referential integritySELECT o.user_idFROM orders oLEFT JOIN users u ON o.user_id = u.idWHERE u.id IS NULL;-- Check for data consistencySELECT COUNT(*) as inconsistent_recordsFROM productsWHERE price < 0 OR stock_quantity < 0;
```

### Performance Testing

- **Execution Plans**: Review query execution plans
- **Load Testing**: Test queries with realistic data volumes
- **Stress Testing**: Verify performance under concurrent load
- **Regression Testing**: Ensure optimizations don't break functionality

## 📊 Common Anti-Patterns

### N+1 Query Problem

> -- ❌ BAD: N+1 queries in application code

## 📋 SQL Review Checklist

> - [ ] All user inputs are parameterized
> - [ ] No dynamic SQL construction with string concatenation
> **Full content:**

## 🎯 Review Output Format

### Issue Template

````

## [PRIORITY] [CATEGORY]: [Brief Description]

> **Location**: [Table/View/Procedure name and line number if applicable]
> **Issue**: [Detailed explanation of the problem]
> **Full content:**

## Template References

Detailed templates in `templates/sql-code-review/`:- `code_quality__maintainability.md`- `common_anti-patterns.md`- `database-specific_best_practic.md`- `performance_optimization.md`- `priority_category_brief_descri.md`- `security_analysis.md`- `sql_review_checklist.md`

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
|---|------|-----------|
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

