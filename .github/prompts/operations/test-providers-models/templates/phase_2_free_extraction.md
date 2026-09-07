# Phase 2: Free Model Extraction

> Template for `test-providers-models`. Filter zero-cost/free-tier models for the fallback chain.

## Inputs

- Catalog from Phase 1
- `hermes auth list` (credential status — excludes rate-limited/dead providers)

## Filter Rule

Only include models with `pricing=0` or `':free'` suffix or explicitly free-tier in provider docs.

## Outputs

- Ordered table of free models with provider, model ID, context window, reasoning flag

## Verification Gate

- [ ] Only `:free` or `pricing=0` models listed
- [ ] Non-working providers (deepseek 402, huggingface 400, nous 403, xai-oauth 402, openai-codex 429, copilot n/a) excluded or marked non-working
- [ ] `docs/free-model-selection.md` updated
