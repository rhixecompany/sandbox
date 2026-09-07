---
name: free-model-catalog
description: "Consolidated list of every model with a :free suffix (or zero pricing) across all configured Hermes providers. Captured on 2026-09-07 15:09 UTC by `scripts/build_free_model_catalog.py`."
---

# Free-model catalog -- 2026-09-07 15:09 UTC

> Source: live `/v1/models` endpoint per provider. Filter: `':free' in model id` OR `pricing.prompt == 0 && pricing.completion == 0`.
> Probe-eligibility is also gated by the per-provider status in `provider_docs/<provider>.md`; only `valid` providers should be probed in Phase 3.

| # | Provider | Model ID | Knowledge Cutoff | Context | Max Output | Reasoning | Source |
|---|----------|----------|------------------|---------|------------|-----------|--------|
| 1 | `opencode-zen` | `deepseek-v4-flash-free` | n/a | n/a | n/a | no | https://opencode.ai/zen/v1/models |
| 2 | `opencode-zen` | `ling-3.0-flash-fin-free` | n/a | n/a | n/a | no | https://opencode.ai/zen/v1/models |
| 3 | `opencode-zen` | `mimo-v2.5-free` | n/a | n/a | n/a | no | https://opencode.ai/zen/v1/models |
| 4 | `opencode-zen` | `muse-spark-1.2-contributor-free` | n/a | n/a | n/a | no | https://opencode.ai/zen/v1/models |
| 5 | `opencode-zen` | `muse-spark-1.3-contributor-free` | n/a | n/a | n/a | no | https://opencode.ai/zen/v1/models |
| 6 | `opencode-zen` | `nemotron-3-ultra-free` | n/a | n/a | n/a | no | https://opencode.ai/zen/v1/models |
| 7 | `opencode-zen` | `nemotron-3.5-lightning-free` | n/a | n/a | n/a | no | https://opencode.ai/zen/v1/models |
| 8 | `openrouter` | `cohere/north-mini-code:free` | n/a | 256000 | 64000 | yes | https://openrouter.ai/api/v1/models |
| 9 | `openrouter` | `dots-studio/dots-3-note-preview:free` | n/a | 512000 | 460800 | yes | https://openrouter.ai/api/v1/models |
| 10 | `openrouter` | `google/gemma-4-26b-a4b-it:free` | n/a | 262144 | 32768 | yes | https://openrouter.ai/api/v1/models |
| 11 | `openrouter` | `google/gemma-4-31b-it:free` | n/a | 262144 | 32768 | yes | https://openrouter.ai/api/v1/models |
| 12 | `openrouter` | `google/lyria-3-clip-preview` | n/a | 1048576 | 65536 | no | https://openrouter.ai/api/v1/models |
| 13 | `openrouter` | `google/lyria-3-pro-preview` | n/a | 1048576 | 65536 | no | https://openrouter.ai/api/v1/models |
| 14 | `openrouter` | `inclusionai/ling-3.0-flash-fin:free` | n/a | 262144 | 32768 | yes | https://openrouter.ai/api/v1/models |
| 15 | `openrouter` | `inclusionai/ling-3.0-flash-sante:free` | n/a | 262144 | 32768 | yes | https://openrouter.ai/api/v1/models |
| 16 | `openrouter` | `liquid/lfm-2.5-2.6b:free` | n/a | 65536 | 8192 | yes | https://openrouter.ai/api/v1/models |
| 17 | `openrouter` | `minimax/minimax-m2.7:free` | n/a | 196608 | 176947 | yes | https://openrouter.ai/api/v1/models |
| 18 | `openrouter` | `minimax/minimax-m3:free` | n/a | 1048576 | 943718 | yes | https://openrouter.ai/api/v1/models |
| 19 | `openrouter` | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | n/a | 256000 | 65536 | yes | https://openrouter.ai/api/v1/models |
| 20 | `openrouter` | `nvidia/nemotron-3-super-120b-a12b:free` | n/a | 262144 | 235929 | yes | https://openrouter.ai/api/v1/models |
| 21 | `openrouter` | `nvidia/nemotron-3-ultra-550b-a55b:free` | n/a | 1000000 | 65536 | yes | https://openrouter.ai/api/v1/models |
| 22 | `openrouter` | `nvidia/nemotron-3.5-content-safety:free` | n/a | 128000 | 8192 | yes | https://openrouter.ai/api/v1/models |
| 23 | `openrouter` | `nvidia/nemotron-3.5-lightning:free` | n/a | 1000000 | 65536 | yes | https://openrouter.ai/api/v1/models |
| 24 | `openrouter` | `openrouter/free` | n/a | 200000 | n/a | yes | https://openrouter.ai/api/v1/models |
| 25 | `openrouter` | `poolside/laguna-s-2.1:free` | n/a | 262144 | 32768 | yes | https://openrouter.ai/api/v1/models |
| 26 | `openrouter` | `poolside/laguna-xs-2.1:free` | n/a | 262144 | 32768 | yes | https://openrouter.ai/api/v1/models |
| 27 | `openrouter` | `thinkingmachines/inkling-small:free` | n/a | 1048576 | 262144 | yes | https://openrouter.ai/api/v1/models |
| 28 | `openrouter` | `thinkingmachines/inkling:free` | n/a | 1048576 | 262144 | yes | https://openrouter.ai/api/v1/models |

