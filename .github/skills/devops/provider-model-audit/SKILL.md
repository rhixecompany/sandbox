---
author: Hermes Agent
description: Inventory all authorized LLM providers via `hermes auth list`, discover
  their free-tier models from the OpenRouter live API, and produce a cross-provider
  comparison. Includes the critical constraint that API keys live in Hermes' credential
  store (not subprocess env vars).
license: MIT
name: provider-model-audit
tags:
- providers
- models
- audit
- openrouter
- auth
- free-tier
- benchmark
- hermes
title: Provider & Model Audit
version: 1.0.0

---

# Provider & Model Audit

## When to Use

- User asks "what models do I have access to?"
- User wants to know which free models are available
- User says "test-providers-models", "/providers", or "/models"
- User wants to benchmark or compare provider performance

## Prerequisites

- `hermes auth list` — must be runnable
- `curl` — for API calls (available via bash terminal)
- `python3` — for JSON parsing
- OpenRouter API key configured in Hermes credential store

## Phase 0: Auth Inventory

Run `hermes auth list` to get the provider inventory table.

```bash
hermes auth list
hermes config show | grep -i "provider\|model"
```

### Expected providers
1. copilot (may be rate-limited 429)
2. huggingface (HF_TOKEN)
3. nous (OAuth device_code)
4. ollama-cloud (OLLAMA_API_KEY)
5. openai-api (OPENAI_API_KEY)
6. openrouter (OPENROUTER_API_KEY)

## ⚠️ Critical Constraint

**API keys (especially `OPENROUTER_API_KEY`) are stored in Hermes' secure
credential store and are NOT exported as subprocess environment variables.**

This means:
- `$OPENROUTER_API_KEY` in bash expands to `*** ` (redacted placeholder)
- `curl` + Python subprocess calls to the API will FAIL
- All API calls must route through the Hermes provider chain:
  ```bash
  hermes chat -q '<prompt>' --model <model_id> --provider openrouter -Q --yolo -t ""
  ```

**Workarounds for scripted benchmarks:**
- Use `execute_code` with `terminal()` helper (inherits Hermes runtime)
- Use `delegate_task` to spawn subagents with provider access
- Pre-fund OpenRouter account with credits for direct API access
- Use `test_models.py --hermes` to route benchmark calls through `hermes chat -q` proxy
- Use `test_models.py --list-providers` to check auth status of all 6 providers at once

## Phase 1: Model Discovery

### Hermes Catalog (curated — only 33 OpenRouter models)
```bash
curl -s https://hermes-agent.nousresearch.com/docs/api/model-catalog.json
```

### OpenRouter Live API (340 models — 10× more than catalog)
```bash
curl -s https://openrouter.ai/api/v1/models -H "Authorization: Bearer $OPENROUTER_API_KEY"
```
(Use `web_extract` or `mcp_fetch` if available — avoids subprocess key issue)

### Free Models Filter
Free models have `pricing: {prompt: "0", completion: "0"}` in the API response:
```python
free = [m for m in models if m.get("pricing") and any(v == "0" for k,v in m["pricing"].items())]
```

## Phase 2: Free Models (27 from OpenRouter)

### Top Picks by Context Window

| Model | Context | Why |
|-------|---------|-----|
| `nvidia/nemotron-3-ultra-550b-a55b:free` | 1M | Frontier reasoning, 550B MoE |
| `nvidia/nemotron-3-super-120b-a12b:free` | 1M | Hybrid Mamba-Transformer |
| `qwen/qwen3-coder:free` | 1M | Qwen coding MoE, 480B total |
| `openrouter/owl-alpha` | 1M+ | Agentic foundation model |
| `cohere/north-mini-code:free` | 256K | Agentic coding, 30B MoE |
| `nex-agi/nex-n2-pro:free` | 262K | Agentic 397B MoE (17B active) |

### All 27 Free Models by Provider

