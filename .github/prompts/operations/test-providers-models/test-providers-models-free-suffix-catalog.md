---
name: test-providers-models-free-suffix-catalog
title: "Free Suffix Catalog"
description: "Catalog of free LLM models across all authorized providers for Hermes Agent testing"
version: 1.0.0
author: Alexa
license: MIT
tags: [providers, models, catalog, free, llm]
---

# Free Suffix Catalog — LLM Models for Hermes Agent

## Provider: OpenRouter
| Model | Context | Max Output | Capabilities | API URL |
|-------|---------|------------|--------------|---------|
| nvidia/nemotron-3-ultra-550b-a55b:free | 131K | 16K | reasoning, tool_use, code | https://openrouter.ai/api/v1 |
| nvidia/nemotron-3-nano-omni-30b-a3b | 131K | 8K | reasoning, tool_use | https://openrouter.ai/api/v1 |
| meituan/longcat-2.0:free | 131K | 8K | reasoning, code, tool_use | https://openrouter.ai/api/v1 |
| meta-llama/llama-4-maverick-17b-128e-instruct:free | 131K | 8K | reasoning, code | https://openrouter.ai/api/v1 |
| google/gemini-2.5-flash:free | 1M | 8K | reasoning, tool_use, vision | https://openrouter.ai/api/v1 |
| deepseek/deepseek-v4-flash:free | 131K | 8K | reasoning, code, tool_use | https://openrouter.ai/api/v1 |
| minimax/mimo-v2.5-free | 131K | 8K | reasoning, code | https://openrouter.ai/api/v1 |
| upstage/solar-pro4:free | 131K | 8K | reasoning, code, tool_use | https://openrouter.ai/api/v1 |
| ling-3.0-flash-fin:free | 131K | 8K | reasoning, code | https://openrouter.ai/api/v1 |
| inkling:free | 131K | 8K | reasoning, code | https://openrouter.ai/api/v1 |

## Provider: Nous Research (via OpenRouter)
| Model | Context | Max Output | Capabilities | API URL |
|-------|---------|------------|--------------|---------|
| upstage/solar-pro4:free | 131K | 8K | reasoning, code, tool_use | https://openrouter.ai/api/v1 |
| nousresearch/hermes-4-70b | 131K | 8K | reasoning, tool_use, code | https://openrouter.ai/api/v1 |

## Provider: Google Gemini (Direct)
| Model | Context | Max Output | Capabilities | API URL |
|-------|---------|------------|--------------|---------|
| gemini-2.5-flash | 1M | 8K | reasoning, tool_use, vision | https://generativelanguage.googleapis.com/v1 |
| gemini-3-flash-preview | 1M | 8K | reasoning, tool_use, vision | https://generativelanguage.googleapis.com/v1 |
| gemini-2.5-flash-lite | 1M | 8K | reasoning, tool_use | https://generativelanguage.googleapis.com/v1 |

## Provider: DeepSeek (Direct)
| Model | Context | Max Output | Capabilities | API URL |
|-------|---------|------------|--------------|---------|
| deepseek-v4-flash | 131K | 8K | reasoning, code, tool_use | https://api.deepseek.com/v1 |
| deepseek-chat (legacy) | 131K | 8K | reasoning, code | https://api.deepseek.com/v1 |

## Provider: OpenCode Zen (Pool)
| Model | Context | Max Output | Capabilities | API URL |
|-------|---------|------------|--------------|---------|
| nemotron-3-ultra-free | 131K | 16K | reasoning, tool_use, code | https://inference-api.nousresearch.com/v1 |
| deepseek-v4-flash-free | 131K | 8K | reasoning, code, tool_use | https://inference-api.nousresearch.com/v1 |

## Test Status
| Model | Tested | Status | Score |
|-------|--------|--------|-------|
| nvidia/nemotron-3-ultra-550b-a55b:free | - | pending | - |
| meituan/longcat-2.0:free | - | pending | - |
| google/gemini-2.5-flash:free | - | pending | - |
| deepseek/deepseek-v4-flash:free | - | pending | - |
| upstage/solar-pro4:free | - | pending | - |
| minimax/mimo-v2.5-free | - | pending | - |
| ling-3.0-flash-fin:free | - | pending | - |
| inkling:free | - | pending | - |
| nvidia/nemotron-3-nano-omni-30b-a3b | - | pending | - |
| meta-llama/llama-4-maverick-17b-128e-instruct:free | - | pending | - |

## Documentation URLs
- OpenRouter Free Models: https://openrouter.ai/collections/free-models
- OpenRouter Models: https://openrouter.ai/models
- Gemini API Docs: https://ai.google.dev/gemini-api/docs
- DeepSeek API Docs: https://api-docs.deepseek.com
- Nous Research: https://nousresearch.com
- Hermes Agent Docs: https://hermes-agent.nousresearch.com/docs
