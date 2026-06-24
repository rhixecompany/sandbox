---
name: plan-models-openrouter-noun-openai-zen
title: Plan to List and Select Top 3 Free Models from OpenRouter, NVIDIA NIM, and OpenAI Zen Providers
description: Plan to gather model lists from specified providers, filter for free models, evaluate context length, knowledge cutoff, and reasoning capabilities, and select the top three models.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [planning, model-selection, openrouter, nvidia, openai]
---

# Plan: List and Select Top 3 Free Models from OpenRouter, NVIDIA NIM, and OpenAI Zen Providers

## Goal

Retrieve the list of available models from OpenRouter, NVIDIA NIM (referred to as "noun" in the request), and OpenAI Zen provider, filter for free models, evaluate them based on context length, knowledge cutoff date, and reasoning capabilities, and select the top three models.

## Current Context / Assumptions

- The user has access to the Hermes agent with web search, terminal, and MCP tools (fetch, etc.).
- The provider "noun" likely refers to NVIDIA NIM (NVIDIA Inference Microservices) provider, which may be disabled in the current Hermes configuration but can still be queried via its public API if available.
- OpenAI Zen provider likely refers to an OpenAI-compatible endpoint offered under the "zen" branding (maybe via OpenRouter or a specific endpoint). We will need to investigate.
- Free models are defined as those with zero cost per token (or a free tier) as indicated by the provider's pricing field.
- Context length and knowledge cutoff are typical model metadata fields; reasoning capabilities may be inferred from model name, family, or benchmark scores if provided.
- We will use web search and HTTP fetch to gather data, then process and rank.

## Proposed Approach

1. **Discover API endpoints** for each provider that list models with metadata.
   - OpenRouter: `https://openrouter.ai/api/v1/models`
   - NVIDIA NIM: Possibly `https://integrate.api.nvidia.com/v1/models` or similar; need to verify.
   - OpenAI Zen: Possibly an OpenAI-compatible endpoint like `https://api.zen.ai/v1/models` or via OpenRouter; we will search.
2. **Fetch model lists** from each endpoint using HTTP GET (via `fetch` MCP or `curl` in terminal).
3. **Parse JSON** to extract model ID, context length, knowledge cutoff, pricing, and any reasoning-related fields.
4. **Filter** models where price == 0 or free tier is available.
5. **Score** each model:
   - Primary: context length (higher is better).
   - Secondary: knowledge cutoff date (newer is better).
   - Tertiary: reasoning capability (if indicated by model name/family like "Reasoning", "o1", "Qwen\*", "Nemotron", etc.).
6. **Rank** models within each provider, then combine and pick top 3 overall.
7. **Output** a summary table with model name, provider, context length, cutoff, reasoning indicator, and cost.

## Step-by-Step Plan

1. **Research API endpoints**
   - Use web search to find the correct model listing URLs for NVIDIA NIM and OpenAI Zen providers.
   - Document the endpoints and any required headers (e.g., API keys may not be needed for public listing).
2. **Fetch data**
   - For each provider, issue a GET request to the models endpoint.
   - Save raw JSON responses to temporary files for inspection.
3. **Parse and normalize**
   - Extract fields: `id`, `context_length` (or `max_context_length`), `training_data`/`knowledge_cutoff`, `pricing` (prompt/completion cost), `architecture`, `top_provider`.
   - Normalize naming across providers.
4. **Filter free models**
   - Keep models where `prompt_cost` == 0 and `completion_cost` == 0 (or where `free_tier` is true).
5. **Score and rank**
   - Assign weights: 50% context length (normalized), 30% knowledge cutoff (newer = higher score), 20% reasoning indicator (boolean or based on known reasoning models).
   - Compute total score.
6. **Select top 3**
   - Pick the three highest-scoring models across all providers.
7. **Validate**
   - Cross-check model details on provider websites or known benchmarks.
8. **Report**
   - Create a markdown table with the selected models and their key attributes.
   - Note any caveats (e.g., rate limits, availability).

## Files Likely to be Changed / Created

- Temporary JSON files in `/tmp` or workspace for raw API responses.
- Final report: `.hermes/plans/2026-06-24_215027-list-models-openrouter-noun-openai-zen-select-top3-free-models.md` (this plan) and possibly a separate results file in `.hermes/plans/` or workspace root if user wants output.

## Tests / Validation

- Verify that each selected model is indeed free by checking pricing on provider's website.
- Ensure context length and cutoff values are plausible (e.g., context length > 1K, cutoff date after 2020).
- If possible, make a trivial test request to the model endpoint (if API key available) to confirm accessibility, but this is optional for the plan.

## Risks, Tradeoffs, and Open Questions

- **Provider API availability**: Some provider model listings may require authentication or may not be publicly accessible. We may need to rely on web scraping or alternative sources.
- **Definition of "free"**: Some models may have free tier with rate limits; we need to decide if that counts as free.
- **Reasoning capability metric**: This is subjective; we may rely on known model families (e.g., models with "Reasoning" in name, or those known for strong reasoning like Qwen\*-RM, Nemotron 4 340B Instruct, etc.).
- **Data freshness**: The model lists may change; we will note the timestamp of retrieval.
- **Ambiguity of "noun" and "openai zen"**: If the intended providers differ, the plan may need adjustment after clarification.

## References

- .hermes.md for provider configuration and MCP tools.
- OpenRouter API documentation (<https://openrouter.ai/docs>).
- NVIDIA NIM API documentation (if available).
- OpenAI compatible API standards.
