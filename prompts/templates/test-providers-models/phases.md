# Test Providers & Models — Phases

> Full operational phases for `prompts/test-providers-models.prompt.md`.
> Regenerated 2026-07-10 from live run (prior 2026-07-09 artifacts were stale:
> provider count 8→9 and rate-limit states flipped).

## Phase 0: Auth & Provider Inventory

- Run `hermes auth list`; inventory providers and credential status (9 live providers).
- Gate: all authorized providers captured and documented.

## Phase 1: Model Catalog Discovery

- Query each provider for available models (`hermes config show`, catalog fetch).
- Gate: catalog entries documented per provider (openrouter 40, nous 30).

## Phase 2: Free Model Extraction

- Extract free/zero-cost models per provider; record auth constraints.
- Gate: free-tier model table complete (5 benchmarked, 4 excluded).

## Phase 3: Provider-by-Provider Benchmarking

- Run 3-task benchmark (reasoning/tool calling/knowledge) on accessible free models.
- Gate: benchmark outputs saved per provider/model (15/15 tasks, 0 failures).

## Phase 4: Cross-Provider Comparison & Report

- Compile comparison report from benchmark outputs.
- Gate: comparison report generated and reviewed.

## Phase 5: Rate Limit & Fallback Chain Analysis

- Document rate limits/errors and recommend fallback chain.
- Gate: fallback recommendation completed (volatile — re-check before trust).

## Phase 6: Script Creation & Automation

- Create/update benchmark scripts in `~/AppData/Local/hermes/scripts/`.
- Gate: scripts committed/preserved and runnable (bug fixed 2026-07-10).

## Current Status (2026-07-10)

| Phase | Title | Status | Notes |
|-------|-------|--------|-------|
| 0 | Auth & Provider Inventory | ✅ Complete | 9 providers from `hermes auth list` |
| 1 | Model Catalog Discovery | ✅ Complete | OpenRouter 40, Nous 30 |
| 2 | Free Model Extraction | ✅ Complete | 5 benchmarked, 4 excluded |
| 3 | Provider-by-Provider Benchmarking | ✅ Complete | 5/5 models, 15/15 tasks, 0 failures |
| 4 | Cross-Provider Comparison & Report | ✅ Complete | Live scores (xai-oauth fastest) |
| 5 | Rate Limit & Fallback Chain Analysis | ✅ Complete | xai-oauth→huggingface→…→openai-codex(dead) |
| 6 | Script Creation & Automation | ✅ Complete | `benchmark_providers.py` fixed + results |
