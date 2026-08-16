# HuggingFace Provider Workflow Specification

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

## Workflow Steps

### Step 1: Credential Verification

**Actions:**
- [ ] Confirm `HF_TOKEN` is set in `.env` (must have "Make calls to Inference Providers" permission)
- [ ] Check if `HF_INFERENCE_TOKEN` is set separately (optional)
- [ ] Run `hermes auth list huggingface` to verify credential
- [ ] Run `hermes doctor` to validate connectivity

**Expected result:** Token valid, connectivity confirmed

**Acceptance criteria:** `hermes doctor` reports huggingface connectivity

---

### Step 2: Model Selection & Validation

**Actions:**
- [ ] Run `hermes model` → select huggingface → list available models
- [ ] Confirm Qwen/Qwen3.5-397B-A17B is selectable
- [ ] Check other models: deepseek-ai/DeepSeek-V3.2, Llama, Mistral, and 100s more
- [ ] Test routing suffixes: `:fastest`, `:cheapest`, `:provider_name`
- [ ] Verify context window ≥ 64K for selected models

**Expected result:** Model list accessible, routing suffixes functional

**Acceptance criteria:** At least 2 models confirmed available; routing suffix tested

---

### Step 3: Config.yaml Review

**Actions:**
- [ ] Verify `model.provider: huggingface` is correct
- [ ] Verify `model.default_model: Qwen/Qwen3.5-397B-A17B` is set
- [ ] Check `fill_first` strategy in credential pool
- [ ] Note: huggingface is NOT in the main `fallback_providers` chain

**Expected result:** Config sections correct

**Acceptance criteria:** All config values match expected state

---

### Step 4: Backend Routing Analysis

**Actions:**
- [ ] Document backend providers: Groq, Together, SambaNova, and more
- [ ] Explain automatic failover behavior
- [ ] Document routing suffix behavior:
  - `:fastest` — default, routes to fastest available backend
  - `:cheapest` — routes to cheapest backend
  - `:provider_name` — force specific backend (e.g., `:groq`)

**Expected result:** Backend routing documented

**Acceptance criteria:** Routing suffixes documented with examples

---

### Step 5: MCP Server Compatibility

**Actions:**
- [ ] Test MCP servers with huggingface backing model (sample at least 1)
- [ ] Document any provider-specific quirks

**Expected result:** MCP compatibility verified

**Acceptance criteria:** At least 1 MCP server tested

---

### Step 6: Rate Limit & Quota Management

**Actions:**
- [ ] Document free tier: $0.10/month credit, no markup
- [ ] Document rate limits for Inference Providers
- [ ] Identify cold start / latency behavior (serverless endpoints)

**Expected result:** Rate limit documentation complete

**Acceptance criteria:** Free tier and limits documented

---

## HF_TOKEN vs HF_INFERENCE_TOKEN

| Token | Purpose | Permission Needed |
|-------|---------|-------------------|
| `HF_TOKEN` | Primary token, backup for inference | Write access (default) |
| `HF_INFERENCE_TOKEN` | Dedicated inference token (optional) | "Make calls to Inference Providers" |

**Recommendation:** Use `HF_TOKEN` with Inference Providers permission for simplicity. Set `HF_INFERENCE_TOKEN` separately only if you need to isolate inference access.

---

## Open Questions

1. Is `HF_TOKEN` currently valid and does it have Inference Providers permission?
2. Is `HF_INFERENCE_TOKEN` used separately or is `HF_TOKEN` used for both?
3. Which models are currently accessible with the current token?
4. Should huggingface be added to the fallback chain?

## Research Notes

- HuggingFace Inference Providers routes to 20+ open models through unified OpenAI-compatible endpoint
- `router.huggingface.co/v1` — one API, 100s of models
- Automatic backend routing: requests routed to fastest available backend with automatic failover
- No markup on provider rates — pay provider rates directly
- Free tier: $0.10/month credit included
- Routing suffixes: `:fastest` (default), `:cheapest`, `:provider_name`
- `HF_BASE_URL` env var overrides default base URL
- Token must have "Make calls to Inference Providers" permission
- Popular models: Qwen/Qwen3.5-397B-A17B, deepseek-ai/DeepSeek-V3.2, Llama, Mistral
