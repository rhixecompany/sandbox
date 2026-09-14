# OpenRouter Free Models Report

Fetched: https://openrouter.ai/models?variant=free
Date: 2026-09-14
Source: web_extract (full page, 20,411 chars, head+tail)

## Free Models (prompt $0/M, completion $0/M, or `:free` suffix)

| # | Model ID | Provider | Tokens (params) | Context | Prompt Cost | Completion Cost | Notes |
|---|----------|----------|-----------------|---------|-------------|-----------------|-------|
| 1 | `inclusionai/ling-3.0-flash-vl:free` | inclusionai | 102B | 262K | $0/M | $0/M | VL model; hybrid instant/reasoning; tool calling |
| 2 | `nex-agi/nex-n2.5-mini:free` | nex-agi | 86.3B | 262K | $0/M | $0/M | Agentic coding; GUI QA; browser/desktop automation |
| 3 | `nex-agi/nex-n2.5-pro:free` | nex-agi | 278B | 262K | $0/M | $0/M | Agentic pro variant; multi-file changes |
| 4 | `inclusionai/ling-3.0-flash-sante:free` | inclusionai | 366B | 262K | $0/M | $0/M | Health/medicine MoE; 5.1B active of 124B |
| 5 | `inclusionai/ling-3.0-flash-fin:free` | inclusionai | 981B | 262K | $0/M | $0/M | Finance MoE; investment workflows |
| 6 | `liquid/lfm-2.5-embedding-350m:free` | liquid | 350M | 512 | $0/M | $0/M | Text embedding; 1024-dim retrieval |
| 7 | `dots-studio/dots-3-note-preview:free` | dots-studio | 534B | 512K | $0/M | $0/M | MoE reasoning/coding; going away Sep 30 2026 |
| 8 | `deepgram/flux-tts:free` | deepgram | 3.16M | — | $0/M | $0/M | Text-to-speech; Flux voice catalog |
| 9 | `liquid/lfm-2.5-2.6b:free` | liquid | 2.6B | 66K | $0/M | $0/M | Compact reasoning; agent workflows; RAG |
| 10 | `nvidia/nemotron-3.5-lightning:free` | nvidia | 964B | 1M | $0/M | $0/M | MoE 3B active of 30B; agentic workloads |
| 11 | `cohere/north-mini-code:free` | cohere | 124B | 256K | $0/M | $0/M | Agentic coding; Apache 2.0; SWE-Agent |
| 12 | `thinkingmachines/inkling-small:free` | thinkingmachines | 133B | 1.05M | $0/M | $0/M | MoE 12B active of 276B; multimodal |
| 13 | `fish-audio/s2.1-pro-free:free` | fish-audio | — | — | $0/M | $0/M | STT/TTS; testing/prototyping |
| 14 | `poolside/laguna-s-2.1:free` | poolside | 118B | 262K | $0/M | $0/M | Coding agent; Terminal-Bench 70.2% |
| 15 | `thinkingmachines/inkling:free` | thinkingmachines | 401B | 1.05M | $0/M | $0/M | MoE 41B active of 975B; multimodal |
| 16 | `nvidia/nemotron-3-embed-1b:free` | nvidia | 1B | 33K | $0/M | $0/M | Embedding; 95%+ of 8B accuracy |
| 17 | `poolside/laguna-xs-2.1:free` | poolside | 33B | 262K | $0/M | $0/M | Coding agent; FP8 quantized |

**Total free models: 17** (19 text + 2 speech + 3 embedding + 1 rerank ≈ 25 total listed on page; 17 confirmed `:free` variant)
