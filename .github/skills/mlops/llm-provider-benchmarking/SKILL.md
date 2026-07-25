---
name: llm-provider-benchmarking
description: Class-level skill for inventorying, benchmarking, and comparing LLM providers/models in Hermes Agent. Covers 7-phase workflow from auth inventory through fallback chain analysis.
trigger: /test-providers-models or any task requiring multi-provider LLM benchmarking
version: 1.0.0
---

# LLM Provider Benchmarking

> Comprehensive workflow for auditing authorized providers, discovering free-tier models, running standardized benchmarks, and producing cross-provider comparison reports with validated fallback chains.

## When to Use

- Auditing LLM provider credentials and usage limits via `hermes auth list`
- Evaluating free-tier model capabilities before committing to paid plans
- Planning multi-provider AI deployments with fallback chains
- Periodic re-benchmarking to detect provider degradation

## Phase Workflow (7 Phases)

| Phase | Title | Tier | Profile | Key Output |
|-------|-------|------|---------|------------|
| 0 | Auth & Provider Inventory | Needed | `default` | Live provider inventory from `hermes auth list` |
| 1 | Model Catalog Discovery | Needed | `research-analyst` | Model catalogs per provider |
| 2 | Free Model Extraction | Needed | `code-architect` | Free/zero-cost model table with tier |
| 3 | Provider-by-Provider Benchmarking | Recommended | `code-architect` | 3-task benchmark results per accessible model |
| 4 | Cross-Provider Comparison & Report | Recommended | `research-analyst` | Scored comparison + fallback chain |
| 5 | Rate Limit & Fallback Chain Analysis | Optional | `adminbot` | Cooldown profiles + validated chain |
| 6 | Script Creation & Automation | Recommended | `code-architect` | Reusable `benchmark_providers.py` + JSON results |

## Benchmark Tasks (Standard 3-Task Suite)

1. **Reasoning** — Multi-step logic puzzle (wolf/goat/cabbage river crossing)
2. **Tool Calling** — Execute function with structured args (`get_weather(location)`)
3. **Knowledge** — Factual QA with citation requirement

## Key Techniques

### Provider Invocation Pattern
```bash
# Use Hermes CLI, NOT direct API — keys in credential store not exported to subprocess
hermes chat -q "prompt" --provider <provider> --model <model> --toolsets "skills,web,terminal,file"
```

### Rate Limit Handling
- Run `hermes auth list` before each benchmark batch
- Parse cooldown from status strings (e.g., "429 rate limited (~2h cooldown)")
- Skip providers with >5min cooldown; re-check after primary completes
- Log all fallbacks for chain optimization

### Fallback Chain Validation
**Critical observation**: Both `ollama-cloud` and `xai-oauth` with `model=auto` fell back to `deepseek-v4-flash-free` via `opencode-zen`. This is a **feature of Hermes provider chain**, not failure — fallback models scored 9/8/8.

### Resume-Safe Benchmarking
The `benchmark_providers.py` harness:
- Tracks completed (provider, model, task) tuples in JSON
- Skips already-completed work on re-run
- Outputs structured results for Phase 4 comparison

## Scoring Rubric

| Dimension | 9-10 | 7-8 | 4-6 | 0-3 |
|-----------|------|-----|-----|-----|
| Reasoning | Correct + clear explanation | Correct, minor gaps | Partial | Incorrect |
| Tool Calling | Correct function + args + handles result | Minor arg issues, self-corrects | Wrong function/malformed | No tool use |
| Knowledge | Accurate + citation | Accurate, no citation | Partially correct | Hallucinated |

## Deliverables Structure

