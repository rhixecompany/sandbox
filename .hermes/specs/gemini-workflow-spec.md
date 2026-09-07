---
name: gemini-workflow
title: Gemini Provider Workflow Specification
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Gemini provider workflow specification covering credential verification, model selection, config review, free tier quota awareness, MCP compatibility, and gateway compatibility.

## Requirements

### Credential Verification
- [ ] Confirm `GOOGLE_API_KEY` or `GEMINI_API_KEY` is set in `.env`
- [ ] Run `hermes auth list gemini` to verify credential
- [ ] Run `hermes doctor` to validate connectivity
- [ ] **Workaround for known bug:** If doctor reports "invalid API key", verify actual chat works (GitHub #26623)

### Model Selection & Validation
- [ ] Run `hermes model` → select gemini → list available models
- [ ] Confirm gemini-2.5-flash is selectable
- [ ] Check available models: gemini-2.5-flash, gemini-2.5-pro, gemma models
- [ ] Verify context window meets 64K minimum requirement

### Config.yaml Review
- [ ] Verify `model.provider: gemini` is correct
- [ ] Verify `model.default_model: gemini-2.5-flash` is set
- [ ] Check that gemini is 3rd in `fallback_providers` chain

### Free Tier Quota Awareness
- [ ] Document free tier quota limitations
- [ ] Estimate per-session quota consumption (tool calls, retries, compression, auxiliary tasks)
- [ ] Check for quota exhaustion in recent sessions
- [ ] Evaluate paid tier upgrade if free tier insufficient

### MCP Server Compatibility
- [ ] Test MCP servers with gemini backing model (sample at least 2)
- [ ] Document any Gemini-specific MCP quirks
- [ ] Test structured tool calls (function calling)

### Gateway Compatibility
- [ ] Gemini works with all Hermes gateway platforms (Telegram, Discord, Slack, etc.)
- [ ] Verify gateway config if gateway is used

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Doctor reports | `hermes doctor` | Reports gemini connectivity |
| Chat test | Test query | Succeeds even if doctor shows false positive |
| Model confirmed | `hermes model` → gemini | gemini-2.5-flash confirmed available |
| Context window | `hermes model` | ≥ 64K confirmed |
| Config correct | grep config.yaml | provider: gemini, default_model set |
| MCP tested | `hermes mcp test <server>` | At least 2 MCP servers tested |
| Gateway verified | Check config | Gateway platforms documented |

## Non-Functional Requirements

Credential verification within 10 seconds. Model list loads within 5 seconds. Free tier quota monitoring is ongoing. Context window ≥ 64K for all models. Doctor false positive bug #26623 documented.

## Verification

```bash
# 1. Verify credential
hermes auth list gemini
hermes doctor

# 2. If doctor shows false positive, test actual chat
# Run a simple test query to verify gemini works

# 3. Verify model selection
hermes model

# 4. Check config
grep -n "provider.*gemini\|default_model.*gemini" ~/AppData/Local/hermes/config.yaml

# 5. Test MCP servers
hermes mcp test <at_least_2_servers>

# 6. Verify known issues
# GitHub #26623: hermes doctor false positive
# GitHub #21399: tier detection bug
```

## Linked Specs
- gemini-workflow-spec.md

## Linked Plan
- ../provider-workflow-master-plan.md

