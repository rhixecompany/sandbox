---
name: hermes-ecosystem-reliability-spec
title: Hermes Ecosystem Reliability Specification
description: Define verifiable lifecycle, MCP, quick-command, memory, and provider-resilience invariants.
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, lifecycle, mcp, quick-commands, reliability, security]
status: implemented-with-verification
plan: .hermes/plans/2026-09-05_084556-hermes-ecosystem-reliability.md
---

# Hermes Ecosystem Reliability Specification

## 1. Purpose

Provide a deterministic, secret-safe baseline for Hermes startup/end capture,
MCP configuration projections, root-script quick commands, memory limits, and
provider rate-limit resilience. The existing dirty repository is preserved;
this specification does not authorize reset, restore, delete, commit, push, or
quota evasion.

## 2. Canonical sources and scopes

| Area | Canonical source | Projection or evidence |
|---|---|---|
| Session lifecycle | Hermes state database + start/end capture hooks | `SESSION_REPORT.md`, capture regression |
| Hermes MCP | active profile `ops/config.yaml` and root config | `.mcp/registry.json`, four client projections |
| Client MCP | `.mcp/registry.json` | `opencode.json`, `.codex/mcp.json`, `.copilot/mcp.json`, `.vscode/mcp.json` |
| Hermes root scripts | `C:/Users/Alexa/AppData/Local/hermes/scripts` | generated quick-command registry + live readback |
| Memory | profile `USER.md`/`MEMORY.md` files | `validate_memories.py` |
| Provider resilience | `scripts/rate_limit_bypass.py` | unified copy, self-test, redacted JSONL audit |

Hermes YAML is edited only through supported CLI or purpose-built Python I/O;
raw credentials are never emitted, copied into reports, or included in tests.

## 3. Functional requirements

### FR-001 — Lifecycle continuity

- Start capture records session identity, baseline, and environment metadata
  without secret values.
- End capture records tool/error/prompt summaries and is idempotent.
- Report generation selects an ended/completed session and accepts the current
  SQLite timestamp representation.
- The lifecycle regression executes twice and exits zero.

**Verification:** `python scripts/test_session_capture.py`; report generator
`--no-mcp`; exact `SESSION_REPORT.md` readback; `hermes hooks doctor`.

### FR-002 — Memory limits

Every discovered Hermes profile must have valid `SOUL.md`, `USER.md`, and
`MEMORY.md` files within the validator’s hard byte limits.

**Verification:** `validate_memories.py` reports `Files failing: 0` and
`Total issues: 0`.

### FR-003 — MCP registry and projections

- Registry server names and enabled flags equal the selected `ops` profile’s
  enabled MCP set; disabled registry-only records remain explicitly disabled.
- Root Hermes MCP names equal the selected profile without rewriting unrelated
  YAML settings.
- The four client projections are generated from the registry and are
  idempotent under strict `mcp_sync.py --check`.
- HTTP/SSE entries are classified as remote/stdio-skipped by the local
  handshake runner; command-capable entries receive a real initialize probe.
- Long-lived stdio servers are terminated after a valid response, not after
  waiting for process exit.

**Verification:** `reconcile_mcp_registry.py` readback; root-MCP reconciler
readback; `python scripts/mcp_sync.py --check --hermes-diff`; ops handshake
JSON and exit marker.

### FR-004 — Quick-command coverage

For every supported file directly under the Hermes root scripts directory:

- exactly one generated `{type: exec, command: ...}` command targets it;
- the command invokes the approved safe wrapper in audit mode;
- command parsing and wrapper smoke execution return zero;
- coverage and smoke counts are parsed programmatically; no hand-counted
  totals are accepted.

The judge must fail on missing, duplicate, malformed, stale, or untested
entries. It must not execute the target scripts themselves.

**Verification:** scripts-judge report with `--quick-commands-json` and
`--quick-command-timeout`; acceptance is `scripts=220`, `generated=220`,
`covered=220`, `smoked=220`, `smoke_failed=0`, `passed=true`.

### FR-005 — Provider resilience

- Retry only rate-limit/usage-limit/quota signals.
- Honor valid `Retry-After` values, then apply bounded exponential backoff and
  jitter.
- Rotate fallback factories after the per-model budget while enforcing one
  total-attempt budget across the request.
- Stop immediately on permanent errors such as invalid credentials, missing
  models, and context-length failures.
- Redact bearer tokens and credential-like values from audit errors.
- Never evade quotas, bypass provider controls, or loop indefinitely.

**Verification:** both rate-limit copies pass `--self-test`; tests cover retry,
rotation, permanent failure, total budget, and audit redaction.

### FR-006 — Instruction and secret safety

Instruction files remain protected unless separately approved. Audits and
reports may include paths, names, counts, statuses, and variable names, but
never `.env` values, token previews, connection strings, or API responses that
contain credentials.

**Verification:** instruction audit, config audit, report scan, and targeted
readback of generated evidence.

## 4. Non-functional requirements

- Operations are deterministic and idempotent.
- Windows paths use forward slashes where native tools require them; `.cmd` and
  `.bat` commands are invoked with their arguments intact.
- Writes are limited to proven defect owners and preserve unrelated dirty work.
- A failed phase is recorded and fixed or reported as an external blocker; no
  silent downgrade is accepted.

## 5. Acceptance matrix

| Gate | Pass condition |
|---|---|
| Lifecycle | capture regression, report generation, and hooks doctor pass |
| Memory | 14 profiles, 45 files, zero validator issues |
| MCP projection | strict sync check exits 0; all four projection files read back |
| MCP health | 28 ops records: 12 PASS, 16 explicit SKIP, 0 FAIL, exit 0 |
| Quick commands | 220/220 scripts covered and smoke-tested; zero smoke failures |
| Rate limit | workspace and unified self-tests exit 0; no secrets in audit output |
| Syntax | root script judge reports zero syntax failures |
| Repository | `git diff --check` and applicable project gates run; pre-existing dirty work remains distinguishable |

## 6. Known limitations and blockers

- Remote HTTP/SSE MCP services are not proven authenticated by a local stdio
  probe; their status is an explicit `SKIP`, not a connectivity claim.
- Copilot has a workspace projection but no live Copilot provider is claimed.
- The scripts judge’s quality average is an audit metric and is not confused
  with quick-command coverage; the coverage gate is independently mandatory.
- Protected instruction-file normalization requires separate explicit approval.

## 7. Required evidence files

Evidence belongs under `.hermes/reports/2026-09-05-hermes-ecosystem-reliability/`
and must contain exit markers plus machine-readable output where applicable.
No evidence file may contain credentials or token previews.
