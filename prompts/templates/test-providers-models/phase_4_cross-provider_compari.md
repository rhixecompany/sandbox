# Phase 4: Cross-Provider Comparison & Report

Generated: 2026-07-09
Source: Phase 3 benchmark results (5/5 accessible models complete)

## Comparison Framework

| Model | Provider | Reasoning Score | Tool Calling Score | Knowledge Score | Latency (avg) | Rate Limits | Verdict |
|-------|----------|-----------------|-------------------|-----------------|---------------|-------------|---------|
| gemini-3.5-flash | gemini | 9/10 | 8/10 | 9/10 | 40s | ✅ None | 🥇 Primary |
| stepfun/step-3.7-flash:free | nous | 9/10 | 8/10 | 9/10 | 56s | ✅ None | 🥈 Fallback 1 |
| HF Inference (auto) | huggingface | 8/10 | 7/10 | 8/10 | 101s | ✅ Daily quota | 🥉 Fallback 2 |
| auto (fallback: deepseek-v4-flash-free) | ollama-cloud | 9/10 | 8/10 | 8/10 | 53s | ✅ Active | 🏅 Strong Alternative |
| auto (fallback: deepseek-v4-flash-free) | xai-oauth | 9/10 | 8/10 | 8/10 | 57s | ✅ Active | 🏅 Strong Alternative |

## Scoring Criteria

### Reasoning (0-10)

- 10: Solves multi-step logic correctly with clear explanation
- 7-9: Correct answer, minor gaps in reasoning
- 4-6: Partial credit, significant gaps
- 0-3: Incorrect or no meaningful reasoning

**Results:**

- **gemini-3.5-flash**: Solved river crossing correctly, clear step-by-step explanation, identified constraints properly
- **stepfun/step-3.7-flash:free**: Solved river crossing correctly, clear reasoning, acknowledged constraints
- **HF Inference**: Solved river crossing correctly, slightly more verbose but correct
- **ollama-cloud (deepseek-v4-flash-free)**: Solved river crossing correctly, detailed step-by-step with verification, identified the "critical move" (step 4)
- **xai-oauth (deepseek-v4-flash-free)**: Solved river crossing correctly, clear reasoning with emoji diagram, identified the "lightbulb moment"

### Tool Calling (0-10)

- 10: Correct function name, valid args, handles result
- 7-9: Minor arg issues, self-corrects
- 4-6: Wrong function or malformed args
- 0-3: No tool use or complete failure

**Results:**

- **gemini-3.5-flash**: Recognized no get_weather function, used web_search instead, found London weather, reported in requested format
- **stepfun/step-3.7-flash:free**: Recognized no get_weather function, used web_search, found London weather, reported result
- **HF Inference**: Recognized no get_weather function, used web_search, found London weather, reported result
- **ollama-cloud (deepseek-v4-flash-free)**: Recognized no get_weather function, used web_search, found London weather, reported result
- **xai-oauth (deepseek-v4-flash-free)**: Recognized no get_weather function, used web_search + skills_list, found London weather via WeatherAPI, formatted as requested JSON

### Knowledge (0-10)

- 10: Accurate answer with citation
- 7-9: Accurate, missing citation
- 4-6: Partially correct
- 0-3: Incorrect or hallucinated

**Results:**

- **gemini-3.5-flash**: Correctly identified Astana (formerly Nur-Sultan), cited Wikipedia
- **stepfun/step-3.7-flash:free**: Correctly identified Astana, cited Wikipedia
- **HF Inference**: Correctly identified Astana, cited Wikipedia
- **ollama-cloud (deepseek-v4-flash-free)**: Correctly identified Astana, cited Wikipedia
- **xai-oauth (deepseek-v4-flash-free)**: Correctly identified Astana, cited Wikipedia with infobox reference

## Fallback Chain Recommendation (Based on Complete Data)

```
Primary:     gemini-3.5-flash (gemini)           → No rate limits, fastest, best scores
Fallback 1:  stepfun/step-3.7-flash:free (nous)  → No rate limits, excellent scores
Fallback 2:  HF Inference free tier (huggingface) → Daily quota, slower, good scores
Fallback 3:  deepseek-v4-flash-free (ollama-cloud) → Active auth, strong scores, fallback behavior
Fallback 4:  deepseek-v4-flash-free (xai-oauth)    → Active auth, strong scores, fallback behavior
Emergency:   openrouter/owl-alpha (openrouter)    → Rate-limited (~1h cooldown)
Emergency:   copilot (copilot)                    → Rate-limited (~22m cooldown)
Dead:        openai-codex                         → 29d cooldown
```

## Chain Logic

1. **Start with primary** — gemini-3.5-flash is default in config, no observed limits
2. **Failover on 429/error** — Switch to next in chain
3. **Track per-provider cooldown** — Don't hammer rate-limited providers
4. **Re-evaluate chain hourly** — Rate limits may reset
5. **Log all fallbacks** — For analysis and chain optimization

## Status

- ✅ Complete: 5/5 accessible models benchmarked (15 tasks)
- ⚠️ 3 rate-limited models need cooldown monitoring
- 📝 Full report ready for review
