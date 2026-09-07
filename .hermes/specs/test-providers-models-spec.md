---
name: test-providers-models-spec
title: Test Providers & Models Specification
description: "Define the requirements for the test-providers-models workflow: capture Hermes auth inventory, build a :free suffix model catalog, run live probes, rank the top 5 free models, and configure the optimal primary + fallback chain."
version: 1.0.0
author: Alexa
license: MIT
tags: [hermes, providers, models, probe, audit, free-tier, config, fallback]
status: implemented
owner: Alexa
plan: ../../plans/2026-09-07_162000-test-providers-models-implementation.md
---

# Test Providers & Models Specification

## Goal

Provide a deterministic, secret-safe, end-to-end test of every authorized Hermes auth provider and every model with a `:free` (or zero-priced) suffix, then configure the primary model plus a 4-deep fallback chain driven by the verified probe results.

The workflow MUST be re-runnable end-to-end without leaking credentials, and MUST emit machine-readable artifacts (catalog, per-probe results, ranking) that can be diffed across runs.

## Requirements

### Functional Requirements

- **FR-001 — Auth inventory capture**: For every credential in `~/AppData/Local/hermes/auth.json`, render a one-file-per-provider markdown in `provider_docs/<provider>.md` containing: provider name, key env var, status (one of `valid`, `exhausted-402`, `rate-limited-429`, `auth-failed-401/403`, `missing`), rate/auth notes, docs URL, and the full credential list with index, key name, type, source, and note. Also emit `provider_docs/_consolidated.md` as a single-table rollup of all 13+ providers.

- **FR-002 — Free-model catalog**: For every reachable catalog endpoint (opencode-zen, openrouter), enumerate models. A model is `:free` if its id contains `:free` or ends in `-free`, OR its `pricing.prompt == 0 && pricing.completion == 0`. Emit `templates/free-model-catalog.md` as a table with at minimum: index, provider, model id, knowledge cutoff, context length, max output, reasoning flag, source URL.

- **FR-003 — Probe task generation**: For each catalog row, write a `probes/probe-NNN-<provider>-<safe-model>.txt` file containing the exact `hermes chat` invocation that should be run. The safe-model encoding replaces `/` with `_` and preserves `.`, `-`, `:`.

- **FR-004 — Live probe execution**: For each probe file, run `hermes chat --provider <p> --model <m> -q "<question>" --oneshot --yolo --run-budget <N>` with a per-probe timeout, capture the result, and detect known failure markers (HTTP 400 model_unavailable, 401 auth_failed, 402 exhausted, 403 auth_failed, 404 model_not_found, 429 rate_limited). A probe that exits 0 from hermes but emits one of these markers is recorded as `exit=-2, failure=<reason>`.

- **FR-005 — Response claim extraction**: From the model's stdout, extract via regex: knowledge cutoff (YYYY-MM-DD or "Month YYYY"), context length (e.g. "128k" → 128000), reasoning support (yes/no), max output tokens. A model that does not state a value gets `?` for that field; this is honest, not a failure.

- **FR-006 — Ranking and config**: Score each probed model with `score = recent_kc + context_ge_32k + reasoning + max_output_ge_4k + exit_0`. Take the top 5 by score, tiebreak by lowest `elapsed_s`. Apply:
  - `hermes config set model.default <top1.provider>:<top1.model>`
  - `hermes config set model.provider <top1.provider>`
  - `hermes fallback clear`
  - `hermes fallback add <top2.provider>:<top2.model>` × 4

- **FR-007 — Audit report**: `templates/ranking-report.md` MUST contain a top-10 table with score, provider, model, knowledge cutoff, context length, reasoning, max output, and the `hermes config set` + `hermes fallback add` commands actually applied.

- **FR-008 — Configuration verification**: `hermes config check` MUST exit 0 after the config is applied. `hermes config show` MUST show the top-1 model as the default.

### Non-Functional Requirements

- **NFR-001 — Secret safety**: No `.env` values, bearer tokens, or `Authorization:` headers appear in any committed artifact. Auth keys are read from `os.environ` and used only at HTTP-call time, never written to disk.

- **NFR-002 — Idempotency**: Re-running the workflow on the same Hermes install produces the same auth-inventory, the same catalog, the same probe task files, and a fresh probe-results JSON. The catalog script deletes prior `probes/probe-*.txt` before writing new ones.

- **NFR-003 — Resumability**: If a single probe times out, the workflow continues with the remaining probes. Per-probe results are written to `templates/probe-live-template.md` after every probe completes.

- **NFR-004 — Bounded runtime**: With 4 concurrent probes at a 35-second per-probe budget, the full Phase 3 sweep MUST complete in under 5 minutes. Slow models that time out at 35s are recorded as failures and excluded from the ranking.

- **NFR-005 — Path portability**: All scripts under `scripts/` use `Path(__file__).resolve().parents[N]` to compute the repo root, so they work regardless of the cwd they are invoked from.

## Acceptance Criteria

- [ ] `python scripts/test-providers-probe.py` exits 0 and writes `.hermes/reports/test-providers-probe.{json,md}` with 8 command results.
- [ ] `python scripts/render_auth_inventory.py` exits 0 and writes one `provider_docs/<provider>.md` per credentialed provider plus `_consolidated.md`.
- [ ] `python scripts/build_free_model_catalog.py` exits 0 and writes `templates/free-model-catalog.md` and one `probes/probe-*.txt` per catalog row.
- [ ] `python scripts/run_probes.py --budget 35 --concurrency 4` exits 0 and writes `templates/probe-live-template.md` plus `.hermes/reports/test-providers-probe-results.json`.
- [ ] Every catalog row has a corresponding probe result; the counts match.
- [ ] For at least one probed model, the ranking script records a real response (not a failure marker).
- [ ] `hermes config show` shows the top-1 free model as `model.default` and 4 fallbacks in the order added.
- [ ] `hermes config check` exits 0 after config is applied.
- [ ] No secrets (`.env` values, bearer tokens) appear in any committed artifact.

## Verification

- [ ] All 8 acceptance criteria above pass.
- [ ] `python scripts/test-providers-probe.py && python scripts/render_auth_inventory.py && python scripts/build_free_model_catalog.py && python scripts/run_probes.py` runs end-to-end without error.
- [ ] `python "C:/Users/Alexa/AppData/Local/hermes/skills/qa/prompts-judge/scripts/judge.py" --prompts-dir .github/prompts` reports the `test-providers-models.prompt.md` at score >= 98.
- [ ] `python "C:/Users/Alexa/AppData/Local/hermes/skills/qa/plans-judge/scripts/judge.py" --plans-dir .hermes/plans` reports this spec's linked plan at score >= 95.

## Linked Specs
- ./hermes-ecosystem-reliability-spec.md (cross-references the safe probe pattern)

## Linked Plan
- ../../plans/2026-09-07_162000-test-providers-models-implementation.md