- **NVIDIA (7):** nemotron-3-nano-30b-a3b, nemotron-3-nano-omni-30b-a3b-reasoning, nemotron-3-super-120b-a12b, nemotron-3-ultra-550b-a55b, nemotron-3.5-content-safety, nemotron-nano-12b-v2-vl, nemotron-nano-9b-v2
- **Google (4):** gemma-4-26b-a4b-it, gemma-4-31b-it, lyria-3-clip-preview (music), lyria-3-pro-preview (music)
- **Qwen (2):** qwen3-coder, qwen3-next-80b-a3b-instruct
- **Meta (2):** llama-3.2-3b-instruct, llama-3.3-70b-instruct
- **Poolside (2):** laguna-m.1, laguna-xs.2 (coding agents)
- **OpenAI OSS (2):** gpt-oss-120b, gpt-oss-20b
- **Liquid (2):** lfm-2.5-1.2b-instruct, lfm-2.5-1.2b-thinking
- **OpenRouter (2):** free (router), owl-alpha (agentic)
- **Cohere (1):** north-mini-code
- **Nex AGI (1):** nex-n2-pro
- **Nous (1):** hermes-3-llama-3.1-405b
- **CognitiveComputations (1):** dolphin-mistral-24b-venice-edition

## Phase 3: Benchmarking

### 3-Task Standard Benchmark
1. **Reasoning:** `30 ÷ 6 = 5`, start $10 spend $4 → remaining = $6
2. **Tool Calling:** Describe how an LLM agent calls a tool
3. **Knowledge:** Describe Hermes learning loop + auto-skill trigger

### Via Hermes Provider Chain
```bash
hermes chat -q '<prompt>' --model <model_id> --provider openrouter -Q --yolo -t ""
```

### Via Subagent (delegate_task)
Pass the task through a background subagent that inherits the Hermes provider chain.

### Via Direct API (requires credits)
If the OpenRouter account is pre-funded, use direct curl calls with `$OPENROUTER_API_KEY` in bash (the key IS accessible in the interactive terminal, just not in Python subprocesses).

## Script Reference

`~/AppData/Local/hermes/scripts/test_models.py` is the multi-provider benchmark harness:

| Flag | Purpose |
|------|---------|
| `--list-providers` | Show auth status for all 6 configured providers |
| `--list-free` | List all free models from OpenRouter (requires direct API access) |
| `--benchmark` | Benchmark all free models (OpenRouter direct API) |
| `--hermes` | Route benchmark through `hermes chat -q` (bypasses key boundary) |
| `--provider ORG` | Filter by provider (e.g., `--provider nvidia`) |
| `--model MODEL` | Test specific model only |

**Note:** `--list-providers` works in any environment. `--list-free` and `--benchmark` require `OPENROUTER_API_KEY` in the subprocess environment (not Hermes' secure store). Use `--hermes` to benchmark when the key is only in Hermes' store.

## Pitfalls

1. **`*** ` in subprocess env** — `$OPENROUTER_API_KEY` expands to the literal redacted placeholder in subprocess envs. Test with `echo ${#OPENROUTER_API_KEY}` — if it's 5, it's the placeholder.
2. **Rate-limited copilot** — The gh auth token + GITHUB_TOKEN may be in 429 cooldown for ~22m.
3. **`:free` suffix** — Some models are free without the `:free` suffix (e.g., `openrouter/owl-alpha`). Always check the `pricing` object in the API response.
4. **Non-text models** — Lyria models are music generation, not text LLMs. Filter these out.
5. **Hermes catalog vs live API** — The curated catalog has 33 models but OpenRouter live has 340. Don't rely solely on the catalog.
6. **`hermes chat -q` agent overhead** — Each `hermes chat -q` call spawns a full agent session (reasoning + tool loading), adding 60-120s of overhead per call. This makes bulk benchmarking (27 models × 3 tasks) impractical through this proxy. Either pre-fund OpenRouter for direct API access, or benchmark in batches of 3-5 models per session.
7. **Provider API discovery blocked** — HuggingFace, Nous Portal, and Ollama Cloud APIs are not directly queryable from subprocess without credentials. Use `hermes auth list` for auth status and OpenRouter API for the most comprehensive model catalog.

## Verification Checklist

- [ ] `hermes auth list` shows all expected providers
- [ ] Rate-limit status logged per provider
- [ ] Free models filtered by `pricing.prompt == "0"` and `pricing.completion == "0"`
- [ ] Non-text models (music, image) excluded from benchmark
- [ ] Benchmark results compiled into comparison table
- [ ] Prompt file updated with actual findings
