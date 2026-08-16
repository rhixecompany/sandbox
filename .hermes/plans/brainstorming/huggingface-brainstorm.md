# HuggingFace Provider Workflow — Brainstorming

**Date:** 2026-08-16  
**Provider:** huggingface  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `huggingface` (alias: `hf`) |
| Default model | Qwen/Qwen3.5-397B-A17B |
| Auth type | Token |
| Env vars | `HF_TOKEN` (or `HF_INFERENCE_TOKEN` for separate inference token) |
| Base URL | `https://router.huggingface.co/v1` |
| Override | `HF_BASE_URL` env var |
| Models | 100s of open models from 17+ providers (Groq, Together, SambaNova, etc.) |
| Credential pool | Single token |
| Pool strategy | fill_first |
| Role | Fill-first provider (not in main fallback chain) |
| Free tier | $0.10/month credit, no markup on provider rates |
| Routing suffixes | `:fastest` (default), `:cheapest`, `:provider_name` |

---

## What "Repeat the OpenRouter Workflow" Means for HuggingFace

Adapting the 8-step template to HuggingFace:

1. **Credential verification** — Confirm HF_TOKEN in .env (with "Make calls to Inference Providers" permission)
2. **Model selection** — `hermes model` → huggingface → pick from 100s of open models (Llama, Mistral, Qwen, DeepSeek-V3.2, etc.)
3. **Config.yaml validation** — Verify model.provider, model.default_model, HF_BASE_URL override
4. **Fallback chain position** — Not in main fallback chain; fill_first in credential pool
5. **MCP compatibility** — Test MCP servers with huggingface backing model
6. **Rate limit / quota management** — Free tier $0.10/month, backend routing with automatic failover
7. **Routing optimization** — Use `:fastest`, `:cheapest`, or `:provider_name` suffixes
8. **Verification** — `hermes doctor`, test chat

---

## Key Features

- **Unified endpoint**: All models via `router.huggingface.co/v1` — one API, 100s of models
- **Automatic backend routing**: Requests routed to fastest available backend (Groq, Together, SambaNova, etc.) with automatic failover
- **No markup**: Pay provider rates directly, HF adds no markup
- **Free tier**: $0.10/month credit included
- **Routing suffixes**: `:fastest` (default), `:cheapest`, `:provider_name` to force specific backend
- **HF_BASE_URL override**: Custom base URL if needed
- **HF_INFERENCE_TOKEN**: Optional separate token for inference (HF_TOKEN used as backup)

---

## SCAMPER Analysis

### Substitute
- Substitute any model via the unified endpoint — Qwen, Llama, Mistral, DeepSeek-V3.2, etc.
- Substitute backends via routing suffixes — Groq, Together, SambaNova, etc.

### Combine
- HF_TOKEN + OpenRouter = dual open-model access paths
- HuggingFace + local models = comprehensive open-model workflow

### Adapt
- Adapt 8-step template — HF-specific: routing suffixes, backend failover, HF_INFERENCE_TOKEN distinction

### Modify
- Not in main fallback chain — fill_first in credential pool only
- Model access depends on token permissions (Inference Providers permission required)

### Eliminate
- Eliminate if HF_TOKEN lacks Inference Providers permission or is expired

### Reverse
- HuggingFace as primary for open-model workloads? Yes — best access to 100s of open models

---

## Key Questions

1. Is HF_TOKEN set and does it have Inference Providers permission?
2. Is HF_INFERENCE_TOKEN used separately or is HF_TOKEN used for both?
3. Which models are currently accessible?
4. Should huggingface be added to the fallback chain?

---

## Implementation Artifacts Needed

- `.hermes/plans/specs/huggingface-workflow-spec.md`
- `.hermes/plans/huggingface-workflow.md` (implementation plan)
- `.hermes/plans/results/huggingface-*.txt` (execution results)
