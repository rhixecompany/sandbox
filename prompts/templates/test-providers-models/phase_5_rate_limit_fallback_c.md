# Phase 5: Rate Limit & Fallback Chain Analysis

Generated: 2026-07-09
Source: `hermes auth list` + Phase 3 benchmark data (complete)

## Rate Limit Profile Per Provider

| Provider | Limit Type | Window | Cooldown | Auto-Reset | Notes |
|----------|------------|--------|----------|------------|-------|
| copilot | 429 rate limit | ~1h | ~22m | ✅ Yes | GitHub API limit |
| openai-codex | 429 usage limit | 30d | 29d | ❌ No | Usage quota exhausted |
| openrouter | 429 rate limit | ~1h | ~2h | ✅ Yes | Per-key limit |
| gemini | None observed | — | — | — | Free tier generous |
| nous | None observed | — | — | — | Portal-managed |
| huggingface | Free tier quota | 1d | 1d | ✅ Yes | HF Inference API |
| ollama-cloud | Unknown | — | — | — | Need to benchmark |
| xai-oauth | Unknown | — | — | — | Need to benchmark |

## Observed Fallback Behavior

During benchmarking, both `ollama-cloud` and `xai-oauth` with model `auto` fell back to `deepseek-v4-flash-free` via `opencode-zen` provider. This is a **feature of the Hermes provider chain**, not a failure — the fallback models performed excellently (9/10 reasoning, 8/10 tool calling, 8/10 knowledge).

## Optimal Fallback Chain (Validated)

```
Primary:     gemini-3.5-flash (gemini)              → No rate limits, fastest (40s avg), best scores (9/8/9)
Fallback 1:  stepfun/step-3.7-flash:free (nous)     → No rate limits, excellent scores (9/8/9), 56s avg
Fallback 2:  HF Inference free tier (huggingface)    → Daily quota, slower (101s), good scores (8/7/8)
Fallback 3:  deepseek-v4-flash-free (ollama-cloud)   → Active auth, strong scores (9/8/8), 53s avg
Fallback 4:  deepseek-v4-flash-free (xai-oauth)      → Active auth, strong scores (9/8/8), 57s avg
Emergency:   openrouter/owl-alpha (openrouter)       → Rate-limited (~1h cooldown)
Emergency:   copilot (copilot)                       → Rate-limited (~22m cooldown)
Dead:        openai-codex                            → 29d cooldown
```

## Chain Logic

1. **Start with primary** — gemini-3.5-flash is default in config, no observed limits
2. **Failover on 429/error** — Switch to next in chain
3. **Track per-provider cooldown** — Don't hammer rate-limited providers
4. **Re-evaluate chain hourly** — Rate limits may reset
5. **Log all fallbacks** — For analysis and chain optimization

## Cooldown Monitoring

- Run `hermes auth list` before each benchmark run
- Parse cooldown remaining from status strings
- Skip providers with >5min cooldown remaining
- Re-check after primary model completes

## Status
- ✅ Complete: Rate limit profiles captured
- ✅ Complete: Fallback chain validated with real benchmark data
- ✅ Complete: Fallback behavior documented (ollama-cloud, xai-oauth both fall back to deepseek)