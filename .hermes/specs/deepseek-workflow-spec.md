---
name: deepseek-workflow
title: DeepSeek Provider Workflow Specification
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

DeepSeek provider workflow specification covering credential verification, model selection, config review, fallback chain position, MCP compatibility, and rate limiting.

## Requirements

### Credential Verification
- [ ] Confirm `DEEPSEEK_API_KEY` is set in `.env` (not just config.yaml)
- [ ] Run `hermes auth list deepseek` to verify credential
- [ ] Run `hermes doctor` to validate connectivity
- [ ] Document bug #21725: provider ignores config.yaml api_key, only reads env var

### Model Selection & Validation
- [ ] Run `hermes model` → select deepseek → list available models
- [ ] Confirm deepseek-v4-flash-free is accessed via opencode-zen, NOT directly
- [ ] Check direct deepseek models: deepseek-chat, deepseek-coder, DeepSeek-V3.2
- [ ] Verify context window ≥ 64K for selected models

### Config.yaml Review
- [ ] Verify `model.provider: deepseek` is correct
- [ ] Verify `DEEPSEEK_API_KEY` env var is set (NOT just config.yaml api_key)
- [ ] Check `fill_first` strategy in credential pool

### Fallback Chain Position
- [ ] Document that deepseek is NOT in the main `fallback_providers` chain
- [ ] Explain fill_first role: used when credential pool fires

### MCP Server Compatibility
- [ ] Test MCP servers with deepseek backing model (sample at least 1)

### Rate Limit & Quota Management
- [ ] Document rate limits for DeepSeek API
- [ ] Identify pricing model (free tier vs paid)
- [ ] Document known DeepSeek API reliability patterns

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Doctor reports | `hermes doctor` | Reports deepseek connectivity |
| Env var verified | `echo $DEEPSEEK_API_KEY` | Not empty |
| Model accessible | `hermes model` → deepseek | At least 1 model confirmed |
| Bug #21725 documented | grep config.yaml | api_key field ignored |
| MCP tested | `hermes mcp test <server>` | At least 1 MCP server connected |
| Rate limits documented | Review spec | Limits and pricing stated |

## Non-Functional Requirements

Config validation completes within 10 seconds. DeepSeek API calls respond within 5 seconds p95. Credential pool strategy is fill_first with single API key. No hardcoded credentials in config.yaml.

## Verification

```bash
# 1. Verify credential
hermes auth list deepseek
hermes doctor

# 2. Verify env var (NOT config.yaml api_key)
echo $DEEPSEEK_API_KEY

# 3. Test model selection
hermes model

# 4. Test MCP compatibility
hermes mcp test <at_least_1_server>

# 5. Verify bug #21725
grep -n "api_key" ~/AppData/Local/hermes/config.yaml
# Should show env var is primary, not config.yaml field
```

## Linked Specs
- deepseek-workflow-spec.md

## Linked Plan
- ../provider-workflow-master-plan.md

