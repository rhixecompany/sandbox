---
name: openrouter-workflow
title: OpenRouter Provider Workflow Specification
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

OpenRouter provider workflow specification covering credential verification, model selection, provider routing configuration, fallback chain verification, auxiliary model offload, MCP compatibility, and rate limiting.

## Requirements

### Credential Verification
- [ ] Confirm `OPENROUTER_API_KEY` is set in `.env`
- [ ] Run `hermes auth list openrouter` to verify credential
- [ ] Run `hermes doctor` to validate connectivity
- [ ] Test with a simple chat query

### Model Selection & Validation
- [ ] Run `hermes model` → select openrouter → list available models
- [ ] Verify nvidia/nemotron-3-ultra-550b-a55b:free is available
- [ ] Check alternative free models: nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free, nvidia/nemotron-3-super-120b-a12b:free
- [ ] Document model tier (free vs paid) and rate limits

### Provider Routing Configuration
- [ ] Review `provider_routing` section in config.yaml for openrouter
- [ ] Check `sort`, `only`, `ignore`, `order`, `require_parameters`, `data_collection` settings
- [ ] Test routing behavior with a model-specific query

### Fallback Chain Verification
- [ ] Confirm openrouter is 2nd in `fallback_providers` chain
- [ ] Test fallback trigger: simulate opencode-zen failure, verify openrouter takes over
- [ ] Document mid-session model swap behavior

### Auxiliary Model Offload
- [ ] Check if openrouter is configured for auxiliary tasks (vision, web extraction)
- [ ] Recommendation: use cheapest trusted model for side tasks
- [ ] Document cost optimization strategies

### MCP Server Compatibility
- [ ] Test all 21 MCP servers with openrouter as the backing model (sample at least 3)
- [ ] Document any provider-specific MCP quirks
- [ ] Pay special attention to MCP servers using npx (node CLI) — Windows quirks

### Rate Limit & Quota Management
- [ ] Document free tier rate limits for key models
- [ ] Identify credential pooling strategy (single key — no backup)
- [ ] Document retry behavior on 429 responses
- [ ] Add backup OPENROUTER_API_KEY to credential pool

### Reference Models
- [ ] Review `reference_models` config
- [ ] Verify these are used for cost/quality comparison

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Doctor reports | `hermes doctor` | Reports openrouter connectivity |
| Chat test | Simple query | Succeeds |
| Model available | `hermes model` → openrouter | nvidia/nemotron-3-ultra-550b-a55b:free confirmed |
| Config correct | grep config.yaml | provider: openrouter, routing settings verified |
| Fallback 2nd | Check config | openrouter is 2nd in fallback_providers |
| MCP tested | `hermes mcp test <server>` | At least 3 MCP servers tested |
| Reference models | Check config | reference_models section reviewed |

## Non-Functional Requirements

Credential pool uses fill_first strategy with single OPENROUTER_API_KEY key. Response cache enabled: 300s TTL. min_coding_score: 0.65. Fallback providers swap model mid-session without losing conversation. Auxiliary model offload available for cost optimization.

## Verification

```bash
# 1. Verify credential
hermes auth list openrouter
hermes doctor

# 2. Check env var
echo $OPENROUTER_API_KEY

# 3. Verify model selection
hermes model

# 4. Check provider routing config
grep -A 10 "provider_routing" ~/AppData/Local/hermes/config.yaml

# 5. Verify fallback chain position (should be 2nd)
grep -A 5 "fallback_providers" ~/AppData/Local/hermes/config.yaml

# 6. Test MCP compatibility
hermes mcp test <at_least_3_servers>

# 7. Check reference models
grep -A 5 "reference_models" ~/AppData/Local/hermes/config.yaml

# 8. Verify response cache
grep -n "cache\|TTL\|300" ~/AppData/Local/hermes/config.yaml
```

## Linked Specs
- openrouter-workflow-spec.md

## Linked Plan
- ../provider-workflow-master-plan.md

