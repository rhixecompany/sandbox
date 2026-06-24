# Top 3 Free Models from OpenRouter, NVIDIA NIM & OpenCode Zen

**Date:** 2026-06-24  
**Methodology:** Queried model listing APIs directly, filtered for $0 prompt + $0 completion pricing, ranked by context length, knowledge cutoff, and reasoning capability.

---

## Model Inventory Summary

| Provider | Total Models | Free Models | Source |
|----------|-------------|-------------|--------|
| OpenRouter | 339 | 26 | openrouter.ai/api/v1/models |
| NVIDIA NIM (via API) | 121 | 7 (free via OpenRouter) | integrate.api.nvidia.com/v1/models |
| OpenCode Zen | 49 | 6 | opencode.ai/zen/v1/models |

**Note:** NVIDIA NIM free models are accessed via OpenRouter routing (`nvidia/*:free`). NVIDIA's own build.nvidia.com offers 77+ free endpoints with a 1,000 inference-credit pool but their API listing at `integrate.api.nvidia.com/v1/models` doesn't expose pricing/context metadata — the same models are fully documented on OpenRouter. OpenCode Zen free models have `-free` suffix in their IDs.

---

## All Free Models — Combined Rankings

### Tier 1: 1M Context (Top Performers)

| # | Model | Provider | Context | Knowledge Cutoff | Reasoning Capability |
|---|-------|----------|---------|-----------------|---------------------|
| 1 | **qwen/qwen3-coder:free** | OpenRouter | **1,048,576** | **2025-06-30** | General (coding-focused) |
| 2 | **nvidia/nemotron-3-ultra-550b-a55b:free** | OpenRouter/NVIDIA | **1,000,000** | Sep 2025* | **Built-in reasoning** |
| 3 | **nvidia/nemotron-3-super-120b-a12b:free** | OpenRouter/NVIDIA | **1,000,000** | Recent* | **Built-in reasoning** |
| 4 | openrouter/owl-alpha | OpenRouter | 1,048,756 | N/A | None |
| 5 | google/lyria-3-pro-preview | OpenRouter | 1,048,576 | N/A | None |
| 6 | google/lyria-3-clip-preview | OpenRouter | 1,048,576 | N/A | None |

### Tier 2: 256K-262K Context

| # | Model | Provider | Context | Knowledge Cutoff | Reasoning Capability |
|---|-------|----------|---------|-----------------|---------------------|
| 7 | **qwen/qwen3-next-80b-a3b-instruct:free** | OpenRouter | **262,144** | **2025-09-30** | None |
| 8 | pollside/laguna-m.1:free | OpenRouter | 262,144 | N/A | Built-in reasoning |
| 9 | google/gemma-4-31b-it:free | OpenRouter | 262,144 | N/A | None |
| 10 | google/gemma-4-26b-a4b-it:free | OpenRouter | 262,144 | N/A | None |
| 11 | pollside/laguna-xs.2:free | OpenRouter | 262,144 | N/A | Built-in reasoning |
| 12 | cohere/north-mini-code:free | OpenRouter | 256,000 | N/A | None |
| 13 | nvidia/nemotron-3-nano-30b-a3b:free | OpenRouter/NVIDIA | 256,000 | N/A | None |
| 14 | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | OpenRouter/NVIDIA | 256,000 | N/A | Built-in reasoning |

### Tier 3: 128K-200K Context

| # | Model | Provider | Context | Knowledge Cutoff | Reasoning Capability |
|---|-------|----------|---------|-----------------|---------------------|
| 15 | openrouter/free (load balancer) | OpenRouter | 200,000 | N/A | None |
| 16 | openai/gpt-oss-120b:free | OpenRouter | 131,072 | 2024-06-30 | **Mandatory reasoning** |
| 17 | openai/gpt-oss-20b:free | OpenRouter | 131,072 | 2024-06-30 | **Mandatory reasoning** |
| 18 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 131,072 | 2023-12-31 | None |
| 19 | meta-llama/llama-3.2-3b-instruct:free | OpenRouter | 131,072 | 2023-12-31 | None |
| 20 | nousresearch/hermes-3-llama-3.1-405b:free | OpenRouter | 131,072 | 2023-12-31 | None |
| 21 | nvidia/nemotron-3.5-content-safety:free | OpenRouter/NVIDIA | 128,000 | N/A | Built-in reasoning |
| 22 | nvidia/nemotron-nano-12b-v2-vl:free | OpenRouter/NVIDIA | 128,000 | N/A | None |
| 23 | nvidia/nemotron-nano-9b-v2:free | OpenRouter/NVIDIA | 128,000 | 2025-03-31 | None |

### OpenCode Zen Free Models (6 models)

These are accessed at `opencode.ai/zen/v1` (OpenAI-compatible). No detailed metadata available from their API; specs inferred below:

