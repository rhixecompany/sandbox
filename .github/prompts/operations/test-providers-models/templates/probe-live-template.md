---
name: probe-live
description: Live results from the most recent probe run, captured by `scripts/run_probes.py` on 2026-09-07 15:22 UTC.
---

# Probe results -- live -- 2026-09-07 15:22 UTC

> Source: `hermes chat --oneshot --yolo --run-budget 45` per `probes/probe-*.txt` task file.
> Exit 0 = model returned a response; Exit -2 = a known hermes failure marker was detected (see Failure column).
> Knowledge cutoff / context / reasoning / max output are heuristically extracted from the model's free-form response; "?" means the model did not state a value.

| # | Provider | Model | Exit | Elapsed (s) | Failure | Knowledge Cutoff | Context | Reasoning | Max Output |
|---|----------|-------|------|-------------|---------|------------------|---------|-----------|------------|
| 1 | `opencode-zen` | `deepseek-v4-flash-free` | -1 | 55.1 |  | ? | ? | ? | ? |
| 2 | `opencode-zen` | `ling-3.0-flash-fin-free` | -1 | 55.1 |  | ? | ? | ? | ? |
| 3 | `opencode-zen` | `mimo-v2.5-free` | -1 | 55.1 |  | ? | ? | ? | ? |
| 4 | `opencode-zen` | `muse-spark-1.2-contributor-free` | 1 | 2.7 |  | ? | ? | ? | ? |
| 5 | `opencode-zen` | `muse-spark-1.3-contributor-free` | 1 | 3.0 |  | ? | ? | ? | ? |
| 6 | `opencode-zen` | `nemotron-3-ultra-free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 7 | `opencode-zen` | `nemotron-3.5-lightning-free` | -1 | 55.3 |  | ? | ? | ? | ? |
| 8 | `openrouter` | `cohere/north-mini-code:free` | -1 | 55.3 |  | ? | ? | ? | ? |
| 9 | `openrouter` | `dots-studio/dots-3-note-preview:free` | -1 | 55.4 |  | ? | ? | ? | ? |
| 10 | `openrouter` | `google/gemma-4-26b-a4b-it:free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 11 | `openrouter` | `google/gemma-4-31b-it:free` | -1 | 55.4 |  | ? | ? | ? | ? |
| 12 | `openrouter` | `google/lyria-3-clip-preview` | -1 | 55.3 |  | ? | ? | ? | ? |
| 13 | `openrouter` | `google/lyria-3-pro-preview` | -1 | 55.4 |  | ? | ? | ? | ? |
| 14 | `openrouter` | `inclusionai/ling-3.0-flash-fin:free` | -1 | 55.3 |  | ? | ? | ? | ? |
| 15 | `openrouter` | `inclusionai/ling-3.0-flash-sante:free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 16 | `openrouter` | `liquid/lfm-2.5-2.6b:free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 17 | `openrouter` | `minimax/minimax-m2.7:free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 18 | `openrouter` | `minimax/minimax-m3:free` | -1 | 55.3 |  | ? | ? | ? | ? |
| 19 | `openrouter` | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 20 | `openrouter` | `nvidia/nemotron-3-super-120b-a12b:free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 21 | `openrouter` | `nvidia/nemotron-3-ultra-550b-a55b:free` | -1 | 55.3 |  | ? | ? | ? | ? |
| 22 | `openrouter` | `nvidia/nemotron-3.5-content-safety:free` | -1 | 55.4 |  | ? | ? | ? | ? |
| 23 | `openrouter` | `nvidia/nemotron-3.5-lightning:free` | -1 | 55.3 |  | ? | ? | ? | ? |
| 24 | `openrouter` | `openrouter/free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 25 | `openrouter` | `poolside/laguna-s-2.1:free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 26 | `openrouter` | `poolside/laguna-xs-2.1:free` | -1 | 55.3 |  | ? | ? | ? | ? |
| 27 | `openrouter` | `thinkingmachines/inkling-small:free` | -1 | 55.2 |  | ? | ? | ? | ? |
| 28 | `openrouter` | `thinkingmachines/inkling:free` | -1 | 55.2 |  | ? | ? | ? | ? |

