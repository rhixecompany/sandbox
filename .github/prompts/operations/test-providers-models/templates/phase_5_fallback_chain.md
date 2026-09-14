# Phase 5: Rate Limit & Fallback Chain Analysis

> Template for `test-providers-models`. Analyze rate limits and recommend fallback chain.

## Rate Limit Profile (live 2026-07-10)

|| Provider | Limit Type | Status | Cooldown ||
|| --- | --- | --- | --- ||
|| copilot | 429 rate limit | ⚠️ Limited | ~22m ||
|| gemini | 429 rate limit | ⚠️ Limited | unknown ||
|| openai-codex | usage limit | ⚠️ Exhausted | 28d 20h ||
|| openrouter | 429 (was limited) | ✅ Active now | — ||
|| huggingface | daily quota | ✅ Active | 1d ||
|| nous | portal-managed | ✅ Active | — ||
|| ollama-cloud | unknown | ✅ Active | — ||
|| xai-oauth | unknown | ✅ Active | — ||
|| openai-api | paid only | n/a | — ||

## Recommended Fallback Chain

```
Primary:     xai-oauth (auto / Grok free)     → fastest (41s avg), correct, active
Fallback 1:  huggingface (auto)                  → cleanest reasoning, daily quota
Fallback 2:  ollama-cloud (auto)                 → strong, active
Fallback 3:  nous (stepfun/step-3.7-flash:free)  → active, slightly verbose
Fallback 4:  openrouter (tencent/hy3:free)       → active, slower knowledge
Emergency:   copilot                              → 429 (~22m cooldown)
Emergency:   gemini                               → 429 (cooldown)
Dead:        openai-codex                         → 28d 20h cooldown
```

## Chain Logic

1. Start with primary — fastest + correct, no observed limits.
2. During probe runs, skip every model for a provider whose auth inventory is rate-limited; never add it to the primary or fallback chain.
3. During live sessions, fail over on 429/error — switch to the next eligible provider/model in the configured chain.
4. Track per-provider cooldown — don't hammer rate-limited providers.
5. Re-evaluate chain hourly — rate limits are volatile.
6. Log all fallbacks — for analysis and optimization.

## Verification Gate

- [ ] Fallback chain configured via `hermes config set fallback_providers`
- [ ] `fallback_providers` is a YAML list (verified via Python yaml inspection)
- [ ] Each provider in chain has working `default_model` set
- [ ] No provider with a current `rate-limited`/`429` auth status appears in the chain
