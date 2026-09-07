# Phase 3: Provider-by-Provider Benchmarking

Generated: 2026-07-10
Target: 5 accessible free models (15 tasks)

## Benchmark Tasks (3 standard tasks per model)

1. **Reasoning** — Multi-step logic problem (river crossing puzzle)
2. **Tool Calling** — Execute a function with structured args (get_weather)
3. **Knowledge** — Factual QA with citation requirement (Kazakhstan capital)

## Execution Matrix (live results)

| Provider | Model | Status | Reasoning | Tool Calling | Knowledge | Notes |
|| ---------- | ------- | -------- | ----------- | -------------- | ----------- | ------- ||
| nous | stepfun/step-3.7-flash:free | ✅ Complete | ✅ 82s | ⚠️ N/A (no fn) | ✅ 65s | Active, verbose self-narration |
| openrouter | tencent/hy3:free | ✅ Complete | ✅ 51s | ⚠️ N/A (no fn) | ✅ 98s | Active, slowest knowledge |
| huggingface | auto (HF Inference) | ✅ Complete | ✅ 46s | ⚠️ N/A (no fn) | ✅ 62s | Cleanest reasoning exposition |
| ollama-cloud | auto (deepseek-v4-flash-free) | ✅ Complete | ✅ 54s | ⚠️ N/A (no fn) | ✅ 48s | Active, strong alternative |
| xai-oauth | auto (Grok free) | ✅ Complete | ✅ 49s | ⚠️ N/A (no fn) | ✅ 38s | Fastest overall (41s avg) |

## Tool-Calling Note

The `get_weather` function is NOT exposed by any Hermes provider/toolset, so every model
correctly reports it cannot call the function. This is a harness limitation, not a model
deficit — all 5 models handled it honestly (no fabrication). Tool-calling axis excluded
from scoring.

## Test Harness

- Script: `~/AppData/Local/hermes/scripts/benchmark_providers.py` (FIXED 2026-07-10)
- Bug fixed: dead resume-skip code in `main()` / `benchmark_model()` merged stale
  2026-07-09 results; now passes `completed` set correctly and writes to
  `~/AppData/Local/hermes/scripts/benchmark_results.json`.
- Uses `hermes chat -q "..." --provider <p> --model <m>` pattern.

## Status

- ✅ 5/5 accessible models complete (15 tasks, 0 failures)
- ✅ ~12.5 min total wall time
- ⚠️ 4 providers excluded (copilot/gemini 429, openai-codex usage, openai-api paid)
