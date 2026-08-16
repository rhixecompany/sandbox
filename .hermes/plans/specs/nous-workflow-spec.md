# Deepseek Provider Workflow Specification

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

## Workflow Steps

### Step 1: Credential Verification

**Actions:**
- [ ] Confirm `DEEPSEEK_API_KEY` is set in `.env`
- [ ] Run `hermes auth list deepseek` to verify credential
- [ ] Run `hermes doctor` to validate connectivity

**Expected result:** API key valid, connectivity confirmed

**Acceptance criteria:** `hermes doctor` reports deepseek connectivity

---

### Step 2: Model Selection & Validation

**Actions:**
- [ ] Run `hermes model` → select deepseek → list available models
- [ ] **Critical distinction:** deepseek-v4-flash-free is accessed via opencode-zen, NOT directly via deepseek provider
- [ ] Check available models via direct deepseek provider: deepseek-chat, deepseek-coder, DeepSeek-V3.2
- [ ] Verify context window ≥ 64K for selected models

**Expected result:** Model list accessible, model access paths clarified

**Acceptance criteria:** Model access paths documented (direct vs opencode-zen)

---

### Step 3: Config.yaml Review

**Actions:**
- [ ] Verify `model.provider: deepseek` is correct
- [ ] **BUG AWARENESS (GitHub #21725):** The deepseek provider IGNORES `api_key` in config.yaml — only reads `DEEPSEEK_API_KEY` env var
- [ ] Verify `DEEPSEEK_API_KEY` env var is set (NOT just config.yaml api_key)
- [ ] Check `fill_first` strategy in credential pool

**Expected result:** Config reviewed with bug awareness

**Acceptance criteria:** Bug #21725 documented; env var verified as primary auth method

---

### Step 4: Fallback Chain Position

**Actions:**
- [ ] Document that deepseek is NOT in the main `fallback_providers` chain
- [ ] Explain fill_first role: used when credential pool fires, not as systematic fallback

**Expected result:** Fallback position documented

**Acceptance criteria:** Position clarified

---

### Step 5: MCP Server Compatibility

**Actions:**
- [ ] Test MCP servers with deepseek backing model (sample at least 1)
- [ ] Document any provider-specific quirks

**Expected result:** MCP compatibility verified

**Acceptance criteria:** At least 1 MCP server tested

---

### Step 6: Rate Limit & Quota Management

**Actions:**
- [ ] Document rate limits for DeepSeek API
- [ ] Identify pricing model (free tier vs paid)
- [ ] Document known DeepSeek API reliability patterns

**Expected result:** Rate limit documentation complete

**Acceptance criteria:** Limits and pricing documented

---

## Known Bug: GitHub #21725

**Issue:** DeepSeek provider ignores `api_key` in config.yaml

**Description:** The DeepSeek provider in Hermes Agent has an implementation defect:
- It completely ignores the `api_key` field configured in config.yaml
- Hardcoded to only read the `DEEPSEEK_API_KEY` environment variable
- This is inconsistent with other providers (OpenAI, Anthropic, etc.) which read from config.yaml first, then fall back to env var

**Impact:** If you set `api_key` in config.yaml but don't set `DEEPSEEK_API_KEY` env var, authentication fails.

**Workaround:** Always set `DEEPSEEK_API_KEY` in `.env`, not just in config.yaml.

**Fix status:** Bug reported — not yet fixed. Must work around until fixed.

---

## Model Access Clarification

| Model | Access Path | Notes |
|-------|------------|-------|
| deepseek-v4-flash-free | opencode-zen provider | Active model across all profiles |
| deepseek-chat | direct deepseek provider | May be available |
| deepseek-coder | direct deepseek provider | May be available |
| DeepSeek-V3.2 | huggingface provider or direct deepseek | Available via HF Inference |

---

## Open Questions

1. Is `DEEPSEEK_API_KEY` currently valid?
2. Is the deepseek provider used directly or only as a credential pool entry?
3. What models are accessible via the direct deepseek provider vs opencode-zen?
4. Is bug #21725 causing any authentication issues in this environment?

## Research Notes

- DeepSeek provider in config.yaml credential pool with fill_first strategy
- `DEEPSEEK_API_KEY` env var required (NOT config.yaml api_key — bug #21725)
- deepseek-v4-flash-free is the active model — but accessed via opencode-zen, not directly
- DeepSeek models known for strong coding capabilities
- API has rate limits and quota management
- Bug #21725: must set DEEPSEEK_API_KEY env var, not just config.yaml api_key
