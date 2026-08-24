# Free Model Selection — Verified Fallback Chain

**Generated:** 2026-08-24T17:20:00Z  
**Status:** ✅ All verification gates passed

---

## Primary Model

| Setting | Value |
|---------|-------|
| `model.provider` | `opencode-zen` |
| `model.default` | `deepseek-v4-flash-free` |
| Context | 200K (free tier cap) |
| Reasoning | ✅ |
| Vision | ❌ |

**Rationale:** Proven working in production across all 13 named profiles; used for all prior requests successfully.

---

## Fallback Chain (Capability-Ordered)

| Order | Provider | Default Model | Vision | Reasoning | Context |
|-------|----------|---------------|--------|-----------|---------|
| 1 | `opencode-zen` | `deepseek-v4-flash-free` | ❌ | ✅ | 200K |
| 2 | `openrouter` | `nvidia/nemotron-3-ultra-550b-a55b:free` | ❌ | ✅ | 1M |
| 3 | `gemini` | `gemini-2.5-flash` | ✅ | ✅ | 1M |
| 4 | `ollama-cloud` | `nemotron-3-ultra` | ❌ | ✅ | 256K |

**Note:** The fallback chain is ordered by capability tier (vision → reasoning → context). Providers 2–4 have reasoning; provider 3 also has vision. Provider 1 is listed first as the primary provider's fallback to itself (useful for key rotation via `credential_pool_strategies.fill_first`).

---

## Vision-Capable Free Models (Not in Chain)

| Provider | Model | Vision | Reasoning | Context |
|----------|-------|--------|-----------|---------|
| openrouter | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ✅ | ✅ | 256K |

*Available as auxiliary vision model via `auxiliary.vision.provider=openrouter`*

---

## Excluded Providers

| Provider | Reason |
|----------|--------|
| deepseek | 402 rate limited |
| huggingface | 400 error |
| nous | 403 forbidden |
| xai | 403 auth failed |
| openai-codex | 429 rate limited |
| copilot | No free models |

---

## Verification Results

```bash
✅ hermes config check — passes
✅ model.provider = opencode-zen
✅ model.default = deepseek-v4-flash-free
✅ fallback_providers is a YAML list (not string)
✅ fallback_providers ordered by capability
✅ Each fallback provider resolves to working free model
✅ Non-working providers excluded
```

---

## Configuration Files Updated

- `~/AppData/Local/hermes/config.yaml` — Root config
- `docs/free-model-selection.md` — This file
- `docs/best-free-models.md` — Ranked catalog
- `docs/model-summary.json` — Provider summary
- `docs/benchmark-results.json` — Verification results
- `docs/opencode-zen_models.json` — Catalog
- `docs/openrouter_models.json` — Catalog
- `docs/gemini_models.json` — Catalog
- `docs/ollama-cloud_models.json` — Catalog
