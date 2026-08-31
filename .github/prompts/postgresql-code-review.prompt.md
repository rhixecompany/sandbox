---
name: postgresql-code-review
title: PostgreSQL Code Review
description: PostgreSQL-specific code review focused on JSONB operations, array usage, custom types, function optimization, and Row Level Security best practices.
trigger: /postgresql-code-review
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
PostgreSQL-specific code review focused on JSONB operations, array usage, custom types, function optimization, and Row Level Security best practices.

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
- [🎯 PostgreSQL-Specific Review Areas](#🎯-postgresql-specific-review-areas)
  - [JSONB Best Practices](#jsonb-best-practices)
- [🔍 PostgreSQL-Specific Anti-Patterns](#🔍-postgresql-specific-anti-patterns)
  - [Performance Anti-Patterns](#performance-anti-patterns)
- [📊 PostgreSQL Extension Usage Review](#📊-postgresql-extension-usage-review)
  - [Extension Best Practices](#extension-best-practices)
- [🛡️ PostgreSQL Security Review](#🛡️-postgresql-security-review)
  - [Row Level Security (RLS)](#row-level-security-rls)
  - [Privilege Management](#privilege-management)
- [🎯 PostgreSQL Code Quality Checklist](#🎯-postgresql-code-quality-checklist)
- [📝 PostgreSQL-Specific Review Guidelines](#📝-postgresql-specific-review-guidelines)
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
- [🎯 PostgreSQL-Specific Review Areas](#🎯-postgresql-specific-review-areas)
- [JSONB Best Practices](#jsonb-best-practices)
- [🔍 PostgreSQL-Specific Anti-Patterns](#🔍-postgresql-specific-anti-patterns)
- [Performance Anti-Patterns](#performance-anti-patterns)
- [📊 PostgreSQL Extension Usage Review](#📊-postgresql-extension-usage-review)
- [Extension Best Practices](#extension-best-practices)
- [🛡️ PostgreSQL Security Review](#🛡️-postgresql-security-review)
- [Row Level Security (RLS)](#row-level-security-rls)
- [Privilege Management](#privilege-management)
- [🎯 PostgreSQL Code Quality Checklist](#🎯-postgresql-code-quality-checklist)
- [📝 PostgreSQL-Specific Review Guidelines](#📝-postgresql-specific-review-guidelines)
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





PostgreSQL-specific code review assistant focusing on PostgreSQL best practices, anti-patterns, and unique quality standards. Covers JSONB operations, array usage, custom types, schema design, function optimization, and PostgreSQL-exclusive security features like Row Level Security (RLS).


Use when performing PostgreSQL-specific code reviews covering JSONB, arrays, custom types, and RLS.

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

## 🎯 PostgreSQL-Specific Review Areas

### JSONB Best Practices

> -- ❌ BAD: Inefficient JSONB usage

## 🔍 PostgreSQL-Specific Anti-Patterns

### Performance Anti-Patterns

> - **Avoiding PostgreSQL-specific indexes**: Not using GIN/GiST for appropriate d

## 📊 PostgreSQL Extension Usage Review

### Extension Best Practices

```
sql-- ✅ Check if extension exists before creatingCREATE EXTENSION IF NOT EXISTS "uuid-ossp";CREATE EXTENSION IF NOT EXISTS "pgcrypto";CREATE EXTENSION IF NOT EXISTS "pg_trgm";-- ✅ Use extensions appropriately-- UUID generationSELECT uuid_generate_v4();-- Password hashingSELECT crypt('password', gen_salt('bf'));-- Fuzzy text matchingSELECT word_similarity('postgres', 'postgre');
```

## 🛡️ PostgreSQL Security Review

### Row Level Security (RLS)

```
sql-- ✅ GOOD: Implementing RLSALTER TABLE sensitive_data ENABLE ROW LEVEL SECURITY;CREATE POLICY user_data_policy ON sensitive_data FOR ALL TO application_role USING (user_id = current_setting('app.current_user_id')::INTEGER);
```

### Privilege Management

```
sql-- ❌ BAD: Overly broad permissionsGRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;-- ✅ GOOD: Granular permissionsGRANT SELECT, INSERT, UPDATE ON specific_table TO app_user;GRANT USAGE ON SEQUENCE specific_table_id_seq TO app_user;
```

## 🎯 PostgreSQL Code Quality Checklist

> - [ ] Using appropriate PostgreSQL data types (CITEXT, JSONB, arrays)
> - [ ] Leveraging ENUM types for constrained values
> - [ ] Using GIN/GiST indexes for JSONB and array columns
> - [ ] Implementing Row Level Security where appropriate
> - [ ] Avoiding SELECT * in production queries

## 📝 PostgreSQL-Specific Review Guidelines

1. **Data Type Optimization**: Ensure PostgreSQL-specific types are used appropriately2. **Index Strategy**: Review index types and ensure PostgreSQL-specific indexes are utilized3. **JSONB Structure**: Validate JSONB schema design and query patterns4. **Function Quality**: Review PL/pgSQL functions for efficiency and best practices5. **Extension Usage**: Verify appropriate use of PostgreSQL extensions6. **Performance Features**: Check utilization of PostgreSQL's advanced features7. **Security Implementation**: Review PostgreSQL-specific security featuresFocus on PostgreSQL's unique capabilities and ensure the code leverages what makes PostgreSQL special rather than treating it as a generic SQL database.

## Template References

Detailed templates in `templates/postgresql-code-review/`:- `postgresql-specific_anti-patte.md`- `postgresql-specific_review_are.md`- `postgresql_code_quality_checkl.md`

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

## Workflow

<content>

Same-family prompts:

- [`postgresql-optimization.prompt.md`](postgresql-optimization.prompt.md)