# xAI (Grok) Provider Workflow Specification

**Date:** 2026-08-16  
**Provider:** xai  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `xai` (direct API) / `xai-oauth` (SuperGrok) |
| Default model | grok-4.3 (OAuth) / varies (API key) |
| Auth type | API key (XAI_API_KEY) OR OAuth (SuperGrok/X Premium+) |
| Env var | `XAI_API_KEY` (direct API) |
| Base URL | xAI API |
| Models | grok-4.3 (1M context), grok-4.3-fast, grok-4.6, voxtral-mini-tts-2603 (TTS) |
| Credential pool | Single key or OAuth token |
| Pool strategy | fill_first |
| Role | Fill-first provider (not in main fallback chain) |
| Direct tools | TTS, image gen, video gen, transcription, X search |

---

## Workflow Steps

### Step 1: Credential Verification

**Actions:**
- [ ] Confirm `XAI_API_KEY` is set in `.env` (direct API path) OR verify SuperGrok OAuth
- [ ] Run `hermes auth list xai` / `hermes auth list xai-oauth` to verify credential
- [ ] Run `hermes doctor` to validate connectivity
- [ ] Determine which auth path is active: API key or OAuth

**Expected result:** Credential valid, connectivity confirmed

**Acceptance criteria:** Doctor reports connectivity or chat test succeeds

---

### Step 2: Model Selection & Validation

**Actions:**
- [ ] Run `hermes model` → select xai/xai-oauth → list available models
- [ ] Confirm grok-4.3 (1M context) or grok-4.6 is selectable
- [ ] Check grok-4.3-fast (cheaper, same large context)
- [ ] Verify context window meets 64K minimum

**Expected result:** Model list accessible, key models verified

**Acceptance criteria:** At least 1 Grok model confirmed available

---

### Step 3: Config.yaml Review

**Actions:**
- [ ] Verify `model.provider: xai` or `xai-oauth` is correct
- [ ] Verify `model.default_model` is set appropriately
- [ ] Check `fill_first` strategy in credential pool
- [ ] Note: xai is NOT in the main `fallback_providers` chain

**Expected result:** Config sections correct

**Acceptance criteria:** Config values match expected state

---

### Step 4: Direct-to-xAI Tools Verification

**Actions:**
- [ ] Check TTS configuration: voxtral-mini-tts-2603
- [ ] Verify image gen, video gen, transcription tools availability
- [ ] Check X search tool availability
- [ ] Document which tools are auto-enabled by OAuth token

**Expected result:** Direct tools documented

**Acceptance criteria:** Direct-to-xAI tools inventory complete

---

### Step 5: Provider Aliases

**Actions:**
- [ ] Document provider aliases: `xai-oauth`, `grok-oauth`, `x-ai-oauth`, `xai-grok-oauth`
- [ ] Verify alias resolution works correctly

**Expected result:** Aliases documented

**Acceptance criteria:** All aliases listed

---

### Step 6: MCP Server Compatibility

**Actions:**
- [ ] Test MCP servers with xai backing model (sample at least 1)
- [ ] Document any provider-specific quirks

**Expected result:** MCP compatibility verified

**Acceptance criteria:** At least 1 MCP server tested

---

## Two Auth Paths

### API Key Path (provider: `xai`)
```
XAI_API_KEY in .env
model:
  provider: xai
  default: grok-4.3
```

### OAuth Path (provider: `xai-oauth`)
```
hermes auth xai  # browser OAuth flow
model:
  provider: xai-oauth
  default: grok-4.3
```

**Same OAuth token auto-reused by:** TTS, image gen, video gen, transcription, X search

---

## Provider Aliases

| Alias | Resolves to |
|-------|-------------|
| `xai-oauth` | xai-oauth (canonical) |
| `grok-oauth` | xai-oauth |
| `x-ai-oauth` | xai-oauth |
| `xai-grok-oauth` | xai-oauth |

---

## Open Questions

1. Is the xAI API key currently valid, or is SuperGrok OAuth used?
2. Is xAI used for chat or only TTS in this environment?
3. What Grok models are available via the current auth method?
4. Should xAI be added to the fallback chain?

## Research Notes

- xAI/Grok provider in config.yaml credential pool with fill_first strategy
- TTS model: voxtral-mini-tts-2603
- SuperGrok OAuth: sign in with xAI account (no API key), includes grok-composer-2.5-fast
- model_catalog references grok-4.20-reasoning
- grok-4.3 has 1M token context — excellent for large codebases
- Config section under `xai` provider in config.yaml
- Direct-to-xAI tools auto-enabled by OAuth token
