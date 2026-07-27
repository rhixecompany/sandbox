---
name: postgresql-code-review
title: PostgreSQL Code Review Assistant
description: PostgreSQL-specific code review assistant focusing on PostgreSQL best practices, anti-patterns,
  and unique quality standards. Covers JSONB operations, array usage, custom types,
  schema design, function optimization, and PostgreSQL-exclusive security features
  like Row Level Security (RLS).
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - terminal
  - file
scripts: []
skills: []
formatter: default
plan: ''
tags:
  - architecture
  - audit
  - database
  - prompts
  - security
  - specification
  - sql
  - typescript
trigger: /postgresql-code-review
tested_with: GitHub Copilot Chat (GPT-4o) - Validated July 20, 2025
---

## GoalPostgreSQL-specific code review assistant focusing on PostgreSQL best practices, anti-patterns, and unique quality standards. Covers JSONB operations, array usage, custom types, schema design, function optimization, and PostgreSQL-exclusive security features like Row Level Security (RLS).## ContextUse when you need to work on the current workspace or task.## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.## Phases### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.## 🎯 PostgreSQL-Specific Review Areas> ### JSONB Best Practices>> -- ❌ BAD: Inefficient JSONB usage> **Full content:** `templates/postgresql-code-review/postgresql-specific_review_are.md`## 🔍 PostgreSQL-Specific Anti-Patterns> ### Performance Anti-Patterns>> - **Avoiding PostgreSQL-specific indexes**: Not using GIN/GiST for appropriate d> **Full content:** `templates/postgresql-code-review/postgresql-specific_anti-patte.md`## 📊 PostgreSQL Extension Usage Review### Extension Best Practices```sql-- ✅ Check if extension exists before creatingCREATE EXTENSION IF NOT EXISTS "uuid-ossp";CREATE EXTENSION IF NOT EXISTS "pgcrypto";CREATE EXTENSION IF NOT EXISTS "pg_trgm";-- ✅ Use extensions appropriately-- UUID generationSELECT uuid_generate_v4();-- Password hashingSELECT crypt('password', gen_salt('bf'));-- Fuzzy text matchingSELECT word_similarity('postgres', 'postgre');```## 🛡️ PostgreSQL Security Review### Row Level Security (RLS)```sql-- ✅ GOOD: Implementing RLSALTER TABLE sensitive_data ENABLE ROW LEVEL SECURITY;CREATE POLICY user_data_policy ON sensitive_data    FOR ALL TO application_role    USING (user_id = current_setting('app.current_user_id')::INTEGER);```### Privilege Management```sql-- ❌ BAD: Overly broad permissionsGRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_user;-- ✅ GOOD: Granular permissionsGRANT SELECT, INSERT, UPDATE ON specific_table TO app_user;GRANT USAGE ON SEQUENCE specific_table_id_seq TO app_user;```## 🎯 PostgreSQL Code Quality Checklist> - [ ] Using appropriate PostgreSQL data types (CITEXT, JSONB, arrays)> - [ ] Leveraging ENUM types for constrained values> **Full content:** `templates/postgresql-code-review/postgresql_code_quality_checkl.md`## 📝 PostgreSQL-Specific Review Guidelines1. **Data Type Optimization**: Ensure PostgreSQL-specific types are used appropriately2. **Index Strategy**: Review index types and ensure PostgreSQL-specific indexes are utilized3. **JSONB Structure**: Validate JSONB schema design and query patterns4. **Function Quality**: Review PL/pgSQL functions for efficiency and best practices5. **Extension Usage**: Verify appropriate use of PostgreSQL extensions6. **Performance Features**: Check utilization of PostgreSQL's advanced features7. **Security Implementation**: Review PostgreSQL-specific security featuresFocus on PostgreSQL's unique capabilities and ensure the code leverages what makes PostgreSQL special rather than treating it as a generic SQL database.## Template ReferencesDetailed templates in `templates/postgresql-code-review/`:- `postgresql-specific_anti-patte.md`- `postgresql-specific_review_are.md`- `postgresql_code_quality_checkl.md`