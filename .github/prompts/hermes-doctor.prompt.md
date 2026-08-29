---
name: hermes-doctor
title: Hermes Doctor Diagnostic
description: Run a full Hermes platform diagnostic battery (doctor/--fix/security/status/insights + log triage + bun run check) and produce a classified report. Use for "find all hermes bugs", pre-deploy checks, or post-upgrade audits.
trigger: /hermes-doctor
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, diagnostic, doctor, log-triage, verification]
toolsets:
  - file
  - terminal
skills:
  - skill:using-superpowers
dependencies: []
formatter: markdown
metadata:
  hermes:
    profile: default
    context_size: medium
  copilot:
    context_size: medium
    extensions: []
  opencode:
    command: "opencode //hermes-doctor"
    flags: {{}}
  codex:
    model_override: null
---

# Hermes Doctor Diagnostic

Full-platform health pass with classified findings.

## When to Use

- "Find all hermes bugs/issues/warnings"
- "Run hermes doctor + log triage"
- Pre-deploy or pre-commit health check
- Post-upgrade audit (hermes, ollama, plugins)
- Cron nightly platform audit

## Workflow

1. **Run the battery**

   ```bash
   cd "C:/Users/Alexa/Desktop/SandBox"
   python scripts/hermes_doctor.py
   ```

   Runs 12 commands: `hermes doctor`, `hermes doctor --fix`, `hermes security audit`, `hermes status`, `hermes insights`, `hermes logs list/errors/desktop/gateway/gui/agent`, `bun run check`. ~90s typical.

2. **Read the report**

   ```bash
   cat .hermes/plans/diagnostic-$(date +%F)/report.md
   ```

   Section "Findings" lists only real_bug + transient (actionable). Intentional and advisory are tallied but not flagged.

3. **Interpret results**

   | Count | Meaning | Action |
   | ----- | ------- | ------ |
   | 0 real_bug | Healthy | None |
   | 1+ real_bug | Real bug(s) present | Use `systematic-debugging` on each |
   | transient only | Network/external issues | Document, retry later |
   | advisory only | Config noise | Optional cleanup |

4. **Verify gates**

   - Script exit 0: clean platform
   - report.json schema_version=1
   - All 12 commands show ok=true OR fail classified as transient/advisory

## Flags

| Flag | Effect |
| ---- | ------ |
| `--doctor-only` | Skip log commands + bun run check (5 commands, ~70s) |
| `--logs-only` | Only the 6 log commands |
| `--no-bun` | Skip `bun run check` (saves ~3-5 min) |
| `--json-only` | Suppress markdown output |
| `--output DIR` | Custom output directory |
| `--timeout N` | Per-command timeout in seconds (default 120) |

## Pitfalls

- **`bun run check` is the slow one** — if you're in a hurry, `--no-bun`
- **Advisory ≠ bug** — `not logged in` for unused OAuth providers is expected
- **Log classifications drift** — patterns in `scripts/hermes_doctor.py` are Hermes-specific; update as you encounter new false-positives

## Verification

- [ ] `python scripts/hermes_doctor.py` exits 0 on clean platform
- [ ] `report.json` is valid JSON, has `schema_version: 1`
- [ ] `report.md` has summary table with command counts and findings
- [ ] `bun run lint` clean (script AST-valid)

## See Also

- `hermes-diagnostic-repair` (skill) — deep repair workflow with code-patching
- `log-analysis-and-triage` (skill) — Hermes log classification reference
- `systematic-debugging` (skill) — for each real_bug finding
- `scripts/hermes_doctor.py` — the implementation
