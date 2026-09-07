# Test Providers & Models - Implementation Plan

## Overview
This plan implements the complete test-providers-models workflow: inventory all authorized providers, probe free models, rank by capability, and configure Hermes with the optimal fallback chain.

## Phases

### Phase 1: Inventory & Auth Capture
- [ ] Run `hermes auth list` and capture full provider state
- [ ] Run `hermes config show` to capture current config
- [ ] Run `hermes status` and `hermes insights` 
- [ ] Run `hermes fallback list` to capture current fallback chain
- [ ] Save all outputs to `.hermes/reports/`

### Phase 2: Free Model Catalog Generation
- [ ] Web research all authorized providers for `:free` tier models
- [ ] Extract model IDs, context lengths, reasoning support, max output
- [ ] Document API URLs and documentation URLs
- [ ] Build `templates/free-model-catalog.md` with all models
- [ ] Build `templates/free-model-catalog-updated.md` with capabilities

### Phase 3: Live Probing
- [ ] Execute `scripts/run_probes.py` with concurrent probes
- [ ] Capture exit codes, response claims (knowledge cutoff, context, reasoning, max output)
- [ ] Handle 429 rate limits gracefully (fallback to baseline)
- [ ] Write results to `templates/probe-live-template.md`
- [ ] Save JSON results to `.hermes/reports/test-providers-probe-results.json`

### Phase 4: Ranking & Scoring
- [ ] Execute `scripts/apply_config.py` to score all probed models
- [ ] Apply scoring formula: recent_kc + context_ge_32k + reasoning + max_output_ge_4k + exit_0
- [ ] Rank top 5 models by score (descending), tiebreak by lowest latency
- [ ] Write `templates/ranking-report.md` with full ranking

### Phase 5: Configuration
- [ ] Set primary model via `hermes config set model.provider <provider>`
- [ ] Set primary model via `hermes config set model.default <provider>:<model>`
- [ ] Clear existing fallback chain via `hermes fallback clear`
- [ ] Add top 4 fallback models via `hermes fallback add <provider>:<model>` (4x)
- [ ] Set each provider's `default_model` in the providers: block

### Phase 6: Verification
- [ ] Run `hermes config check` - must exit 0
- [ ] Run `hermes config show` - verify model.provider and model.default
- [ ] Run `hermes fallback list` - verify fallback chain
- [ ] Run `hermes chat --provider <top1> --model <top1> -q "ping" --oneshot` - must exit 0
- [ ] Update `docs/free-model-selection.md`
- [ ] Run `scripts/audit-sessions.py` to rank sessions

### Phase 7: Cleanup & Dedup
- [ ] Remove duplicate entries from catalog
- [ ] Delete non-working providers from fallback chain
- [ ] Verify all files are on disk without issues
- [ ] Run `plans-judge` skill on `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md`
- [ ] Debug fix all issues, raise score to >= 98

## Provider Clusters for Subagent Delegation

### Cluster A: OpenCode Zen + OpenRouter + Deepseek
- Provider models to probe: opencode-zen models, openrouter :free models, deepseek variants

### Cluster B: Google/Gemini + Ollama Cloud + Nous/HuggingFace
- Provider models to probe: gemini models, ollama-cloud nemotron-3-ultra, nous/hf models

### Cluster C: OAuth/codex/copilot/xAI
- Provider models to probe: openai-codex, copilot, xai-oauth models

Each subagent receives the full Context Block from the prompt and returns structured `provider | model | working | vision | reasoning | ctx` lines.

## Scoring Algorithm
```
score = (1 if knowledge_cutoff >= 2025) 
      + (1 if context_length >= 32000) 
      + (1 if reasoning == yes) 
      + (1 if max_output >= 4096) 
      + (1 if exit == 0)
Max score = 5. Tiebreak by lowest elapsed_s.
```

## Top Ranking Rule (from 2026-08-07 baseline, no vision anywhere)
1. `nemotron-3-ultra-free` (opencode-zen, 1M, reasoning✓)
2. `nvidia/nemotron-3-ultra-550b-a55b:free` (openrouter, 1M, ✓)
3. `nvidia/nemotron-3-super-120b-a12b:free` (openrouter, 1M, ✓)
4. `gemini-2.5-flash` (gemini, 1M, ✓)
5. `nemotron-3-ultra` (ollama-cloud, 1M, ✓)