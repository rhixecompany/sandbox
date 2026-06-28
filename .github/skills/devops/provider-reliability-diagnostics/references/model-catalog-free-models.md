# Model Catalog & Free Models Reference

**Source:** https://hermes-agent.nousresearch.com/docs/api/model-catalog.json (updated 2026-06-13)

## OpenRouter Free Models (27 confirmed live 2026-06-22)

| # | Model | Context | Type |
|---|-------|---------|------|
| 1 | cognitivecomputations/dolphin-mistral-24b-venice-edition:free | 32K | Uncensored general |
| 2 | cohere/north-mini-code:free | 256K | Agentic coding (30B MoE) |
| 3 | google/gemma-4-26b-a4b-it:free | 262K | MoE instruction-tuned |
| 4 | google/gemma-4-31b-it:free | 262K | Dense multimodal 31B |
| 5 | google/lyria-3-clip-preview | 1M | Music generation (non-text) |
| 6 | google/lyria-3-pro-preview | 1M | Music generation (non-text) |
| 7 | liquid/lfm-2.5-1.2b-instruct:free | 32K | Compact 1.2B instruct |
| 8 | liquid/lfm-2.5-1.2b-thinking:free | 32K | Compact 1.2B reasoning |
| 9 | meta-llama/llama-3.2-3b-instruct:free | 131K | Multilingual 3B |
| 10 | meta-llama/llama-3.3-70b-instruct:free | 131K | Multilingual 70B |
| 11 | nex-agi/nex-n2-pro:free | 262K | Agentic 397B MoE (17B active) |
| 12 | nousresearch/hermes-3-llama-3.1-405b:free | 131K | Generalist 405B |
| 13 | nvidia/nemotron-3-nano-30b-a3b:free | 256K | Small MoE 30B |
| 14 | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | 256K | Reasoning MoE 30B |
| 15 | nvidia/nemotron-3-super-120b-a12b:free | 1M | Hybrid MoE 120B |
| 16 | nvidia/nemotron-3-ultra-550b-a55b:free | 1M | Frontier reasoning 550B |
| 17 | nvidia/nemotron-3.5-content-safety:free | 128K | Content safety guardrail |
| 18 | nvidia/nemotron-nano-12b-v2-vl:free | 128K | Multimodal VL 12B |
| 19 | nvidia/nemotron-nano-9b-v2:free | 128K | LLM 9B |
| 20 | openai/gpt-oss-120b:free | 131K | Open-weight 117B MoE |
| 21 | openai/gpt-oss-20b:free | 131K | Open-weight 21B |
| 22 | openrouter/free | 200K | Auto-router to free models |
| 23 | openrouter/owl-alpha | 1M+ | Agentic foundation model |
| 24 | poolside/laguna-m.1:free | 262K | Coding agent model |
| 25 | poolside/laguna-xs.2:free | 262K | Coding agent model (XS) |
| 26 | qwen/qwen3-coder:free | 1M | MoE code model 480B |
| 27 | qwen/qwen3-next-80b-a3b-instruct:free | 262K | MoE instruct 80B |

## Nous Portal Free Models

Free-tier gating is **determined live** via Portal pricing (partition_nous_models_by_tier), not in the manifest. The catalog lists the same model IDs as OpenRouter but without `:free` suffix or pricing metadata.

## Current Configuration (June 2026)

```yaml
# ~/.hermes/config.yaml
model:
  provider: opencode-zen
  default: nemotron-3-ultra-free
  base_url: https://opencode.ai/zen/v1
  api_mode: chat_completions
```

## Benchmark Test Template

Three micro-tasks for validating a model:

1. **Reasoning/Logic**: `30 ÷ 6 = 5`, then `$10 - $4 = $6`
2. **Tool Calling**: Execute `ls -la` on workspace directory
3. **Knowledge**: Describe Hermes built-in learning loop + auto-skill trigger

## Known Issues

- **opencode-zen API keys** in `.env` appear masked (`***`) — direct API calls require valid `OPENCODE_ZEN_API_KEY`
- **OpenRouter free models** require valid `OPENROUTER_API_KEY` with credits
- Model catalog TTL: 1 hour (config: `model_catalog.ttl_hours: 1`)

## Test Script

See `scripts/test-free-models.py` — runs benchmark against configured models via opencode-zen endpoint.