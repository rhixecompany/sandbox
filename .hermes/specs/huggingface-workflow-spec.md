---
name: huggingface-workflow
title: HuggingFace Provider Workflow Specification
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

HuggingFace provider workflow specification covering credential verification, model selection, config review, backend routing analysis, MCP compatibility, and rate limit management.

## Requirements

### Credential Verification
- [ ] Confirm `HF_TOKEN` is set in `.env` (must have "Make calls to Inference Providers" permission)
- [ ] Check if `HF_INFERENCE_TOKEN` is set separately (optional)
- [ ] Run `hermes auth list huggingface` to verify credential
- [ ] Run `hermes doctor` to validate connectivity

### Model Selection & Validation
- [ ] Run `hermes model` → select huggingface → list available models
- [ ] Confirm Qwen/Qwen3.5-397B-A17B is selectable
- [ ] Check other models: deepseek-ai/DeepSeek-V3.2, Llama, Mistral, and 100s more
- [ ] Test routing suffixes: `:fastest`, `:cheapest`, `:provider_name`
- [ ] Verify context window ≥ 64K for selected models

### Config.yaml Review
- [ ] Verify `model.provider: huggingface` is correct
- [ ] Verify `model.default_model: Qwen/Qwen3.5-397B-A17B` is set
- [ ] Check `fill_first` strategy in credential pool
- [ ] Note: huggingface is NOT in the main `fallback_providers` chain

### Backend Routing Analysis
- [ ] Document backend providers: Groq, Together, SambaNova, and more
- [ ] Explain automatic failover behavior
- [ ] Document routing suffix behavior (`:fastest`, `:cheapest`, `:provider_name`)

### MCP Server Compatibility
- [ ] Test MCP servers with huggingface backing model (sample at least 1)
- [ ] Document any provider-specific quirks

### Rate Limit & Quota Management
- [ ] Document free tier: $0.10/month credit, no markup
- [ ] Document rate limits for Inference Providers
- [ ] Identify cold start / latency behavior

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Doctor reports | `hermes doctor` | Reports huggingface connectivity |
| Token verified | `hermes auth list huggingface` | Credential valid |
| Models accessible | `hermes model` → huggingface | At least 2 models confirmed |
| Routing suffixes | Test `:fastest`, `:cheapest`, `:provider_name` | All suffixes functional |
| Config correct | grep config.yaml | provider: huggingface, default_model set |
| MCP tested | `hermes mcp test <server>` | At least 1 MCP server tested |
| Free tier documented | Review spec | $0.10/month credit stated |

## Non-Functional Requirements

Credential verification within 10 seconds. Model list loads within 5 seconds. Routing suffixes (fastest/cheapest/provider_name) all functional. Free tier: $0.10/month credit, no markup on provider rates. Context window ≥ 64K.

## Verification

```bash
# 1. Verify credential
hermes auth list huggingface
hermes doctor

# 2. Check env vars
echo "HF_TOKEN=${HF_TOKEN:+set}"
echo "HF_INFERENCE_TOKEN=${HF_INFERENCE_TOKEN:+set}"

# 3. Verify model selection and routing
hermes model

# 4. Check config
grep -n "provider.*huggingface\|default_model.*Qwen" ~/AppData/Local/hermes/config.yaml

# 5. Test MCP compatibility
hermes mcp test <at_least_1_server>

# 6. Verify routing suffixes work
# Test with model:model:fastest, model:model:cheapest, model:model:provider_name
```

## Linked Specs
- huggingface-workflow-spec.md

## Linked Plan
- ../provider-workflow-master-plan.md

