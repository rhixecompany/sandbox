# Phase 6: Script Creation & Automation

> Template for `test-providers-models`. Create or update automation scripts with web research.

## Requirements

**Script must include web research calls** — `web_search` / `web_extract` for refreshing provider info before each run, not just local `hermes` commands.

## Deliverables

- `benchmark_providers.py` — standardized 3-task benchmark harness
- `benchmark_results.json` — raw benchmark data
- `docs/test-providers-models-2026-07-10.md` — full live report

## Script Header Requirement

```python
# Web research sources for refresh:
# - https://openrouter.ai/models (catalog)
# - https://docs.nousresearch.com/ (provider docs)
# - https://hermes-agent.nousresearch.com/docs/api/model-catalog.json
```

## Verification Gate

- [ ] Scripts are runnable (`python scripts/run.py` exits 0)
- [ ] Web research sources documented in script header
- [ ] All 6 phase templates have at least one `.md` file in `templates/`
