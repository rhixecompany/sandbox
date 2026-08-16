# OpenCode-Zen Provider Workflow Specification

**Date:** 2026-08-16  
**Provider:** opencode-zen  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `opencode-zen` |
| Default model | laguna-s-2.1-free |
| Active model | deepseek-v4-flash-free |
| Fallback model | nemotron-3-ultra-free |
| Auth type | API key |
| Env var | `OPENCODE_ZEN_API_KEY` |
| Base URL | `https://opencode.ai/zen/v1` |
| Credential pool | 2 keys (vault primary + zen-backup manual) |
| Pool strategy | fill_first |
| Profile usage | default (primary), creative-director, code-architect, exec-assistant, research-analyst, patient-tutor, ops, pm, qa, security, dev, cto, designer, alexa |

---

## Workflow Steps

### Step 1: Credential Verification

**Actions:**
- [ ] Confirm `OPENCODE_ZEN_API_KEY` is set in `.env` (vault primary)
- [ ] Confirm backup key exists in opencode auth.json (`zen-backup`)
- [ ] Run `hermes auth list opencode-zen` to verify 2 credentials
- [ ] Run `hermes doctor` to validate connectivity

**Expected result:** 2 credentials listed, both valid

**Acceptance criteria:** `hermes auth list opencode-zen` shows 2 credentials; doctor reports connectivity

---

### Step 2: Model Selection & Validation

**Actions:**
- [ ] Run `hermes model` → verify opencode-zen provider shows available models
- [ ] Confirm deepseek-v4-flash-free is selectable
- [ ] Test fallback: if primary fails, does it fall back to openrouter → gemini → ollama-cloud?

**Expected result:** deepseek-v4-flash-free selectable and responsive

**Acceptance criteria:** Model responds to test query; fallback chain verified

---

### Step 3: Config.yaml Review

**Actions:**
- [ ] Verify `model.base_url: https://opencode.ai/zen/v1`
- [ ] Verify `model.provider: opencode-zen`
- [ ] Verify `fallback_providers` chain includes opencode-zen first
- [ ] Check credential_pool_strategies: fill_first for opencode-zen

**Expected result:** Config sections correct

**Acceptance criteria:** All config values match expected state

---

### Step 4: MCP Server Compatibility

**Actions:**
- [ ] Test sequential-thinking MCP with opencode-zen model
- [ ] Test github MCP with opencode-zen model
- [ ] Test filesystem MCP with opencode-zen model
- [ ] Document any provider-specific MCP quirks

**Expected result:** MCP servers connect and discover tools

**Acceptance criteria:** At least 2 MCP servers tested successfully

---

### Step 5: Rate Limit / Quota Management

**Actions:**
- [ ] Document known rate limits for deepseek-v4-flash-free
- [ ] Document credential rotation behavior (2 keys in pool, fill_first)
- [ ] Identify any failures from previous sessions due to rate limits

**Expected result:** Rate limit documentation complete

**Acceptance criteria:** Rate limits documented with mitigation strategies

---

### Step 6: Auxiliary Model Offload

**Actions:**
- [ ] Check if opencode-zen is used for auxiliary tasks (vision, compression, session_search)
- [ ] If not, evaluate whether it should be (cost/quality tradeoffs)

**Expected result:** Auxiliary model usage documented

**Acceptance criteria:** Auxiliary model configuration reviewed

---

## Open Questions

1. Are both API keys in the pool currently valid, or has one expired?
2. Has deepseek-v4-flash-free ever hit a rate limit in this environment?
3. Should the fallback chain be reordered given current provider reliability?
4. Why does `hermes model` show Nous Portal as active instead of opencode-zen?

## Research Notes

- OpenCode Zen is the **primary** provider — all 13 profiles default to it
- The model `deepseek-v4-flash-free` is the active model across all profiles
- `OPENCODE_ZEN_BASE_URL: https://opencode.ai/zen/v1` is set in config.yaml
- Credential pool has `fill_first` strategy — both keys tried before fallback
- OpenCode CLI v1.18.13 at `C:\nm4w\nodejs\opencode.cmd`
- Pitfall: `opencode.cmd run` zero exit ≠ work done; verify artifacts after dispatch
- 2 credentials in pool: vault primary (env var) + zen-backup (manual)
