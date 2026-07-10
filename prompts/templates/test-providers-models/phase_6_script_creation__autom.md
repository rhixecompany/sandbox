# Phase 6: Script Creation & Automation

Generated: 2026-07-09
Source: `benchmark_providers.py` + `test_models.py` update

## Summary

- Created `benchmark_providers.py` — standardized 3-task benchmark harness
- Supports all 6+ providers via `hermes chat` CLI
- Resume capability (skips completed tasks)
- JSON output for Phase 4 comparison

## Script: `benchmark_providers.py`

```python
# Location: ~/AppData/Local/hermes/scripts/benchmark_providers.py
# Usage: python benchmark_providers.py

Features:
- 3 standardized tasks: reasoning, tool_calling, knowledge
- Runs across accessible models (gemini, nous, huggingface, ollama-cloud, xai-oauth)
- Handles rate-limited models with retry-after-cooldown logic
- Outputs benchmark_results.json with latency, success, response
- Resume-safe: skips already-completed (provider, model, task) tuples
```

## Integration with `test_models.py`

The existing `test_models.py` stub should be updated to:

1. Import and reuse `benchmark_providers.py` logic
2. Add provider-specific model discovery
3. Generate the Phase 4 comparison report

## Deliverables

- `benchmark_results.json` — raw benchmark data (15 entries, 5 models × 3 tasks)
- `benchmark_providers.py` — reusable harness
- Updated `test_models.py` with full provider support

## Status

- ✅ `benchmark_providers.py` created and validated
- ✅ Benchmark execution complete (15/15 tasks for accessible models)
- ⏳ Integration with `test_models.py` pending
