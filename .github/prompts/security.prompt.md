---
name: security
title: Security Review
description: 'Comprehensive prompt for security review, vulnerability assessment, and secure coding practices.'
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
  - api
  - architecture
  - audit
  - data
  - documentation
  - frontend
  - prompts
  - security
  - skills
  - typescript
trigger: /security
dependencies: []
metadata:
  hermes: {}
---
## GoalUse when "Comprehensive security prompt aligned to repository secure development requirements." to accomplish the associated tasks and objectives.

## DescriptionApply secure-by-default engineering practices to code and documentation updates, with explicit handling for secrets, input validation, and least-privilege design.

## ContextUse this prompt for any change that handles external input, authentication, authorization, secrets, APIs, or data persistence.

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)- Threat modeling and trust-boundary analysis- Input validation and secure coding patterns- Secret management and least-privilege architecture

## Subagents| Subagent | Role | When to Use || --- | --- | --- || Security Reviewer | Detects vulnerabilities and misuse of trust boundaries | Always || Validation Specialist | Enforces schema and sanitization controls | External input paths || Secret Auditor | Checks secret handling and environment safety | Config and deployment changes |

## Personas- Security Reviewer: Assumes input is hostile until validated.- Validation Specialist: Requires strict schemas and typed boundaries.- Secret Auditor: Blocks secret leakage and over-privileged access patterns.

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Never commit secrets or sensitive values in code, docs, or examples.- Validate and sanitize all external inputs.- Enforce least privilege in service and credential usage.- Add logging and monitoring guidance for suspicious or failed auth events.- Keep dependencies current and note known CVE implications.

## Phases>

### Phase 1: Threat Surface Identification>>

### Phase 2: Security Control Implementation> **Full content:** `templates/security/phases.md`

## Steps1. Map data flows and trust boundaries.2. Validate and sanitize external input paths.3. Enforce auth, authorization, and least-privilege controls.4. Verify secret handling and dependency hygiene.5. Report findings and residual risks.

## Tasks- Task 1.1 — Identify sensitive flows and security-critical boundaries.- Task 1.2 — Enforce strict input validation and sanitization.- Task 1.3 — Verify authentication and authorization correctness.- Task 1.4 — Check secret management and dependency risk posture.- Task 1.5 — Document mitigations and unresolved security risks.

## Subtasks- Subtask 1.1.1 — List entry points receiving untrusted input.- Subtask 1.2.1 — Apply schema validation at boundary layers.- Subtask 1.3.1 — Confirm permission checks precede sensitive actions.- Subtask 1.4.1 — Ensure secrets are not present in source-controlled files.- Subtask 1.5.1 — Provide actionable remediation for remaining risks.

## Actions Summary1. Identify security-sensitive paths.2. Harden validation and authorization.3. Verify secrets and dependency safety.4. Deliver a risk-focused security outcome.

## Template ReferencesTemplates in `templates/security/`:- `phases.md`

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

Comprehensive prompt for security review, vulnerability assessment, and secure coding practices.


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


