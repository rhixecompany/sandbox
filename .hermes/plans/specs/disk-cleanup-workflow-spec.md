# Nous Portal Provider Workflow Specification

**Date:** 2026-08-16  
**Provider:** nous  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `nous` |
| Default model | varies (portal-dependent) |
| Auth type | OAuth |
| Auth method | `hermes auth` (Nous Portal) |
| Base URL | `https://inference-api.nousresearch.com/v1` |
| Portal URL | `https://portal.nousresearch.com` |
| Model catalog | 300+ models with bundled tool use |
| Model catalog URL | `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json` |
| Credential pool | OAuth token via hermes auth |
| Pool strategy | Primary base_url |
| Role | Primary provider foundation (base_url for model) |
| Current active model | upstage/solar-pro4:free (via Nous Portal) |

---

## Workflow Steps

### Step 1: Credential Verification

**Actions:**
- [ ] Run `hermes auth list nous` to verify OAuth token
- [ ] Run `hermes doctor` to validate connectivity
- [ ] Verify portal authentication is active

**Expected result:** OAuth token valid, connectivity confirmed

**Acceptance criteria:** `hermes doctor` reports nous connectivity

---

### Step 2: Model Selection & Validation

**Actions:**
- [ ] Run `hermes model` → verify nous provider shows available models
- [ ] Check models available via Nous Portal (300+ models with bundled tool use)
- [ ] Verify context window ≥ 64K minimum
- [ ] Note: current active model is upstage/solar-pro4:free

**Expected result:** Model list accessible, key models verified

**Acceptance criteria:** At least 1 model confirmed available

---

### Step 3: Config.yaml Review

**Actions:**
- [ ] Verify `model.base_url: https://inference-api.nousresearch.com/v1` is correct
- [ ] Verify `model.provider: nous` is set
- [ ] Check that nous serves as the model foundation (base_url reference)

**Expected result:** Config sections correct

**Acceptance criteria:** All config values match expected state

---

### Step 4: Portal Authentication

**Actions:**
- [ ] Verify `hermes auth` OAuth flow is complete
- [ ] Check token expiration / refresh behavior
- [ ] Test portal URL accessibility: `https://portal.nousresearch.com`

**Expected result:** Authentication verified

**Acceptance criteria:** OAuth token active; portal accessible

---

### Step 5: Model Catalog Access

**Actions:**
- [ ] Verify model catalog URL accessibility: `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`
- [ ] Document catalog refresh behavior
- [ ] List key model categories available

**Expected result:** Model catalog verified

**Acceptance criteria:** Catalog URL accessible; model categories documented

---

### Step 6: MCP Server Compatibility

**Actions:**
- [ ] Test MCP servers with nous backing model (sample at least 1)
- [ ] Document any provider-specific quirks

**Expected result:** MCP compatibility verified

**Acceptance criteria:** At least 1 MCP server tested

---

### Step 7: Rate Limit & Quota Management

**Actions:**
- [ ] Document rate limits for Nous Portal
- [ ] Identify any quota or usage restrictions
- [ ] Check model_catalog URL: `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`

**Expected result:** Rate limit documentation complete

**Acceptance criteria:** Limits documented

---

## Key Insight: Active Model Discrepancy

**Config.yaml says:** opencode-zen / deepseek-v4-flash-free (primary provider)

**hermes model shows:** Nous Portal / upstage/solar-pro4:free (active provider)

**Possible explanations:**
1. The running session has overridden the config default
2. The config hasn't been applied to the running session
3. `hermes model` reads session state, not config defaults

**Action needed:** Investigate and reconcile this discrepancy.

---

## Open Questions

1. Is the Nous Portal OAuth token currently valid?
2. Why does `hermes model` show Nous Portal as active instead of opencode-zen?
3. What models are available through the portal right now?
4. Is the portal used as the primary inference backend or only as a base_url reference?

## Research Notes

- Nous Portal uses OAuth authentication via `hermes auth`
- Base URL: `https://inference-api.nousresearch.com/v1`
- Portal URL: `https://portal.nousresearch.com`
- Model catalog: `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`
- Provider in config.yaml — serves as the model foundation
- The `nous` provider plugin is enabled (`model-providers/nous`)
- 300+ models with bundled tool use
- Current active model: upstage/solar-pro4:free
