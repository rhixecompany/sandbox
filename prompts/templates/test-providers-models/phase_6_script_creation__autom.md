# Phase 6: Script Creation & Automation

Generated: 2026-07-10
Source: `benchmark_providers.py` (fixed) + `benchmark_results.json` (regenerated)

## Summary

- `benchmark_providers.py` — standardized 3-task benchmark harness (FIXED this run)
- Supports all accessible providers via `hermes chat` CLI
- Resume capability (skips completed tasks) — bug fixed
- JSON output for Phase 4 comparison

## Fix Applied (2026-07-10)

The original `main()` had a dead resume-skip check (it iterated tasks but never passed
`completed` into `benchmark_model`, which re-ran all 3 tasks unconditionally and merged
stale 2026-07-09 rows). Corrected:
- `benchmark_model(provider, model, completed)` now accepts + honors the skip set.
- `main()` updates `completed` after each model and writes to
  `~/AppData/Local/hermes/scripts/benchmark_results.json`.
- `ACCESSIBLE_MODELS` / `RATE_LIMITED_MODELS` re-pointed to live 2026-07-10 state
  (gemini + openrouter swapped places vs 2026-07-09).

## Script: `benchmark_providers.py`

```python
# Location: ~/AppData/Local/hermes/scripts/benchmark_providers.py
# Usage: python benchmark_providers.py

Features:
- 3 standardized tasks: reasoning, tool_calling, knowledge
- Runs across accessible free models (nous, openrouter, huggingface, ollama-cloud, xai-oauth)
- Handles rate-limited models (skipped this run; re-auth when cooldown clears)
- Outputs benchmark_results.json with latency, success, response
- Resume-safe: skips already-completed (provider, model, task) tuples
```

## Deliverables

- `benchmark_results.json` — raw benchmark data (15 entries, 5 models × 3 tasks), regenerated
- `benchmark_providers.py` — reusable harness (bug fixed)
- `docs/test-providers-models-2026-07-10.md` — full live report

## Status

- ✅ `benchmark_providers.py` fixed and validated
- ✅ Benchmark execution complete (15/15 tasks, 0 failures)
- ✅ Results regenerated from live run (no stale 2026-07-09 rows)
