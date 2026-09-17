---
name: phase1-stashes-debug-2026-09-14
version: 1.0.0
author: Alexa / adminbot
license: MIT
description: "Phase 1 spec: apply 4 git stashes (abort-on-conflict) + systematic-debugging audit config.yaml (YAML list conflict) + browser/debug tool timeout audit."
---

# Phase 1 Spec — Stashes + Systematic Debug + Browser/Config Audit

## Goal
Apply 4 stashes sequentially to `clean-development`; audit `config.yaml` for MCP args YAML list conflict; audit browser/debug artifacts (`agent-browser` skill + `test-providers-models`); document all findings honestly (no hidden errors).

## Subgoals / Tasks
| # | Task | Method | Verification Gate |
|---|---|---|---|
| 1.1 | Apply stash `hermes-update-autostash-20260905-011604` | `git stash apply` (abort-on-conflict) | Exit code 0; no conflicts in `git status` |
| 1.2 | Apply stash `hermes-update-autostash-20260828-151448` | `git stash apply` | Same; document any abort |
| 1.3 | Apply stash `hermes-update-autostash-20260804-191747` | `git stash apply` | Same |
| 1.4 | Apply stash `hermes-update-autostash-20260728-015200` | `git stash apply` | Same; if any abort, document honestly |
| 1.5 | Audit `config.yaml` (MCP server args YAML list) | Read file; check args format; compare with `$HERMES_HOME.md` references; check `.env` variables | Audit result: PASS or conflict documented with exact line reference |
| 1.6 | Audit `.eslintrc.json` parser fix (69 B, verified) | Read file; verify `parserOptions.project` points to `./tsconfig.json`; verify `ruff` clean; verify syntax PASS | `ruff check` PASS; `python -m py_compile` PASS; no new hidden errors |
| 1.7 | Audit browser/debug artifacts (`agent-browser` skill reference; `.github/prompts/operations/test-providers-models/`) | Read skill SKILL.md; read `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md`; verify real file sizes | All files verified real (os.path.getsize / ls); no synthetic content |
| 1.8 | Systematic-debugging: capture sequential exit codes in `./plans/debug-run-logs.md` | Run `hermes mcp test`, `hermes doctor`, `hermes security audit`, `hermes status`, `hermes insights`, 6 `hermes logs` commands; capture stdout/stderr/exit code | All exit codes real (verified by terminal output); no fabricated results |
| 1.9 | Document vulnerabilities (26 REAL findings) + parsing errors (41 remaining) + rate-limit 403 + MSYS2 FAIL | Read `./plans/debug-run-logs.md` (53152 B); read `./specs/debug-analysis-2026-09-13.md` (6081 B) | All findings preserved honestly; NOT suppressed; NOT hidden |

## Evidence Before Fix (Phase 1 of systematic-debugging)
As your patient teacher: before touching anything, document what's broken. Example — the `.eslintrc.json` parser conflict shows `parserOptions.project` missing; the fix adds `parserOptions.project = "./tsconfig.json"` + `parserOptions.tsconfigRootDir = "."`. This is ONE minimal fix; 41 parsing errors remain → architecture concern (nested `.codex/.copilot` scope conflict) — NOT hidden; documented in analysis spec.

## Implementation Details
- Subagent: Subagent-1 (delegated with full context: repo path `C:\Users\Alexa\Desktop\SandBox`, hermes home `~/AppData/Local/hermes/`, profile list 14 verified, 14 skill names, best quality path, model `inkling:free`)
- Execution: sequential (stashes must apply in order; audit depends on stash state)
- Blockers handled: if a stash fails, document abort code + `git status` output; continue to next stash; NEVER fabricate a clean apply.
- `agent-browser` skill audit: verify SKILL.md exists; check references (browser automation CLI); verify no synthetic capabilities.
- `test-providers-models` audit: verify `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` (2886 B verified); verify `.github/prompts/operations/test-providers-models/test-model-01-openrouter-inkling-verified.md` (15255 B verified); verify `test-providers-models-results.json` (26104 B verified); verify 0 synthetic artifacts.

## Verification Checklist (GATE-C)
- [ ] All 4 stashes applied (or conflicts documented honestly)
- [ ] `./plans/debug-run-logs.md` updated with real sequential exit codes (new commands run this phase)
- [ ] `config.yaml` audit completed; conflict documented with line reference if exists
- [ ] `.eslintrc.json` fix verified (69 B; ruff clean; syntax PASS) — does NOT suppress remaining 41 errors (honest reporting)
- [ ] `agent-browser` skill + `test-providers-models` artifacts verified real; 0 synthetic
- [ ] 26 vulnerability findings + 41 parsing errors + 403 + MSYS2 FAIL preserved honestly; NOT hidden
- [ ] `.env` 3334 B unchanged; 0 new `.bak` artifacts
- [ ] DRY enforced: identity/routing rules referenced (not duplicated) from `$HERMES_HOME.md`; best practices referenced from `user-communication-preferences`; protocol referenced from `multi-file-change-protocol`
- [ ] No synthetic session IDs; no synthetic capabilities/quality/ranking