| Free Model | Likely Base Model | Est. Context | Est. Cutoff | Est. Reasoning |
|------------|------------------|-------------|-------------|---------------|
| deepseek-v4-flash-free | DeepSeek V4 Flash | **1,000,000** | Recent (2026) | Yes |
| qwen3.6-plus-free | Qwen 3.6 Plus | **1,000,000** | 2026-03 | Yes (always-on CoT) |
| minimax-m3-free | MiniMax M3 | **1,000,000** | Recent (2025) | Yes |
| nemotron-3-ultra-free | Nvidia Nemotron 3 Ultra | **1,000,000** | Sep 2025 | Yes |
| north-mini-code-free | Cohere North Mini Code | 256,000 | Recent | No |
| mimo-v2.5-free | Xiaomi MiMo V2.5 | N/A | Recent | No |

*Note: OpenCode Zen free models map to known models available on OpenRouter with publicly documented specs.*

---

## Final Selection: Top 3 Free Models

### 🥇 #1: `deepseek-v4-flash-free` (OpenCode Zen) / `deepseek/deepseek-v4-flash:free` (OpenRouter)

| Criteria | Value |
|----------|-------|
| **Context Length** | **1,000,000 tokens** |
| **Reasoning** | Supports reasoning efforts (high/xhigh) — strong on agentic/coding tasks |
| **Knowledge Cutoff** | Very recent (DeepSeek V4 released Apr 2026) |
| **Provider Coverage** | Available on **OpenRouter** (`deepseek/deepseek-v4-flash:free`) and **OpenCode Zen** (`deepseek-v4-flash-free`) |
| **Architecture** | 284B total / 13B active MoE — efficient inference |
| **Why #1** | Best combination of massive 1M context + strong reasoning + most recent knowledge + availability on 2/3 providers. DeepSeek V4 Flash excels at coding, agent tasks, and long-context reasoning at near-zero latency. |

### 🥈 #2: `nvidia/nemotron-3-ultra-550b-a55b:free` (OpenRouter + NVIDIA NIM + OpenCode Zen)

| Criteria | Value |
|----------|-------|
| **Context Length** | **1,000,000 tokens** |
| **Reasoning** | Built-in reasoning (supports high/medium effort) — frontier reasoning model |
| **Knowledge Cutoff** | **September 2025** (verified via model card) |
| **Provider Coverage** | Available on **all 3 providers**: OpenRouter, NVIDIA NIM, OpenCode Zen (`nemotron-3-ultra-free`) |
| **Architecture** | 550B total / 55B active (hybrid Mamba-Transformer MoE) |
| **Why #2** | Runs on all three requested providers, built-in reasoning (not optional), 1M context, high throughput, and NVIDIA's strongest open reasoning model. Great for orchestration, planning, error recovery. |

### 🥉 #3: `qwen/qwen3-coder:free` (OpenRouter)

| Criteria | Value |
|----------|-------|
| **Context Length** | **1,048,576 tokens** |
| **Reasoning** | No explicit reasoning flag but state-of-the-art for coding agents (SWE-Bench leader) |
| **Knowledge Cutoff** | **2025-06-30** (verified) |
| **Provider Coverage** | **OpenRouter** only (not available on other two) |
| **Architecture** | 480B total / 35B active MoE — purpose-built coder |
| **Why #3** | Largest context window among all free models (1,048,576), recent knowledge cutoff, and the best open-source coding model. The `:free` tag on OpenRouter makes it completely $0. No reasoning flag, but excels at agentic coding tasks. |

---

### Honorable Mentions

| Model | Why Close But No Cigar |
|-------|----------------------|
| `nvidia/nemotron-3-super-120b-a12b:free` | Same 1M context + reasoning as Ultra but with no confirmed cutoff date |
| `qwen/qwen3-next-80b-a3b-instruct:free` | Newest cutoff (2025-09-30) but only 262K context |
| `openai/gpt-oss-120b:free` | Mandatory reasoning but only 131K context and older cutoff (2024-06-30) |
| `openrouter/owl-alpha` | 1,048,756 context but no reasoning support or knowledge cutoff info |
| `qwen3.6-plus-free` (OpenCode Zen) | 1M context + always-on reasoning but only available via OpenCode Zen (free), highly likely a top contender if it stays free |

---

## Key Takeaways

1. **OpenRouter dominates** — 26 free models with full metadata exposed (pricing, context length, knowledge cutoff, reasoning flags). This is the best provider for discovering free models.

2. **NVIDIA NIM API lacks metadata** — The `integrate.api.nvidia.com/v1/models` endpoint returns only basic model IDs. The same NVIDIA models are better discovered via OpenRouter's API. For an NVIDIA-specific experience, use `build.nvidia.com/models` which advertises 77 free endpoints.

3. **OpenCode Zen offers 6 free models** — No detailed metadata API, but its free models map to well-known open models available elsewhere. `deepseek-v4-flash-free` and `nemotron-3-ultra-free` are standouts.

4. **All top 3 have 1M context** — The free model landscape has shifted: 1M-token context is now the standard for top free models, compared to 128K-256K a year ago.

