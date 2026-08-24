# Best Free Models — Ranked by Vision → Reasoning → Context Size

**Generated:** 2026-08-24T17:15:00Z  
**Method:** Live catalog discovery + benchmark verification  
**Ranking Rule:** vision (tier 2) → reasoning (tier 1) → context size (tier 0, normalized)

---

## Ranked Free Models (Working)

| Rank | Provider | Model | Vision | Reasoning | Context | Notes |
|------|----------|-------|--------|-----------|---------|-------|
| 1 | openrouter | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | ✅ | ✅ | 256K | **Only vision-capable free model** |
| 2 | gemini | gemini-2.5-flash | ✅ | ✅ | 1M | Vision + reasoning + largest context |
| 3 | opencode-zen | nemotron-3-ultra-free | ❌ | ✅ | 1M | Reasoning + 1M context |
| 4 | openrouter | nvidia/nemotron-3-ultra-550b-a55b:free | ❌ | ✅ | 1M | Reasoning + 1M context |
| 5 | openrouter | nvidia/nemotron-3-super-120b-a12b:free | ❌ | ✅ | 1M | Reasoning + 1M context |
| 6 | ollama-cloud | nemotron-3-ultra | ❌ | ✅ | 256K | Reasoning + 256K context |
| 7 | opencode-zen | deepseek-v4-flash-free | ❌ | ✅ | 200K | **PRIMARY** (used by all 13 named profiles) |
| 8 | openrouter | google/gemma-4-31b-it:free | ❌ | ❌ | 262K | No reasoning |
| 9 | openrouter | google/gemma-4-26b-a4b-it:free | ❌ | ❌ | 262K | No reasoning |
| 10 | openrouter | openai/gpt-oss-20b:free | ❌ | ❌ | 131K | No reasoning |

---

## Ranking Logic

```python
def sort_key(m):
    vision = 2 if m.vision else 0
    reason = 1 if m.reasoning else 0
    ctx = min(m.ctx, 2_000_000) / 2_000_000  # normalized 0..1
    return (vision, reason, ctx)  # descending
```

**Key insight:** No working free model has vision + reasoning + large context simultaneously. The rule degrades to:

1. **Vision + Reasoning** (tier 3) — only `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` and `gemini-2.5-flash`
2. **Reasoning only** (tier 2) — sorted by context size
3. **No reasoning** (tier 1) — sorted by context size

---

## Excluded Providers (Non-Working)

| Provider | Status | Error |
|----------|--------|-------|
| deepseek | ❌ | 402 rate limited |
| huggingface | ❌ | 400 bad request |
| nous | ❌ | 403 forbidden |
| xai | ❌ | 403 auth failed |
| openai-codex | ❌ | 429 rate limited |
| copilot | ❌ | No free models |

---

## Artifacts

- `docs/opencode-zen_models.json` — Full catalog
- `docs/openrouter_models.json` — Full catalog
- `docs/gemini_models.json` — Full catalog
- `docs/ollama-cloud_models.json` — Full catalog
- `docs/benchmark-results.json` — Verification results
- `docs/model-summary.json` — Provider summary
