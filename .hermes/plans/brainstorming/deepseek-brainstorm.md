# Deepseek Provider Workflow — Brainstorming

**Date:** 2026-08-16  
**Provider:** deepseek  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `deepseek` |
| Default model | varies (deepseek-v4-flash-free via opencode-zen, deepseek-chat, deepseek-coder, DeepSeek-V3.2) |
| Auth type | API key |
| Env var | `DEEPSEEK_API_KEY` |
| Base URL | DeepSeek API |
| Credential pool | Single API key |
| Pool strategy | fill_first |
| Role | Fill-first provider (not in main fallback chain) |

---

## What "Repeat the OpenRouter Workflow" Means for Deepseek

Adapting the 8-step template to Deepseek:

1. **Credential verification** — Confirm DEEPSEEK_API_KEY in .env
2. **Model selection** — `hermes model` → deepseek → pick model (NOTE: deepseek-v4-flash-free is accessed via opencode-zen, not directly via deepseek provider)
3. **Config.yaml validation** — Verify model.provider, model.default_model, base_url
4. **Fallback chain position** — Not in main fallback chain; fill_first in credential pool
5. **MCP compatibility** — Test MCP servers with deepseek backing model
6. **Rate limit / quota management** — Document rate limits and pricing
7. **Known bug awareness** — GitHub #21725: deepseek provider ignores api_key in config.yaml, only reads DEEPSEEK_API_KEY env var
8. **Verification** — `hermes doctor`, test chat

---

## Known Bug

**GitHub #21725**: The DeepSeek provider in Hermes Agent has an implementation defect:
- It completely ignores the `api_key` field configured in config.yaml
- Hardcoded to only read the `DEEPSEEK_API_KEY` environment variable
- This is inconsistent with other providers (OpenAI, Anthropic, etc.) which read from config.yaml first, then fall back to env var

**Impact**: If you set `api_key` in config.yaml but don't set `DEEPSEEK_API_KEY` env var, authentication fails.

---

## Model Access Clarification

- `deepseek-v4-flash-free` — accessed via **opencode-zen** provider, NOT directly via deepseek provider
- `deepseek-chat`, `deepseek-coder` — may be accessible via direct deepseek provider
- `DeepSeek-V3.2` — accessible via huggingface provider or direct deepseek provider

The deepseek provider in config.yaml may serve a different purpose than opencode-zen's deepseek-v4-flash-free.

---

## SCAMPER Analysis

### Substitute
- deepseek-v4-flash-free via opencode-zen vs direct deepseek provider — different access paths for different models
- Substitute with DeepSeek-V3.2 via huggingface provider

### Combine
- deepseek provider + opencode-zen = two access paths for DeepSeek models
- DEEPSEEK_API_KEY + credential pooling = rate limit distribution

### Adapt
- Adapt 8-step template — deepseek-specific: known bug workaround, dual access path clarification

### Modify
- Not in main fallback chain — fill_first in credential pool only
- Bug #21725: must set DEEPSEEK_API_KEY env var, not just config.yaml api_key

### Eliminate
- Eliminate if DEEPSEEK_API_KEY is not set or invalid

### Reverse
- deepseek as primary via opencode-zen (already the case for active model) — direct deepseek provider is supplementary

---

## Key Questions

1. Is DEEPSEEK_API_KEY set in .env?
2. Is the deepseek provider used directly or only as a credential pool entry?
3. What models are accessible via the direct deepseek provider vs opencode-zen?
4. Is bug #21725 causing any authentication issues?

---

## Implementation Artifacts Needed

- `.hermes/plans/specs/deepseek-workflow-spec.md`
- `.hermes/plans/deepseek-workflow.md` (implementation plan)
- `.hermes/plans/results/deepseek-*.txt` (execution results)
