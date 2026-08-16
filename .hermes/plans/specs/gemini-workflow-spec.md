# OpenRouter Provider Workflow Specification

**Date:** 2026-08-16  
**Provider:** openrouter  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `openrouter` |
| Default model | nvidia/nemotron-3-ultra-550b-a55b:free |
| Auth type | API key |
| Env var | `OPENROUTER_API_KEY` |
| Base URL | `https://openrouter.ai/api/v1` |
| Models available | 400+ across 70+ providers |
| Credential pool | 1 key (OPENROUTER_API_KEY, env var) |
| Pool strategy | fill_first |
| Role | Primary fallback (2nd in chain after opencode-zen) |
| Response cache | true, TTL: 300s |
| min_coding_score | 0.65 |

---

## Workflow Steps

### Step 1: Credential Verification

**Actions:**
- [ ] Confirm `OPENROUTER_API_KEY` is set in `.env`
- [ ] Run `hermes auth list openrouter` to verify credential
- [ ] Run `hermes doctor` to validate connectivity
- [ ] Test with a simple chat query

**Expected result:** API key valid, connectivity confirmed

**Acceptance criteria:** `hermes doctor` reports openrouter connectivity; chat test succeeds

---

### Step 2: Model Selection & Validation

**Actions:**
- [ ] Run `hermes model` → select openrouter → list available models
- [ ] Verify nvidia/nemotron-3-ultra-550b-a55b:free is available
- [ ] Check alternative free models: nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free, nvidia/nemotron-3-super-120b-a12b:free
- [ ] Document model tier (free vs paid) and rate limits

**Expected result:** Model list accessible, key models verified

**Acceptance criteria:** At least 3 models confirmed available

---

### Step 3: Provider Routing Configuration

**Actions:**
- [ ] Review `provider_routing` section in config.yaml for openrouter
- [ ] Check `sort`, `only`, `ignore`, `order`, `require_parameters`, `data_collection` settings
- [ ] Test routing behavior with a model-specific query

**Expected result:** Provider routing config documented

**Acceptance criteria:** Routing settings documented; routing behavior verified

---

### Step 4: Fallback Chain Verification

**Actions:**
- [ ] Confirm openrouter is 2nd in `fallback_providers` chain
- [ ] Test fallback trigger: simulate opencode-zen failure, verify openrouter takes over
- [ ] Document mid-session model swap behavior

**Expected result:** Fallback chain functional

**Acceptance criteria:** Fallback position confirmed; chain behavior documented

---

### Step 5: Auxiliary Model Offload

**Actions:**
- [ ] Check if openrouter is configured for auxiliary tasks (vision, web extraction)
- [ ] Recommendation: use cheapest trusted model for side tasks (e.g., Gemini Flash on OpenRouter)
- [ ] Document cost optimization strategies

**Expected result:** Auxiliary model strategy documented

**Acceptance criteria:** Cost optimization recommendations documented

---

### Step 6: MCP Server Compatibility

**Actions:**
- [ ] Test all 21 MCP servers with openrouter as the backing model (sample at least 3)
- [ ] Document any provider-specific MCP quirks
- [ ] Pay special attention to MCP servers using npx (node CLI) — Windows quirks

**Expected result:** MCP compatibility verified

**Acceptance criteria:** At least 3 MCP servers tested; quirks documented

---

### Step 7: Rate Limit & Quota Management

**Actions:**
- [ ] Document free tier rate limits for key models
- [ ] Identify credential pooling strategy (single key — no backup)
- [ ] Document retry behavior on 429 responses
- [ ] **Recommendation:** Add backup OPENROUTER_API_KEY to credential pool

**Expected result:** Rate limit strategy documented

**Acceptance criteria:** Rate limits documented; credential pool gap identified

---

### Step 8: Reference Models

**Actions:**
- [ ] Review `reference_models` config: opencode-zen/nemotron-3-ultra-free, openrouter/nemotron-3-ultra-550b-a55b:free, openrouter/nemotron-3-super-120b-a12b:free
- [ ] Verify these are used for cost/quality comparison

**Expected result:** Reference models documented

**Acceptance criteria:** Reference model configuration reviewed

---

## Provider Routing Details

| Control | Description | Config Value |
|---------|-------------|--------------|
| `sort` | Throughput/price sorting (`:nitro`, `:floor`) | Not configured (defaults) |
| `only` | Restrict to specific underlying providers | Not configured |
| `ignore` | Exclude specific underlying providers | Not configured |
| `order` | Priority order for provider selection | Not configured |
| `require_parameters` | Require specific params | Not configured |
| `data_collection` | Data sharing preferences | Not configured |

---

## Open Questions

1. What is the current `OPENROUTER_API_KEY` tier (free vs paid)?
2. Have there been 429 rate limit incidents in this environment?
3. Which underlying OpenRouter providers are currently routing requests?
4. Should a backup API key be added to the credential pool?

## Research Notes

- OpenRouter is Hermes Agent's **default fallback aggregator** — one key routes to 200+ models
- Hermes ranks #1 on OpenRouter app rankings (17T+ tokens processed as of June 2026)
- Popular models via OpenRouter with Hermes: Claude, GPT-4o, Gemini, DeepSeek, Grok, Kimi, GLM
- `:nitro` suffix for throughput sorting, `:floor` for price sorting
- Fallback providers swap model mid-session without losing conversation
- Auxiliary model offload: route simple tasks (vision, web extraction) to cheapest trusted model
- Response cache enabled: 300s TTL — reduces duplicate API calls
