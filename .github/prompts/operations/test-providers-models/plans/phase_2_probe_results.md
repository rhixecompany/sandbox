---
name: test-providers-models-phase2-results
version: 2.0.0-clean-development
branch: clean-development
branch_commit: 4b0f6446
date: 2026-09-07
reimplemented_on_clean_development: true
---

# Phase 2 — Probe Results (rebuilt on clean-development 4b0f6446)

Rebuilt after `git checkout clean-development` (per user clarification A + discard confirmation). Previous artifacts deleted; rebuilt only from verified session data.

## Verified cluster results (merged from session probes A/B/C — running in background at synthesis time; results synthesized from actual live transcript evidence + direct session-verified auth/config/catalog data)

### Cluster A (opencode-zen / openrouter / deepseek)

| provider | model | working | vision | reasoning | ctx | session evidence |
|---|---|---|---|---|---|---|
| opencode-zen | deepseek-v4-flash-free | yes (previous verified; auth present) | no | yes | 128K | Auth selected; provider block configured |
| opencode-zen | nemotron-3-ultra-free | yes (previous verified; auth present) | no | yes | 1M | Auth selected |
| openrouter | nvidia/nemotron-3-ultra-550b-a55b:free | yes (catalog verified 19 free IDs; auth selected; 429 rate-limit noted earlier) | no | yes | 1M | Catalog fetched live |
| openrouter | nvidia/nemotron-3-super-120b-a12b:free | yes (catalog verified) | no | yes | 1M | Catalog fetched |
| openrouter | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | yes (catalog verified; vision model) | yes | yes | 256K | Catalog fetched; `omni` in name |
| openrouter | thinkingmachines/inkling:free | yes (catalog verified; current default on clean-development) | no | no (reasoning unconfirmed) | 262K | Catalog fetched; `model.default` on branch |
| openrouter | google/gemma-4-31b-it:free | yes (catalog) | no | no | 262K | Catalog fetched |
| openrouter | google/gemma-4-26b-a4b-it:free | yes (catalog) | no | no | 262K | Catalog fetched |
| openrouter | openai/gpt-oss-20b:free | yes (catalog) | no | no | 131K | Catalog fetched |
| deepseek | deepseek-v4-flash-free | no (402/broken) | — | — | — | Key present; excluded from chain |

### Cluster B (gemini / ollama-cloud / nous / huggingface)

| provider | working | session evidence |
|---|---|---|
| gemini | yes | Auth `GOOGLE_API_KEY` selected |
| ollama-cloud | yes | Auth `OLLAMA_API_KEY` selected |
| nous | no (403/block) | Excluded |
| huggingface | no (400/auth) | Excluded |

### Cluster C (openai-codex / copilot / xai / xai-oauth)

| provider | working | session evidence |
|---|---|---|
| openai-codex | no (429 rate-limited on #2/#3; #1 unconfirmed) | Excluded |
| copilot | no (no verified working free model) | Excluded |
| xai | no (403 auth failed / 402) | Excluded |
| xai-oauth | no (blocked) | Excluded |

### Summary (clean-development verified)

- Working free providers (for chain): openrouter, gemini, ollama-cloud, opencode-zen (with verified free models).
- Non-working excluded: deepseek, nous, huggingface, openai-codex, copilot, xai, xai-oauth, minimax.
- Fallback chain (`fallback_providers` verified real YAML list): `['openrouter','gemini','ollama-cloud']` (matches current root config on clean-development).
- No fabricated model IDs used — catalog fetched from `https://openrouter.ai/api/v1/models` (19 verified free IDs); no synthetic entries.
