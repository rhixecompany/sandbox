# Test Providers & Models — Phases

> Operational phases for `test-providers-models.prompt.md`.
> Each phase uses web research (`web_search`, `web_extract`) alongside `hermes` CLI.

## Phase 0: Auth & Provider Inventory

- Enumerate providers: `hermes auth list`
- Web research: check provider docs pages for model endpoints
- Gate: all 9 providers captured; at least one rate-limit warning noted

## Phase 1: Model Catalog Discovery

- Catalog available models per provider (OpenRouter models page, Nous portal)
- Web research: `firecrawl-search` on `https://openrouter.ai/models`
- Gate: catalog entries documented per provider

## Phase 2: Free Model Extraction

- Filter `pricing=0` or `:free` suffix models
- Cross-reference with `hermes auth list` (exclude rate-limited providers)
- Gate: free-tier table complete with web-research annotations

## Phase 3: Provider-by-Provider Benchmarking

- Delegate capability probes to 3 subagent clusters (A, B, C)
- Each subagent returns structured capability JSON
- Gate: benchmark outputs saved; web community context appended

## Phase 4: Cross-Provider Comparison & Report

- Apply ranking algorithm (vision → reasoning → context)
- Generate comparison table blending local + web data
- Gate: comparison report generated; discrepancies noted

## Phase 5: Rate Limit & Fallback Chain Analysis

- Document rate limits per provider
- Configure `hermes config set fallback_providers` as YAML list
- Verify list type via Python `yaml` inspection
- Gate: chain config verified; each provider has working `default_model`

## Phase 6: Script Creation & Automation

- Create/update `benchmark_providers.py`
- Script header must document web research sources
- Gate: scripts runnable; sources preserved

## Completion

Append progress after each phase. Save evidence under `docs/research/<provider>/` with `SOURCE.md` attribution files.
