## Objective

Inventory, discover model catalogs, extract free-tier models, benchmark, and compare all 7 authorized LLM providers; produce a cross-provider comparison and rate-limit report plus reusable automation scripts.

## Source Plan

`plan/prompt-orchestration-comprehensive-plan.md` → Phase 4 (§4.5), sub-phases 4.1–4.7

## Deliverables

- D13 `hermes auth list` provider inventory (7/7 authorized, auth status captured)
- `docs/model-catalogs.md`
- `judge_results/provider-benchmarks.md`
- `docs/provider-comparison.md`
- `docs/rate-limit-report.md`
- `~/AppData/Local/hermes/scripts/benchmark*.py`

## Sub-phases

4.1 Auth inventory · 4.2 Catalog discovery · 4.3 Free-model extraction · 4.4 Benchmark · 4.5 Cross-provider comparison · 4.6 Rate-limit analysis · 4.7 Script creation & automation

## Success Criteria

7/7 authorized providers captured with auth status; free-tier comparison report; rate-limit analysis with retry-after notes; benchmark automation scripts created.

## Safety Gate G4

Never hardcode API keys — use `$ENV_VAR` references only. Respect provider rate limits (HTTP 429); note retry-after time, do NOT retry aggressively.

## Dependencies

Phase 3 complete. Final phase.
