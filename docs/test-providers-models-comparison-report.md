# Cross-Provider Comparison & Report — Phase 4.5

> Generated: 2026-06-22 | Sources: `hermes auth list`, OpenRouter API, phase benchmarks

## 1. Provider Overview

| Provider | Auth Status | Free Models | Limits | Recommended For |
|----------|------------|-------------|--------|-----------------|
| **openrouter** | ✓ Active (managed) | 27 free models | Rate-limited per IP | General purpose, coding, reasoning |
| **opencode-zen** (active) | ✓ Active | deepseek-v4-flash-free (current) | None observed | System admin, ops, fallback |
| **nous** | ✓ Active (OAuth) | Portal free tier (Claude, GPT, Gemini, etc.) | Portal pricing | Premium models via portal |
| **huggingface** | ✓ Active (HF_TOKEN) | Free inference API | Unstable | Community models, experimental |
| **ollama-cloud** | ✓ Active (API key) | Cloud-hosted OSS models | Per-usage limits | Local dev/OSS model testing |
| **openai-api** | ✓ Keys present | GPT-4o mini (low-cost) | Not exported to subprocess | Production API access |
| **copilot** | ⚠️ Rate-limited (429) | GPT-4o mini, Claude Haiku, Gemini Flash | 429 cooldown | IDE integration only |

## 2. Benchmark Ranking (By Task)

### Reasoning / Logic
| Rank | Provider | Model | Result |
|------|----------|-------|--------|
| 1 | opencode-zen | deepseek-v4-flash-free | ✅ PASS |
| 2 | openrouter | qwen/qwen3-coder:free | ✅ PASS |
| 3 | openrouter | nvidia/nemotron-3-ultra-550b-a55b:free | ⏳ Timeout (agent overhead) |

### Tool Calling
| Rank | Provider | Model | Result |
|------|----------|-------|--------|
| 1 | opencode-zen | deepseek-v4-flash-free | ✅ PASS |
| 2 | openrouter | qwen/qwen3-coder:free | ✅ PASS |

### Knowledge
| Rank | Provider | Model | Result |
|------|----------|-------|--------|
| 1 | opencode-zen | deepseek-v4-flash-free | ✅ PASS |
| 2 | openrouter | qwen/qwen3-coder:free | ⏳ Timeout (tool-restricted mode) |

## 3. Reliability Score

| Provider | Auth Reliability | API Stability | Rate Limit Risk | Overall |
|----------|----------------|--------------|-----------------|---------|
| opencode-zen | ★★★★★ | ★★★★★ | None | **5/5** |
| openrouter | ★★★★☆ | ★★★★☆ | Medium (rate per IP) | **4/5** |
| nous | ★★★★☆ | ★★★★☆ | Low (OAuth managed) | **4/5** |
| huggingface | ★★★☆☆ | ★★☆☆☆ | Medium | **2.5/5** |
| ollama-cloud | ★★★☆☆ | ★★★☆☆ | Low | **3/5** |
| openai-api | ★★★★☆ | ★★★★★ | Low (usage billing) | **4.5/5** |
| copilot | ★☆☆☆☆ | ★★★★☆ | High (429) | **2/5** |

## 4. Recommendations Per Task Type

| Task Type | Best Provider | Best Model | Reason |
|-----------|--------------|------------|--------|
| **Coding / Agentic** | openrouter | qwen/qwen3-coder:free | 1M context, free, purpose-built coder |
| **System Admin / Ops** | opencode-zen | deepseek-v4-flash-free | Currently active, responsive, free |
| **General Purpose** | openrouter | openrouter/free (router) | Auto-routes to best free model |
| **Reasoning** | openrouter | nvidia/nemotron-3-ultra-550b-a55b:free | Frontier 550B, 1M context |
| **Quick/Simple Tasks** | openrouter | meta-llama/llama-3.3-70b-instruct:free | Fast 70B, multilingual |
| **Premium (if funded)** | nous | Claude Opus 4.8 / GPT-5.5 | Portal access to frontier models |

## 5. Optimal Fallback Chain

```
Primary:    opencode-zen → openrouter → nous → huggingface → ollama-cloud → openai-api → copilot
Code tasks: openrouter (qwen3-coder:free) → opencode-zen (deepseek-v4-flash-free)
```

## Constraints & Known Issues

- **OpenRouter key not in subprocess env** — All API calls must route through `hermes chat -q`
- **Copilot rate-limited** — 429 cooldown active; must wait before retrying
- **Benchmark overhead** — `hermes chat -q` agent session adds 60-120s per call; not suitable for bulk
- **HuggingFace unstable** — Inference API returned errors on direct query
