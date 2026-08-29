---
name: hermes-doctor-systematic-debugging
title: Hermes Doctor and Systematic Remediation
description: Diagnoses, fixes, and verifies all actionable Hermes Agent issues, warnings, and errors using the live installation.
trigger: /hermes-doctor-systematic-debugging
version: 1.0.0
author: Hermes Agent
date: '2026-08-25'
tags:
  - hermes
  - debugging
  - doctor
  - remediation
  - diagnostics
  - automation
  - agent
  - platform
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
- [Scope](#scope)
- [Non-Negotiable Rules](#non-negotiable-rules)
- [Phase 1 — Establish Runtime Context](#phase-1-—-establish-runtime-context)
- [Phase 2 — Required Diagnostic Sequence](#phase-2-—-required-diagnostic-sequence)
- [Phase 3 — Systematic Root-Cause Investigation](#phase-3-—-systematic-root-cause-investigation)
- [Phase 4 — Remediation](#phase-4-—-remediation)
- [Phase 5 — Full Verification](#phase-5-—-full-verification)
- [Failure Handling](#failure-handling)
- [Completion Report](#completion-report)
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
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Scope](#scope)
- [Non-Negotiable Rules](#non-negotiable-rules)
- [Phase 1 — Establish Runtime Context](#phase-1-—-establish-runtime-context)
- [Phase 2 — Required Diagnostic Sequence](#phase-2-—-required-diagnostic-sequence)
- [Phase 3 — Systematic Root-Cause Investigation](#phase-3-—-systematic-root-cause-investigation)
- [Phase 4 — Remediation](#phase-4-—-remediation)
- [Phase 5 — Full Verification](#phase-5-—-full-verification)
- [Failure Handling](#failure-handling)
- [Completion Report](#completion-report)
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
- [Related Prompts](#related-prompts)





Diagnose, fix, and verify all actionable Hermes Agent issues, warnings, and errors using the live installation. Do not stop at a report: complete the remediation loop or report a precise external blocker.

## Scope

The required diagnostic sequence is:

```bash
hermes doctor && hermes doctor --fix && hermes status && hermes insights && hermes logs list && hermes logs errors && hermes logs desktop && hermes logs gateway && hermes logs gui && hermes logs agent
```

The sequence must run in this order. Each command is a gate: do not continue after a non-zero exit until the failure is understood and handled.

## Non-Negotiable Rules

1. Follow systematic-debugging: root-cause investigation before remediation.
2. Capture complete command output to a temporary, non-repository diagnostic file; do not dump unbounded logs into the conversation.
3. Never print or commit secrets, tokens, OAuth values, cookies, or personal message contents. Redact before reporting.
4. `hermes doctor --fix` authorized this prompt, but review the preceding `hermes doctor` findings first.
5. Make one logically independent fix at a time. Re-run the smallest relevant check after each fix.
6. Do not edit `config.yaml` directly. Use Hermes CLI commands for Hermes configuration changes.
7. Do not delete logs or session history. Archive only if explicitly required and reversible.
8. Do not modify unrelated workspace projects.
9. If the same remediation fails twice, stop retrying and form a new hypothesis.
10. If three independent fixes fail, stop and report an architectural or installation-level blocker.

## Phase 1 — Establish Runtime Context

Run and record:

```bash
hermes profile list
hermes config path
hermes config env-path
hermes config check
hermes mcp list
```

Record the active profile, model/provider, config path, enabled MCP servers, OS/shell, and current workspace. Use live command output; do not trust stale reports.

## Phase 2 — Required Diagnostic Sequence

Run the requested sequence exactly, with output captured safely:

```bash
hermes doctor
hermes doctor --fix
hermes status
hermes insights
hermes logs list
hermes logs errors
hermes logs desktop
hermes logs gateway
hermes logs gui
hermes logs agent
```

For each command record:

| Field | Required |
| ------------------ | ------------- |
| Exit code | Yes |
| Errors | Yes, redacted |
| Warnings | Yes, redacted |
| Auto-fixes | Yes |
| Affected component | Yes |
| Evidence path/line | Yes |

Use bounded output where supported (`-n`, `--since`) for follow-up inspection. Never use `-f`/follow mode in an automated workflow.

## Phase 3 — Systematic Root-Cause Investigation

For every warning or error:

1. Read the complete message and any traceback.
2. Classify it as configuration, dependency, authentication, MCP, profile, session store, gateway, desktop/GUI, logging, permissions, or unrelated historical noise.
3. Reproduce with the narrowest command.
4. Check recent changes:

```bash
git status --short
git log --oneline -10
```

1. Trace the failing component to its source file/config key/log producer.
2. Compare with a working sibling component or profile.
3. State one hypothesis: “I think X is the root cause because Y.”
4. Test the hypothesis with one minimal, reversible change.

Do not classify a log line as an active issue solely because it contains the word `error`; distinguish historical entries from current failures using timestamps and a fresh reproduction.

## Phase 4 — Remediation

Apply the smallest root-cause fix:

- Hermes config: `hermes config set ...`, `hermes mcp ...`, or the documented Hermes CLI command.
- Authentication: use `hermes auth` or the client’s OAuth flow; never write literal credentials.
- MCP: use `hermes mcp test <name>`, then correct server config through Hermes CLI.
- Profiles: use `hermes profile ...`; preserve profile isolation.
- Logs: fix the producer/rotation/configuration issue; do not erase evidence.
- Dependencies: verify the installed package/runtime before changing versions.
- Source code: edit only when the root cause is confirmed and the relevant repository is in scope.

After each fix, run the targeted verification immediately. If it passes, proceed to the next issue. If it fails, return to Phase 3 with the new evidence.

## Phase 5 — Full Verification

Re-run the complete sequence after remediation:

```bash
hermes doctor
hermes doctor --fix
hermes status
hermes insights
hermes logs list
hermes logs errors
hermes logs desktop
hermes logs gateway
hermes logs gui
hermes logs agent
hermes config check
hermes mcp list
```

Completion requires:

- No new non-zero exit codes.
- No unresolved actionable doctor findings.
- No recurring active warnings/errors introduced by the fixes.
- Status reports healthy or explains non-actionable external services.
- Insights completes without traceback.
- All expected log targets are readable or their absence is documented as non-actionable.
- MCP servers remain connected and enabled.
- No secrets appear in captured artifacts or the final report.

## Failure Handling

| Failure | Response |
| -------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `doctor` fails | Stop before `--fix`; investigate the exact failure |
| `doctor --fix` changes state but remains unhealthy | Re-run doctor, isolate the remaining finding, then fix one issue |
| Log target missing | Verify with `hermes logs list`; classify as absent/non-applicable versus broken logging |
| Permission or file-lock error on Windows | Identify the locking process and rotation path; do not delete the locked file |
| OAuth/API failure | Re-authenticate through the supported Hermes flow; never request a pasted key |
| Existing unrelated workspace changes | Preserve them; do not reset or overwrite |
| Tool/runtime unavailable | Report the exact command, path, exit code, and blocker |

## Completion Report

Return a compact evidence table:

| Component | Initial state | Root cause | Fix | Final verification |
| --------------- | ------------- | ---------- | --- | ------------------ |
| Doctor | | | | |
| Status | | | | |
| Insights | | | | |
| Logs | | | | |
| MCP | | | | |
| Profiles/config | | | | |

Also report:

- Prompt path
- Exact commands executed
- Files changed, if any
- Remaining non-actionable warnings
- Remaining blockers with exact evidence
- Whether a Hermes restart or `/reset` is required

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------------- | -------------------------------------- |
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
| - | ---------- | ----------------------------------- |
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
| -------------------------------- | ----------------------------- |
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

- [`hermes-breakdown-epic-arch.prompt.md`](hermes-breakdown-epic-arch.prompt.md)
- [`hermes-breakdown-epic-pm.prompt.md`](hermes-breakdown-epic-pm.prompt.md)
- [`hermes-breakdown-feature-implementation.prompt.md`](hermes-breakdown-feature-implementation.prompt.md)
- [`hermes-breakdown-feature-prd.prompt.md`](hermes-breakdown-feature-prd.prompt.md)
- [`hermes-breakdown-plan.prompt.md`](hermes-breakdown-plan.prompt.md)
- [`hermes-breakdown-test.prompt.md`](hermes-breakdown-test.prompt.md)
- [`hermes-comprehensive-setup.prompt.md`](hermes-comprehensive-setup.prompt.md)