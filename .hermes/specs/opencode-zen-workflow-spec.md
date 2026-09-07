---
name: opencode-zen-workflow
title: OpenCode-Zen Provider Workflow Specification
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

OpenCode-Zen provider workflow specification covering credential verification, model selection, config review, MCP compatibility, and rate limit management.

## Requirements

### Credential Verification
- [ ] Confirm `OPENCODE_ZEN_API_KEY` is set in `.env` (vault primary)
- [ ] Confirm backup key exists in opencode auth.json
- [ ] Run `hermes auth list opencode-zen` to verify 2 credentials
- [ ] Run `hermes doctor` to validate connectivity

### Model Selection & Validation
- [ ] Run `hermes model` → verify opencode-zen provider shows available models
- [ ] Confirm deepseek-v4-flash-free is selectable and responsive
- [ ] Test fallback chain: if primary fails, does it fall back to openrouter → gemini → ollama-cloud?

### Config.yaml Review
- [ ] Verify `model.base_url: https://opencode.ai/zen/v1` is correct
- [ ] Verify `model.provider: opencode-zen` is set
- [ ] Verify `fallback_providers` chain includes opencode-zen first
- [ ] Check credential_pool_strategies: fill_first for opencode-zen

### MCP Server Compatibility
- [ ] Test sequential-thinking MCP with opencode-zen model
- [ ] Test github MCP with opencode-zen model
- [ ] Test filesystem MCP with opencode-zen model
- [ ] Document any provider-specific MCP quirks

### Rate Limit / Quota Management
- [ ] Document known rate limits for deepseek-v4-flash-free
- [ ] Document credential rotation behavior (2 keys in pool)
- [ ] Identify any failures from previous sessions due to rate limits

### Auxiliary Model Offload
- [ ] Check if opencode-zen is used for auxiliary tasks (vision, compression, session_search)
- [ ] If not, evaluate whether it should be (cost/quality tradeoffs)

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Credentials listed | `hermes auth list opencode-zen` | 2 credentials shown |
| Doctor reports | `hermes doctor` | Reports opencode-zen connectivity |
| Model selectable | `hermes model` → opencode-zen | deepseek-v4-flash-free confirmed |
| Config correct | grep config.yaml | base_url, provider, fallback chain verified |
| MCP tested | `hermes mcp test <server>` | At least 2 MCP servers tested |
| Fallback chain | Verify config | openrouter → gemini → ollama-cloud |
| Credential pool | Check config | fill_first strategy with 2 keys |

## Non-Functional Requirements

Credential pool has 2 keys with fill_first strategy. OpenCode Zen is primary provider — all 13 profiles default to it. Model deepseek-v4-flash-free is the active model across all profiles. Base URL: https://opencode.ai/zen/v1.

## Verification

```bash
# 1. Verify credentials
hermes auth list opencode-zen
hermes doctor

# 2. Check env var and backup
echo $OPENCODE_ZEN_API_KEY
ls ~/.config/opencode/auth.json 2>/dev/null && cat ~/.config/opencode/auth.json | grep -c "zen"

# 3. Verify model selection
hermes model

# 4. Check config thoroughly
grep -n "base_url.*zen\|provider.*zen\|fallback_providers" ~/AppData/Local/hermes/config.yaml

# 5. Test MCP compatibility
hermes mcp test sequential-thinking
hermes mcp test github
hermes mcp test filesystem

# 6. Verify fallback chain
# openrouter → gemini → ollama-cloud should be documented
```

## Linked Specs
- opencode-zen-workflow-spec.md

## Linked Plan
- ../provider-workflow-master-plan.md

