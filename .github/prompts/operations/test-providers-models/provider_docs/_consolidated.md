---
name: auth-inventory-consolidated
description: Single-table auth inventory across all Hermes providers, rendered from the live `hermes auth list` capture on 2026-09-07 15:07 UTC.
---

# Auth inventory -- consolidated

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on 2026-09-07 15:07 UTC.
> See `provider_docs/<provider>.md` for the full per-provider breakdown.

| Provider | Status | Rate / auth notes | Docs |
|---|---|---|---|
| `copilot` | **valid** | ← | https://github.com/features/copilot |
| `deepseek` | **valid** | ← | https://platform.deepseek.com/api-docs/ |
| `gemini` | **valid** | ← | https://ai.google.dev/gemini-api/docs |
| `huggingface` | **valid** | ← | https://huggingface.co/docs/api-inference |
| `minimax-oauth` | **valid** | ← | https://docs.x.ai/ |
| `nous` | **valid** | ← | https://inference-api.nousresearch.com/ |
| `ollama-cloud` | **valid** | ← | https://ollama.com/docs |
| `openai-api` | **exhausted-402** | exhausted (402) (ready to retry) | exhausted (402) (ready to retry) ← | exhausted (402) (ready to retry) | https://platform.openai.com/docs |
| `openai-codex` | **rate-limited-429** | rate-limited usage_limit_reached (429) (27d 6h left) | rate-limited usage_limit_reached (429) (27d 9h left) | rate-limited usage_limit_reached (429) (27d 17h left) | https://github.com/features/copilot |
| `opencode-zen` | **auth-failed-401/403** | auth failed ModelError (401) (re-auth may be required) ← | auth failed ModelError (401) (re-auth may be required) | auth failed ModelError (401) (re-auth may be required) | https://opencode.ai/docs/zen/ |
| `openrouter` | **valid** | ← | https://openrouter.ai/docs |
| `xai` | **auth-failed-401/403** | auth failed (403) (re-auth may be required) ← | https://docs.x.ai/docs |
| `xai-oauth` | **valid** | ← | https://docs.x.ai/ |

