# Phase 4: Cross-Provider Comparison & Report

> Template for `test-providers-models`. Apply ranking algorithm and generate comparison.

## Ranking Algorithm

```python
def sort_key(m):
    vision = 2 if m.vision else 0
    reason = 1 if m.reasoning else 0
    ctx = min(m.ctx, 2_000_000) / 2_000_000
    return (vision, reason, ctx)  # descending

chain = sorted(working_models, key=sort_key, reverse=True)
```

## Expected Order (verified 2026-08-07)

1. `nemotron-3-ultra-free` (opencode-zen, 1M, reasoning✓)
2. `nvidia/nemotron-3-ultra-550b-a55b:free` (openrouter, 1M, ✓)
3. `nvidia/nemotron-3-super-120b-a12b:free` (openrouter, 1M, ✓)
4. `gemini-2.5-flash` (gemini, 1M, ✓)
5. `nemotron-3-ultra` (ollama-cloud, 1M, ✓)
6. `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` (openrouter, 256K, ✓)
7. `deepseek-v4-flash-free` (opencode-zen, 128K, ✓) — PRIMARY
8. `google/gemma-4-31b-it:free` (openrouter, 262K, ✗)
9. `google/gemma-4-26b-a4b-it:free` (openrouter, 262K, ✗)
10. `openai/gpt-oss-20b:free` (openrouter, 131K, ✗)

## Verification Gate

- [ ] Ordering is deterministic (vision > reasoning > context)
- [ ] No vision-capable free models promoted (current verified set has none)
- [ ] Primary model (`deepseek-v4-flash-free`) is the proven working model that has accomplished prior requests
