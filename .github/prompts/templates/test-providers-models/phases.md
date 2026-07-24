# Test Providers & Models — Phases

> Full operational phases for `prompts/test-providers-models.prompt.md`.

## Phase 0: Auth & Provider Inventory

- Enumerate authorized providers using live Hermes auth/config as source of truth.
- Gate: all authorized providers captured and documented.

## Phase 1: Model Catalog Discovery

- Catalog available models per provider.
- Gate: catalog entries documented per provider.

## Phase 2: Free Model Extraction

- Extract free-tier or otherwise accessible models into a table.
- Gate: free-tier model table complete.

## Phase 3: Provider-by-Provider Benchmarking

- Run lightweight benchmarks/availability checks.
- Gate: benchmark outputs saved per provider/model.

## Phase 4: Cross-Provider Comparison & Report

- Compare findings across providers/models.
- Gate: comparison report generated and reviewed.

## Phase 5: Rate Limit & Fallback Chain Analysis

- Document rate-limit behavior and fallback recommendations.
- Gate: fallback recommendation completed.

## Phase 6: Script Creation & Automation

- Create or update scripts that capture the above for reruns.
- Gate: scripts runnable and preserved.

## Completion

- Append progress after each phase.
- Append evidence to `docs/orchestrator-verification.md` after each phase.
