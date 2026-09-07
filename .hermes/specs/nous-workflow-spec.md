---
name: nous-workflow
title: Nous Portal Provider Workflow Specification
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Nous Portal provider workflow specification covering credential verification, model selection, config review, portal authentication, model catalog access, MCP compatibility, and rate limiting.

## Requirements

### Credential Verification
- [ ] Run `hermes auth list nous` to verify OAuth token
- [ ] Run `hermes doctor` to validate connectivity
- [ ] Verify portal authentication is active

### Model Selection & Validation
- [ ] Run `hermes model` → verify nous provider shows available models
- [ ] Check models available via Nous Portal (300+ models with bundled tool use)
- [ ] Verify context window ≥ 64K minimum
- [ ] Note: current active model is upstage/solar-pro4:free

### Config.yaml Review
- [ ] Verify `model.base_url: https://inference-api.nousresearch.com/v1` is correct
- [ ] Verify `model.provider: nous` is set
- [ ] Check that nous serves as the model foundation (base_url reference)

### Portal Authentication
- [ ] Verify `hermes auth` OAuth flow is complete
- [ ] Check token expiration / refresh behavior
- [ ] Test portal URL accessibility: `https://portal.nousresearch.com`

### Model Catalog Access
- [ ] Verify model catalog URL accessibility: `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`
- [ ] Document catalog refresh behavior
- [ ] List key model categories available

### MCP Server Compatibility
- [ ] Test MCP servers with nous backing model (sample at least 1)
- [ ] Document any provider-specific quirks

### Rate Limit & Quota Management
- [ ] Document rate limits for Nous Portal
- [ ] Identify any quota or usage restrictions
- [ ] Check model_catalog URL

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| OAuth verified | `hermes auth list nous` | OAuth token valid |
| Doctor reports | `hermes doctor` | Reports nous connectivity |
| Portal accessible | `curl https://portal.nousresearch.com` | HTTP 200 |
| Catalog accessible | `curl https://hermes-agent.nousresearch.com/docs/api/model-catalog.json` | JSON model catalog |
| Model confirmed | `hermes model` → nous | At least 1 model confirmed |
| Config correct | grep config.yaml | base_url and provider set |
| MCP tested | `hermes mcp test <server>` | At least 1 MCP server tested |
| Active model noted | `hermes model` | upstage/solar-pro4:free identified |

## Non-Functional Requirements

OAuth verification within 15 seconds. Portal URL accessible within 5 seconds. Model catalog fetched within 5 seconds. 300+ models available with bundled tool use. Context window ≥ 64K minimum.

## Verification

```bash
# 1. Verify OAuth credential
hermes auth list nous
hermes doctor

# 2. Test portal accessibility
curl -s -o /dev/null -w "%{http_code}" https://portal.nousresearch.com

# 3. Verify model catalog
curl -s https://hermes-agent.nousresearch.com/docs/api/model-catalog.json | head -20

# 4. Check config
grep -n "base_url.*nous\|provider.*nous" ~/AppData/Local/hermes/config.yaml

# 5. Test MCP compatibility
hermes mcp test <at_least_1_server>

# 6. Verify active model
hermes model
# Note: hermes model shows Nous Portal as active, not opencode-zen
```

## Linked Specs
- nous-workflow-spec.md

## Linked Plan
- ../provider-workflow-master-plan.md

