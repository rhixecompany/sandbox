---
name: ollama-cloud-workflow
title: Ollama-Cloud Provider Workflow Specification
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Ollama-Cloud provider workflow specification covering credential verification, model selection with dynamic discovery, config review, fallback behavior, MCP compatibility, and rate limiting.

## Requirements

### Credential Verification
- [ ] Confirm `OLLAMA_API_KEY` is set in `.env`
- [ ] Run `hermes auth list ollama-cloud` to verify credential
- [ ] Run `hermes doctor` to validate connectivity
- [ ] Test with a simple chat query

### Model Selection & Validation
- [ ] Run `hermes model` → select ollama-cloud → list dynamically discovered models
- [ ] Confirm nemotron-3-ultra is selectable
- [ ] Check other available models: gpt-oss:120b, glm-4.6:cloud, glm-5.1, qwen3-coder:480b-cloud, mistral-large, minimax-n2.7
- [ ] Verify context window ≥ 64K for all selected models (CRITICAL for Hermes)

### Config.yaml Review
- [ ] Verify `model.provider: ollama-cloud` is correct
- [ ] Verify `model.default_model: nemotron-3-ultra` is set
- [ ] Check that ollama-cloud is last in `fallback_providers` chain

### Fallback Behavior
- [ ] Confirm ollama-cloud is last resort in fallback chain
- [ ] Document scenarios where this would be triggered
- [ ] Evaluate if ollama-cloud should be promoted (free models available)

### MCP Server Compatibility
- [ ] Test MCP servers with ollama-cloud backing model (sample at least 1)

### Rate Limit & Quota Management
- [ ] Document rate limits for nemotron-3-ultra on Ollama Cloud
- [ ] Identify pricing model (free tier vs paid)
- [ ] Document model availability guarantees

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Doctor reports | `hermes doctor` | Reports ollama-cloud connectivity |
| Chat test | Simple query | Succeeds |
| Models discovered | `hermes model` → ollama-cloud | Dynamic catalog fetched |
| Context verified | Check model details | ≥ 64K for selected models |
| Config correct | grep config.yaml | provider: ollama-cloud, default_model set |
| Fallback last | Check config | ollama-cloud is last in chain |
| MCP tested | `hermes mcp test <server>` | At least 1 MCP server tested |
| Pricing documented | Review spec | Free tier vs paid stated |

## Non-Functional Requirements

Model catalog fetched dynamically from ollama.com/v1/models with 1-hour cache. Context window ≥ 64K for all models. Credential pool uses fill_first strategy with single API key. Dynamic model discovery is a key feature.

## Verification

```bash
# 1. Verify credential
hermes auth list ollama-cloud
hermes doctor

# 2. Check env var
echo $OLLAMA_API_KEY

# 3. Verify model selection and dynamic discovery
hermes model

# 4. Check config
grep -n "provider.*ollama-cloud\|default_model.*nemotron" ~/AppData/Local/hermes/config.yaml

# 5. Test MCP compatibility
hermes mcp test <at_least_1_server>

# 6. Verify fallback position
# ollama-cloud should be last in fallback_providers chain
```

## Linked Specs
- ollama-cloud-workflow-spec.md

## Linked Plan
- ../provider-workflow-master-plan.md

