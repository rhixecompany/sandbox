# Phase 5: Rate Limit & Fallback Chain Analysis

Generated: 2026-07-10
Source: `hermes auth list` + Phase 3 benchmark data (live)

## Rate Limit Profile Per Provider

| Provider | Limit Type | Status (live) | Cooldown | Auto-Reset |
|| ---------- | ----------- | --------------- | ---------- | ------------ ||
| copilot | 429 rate limit | ⚠️ Limited | ~22m | ✅ Yes |
| gemini | 429 rate limit | ⚠️ Limited | unknown | ✅ Yes |
| openai-codex | usage limit | ⚠️ Exhausted | 28d 20h | ❌ No |
| openrouter | 429 (was limited) | ✅ Active now | — | ✅ Yes |
| huggingface | daily quota | ✅ Active | 1d | ✅ Yes |
| nous | portal-managed | ✅ Active | — | — |
| ollama-cloud | unknown | ✅ Active | — | — |
| xai-oauth | unknown | ✅ Active | — | — |
| openai-api | paid only | n/a | — | — |

## Recommended Fallback Chain (Validated 2026-07-10)

```
Primary:     xai-oauth (auto / Grok free)        → fastest (41s avg), correct, active
Fallback 1:  huggingface (auto)                   → cleanest reasoning, daily quota
Fallback 2:  ollama-cloud (auto)                  → strong, active
Fallback 3:  nous (stepfun/step-3.7-flash:free)   → active, slightly verbose
Fallback 4:  openrouter (tencent/hy3:free)        → active, slower knowledge
Emergency:   copilot                              → 429 (~22m cooldown)
Emergency:   gemini                               → 429 (cooldown)
Dead:        openai-codex                         → 28d 20h cooldown
```

## Chain Logic

1. **Start with primary** — xai-oauth is fastest + correct, no observed limits.
2. **Failover on 429/error** — Switch to next in chain.
3. **Track per-provider cooldown** — Don't hammer rate-limited providers.
4. **Re-evaluate chain hourly** — Rate limits are volatile (gemini/openrouter flipped since 2026-07-09).
5. **Log all fallbacks** — For analysis and chain optimization.

## Status

- ✅ Complete: Rate limit profiles captured (live)
- ✅ Complete: Fallback chain validated with real benchmark data
- ⚠️ Volatile: re-check `hermes auth list` before trusting any cached cooldown
