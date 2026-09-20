---
name: phase2-web-research-env-2026-09-14
version: 1.0.0
author: Alexa / adminbot
license: MIT
description: "Phase 2 spec: fetch openrouter.ai/models?variant=free; generate markdown report; test each free model via test-providers-models; audit/update env vars in repo + hermes home + all profiles; configure hermes with model + fallback."
---

# Phase 2 Spec — Web Research + Environment Variables + Model Testing

## Goal

Fetch `https://openrouter.ai/models?variant=free` (only free); convert HTML to markdown; generate markdown report; run `/test-providers-models` on each free model entry; audit/update environment variables in repo + hermes home + all 14 profiles; configure hermes (`opencode-zen` + `opencode-free`) with model + fallback (documented); update `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md`.

## Evidence Before Fix

As a concrete example: the `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` (2886 B) defines the test protocol; `.github/prompts/operations/test-providers-models/test-model-01-openrouter-inkling-verified.md` (15255 B) verifies the `inkling:free` model; `.github/prompts/operations/test-providers-models/test-providers-models-results.json` (26104 B) records previous results. These are REAL artifacts — verified by `ls -la` and `os.path.getsize`. No synthetic results.

## Subgoals / Tasks

| #   | Task                                                | Method                                                                                                                                                                                                                 | Gate                                                                                                                            |
| --- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 2.1 | Fetch `openrouter.ai/models?variant=free`           | `browser_exec` with URL; use `agent-browser` tool if available; capture HTML                                                                                                                                           | Page loaded; content verified real                                                                                              |
| 2.2 | Convert HTML to markdown                            | Use `fetch` tool or `agent-browser` conversion; save to `./plans/openrouter-free-models-report.md`                                                                                                                     | Markdown file exists; size > 0; real content                                                                                    |
| 2.3 | Extract all FREE model entries                      | Parse markdown; list model IDs; create table in report                                                                                                                                                                 | All free entries captured; no synthetic entries                                                                                 |
| 2.4 | Run `/test-providers-models` on each free model     | Execute `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` against each model; capture results                                                                                         | Results saved to `.github/prompts/operations/test-providers-models/test-providers-models-results.json` (updated); verified real |
| 2.5 | Audit/update env vars (repo files)                  | Read `.env`, `package.json`, `pyproject.toml`, `.cursorrules`, `.github/prompts/`, `$HERMES_HOME.md`, `AGENTS.md`; check for missing/incorrect env refs; update if needed                                              | All env vars verified; `.env` 3334 B unchanged (no secret exposure)                                                             |
| 2.6 | Audit/update env vars (hermes home)                 | Read `~/AppData/Local/hermes/config.yaml`; read all profile `.env` files (14 profiles); compare with `$HERMES_HOME.md`; update if needed                                                                               | All profile `.env` files verified; no conflicts                                                                                 |
| 2.7 | Best practices for `opencode-free` + `opencode-zen` | Read `.github/prompts/` docs; search `./plans/` for `opencode-zen-workflow.md` (656 B verified), `opencode-free-workflow.md` references; extract best practices                                                        | Best practices documented in `./specs/phase2-...` or `./plans/`                                                                 |
| 2.8 | Configure hermes with model + fallback              | Update `$HERMES_HOME.md` / profile `USER.md` / `SOUL.md` with `opencode-zen` + `opencode-free` references; set fallback (`openrouter` → `nous` → `opencode-zen`); verify via `hermes profile list` and `hermes config` | Config verified; no corruption; identity preserved                                                                              |

## Resource / Model Allocation

- Subagent: Subagent-2 (delegated with full context + 14 skills + best quality + model `inkling:free` + fallback setup)
- Browser timeout audit: check `agent-browser` skill references; verify `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` references; document any timeout patterns honestly.
- Rate-limit 403 blocker: preserved; NOT bypassed; NOT synthesized; future batches 23-628 (`./plans/web-research-628-batch-execution-plan.md` 5991 B verified) = future sequential work — NOT executed this session; NOT fabricated.

## Verification Checklist (GATE-D)

- [ ] Markdown report (`openrouter-free-models-report.md`) verified real (size > 0; real content; no synthetic entries)
- [ ] `test-providers-models` executed; results updated (`results.json`); all exit codes real
- [ ] Env vars audited in repo + hermes home + all profiles; updates verified
- [ ] `.env` 3334 B unchanged; no `.env` exposure (false positive `API_KEY=vault` corrected via `./specs/exposure-correction.md` 1333 B — original vault handle reference, NOT `.env` secret)
- [ ] Best practices (`opencode-zen` + `opencode-free`) documented; config updated with fallback
- [ ] 0 synthetic artifacts; 0 hidden errors; identity preserved; DRY enforced
