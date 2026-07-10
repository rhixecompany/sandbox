# Test Providers & Models — Phases

> Full operational phases for `prompts/test-providers-models.prompt.md`.

## Phase 0: Auth & Provider Inventory
- Run `hermes auth list`; inventory providers and credential status.
- Gate: all authorized providers captured and documented.

## Phase 1: Model Catalog Discovery
- Query each provider for available models (`hermes config show`, catalog fetch).
- Gate: catalog entries documented per provider.

## Phase 2: Free Model Extraction
- Extract free/zero-cost models per provider; record API/runtime constraints.
- Gate: free-tier model table complete.

## Phase 3: Provider-by-Provider Benchmarking
- Run 3-task benchmark (reasoning/tool calling/knowledge) on accessible free models.
- Gate: benchmark outputs saved per provider/model.

## Phase 4: Cross-Provider Comparison & Report
- Compile comparison report from benchmark outputs.
- Gate: comparison report generated and reviewed.

## Phase 5: Rate Limit & Fallback Chain Analysis
- Document rate limits/errors and recommend fallback chain.
- Gate: fallback recommendation completed or explicitly deferred.

## Phase 6: Script Creation & Automation
- Create/update benchmark scripts in `~/AppData/Local/hermes/scripts/`.
- Gate: scripts committed/preserved and runnable.

## Current Status (2026-07-09)

| Phase | Title | Status | Notes |
|-------|-------|--------|-------|
| 0 | Auth & Provider Inventory | ✅ Complete | 9 providers from `hermes auth list` |
| 1 | Model Catalog Discovery | ✅ Complete | OpenRouter 27, Nous 21, others via auth |
| 2 | Free Model Extraction | ✅ Complete | 17+ free models cataloged with tier |
| 3 | Provider-by-Provider Benchmarking | ✅ Complete | 5/5 accessible models, 15/15 tasks |
| 4 | Cross-Provider Comparison & Report | ✅ Complete | Full comparison with scores |
| 5 | Rate Limit & Fallback Chain Analysis | ✅ Complete | Validated chain with fallback behavior |
| 6 | Script Creation & Automation | ✅ Complete | `benchmark_providers.py` + results |