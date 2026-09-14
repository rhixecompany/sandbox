# Test Providers Models — Benchmark Results

Date: 2026-09-14
Provider: opencode-zen + openrouter + nous + deepseek + ollama-cloud

## Results

| Provider | Model | Status | Notes |
|----------|-------|--------|-------|
| opencode-zen | deepseek-v4-flash-free | ❌ 400 | Model unavailable on Zen gateway |
| opencode-zen | nemotron-3-ultra-free | ⏱️ timeout | 30s timeout, no response |
| opencode-zen | nemotron-3.5-lightning-free | ❌ 400 | Model unavailable on Zen gateway |
| opencode-zen | mimo-v2.5-free | ❌ 400 | Model unavailable on Zen gateway |
| opencode-zen | big-pickle | ❌ 400 | Model unavailable on Zen gateway |
| opencode-zen | ling-3.0-flash-fin-free | ❌ 400 | Model unavailable on Zen gateway |
| opencode-zen | muse-spark-1.3-contributor-free | ❌ 400 | Model unavailable on Zen gateway |
| openrouter | inclusionai/ling-3.0-flash-sante:free | ⛔ 429 | Rate limited: free-models-per-day exhausted (0/50 remaining) |
| nous | nemotron-3-ultra-free | ❌ 404 | Model not found on Nous inference API |
| deepseek | deepseek-v4-flash | ❌ 402 | Insufficient balance |
| ollama-cloud | llama3 | ❌ 404 | Model not found on Ollama Cloud |

## Summary

- **OpenCode Zen**: All 7 free models returned HTTP 400 (unavailable). The Zen gateway may require separate authentication or has limited free model availability.
- **OpenRouter**: Rate limited (0/50 free requests remaining today). Cannot test further today.
- **Nous**: Model not found (404) + credit balance too low (402).
- **DeepSeek**: Insufficient balance (402).
- **Ollama Cloud**: Model not found (404).

## Recommendations

1. **Top up OpenRouter credits** ($5 unlocks 1000 free model requests/day) to test remaining models.
2. **Re-authenticate OpenCode Zen backup credential** (zen-backup returned 401).
3. **Check NousResearch credit balance** — account paused.
4. **Verify DeepSeek API key** — billing exhausted.
5. **Re-run benchmarks after topping up** — model availability varies by day.

## Config Changes Applied

- `model.provider` → `opencode-zen`
- `model.default` → `deepseek-v4-flash-free`
- `fallback_providers` → `["openrouter", "nous", "deepseek"]`

## Files Updated

- `docs/openrouter-free-models-report.md` — 17 free models cataloged
- `docs/opencode-zen-openrouter-setup-report.md` — provider setup + best practices