```
templates/test-providers-models/
├── phase_0_auth__provider_invento.md
├── phase_1_model_catalog_discover.md
├── phase_2_free_model_extraction_.md
├── phase_3_provider-by-provider_b.md
├── phase_4_cross-provider_compari.md
├── phase_5_rate_limit_fallback_c.md
├── phase_6_script_creation__autom.md
└── phases.md                    # Status summary

scripts/
└── benchmark_providers.py       # Reusable harness

references/
├── benchmark_results.json       # Raw results (15 entries for 5 models)
├── provider-benchmark-report-final.md  # Comprehensive report
└── harness-fix.md               # Resume-bug fix + live-run recipe (see Pitfalls)
```

## Pitfalls & Lessons

- **OpenRouter/OpenAI keys**: Stored in Hermes credential store — NOT available as env vars in subprocesses. Must use `hermes chat --provider X` pattern.
- **Auto model selection**: Providers with `model=auto` may fall back unexpectedly. Document the actual model used.
- **Rate limit cooldowns**: OpenAI Codex can have 29-day cooldowns. Treat as "dead" until reset.
- **HF Inference**: Slower (~100s avg) but reliable daily quota — good fallback 2.
- **Gemini default**: `gemini-3.5-flash` is default in config, no observed rate limits, fastest (40s avg).
- **Phase templates**: Update with live data each run — don't rely on archived artifacts.

### CRITICAL: Re-derive from live state — never replay archived phase templates
The bundled `prompts/templates/test-providers-models/*.md` phase files (and any
"generated on <date>" report) are a SNAPSHOT of one prior run. Provider counts and
rate-limit statuses DRIFT between runs:
- The prompt hardcodes 6 providers, but live `hermes auth list` returned **9** (adds
  gemini, openai-codex, xai-oauth, openai-api).
- Rate-limit state FLIPS: gemini was active in one run and 429-limited in the next;
  openrouter flipped the opposite way.
Replaying a stale template reports wrong providers and wrong fallback chains.
**Always** run `hermes auth list` fresh, build the free-model list from that, and treat
any existing phase template as a structural guide only — never as data.

### CRITICAL: The benchmark harness has a resume bug — fix before trusting re-runs
`benchmark_providers.py`'s resume logic was BROKEN: the per-task skip-check lived in the
`main()` loop but `benchmark_model()` ignored the `completed` set and re-ran all 3 tasks
unconditionally. On a second run it would (a) duplicate work and (b) **merge stale rows
from an existing `benchmark_results.json`** into the live run, poisoning the report.
Fix (see `references/harness-fix.md`):
1. Change `benchmark_model(provider, model)` → `benchmark_model(provider, model, completed)`
   and skip `(provider, model, task)` keys already in `completed`.
2. In `main()`, call `benchmark_model(..., completed)`, then
   `completed.update((r.provider, r.model, r.task) for r in model_results)`.
3. **Clear stale data before a live re-run**: `rm -f benchmark_results.json` (or use a
   datestamped output path). The resume feature is only safe if the JSON reflects THIS run.

### Tool-calling task is N/A by design — score honestly, not as failure
The standard 3-task suite includes "call `get_weather(location)`". NO Hermes provider
exposes a `get_weather` function/toolset, so every model correctly reports it cannot call
it. This is expected and honest (no fabrication) — exclude tool-calling from scoring or
record it as "N/A (honest decline)". Do NOT mark the model as failed on that axis.

## Verification Checklist

- [ ] Phase 0: All providers from `hermes auth list` captured with credential status
- [ ] Phase 1: Model catalogs queried per provider
- [ ] Phase 2: Free models extracted and tiered (Needed/Recommended/Optional)
- [ ] Phase 3: Benchmark run on all accessible free models (3 tasks each)
- [ ] Phase 4: Cross-provider comparison with scores + fallback chain
- [ ] Phase 5: Rate limits documented + fallback chain validated
- [ ] Phase 6: `benchmark_providers.py` updated + results JSON committed
- [ ] All phase files updated with current run data (not archived)

## Related Skills

- `plans-and-specs` — Phase planning and progress tracking
- `verification-before-completion` — Cross-reference all phases before claiming done
- `using-superpowers` — Workflow foundation and tool conventions
- `user-communication-preferences` — Execution style and preferences