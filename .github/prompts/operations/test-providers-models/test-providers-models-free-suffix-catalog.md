---
name: test-providers-models-free-suffix-catalog
title: "Free Suffix Catalog"
description: "Catalog of free LLM models across all authorized providers for Hermes Agent testing. Verified against OpenRouter API September 2026."
version: 2.0.0
author: Alexa
license: MIT
tags: [providers, models, catalog, free, llm]
---

# Free Suffix Catalog — LLM Models for Hermes Agent

## OpenRouter Free Models (19 verified via API, September 2026)

| Model Slug | Provider | Context | Max Output | Notes |
|------------|----------|---------|------------|-------|
| nvidia/nemotron-3.5-lightning:free | NVIDIA | 1,000,000 | - | Primary candidate, large context |
| nvidia/nemotron-3-ultra-550b-a55b:free | NVIDIA | 1,000,000 | - | Current primary, large context |
| nvidia/nemotron-3-super-120b-a12b:free | NVIDIA | 262,144 | - | Strong reasoning |
| nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | NVIDIA | 256,000 | - | Multimodal reasoning |
| nvidia/nemotron-3.5-content-safety:free | NVIDIA | 128,000 | - | Content safety focused |
| thinkingmachines/inkling:free | Thinking Machines | 1,048,576 | - | Large context |
| thinkingmachines/inkling-small:free | Thinking Machines | 1,048,576 | - | Smaller variant |
| google/gemma-4-26b-a4b-it:free | Google | 262,144 | - | Multimodal (image + video) |
| google/gemma-4-31b-it:free | Google | 262,144 | - | Larger Gemma variant |
| cohere/north-mini-code:free | Cohere | 256,000 | - | Code generation, tool-use |
| inclusionai/ling-3.0-flash-sante:free | InclusionAI | 262,144 | - | General purpose |
| inclusionai/ling-3.0-flash-fin:free | InclusionAI | 262,144 | - | Financial domain |
| dots-studio/dots-3-note-preview:free | Dots Studio | 512,000 | - | Note-taking focused |
| liquid/lfm-2.5-2.6b:free | LiquidAI | 65,536 | - | Small, fast |
| poolside/laguna-s-2.1:free | Poolside | 262,144 | - | Coding agent |
| poolside/laguna-xs-2.1:free | Poolside | 262,144 | - | Compact coding agent |
| openrouter/free | OpenRouter | 200,000 | - | Auto-router (random free model) |

## Deprecated / No Longer Free (verified 404)

| Model Slug | Status | Alternative |
|------------|--------|-------------|
| meituan/longcat-2.0:free | 404 unavailable | meituan/longcat-2.0 (paid) |
| google/gemini-2.5-flash:free | 404 unavailable | google/gemini-2.5-flash (paid) |
| deepseek/deepseek-v4-flash:free | 404 unavailable | deepseek/deepseek-v4-flash (paid) |
| upstage/solar-pro4:free | 404 unavailable | upstage/solar-pro4 (paid) |
| minimax/mimo-v2.5-free | 400 invalid ID | minimax/mimo-v2.5 (paid) |

## Test Results (September 2026)

| Model | Provider | Status | Elapsed | Notes |
|-------|----------|--------|---------|-------|
| nvidia/nemotron-3-ultra-550b-a55b:free | openrouter | timeout | 120s | Model very slow to respond |
| nvidia/nemotron-3.5-lightning:free | openrouter | pending | - | Not yet tested |
| nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | openrouter | pending | - | Not yet tested |
| nvidia/nemotron-3-super-120b-a12b:free | openrouter | pending | - | Not yet tested |
| thinkingmachines/inkling:free | openrouter | pending | - | Not yet tested |
| cohere/north-mini-code:free | openrouter | pending | - | Not yet tested |
| google/gemma-4-26b-a4b-it:free | openrouter | pending | - | Not yet tested |
| google/gemma-4-31b-it:free | openrouter | pending | - | Not yet tested |
| inclusionai/ling-3.0-flash-fin:free | openrouter | success | 45.58s | Response received |
| inclusionai/ling-3.0-flash-sante:free | openrouter | pending | - | Not yet tested |
| meta-llama/llama-4-maverick-17b-128e-instruct:free | openrouter | success | 45.24s | Response received |

## Recommended Configuration

### Primary Model
- **Provider**: openrouter
- **Model**: nvidia/nemotron-3-ultra-550b-a55b:free
- **Context**: 1,000,000 tokens
- **Reasoning**: Yes

### Fallback Chain
1. opencode-zen/nemotron-3-ultra-free (if openrouter fails)
2. openrouter/nvidia/nemotron-3.5-lightning:free (large context alternative)
3. openrouter/nvidia/nemotron-3-super-120b-a12b:free (reasoning alternative)
4. openrouter/thinkingmachines/inkling:free (large context backup)

## Documentation URLs
- OpenRouter Free Models: https://openrouter.ai/collections/free-models
- OpenRouter Models API: https://openrouter.ai/api/v1/models
- Gemini API Docs: https://ai.google.dev/gemini-api/docs
- DeepSeek API Docs: https://api-docs.deepseek.com
- Nous Research: https://nousresearch.com
- Hermes Agent Docs: https://hermes-agent.nousresearch.com/docs
