---
name: 2026-09-07_162000-test-providers-models-implementation
title: Test Providers & Models — Implementation Plan
description: "Phase-by-phase execution plan for the test-providers-models workflow: inventory, catalog, probe, rank, configure, audit."
date: 2026-09-07
author: Alexa
status: in_progress
profile: code-architect
model: nemotron-3-ultra-free
---

# Test Providers & Models -- Implementation Plan

## Goal

Execute every phase of the `test-providers-models` prompt end-to-end on the current Hermes install, producing a verified auth inventory, a `:free` model catalog, real probe results, a ranking, and a configured `model.default` + 4-deep fallback chain.

## Context

The prompt lives at `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` (3.0.0, category=operations). It references 5 templates, 2 scripts, and 2 missing artifacts. The Hermes install has 13 auth providers in `~/AppData/Local/hermes/auth.json`; of those, only the 4 that are `valid` (copilot, deepseek, gemini, huggingface, minimax-oauth, nous, ollama-cloud, openrouter, xai-oauth) are probe-eligible. The other 4 are blocked by 401/402/429. This plan walks through all 5 phases of the prompt and produces a verifiable artifact at each gate.

## Files

- `scripts/test-providers-probe.py` — captures `hermes auth list / config show / status / doctor / doctor --fix / insights / fallback / model`
- `scripts/render_auth_inventory.py` — parses the JSON, writes per-provider + consolidated auth inventory
- `scripts/build_free_model_catalog.py` — fetches `/v1/models` per provider, filters to `:free`, writes catalog + probe task files
- `scripts/run_probes.py` — runs `hermes chat` per probe task, captures results, detects failure markers
- `scripts/apply_config.py` — applies ranking to `hermes config set` + `hermes fallback clear/add`
- `templates/free-model-catalog.md` — catalog output
- `templates/probe-live-template.md` — per-probe result table
- `templates/ranking-report.md` — final ranking + applied config
- `provider_docs/<provider>.md` — 13 per-provider auth inventory files
- `provider_docs/_consolidated.md` — single-table rollup
- `probes/probe-*.txt` — 28 per-model probe task files
- `.hermes/reports/test-providers-probe.{json,md}` — probe capture
- `.hermes/reports/test-providers-probe-results.json` — probe execution results

## Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| `hermes chat` hangs on a slow model | High | High | `--run-budget 35` per probe + overall timeout |
| Model returns HTTP 400/401/402/429 instead of a response | High | High | `detect_failure` regex maps the marker to a normalized exit=-2 + reason |
| Catalog endpoint returns 401 (key not in env) | Medium | Low | Skip the provider and log; do not abort |
| `hermes config set` for an unknown model fails | High | Low | Verify with `hermes model <provider>:<model>` before applying |
| Configured top-1 model is rate-limited at probe time | High | Medium | Ranking score already gates on `exit == 0`; rate-limited models rank lower |

## Phases

### Phase 1 -- Inventory capture
- [x] Run `python scripts/test-providers-probe.py`; 8 commands land in `.hermes/reports/test-providers-probe.{json,md}`.
- [x] Run `python scripts/render_auth_inventory.py`; 13 per-provider files + `_consolidated.md`.

**Gate**: 13 providers inventoried, every credential has a row in the per-provider file.

### Phase 2 -- Provider docs and best practices
- [x] Per-provider docs URLs captured in `provider_docs/<provider>.md` (manual curated metadata; live fetch optional).
- [ ] (Deferred) web-extract each docs URL via `web-research-pipeline` if time permits.

**Gate**: Every `valid` provider has a docs URL in `provider_docs/<provider>.md`.

### Phase 3 -- Free-model catalog and probes
- [x] Run `python scripts/build_free_model_catalog.py`; 28 catalog rows + 28 probe files.
- [x] Run `python scripts/run_probes.py --budget 35 --concurrency 4`; 28 results.
- [x] `templates/probe-live-template.md` populated with exit codes, failure markers, and heuristic claim extractions.

**Gate**: Every catalog row has a corresponding probe result. The counts match (28 = 28).

### Phase 4 -- Rank and configure
- [ ] Run `python scripts/apply_config.py`; reads `.hermes/reports/test-providers-probe-results.json`, scores, applies `hermes config set model.default` + `hermes fallback clear` + 4× `hermes fallback add`.
- [ ] Verify: `hermes config check` exits 0; `hermes config show` shows the new default and 4 fallbacks.

**Gate**: Hermes is configured with the top-5 ranked free models.

### Phase 5 -- Audit and report
- [ ] Run `python scripts/audit-sessions.py --since "<probe-start>"`; ranking captured.
- [ ] Populate `templates/ranking-report.md` with the top-10 table and the applied config commands.
- [ ] Commit all artifacts under `.github/prompts/operations/test-providers-models/`.

**Gate**: `templates/ranking-report.md` committed and `hermes config show` matches the table.

## Timeline

| Phase | Estimate | Status |
|-------|----------|--------|
| 1. Inventory | 1 min | done |
| 2. Docs (manual metadata) | 1 min | done |
| 3. Catalog + probes | 5 min (parallel) | done |
| 4. Rank + configure | 1 min | in progress |
| 5. Audit + report | 2 min | pending |

**Total estimated time**: ~10 min.

## Resource Allocation

- **Subagents**: none — this is a single-agent flow with a few short scripts.
- **Tools required**: `hermes` (CLI), `python` 3.11+, `bash`, `curl` (transitively via `urllib`).
- **Compute**: 4 concurrent `hermes chat` processes, each with a 35s run budget. Peak memory ~500MB.

## Verification

- [ ] `python scripts/test-providers-probe.py` exits 0.
- [ ] `python scripts/render_auth_inventory.py` exits 0; `ls provider_docs/*.md | wc -l` >= 14 (13 providers + _consolidated).
- [ ] `python scripts/build_free_model_catalog.py` exits 0; `ls probes/probe-*.txt | wc -l` matches the catalog row count.
- [ ] `python scripts/run_probes.py --budget 35 --concurrency 4` exits 0; every row in `templates/probe-live-template.md` has an exit code.
- [ ] `hermes config check` exits 0 after `apply_config.py`.
- [ ] `hermes config show | grep -E 'model|fallback'` shows the top-1 + 4 fallbacks in the expected order.
- [ ] `python "C:/Users/Alexa/AppData/Local/hermes/skills/qa/prompts-judge/scripts/judge.py" --prompts-dir .github/prompts` reports the prompt at score >= 98.

## Linked Specs
- ../specs/test-providers-models-spec.md
- ../specs/hermes-ecosystem-reliability-spec.md
