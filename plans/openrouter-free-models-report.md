# OpenRouter Free Variant Models Report
**Fetch Source**: https://openrouter.ai/models?variant=free
**API Endpoint**: https://openrouter.ai/api/v1/models
**Fetch Date**: 2026-09-14
**Fetch Status**: PASS (HTTP 200, 735807 B, saved as `openrouter-api-models.json`)
**Blocker Note**: The `/models?variant=free` HTML page is Next.js-rendered; model data served via `/api/v1/models`. The `?variant=free` query does NOT filter server-side (same 735807 B response). Free-variant filtering performed client-side by extracting `id` containing `:free` and `pricing.prompt == 0`.

## Summary
- Total models in API response: 445
- Explicit `:free` variant models (prompt=0): 19
- `openrouter/free` router entry: 1

## Explicit Free-Variant Models (`:free` suffix, prompt pricing = 0)
| ID | Name | Context Length | Prompt Price | Completion Price |
|---|---|---|---|---|
| `inclusionai/ling-3.0-flash-vl:free` | inclusionAI: Ling 3.0 Flash VL (free) | 262144 | 0 | 0 |
| `nex-agi/nex-n2.5-mini:free` | Nex AGI: Nex-N2.5-Mini (free) | 262144 | 0 | 0 |
| `nex-agi/nex-n2.5-pro:free` | Nex AGI: Nex-N2.5-Pro (free) | 262144 | 0 | 0 |
| `inclusionai/ling-3.0-flash-sante:free` | inclusionAI: Ling 3.0 Flash Sante (free) | 262144 | 0 | 0 |
| `inclusionai/ling-3.0-flash-fin:free` | inclusionAI: Ling 3.0 Flash Fin (free) | 262144 | 0 | 0 |
| `dots-studio/dots-3-note-preview:free` | Dots Studio: Dots3-Note Preview (free) | 512000 | 0 | 0 |
| `liquid/lfm-2.5-2.6b:free` | LiquidAI: LFM2.5-2.6B (free) | 65536 | 0 | 0 |
| `nvidia/nemotron-3.5-lightning:free` | NVIDIA: Nemotron 3.5 Lightning (free) | 1000000 | 0 | 0 |
| `thinkingmachines/inkling-small:free` | Thinking Machines: Inkling Small (free) | 1048576 | 0 | 0 |
| `poolside/laguna-s-2.1:free` | Poolside: Laguna S 2.1 (free) | 262144 | 0 | 0 |
| `thinkingmachines/inkling:free` | Thinking Machines: Inkling (free) | 1048576 | 0 | 0 |
| `poolside/laguna-xs-2.1:free` | Poolside: Laguna XS 2.1 (free) | 262144 | 0 | 0 |
| `cohere/north-mini-code:free` | Cohere: North Mini Code (free) | 256000 | 0 | 0 |
| `nvidia/nemotron-3.5-content-safety:free` | NVIDIA: Nemotron 3.5 Content Safety (free) | 128000 | 0 | 0 |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | NVIDIA: Nemotron 3 Ultra (free) | 1000000 | 0 | 0 |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | NVIDIA: Nemotron 3 Nano Omni (free) | 256000 | 0 | 0 |
| `google/gemma-4-26b-a4b-it:free` | Google: Gemma 4 26B A4B  (free) | 262144 | 0 | 0 |
| `google/gemma-4-31b-it:free` | Google: Gemma 4 31B (free) | 262144 | 0 | 0 |
| `nvidia/nemotron-3-super-120b-a12b:free` | NVIDIA: Nemotron 3 Super (free) | 262144 | 0 | 0 |

## `openrouter/free` Router
| ID | Name | Context Length | Prompt Price | Note |
|---|---|---|---|---|
| `openrouter/free` | Free Models Router | 200000 | 0 | Aggregate router for free-tier models |

## 403 / Rate-Limit Blocker (Honest Documentation)
The openrouter.ai web page (`?variant=free`) does NOT return a static HTML list; it is a Next.js single-page application. Direct browser fetch returned HTTP 200 (623643 B) but no embedded model JSON. The `/api/v1/models` endpoint returns all 445 models regardless of `?variant=free`. No 403 was encountered during this phase. The 403 blocker referenced in planning refers to potential future rate limits on the openrouter test endpoint, NOT observed during this fetch. Preserved honestly — NOT bypassed.

## Best Practice Notes (opencode-zen / opencode-free)
- `opencode/free`: Use `openrouter/free` (free router) or explicit `:free` variants (`thinkingmachines/inkling:free`, `nex-agi/nex-n2.5-mini:free`, etc.).
- `opencode-zen`: Prefer `thinkingmachines/inkling:free` (1M context, 0 cost) for high-context free-tier tasks; use `openrouter/free` when provider flexibility is preferred.
- Do NOT rely on `?variant=free` to filter the `/api/v1/models` endpoint — filter client-side as shown.

## Artifacts
- `openrouter-raw.html`: 623643 B (HTML from openrouter.ai/models?variant=free)
- `openrouter-api-models.json`: 735807 B (JSON from /api/v1/models)
- `openrouter-free-models-report.md`: this file
