---
title: "Hermes Doctor Diagnostic Pipeline"
description: "Full Hermes platform diagnostic battery (12 commands) with classified findings (real_bug/intentional/transient/advisory). Script + skill + prompt + report."
date: 2026-08-28
author: Hermes Agent
status: completed
---

# Hermes Doctor Diagnostic Pipeline — SPEC

## Goal

Build a one-command, end-to-end diagnostic pipeline for the Hermes platform. Runs the full battery the user spec'd, classifies every finding, writes a structured report, and provides a skill + prompt so this is a reusable workflow.

## The Battery (in order, per user spec)

1. `hermes doctor`
2. `hermes doctor --fix`
3. `hermes security audit`
4. `hermes status`
5. `hermes insights`
6. `hermes logs list`
7. `hermes logs errors`
8. `hermes logs desktop`
9. `hermes logs gateway`
10. `hermes logs gui`
11. `hermes logs agent`
12. `bun run check`

## Classification Taxonomy (4 buckets)

| Bucket | Real fix? | Pattern examples |
| ------ | --------- | ---------------- |
| `real_bug` | Yes | `HTTP 402`, `WinError 5`, `shell hook failed.*command not found`, `WAL checkpoint.*disk I/O error` |
| `intentional` | No | `Title generation failed`, `check_fn.*returned False`, `PluginContext.register_flask_app`, `never commit` (user rule) |
| `transient` | Document | `getaddrinfo failed`, `HTTP 429`, `HTTP 5\d\d`, `connection.*refused`, `Insufficient credits` |
| `advisory` | Report only | `not logged in`, `no alias`, `uncommitted` |

## Artifacts

| Path | Size | Purpose |
| ---- | ---- | ------- |
| `scripts/hermes_doctor.py` | ~13 KB | Stdlib-only Python orchestrator |
| `~/AppData/Local/hermes/skills/devops/hermes-doctor-pipeline/SKILL.md` | 4.7 KB | Reusable skill (auto-discovered) |
| `.github/prompts/hermes-doctor.prompt.md` | 3.0 KB | Reusable prompt |
| `.hermes/plans/hermes-doctor-2026-08-28/SPEC.md` | this | Specification |
| `.hermes/plans/hermes-doctor-2026-08-28/PLAN.md` | 6 KB | Sequencing |
| `.hermes/plans/hermes-doctor-2026-08-28/implementation-plan.md` | 3 KB | Tasks |
| `.hermes/plans/diagnostic-<date>/report.{json,md}` | generated | Per-run report |

## Output Schema (report.json)

```json
{
  "schema_version": 1,
  "generated": "2026-08-28T21:28:10+00:00",
  "cwd": "C:\\Users\\Alexa\\Desktop\\SandBox",
  "profile": "default",
  "total_duration_ms": 70363,
  "results": [
    {
      "label": "doctor",
      "command": "hermes doctor",
      "exit_code": 0,
      "duration_ms": 1234,
      "stdout": "...",
      "stderr": "",
      "ok": true
    }
  ],
  "summary": {
    "counts": {
      "total": 5,
      "ok": 5,
      "fail": 0,
      "real_bug": 0,
      "intentional": 0,
      "transient": 0,
      "advisory": 3,
      "info": 2
    },
    "findings": [
      {
        "label": "...",
        "classification": "real_bug|transient",
        "exit_code": 1,
        "excerpt": "first 500 chars of output"
      }
    ]
  }
}
```

## Exit Codes

- `0` — no real_bug findings
- `1` — ≥1 real_bug (action required)
- `2` — tool failure (hermes itself broken)

## Verification Gates (all PASS)

| Gate | Check | Result |
| ---- | ----- | ------ |
| V1 | `python -m py_compile scripts/hermes_doctor.py` | PASS |
| V2 | `python scripts/hermes_doctor.py --doctor-only --no-bun` exits 0 | PASS (5/5 ok) |
| V3 | `report.json` valid JSON, schema_version=1 | PASS |
| V4 | `report.md` has summary table + per-command table | PASS |
| V5 | `bun run lint` clean on `scripts/hermes_doctor.py` | PASS |
| V6 | `hermes skills list \| grep hermes-doctor` shows skill | PASS |
| V7 | `.github/prompts/hermes-doctor.prompt.md` exists | PASS |
| V8 | All 12 commands executed in full battery run | PASS |

## Design Decisions

1. **Stdlib only** — no new deps. Reuses `subprocess`, `json`, `re`, `pathlib` from Python 3.11.
2. **Per-command timeout** — default 120s, configurable. Prevents hangs on log commands during busy sessions.
3. **Classify after capture** — run all commands, then regex-classify. Avoids mid-battery decision noise.
4. **Output capped at 8KB per command** — keeps report.json reasonable; full logs still in Hermes's own log dir.
5. **Reuse `log-analysis-and-triage` patterns** — don't reinvent the regex catalog. The script's PATTERN_* lists mirror the skill's classification table.

## Pitfalls

- **`hermes logs *` can hang** during active sessions — per-command 30s timeout
- **Advisory ≠ bug** — script documents this; user should not panic on `not logged in`
- **Pattern drift** — add new false-positive signatures to PATTERN_INTENTIONAL as discovered
- **Output dir accumulates** — `diagnostic-<date>/` rotates daily; archive if needed

## Open Items

- Cron candidate: nightly `hermes_doctor.py` at 02:00 with `deliver=local`
- Pre-commit hook: `python scripts/hermes_doctor.py --doctor-only --no-bun` as quality gate
- Pattern updates: when new Hermes versions ship, audit for new intentional/transient patterns
