# Shared Rules Core

> This file is referenced by `test-providers-models.prompt.md` at line 23 and contains domain-agnostic rules shared across prompt templates.

## Core Rules (Cross-Prompt)

1. **Never invent providers or models** — Always enumerate from `hermes auth list` or `hermes config show`. If a provider/model is not listed, it is not authorized.

2. **Probe before promote** — A model is only "working" after a live `hermes chat` probe succeeds. Assumptions, cached results, or prior runs do not count unless re-verified.

3. **Ranking is deterministic** — The ordering rule is always: vision → reasoning → context size. Never promote a model based on reputation alone without live verification.

4. **Free-tier only** — The fallback chain can only include models that are confirmed free-tier accessible. Paid models, even if capable, are excluded.

5. **Verify before claiming complete** — All five verification gates (config check, model/provider type, fallback list type, default_model per provider, docs updated) must pass before reporting the chain complete.

6. **String-encoded list remediation** — If `fallback_providers` appears as a YAML scalar string instead of a sequence, repair it via terminal Python one-liner before any config commit.

7. **Provider alias alignment** — `fallback_providers` list entries are provider *names* (opencode-zen, openrouter, gemini, ollama-cloud). Each name must have its `providers.<name>.default_model` set to a working free model.

8. **Root vs profiles alignment** — After root config is set, propagate changes to all named profiles via `scripts/sync_profile_configs.py`. A drift between root and profiles must be documented and resolved before claiming completion.

9. **No vision in free tier** — As of 2026-08-08, no verified working free model has vision capability. Do not attempt to add vision models to the free fallback chain; the rule degrades to reasoning → context.

10. **Re-probe on each run** — Model availability is volatile (rate limits flip, keys expire, cooldowns shift). Each run of `test-providers-models` must re-probe live; never trust cached results from prior runs without fresh verification.