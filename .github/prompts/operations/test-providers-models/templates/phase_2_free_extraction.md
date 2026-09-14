# Phase 2: Free Model Extraction

> Template for `test-providers-models`. Filter zero-cost/free-tier models for the fallback chain.

## Inputs

- Catalog from Phase 1
- `hermes auth list` (credential status — excludes rate-limited/dead providers)

## Filter Rule

Only include models with `pricing=0` or `':free'` suffix or explicitly free-tier in provider docs.

Before probing, remove every model belonging to a provider whose auth inventory
contains rate-limit evidence (`rate-limited`, `429`, `too many requests`, quota
exhaustion, or throttling). Keep those catalog rows for audit history, but do
not send requests, retry them, rank them, or select them for configuration.

## Outputs

- Ordered table of free models with provider, model ID, context window, reasoning flag

## Verification Gate

- [ ] Only `:free` or `pricing=0` models listed
- [ ] Non-working providers (deepseek 402, huggingface 400, nous 403, xai-oauth 402, openai-codex 429, copilot n/a) excluded or marked non-working
- [ ] Every provider marked `rate-limited`/`429` is excluded from live probes and fallback selection as a provider, not only by individual model
- [ ] `docs/free-model-selection.md` updated
