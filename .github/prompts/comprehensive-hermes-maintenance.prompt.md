---
name: comprehensive-hermes-maintenance
title: Comprehensive Hermes Maintenance
description: "Create, execute, and verify a safe Hermes root-script quick-command and configuration maintenance plan."
trigger: /comprehensive-hermes-maintenance
version: 1.0.0
author: Alexa
tags: [hermes, implementation, scripts, quick-commands, config, verification]
profile: code-architect
priority: high
enabled: true
skills:
  - using-superpowers
  - brainstorming
  - user-communication-preferences
  - mcp-sequential-thinking
  - mcp-filesystem
  - mcp-ast-grep
  - mcp-memory
  - plans-and-specs
  - create-implementation-plan
  - implementation-plan
  - executing-plans
  - writing-clearly-and-concisely
  - subagent-driven-development
  - systematic-debugging
---

# Comprehensive Hermes Maintenance

## Goal

Deliver a tested, auditable quick-command registry for every first-party script in the Hermes scripts root, synchronize only the relevant `quick_commands` configuration block across active profiles, and document safe `.env` scope boundaries.

## Inputs

- Workspace: `C:/Users/Alexa/Desktop/SandBox`
- Hermes home: `C:/Users/Alexa/AppData/Local/hermes`
- Spec (active scope): `.hermes/specs/comprehensive-hermes-maintenance-spec.md`
- Plan (active scope): `.hermes/plans/comprehensive-hermes-maintenance-plan.md`
- Spec (quick-command focus, completed): `.hermes/specs/hermes-root-scripts-quick-commands-spec.md`
- Plan (quick-command focus, completed): `.hermes/plans/hermes-root-scripts-quick-commands-plan.md`

## Rules

1. Read repo guidance and live Hermes state before edits.
2. Use MCP filesystem, AST-grep, and sequential-thinking when available; fall back to native tools only when an MCP server is unavailable.
3. Discover scripts before generating commands. Exclude nested/vendor/generated files.
4. Do not execute target scripts during registry smoke tests. Invoke the safe wrapper's `audit` mode instead.
5. Use `hermes config set --force quick_commands <serialized-map>` for config writes; never hand-edit live `config.yaml`.
6. Preserve user commands and profile-specific settings.
7. Inventory `.env*` files without printing or copying values.
8. Stop on a failed verification gate; diagnose root cause before changing code.
9. Do not commit, push, delete, or create backups unless separately requested.

## Phases

### Phase 1 — Discovery (2 hours)

- Read `SESSION_REPORT.md`, repo guidance, and the linked spec/plan.
- Verify profile, MCP, hooks, and memory state.
- Inventory scripts, active config files, and `.env*` paths.
- Capture baseline script-judge and config results.

**Gate:** inventory is deterministic and scope exclusions are explicit.

### Phase 2 — Design (2 hours)

- Choose a wrapper-based, non-destructive command strategy.
- Define registry key normalization and collision handling.
- Define profile sync and `.env` key-name-only verification.
- Record risks, rollback, milestones, and resource allocation in the plan.

**Gate:** every requirement maps to an implementation and verification step.

### Phase 3 — Implementation (4–6 hours)

- Implement/update the registry auditor and comprehensive orchestrator.
- Install the tested wrapper in Hermes root scripts.
- Generate the canonical quick-command map while preserving existing entries.
- Update the scripts-judge skill and its executable judge checks.

**Gate:** local script unit/smoke checks pass before live config writes.

### Phase 4 — Live configuration (1–2 hours)

- Apply the quick-command map through the Hermes CLI.
- Repeat for each active profile, or use the supported profile sync mechanism for only this section.
- Read back each profile's quick-command map and compare structurally.

**Gate:** all active profiles agree on the managed block; no unrelated config drift.

### Phase 5 — Verification and handoff (2 hours)

- Run every generated wrapper command in audit mode.
- Run `.env` inventory/key-name checks.
- Run scripts-judge with registry coverage enabled.
- Run repo lint/typecheck/check/format commands.
- Update the plan with evidence, remaining warnings, and rollback instructions.

**Gate:** all acceptance criteria are evidenced or marked as an explicit environment blocker.

## Output contract

Return a concise report containing:

- discovered script count and registry count;
- profiles synchronized and structural comparison result;
- smoke-test pass/fail counts;
- `.env` scope findings without values;
- scripts-judge and repository gate results;
- exact paths of prompt, spec, plan, scripts, and skill changes;
- unresolved blockers, if any.
