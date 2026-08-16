# Ollama-Cloud Provider Workflow Specification

**Date:** 2026-08-16  
**Provider:** ollama-cloud  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `ollama-cloud` |
| Default model | nemotron-3-ultra |
| Auth type | API key |
| Env var | `OLLAMA_API_KEY` |
| Base URL | Ollama Cloud API (`https://ollama.com forwardslash v1`) |
| Credential pool | Single API key |
| Pool strategy | fill_first |
| Role | 4th/last in fallback chain |
| Model discovery | Dynamic from `ollama.com/v1/models`, cached 1 hour |

---

## Workflow Steps

### Step 1: Credential Verification

**Actions:**
- [ ] Confirm `OLLAMA_API_KEY` is set in `.env`
- [ ] Run `hermes auth list ollama-cloud` to verify credential
- [ ] Run `hermes doctor` to validate connectivity
- [ ] Test with a simple chat query

**Expected result:** API key valid, connectivity confirmed

**Acceptance criteria:** Chat test succeeds

---

### Step 2: Model Selection & Validation

**Actions:**
- [ ] Run `hermes model` → select ollama-cloud → list dynamically discovered models
- [ ] Confirm nemotron-3-ultra is selectable
- [ ] Check other available models: gpt-oss:120b, glm-4.6:cloud, glm-5.1, qwen3-coder:480b-cloud, mistral-large, minimax-n2.7
- [ ] Verify context window ≥ 64K for all selected models (CRITICAL for Hermes)

**Expected result:** Model list accessible, context windows verified

**Acceptance criteria:** At least 1 model confirmed with context ≥ 64K

---

### Step 3: Config.yaml Review

**Actions:**
- [ ] Verify `model.provider: ollama-cloud` is correct
- [ ] Verify `model.default_model: nemotron-3-ultra` is set
- [ ] Check that ollama-cloud is last in `fallback_providers` chain

**Expected result:** Config sections correct

**Acceptance criteria:** All config values match expected state

---

### Step 4: Fallback Behavior

**Actions:**
- [ ] Confirm ollama-cloud is last resort in fallback chain
- [ ] Document scenarios where this would be triggered
- [ ] Evaluate if ollama-cloud should be promoted (free models available)

**Expected result:** Fallback position documented

**Acceptance criteria:** Fallback chain position confirmed; promotion recommendation made

---

### Step 5: MCP Server Compatibility

**Actions:**
- [ ] Test MCP servers with ollama-cloud backing model (sample at least 1)
- [ ] Document any provider-specific quirks

**Expected result:** MCP compatibility verified

**Acceptance criteria:** At least 1 MCP server tested

---

### Step 6: Rate Limit & Quota Management

**Actions:**
- [ ] Document rate limits for nemotron-3-ultra on Ollama Cloud
- [ ] Identify pricing model (free tier vs paid)
- [ ] Document model availability guarantees

**Expected result:** Rate limit documentation complete

**Acceptance criteria:** Pricing and limits documented

---

## Model Discovery Details

- Model catalog fetched dynamically from `ollama.com/v1/models`
- Cache TTL: 1 hour
- `model:tag` notation preserved (e.g., `qwen3-coder:480b-cloud`) — don't use dashes
- Available models: gpt-oss:120b, glm-4.6:cloud, glm-5.1, qwen3-coder:480b-cloud, kimi-k2.5, minimax-n2.7, mistral-large, and more

---

## Ollama Cloud vs Local Ollama

| Aspect | Ollama Cloud | Local Ollama |
|--------|-------------|--------------|
| GPU required | No | Yes |
| API key | Required (OLLAMA_API_KEY) | Not required (localhost) |
| Models | Cloud-hosted catalog | Locally downloaded |
| Cost | Free tier + paid | Free (hardware cost only) |
| Context | Model-dependent | Model-dependent |

---

## Open Questions

1. Is the Ollama Cloud API key currently valid?
2. What is the pricing model — free tier, paid, or trial?
3. Are there context window limitations for available models?
4. Should ollama-cloud be promoted in the fallback chain (free models available)?

## Research Notes

- Ollama Cloud provides managed Ollama-hosted models
- `OLLAMA_API_KEY` required, get from ollama.com/settings/keys
- Default model: nemotron-3-ultra
- Part of fallback chain as last resort
- Config section in config.yaml under `ollama-cloud` provider
- Dynamic model discovery is a key feature — models can change
- Free API key available from Ollama; many models free to use
