# Gemini Provider Workflow Specification

**Date:** 2026-08-16  
**Provider:** gemini  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `gemini` |
| Default model | gemini-2.5-flash |
| Auth type | API key |
| Env vars | `GOOGLE_API_KEY` or `GEMINI_API_KEY` |
| Base URL | `https://generativelanguage.googleapis.com/v1beta` |
| Credential pool | Single API key |
| Pool strategy | fill_first |
| Role | 3rd in fallback chain |
| TTS model | gemini-2.5-flash-preview-tts |

---

## Workflow Steps

### Step 1: Credential Verification

**Actions:**
- [ ] Confirm `GOOGLE_API_KEY` or `GEMINI_API_KEY` is set in `.env`
- [ ] Run `hermes auth list gemini` to verify credential
- [ ] Run `hermes doctor` to validate connectivity
- [ ] **Workaround for known bug:** If doctor reports "invalid API key", verify actual chat works (GitHub #26623)

**Expected result:** API key valid, connectivity confirmed

**Acceptance criteria:** Chat test succeeds even if doctor shows false positive

---

### Step 2: Model Selection & Validation

**Actions:**
- [ ] Run `hermes model` → select gemini → list available models
- [ ] Confirm gemini-2.5-flash is selectable
- [ ] Check available models: gemini-2.5-flash, gemini-2.5-pro, gemma models
- [ ] Verify context window meets 64K minimum requirement

**Expected result:** Model list accessible, key models verified

**Acceptance criteria:** gemini-2.5-flash confirmed available; context window ≥ 64K

---

### Step 3: Config.yaml Review

**Actions:**
- [ ] Verify `model.provider: gemini` is correct
- [ ] Verify `model.default_model: gemini-2.5-flash` is set
- [ ] Check that gemini is 3rd in `fallback_providers` chain

**Expected result:** Config sections correct

**Acceptance criteria:** All config values match expected state

---

### Step 4: Free Tier Quota Awareness

**Actions:**
- [ ] **Critical:** Document free tier quota limitations
- [ ] Estimate per-session quota consumption (tool calls, retries, compression, auxiliary tasks)
- [ ] Check for quota exhaustion in recent sessions
- [ ] Evaluate paid tier upgrade if free tier insufficient

**Expected result:** Quota analysis complete

**Acceptance criteria:** Free tier limitations documented; usage estimate provided

---

### Step 5: MCP Server Compatibility

**Actions:**
- [ ] Test MCP servers with gemini backing model (sample at least 2)
- [ ] Document any Gemini-specific MCP quirks
- [ ] Test structured tool calls (function calling) — Gemini support varies by model

**Expected result:** MCP compatibility verified

**Acceptance criteria:** At least 2 MCP servers tested

---

### Step 6: Auxiliary Model Offload

**Actions:**
- [ ] Gemini Flash is recommended for auxiliary tasks (cheap, fast)
- [ ] Consider explicit `auxiliary.<task>.provider` + `auxiliary.<task>.model` config
- [ ] Document cost/quality tradeoffs vs OpenRouter routing

**Expected result:** Auxiliary model strategy documented

**Acceptance criteria:** Auxiliary offload recommendations documented

---

### Step 7: Gateway Compatibility

**Actions:**
- [ ] Gemini works with all Hermes gateway platforms (Telegram, Discord, Slack, etc.)
- [ ] Verify gateway config if gateway is used

**Expected result:** Gateway compatibility confirmed

**Acceptance criteria:** Gateway setup documented if applicable

---

## Known Issues

| Issue | ID | Workaround |
|-------|----|------------|
| hermes doctor false positive | #26623 | Test actual chat instead of relying on doctor |
| Free tier exhaustion | N/A | Monitor usage; consider paid tier for agent workloads |
| Tier detection bug | #21399 | probe_gemini_tier() may report "paid" for free keys; verify manually |

---

## Open Questions

1. Is the current Gemini API key on the free tier or paid tier?
2. Has the free tier been exhausted in previous sessions?
3. Should gemini be promoted in the fallback chain given its free tier availability?
4. Is Gemini used for gateway/messaging platforms?

## Research Notes

- Setup: Google AI Studio → Get API key → Create in Google Cloud project
- Two env var names accepted: `GOOGLE_API_KEY` and `GEMINI_API_KEY`
- Hermes probes key tier during setup — free tier warning shown
- TTS: gemini-2.5-flash-preview-tts available
- Config: `hermes config set model.provider gemini` + `hermes config set model.api_key KEY`
- `hermes doctor` checks both env var names
- Google bans accounts for third-party app usage via OAuth — API key method is safer
- Gemini via OpenRouter (Option 3): routes through OpenRouter, no separate Google billing
