---
name: hermes-doctor-systematic-debugging
title: "Hermes Doctor, Logs, and Systematic Remediation"
description: "Run the complete Hermes health and log diagnostic sequence, investigate root causes with systematic-debugging, apply minimal fixes, and verify zero actionable issues remain."
version: 1.0.0
license: MIT
author: Alexa
toolsets:
  - file
  - terminal
  - web
skills:
  - systematic-debugging
  - hermes-agent
  - hermes-mcp
  - verification-before-completion
formatter: default
plan: ''
dependencies:
  - skill:systematic-debugging
  - skill:hermes-agent
  - skill:hermes-mcp
  - skill:verification-before-completion
tags:
  - debugging
  - diagnostics
  - doctor
  - errors
  - hermes
  - logs
  - remediation
  - system
  - verification
trigger: /hermes-doctor-systematic-debugging
---

# Hermes Doctor and Systematic Remediation

## Goal

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
4. `hermes doctor --fix` is authorized by this prompt, but review the preceding `hermes doctor` findings first.
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
|---|---|
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

5. Trace the failing component to its source file/config key/log producer.
6. Compare with a working sibling component or profile.
7. State one hypothesis: “I think X is the root cause because Y.”
8. Test the hypothesis with one minimal, reversible change.

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
- Status reports healthy or clearly explains non-actionable external services.
- Insights completes without traceback.
- All expected log targets are readable or their absence is documented as non-actionable.
- MCP servers remain connected and enabled.
- No secrets appear in captured artifacts or the final report.

## Failure Handling

| Failure | Response |
|---|---|
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
|---|---|---|---|---|
| Doctor |  |  |  |  |
| Status |  |  |  |  |
| Insights |  |  |  |  |
| Logs |  |  |  |  |
| MCP |  |  |  |  |
| Profiles/config |  |  |  |  |

Also report:

- Prompt path
- Exact commands executed
- Files changed, if any
- Remaining non-actionable warnings
- Remaining blockers with exact evidence
- Whether a Hermes restart or `/reset` is required
