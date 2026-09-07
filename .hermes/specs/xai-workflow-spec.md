---
name: xai-workflow
title: xAI (Grok) Provider Workflow Specification
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

xAI provider workflow specification covering two auth paths (API key and OAuth), model selection, direct-to-xAI tools verification, provider aliases, MCP compatibility, and rate limiting.

## Requirements

### Credential Verification
- [ ] Confirm `XAI_API_KEY` is set in `.env` (direct API path) OR verify SuperGrok OAuth
- [ ] Run `hermes auth list xai` / `hermes auth list xai-oauth` to verify credential
- [ ] Run `hermes doctor` to validate connectivity
- [ ] Determine which auth path is active: API key or OAuth

### Model Selection & Validation
- [ ] Run `hermes model` → select xai/xai-oauth → list available models
- [ ] Confirm grok-4.3 (1M context) or grok-4.6 is selectable
- [ ] Check grok-4.3-fast (cheaper, same large context)
- [ ] Verify context window meets 64K minimum

### Config.yaml Review
- [ ] Verify `model.provider: xai` or `xai-oauth` is correct
- [ ] Verify `model.default_model` is set appropriately
- [ ] Check `fill_first` strategy in credential pool
- [ ] Note: xai is NOT in the main `fallback_providers` chain

### Direct-to-xAI Tools Verification
- [ ] Check TTS configuration: voxtral-mini-tts-2603
- [ ] Verify image gen, video gen, transcription tools availability
- [ ] Check X search tool availability
- [ ] Document which tools are auto-enabled by OAuth token

### Provider Aliases
- [ ] Document provider aliases: `xai-oauth`, `grok-oauth`, `x-ai-oauth`, `xai-grok-oauth`
- [ ] Verify alias resolution works correctly

### MCP Server Compatibility
- [ ] Test MCP servers with xai backing model (sample at least 1)

### Two Auth Paths
- [ ] Document API Key Path (provider: `xai`)
- [ ] Document OAuth Path (provider: `xai-oauth`)
- [ ] Same OAuth token auto-reused by TTS, image gen, video gen, transcription, X search

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Doctor reports | `hermes doctor` | Reports xai or xai-oauth connectivity |
| Auth verified | `hermes auth list xai` or `hermes auth list xai-oauth` | Credential valid |
| Model confirmed | `hermes model` → xai | At least 1 Grok model confirmed |
| Context verified | Check model details | ≥ 64K for selected models |
| Aliases documented | Review spec | xai-oauth, grok-oauth, x-ai-oauth, xai-grok-oauth listed |
| Direct tools verified | Review spec | TTS, image gen, video gen, transcription, X search documented |
| MCP tested | `hermes mcp test <server>` | At least 1 MCP server tested |

## Non-Functional Requirements

Two auth paths available: API key (XAI_API_KEY) and OAuth (SuperGrok/X Premium+). OAuth token auto-reused by TTS, image gen, video gen, transcription, X search. Provider aliases: xai-oauth, grok-oauth, x-ai-oauth, xai-grok-oauth. grok-4.3 has 1M token context.

## Verification

```bash
# 1. Verify credential (try both paths)
hermes auth list xai
hermes auth list xai-oauth
hermes doctor

# 2. Check env var
echo $XAI_API_KEY

# 3. Verify model selection
hermes model

# 4. Check config
grep -n "provider.*xai\|default_model.*grok" ~/AppData/Local/hermes/config.yaml

# 5. Verify provider aliases
# Document: xai-oauth, grok-oauth, x-ai-oauth, xai-grok-oauth

# 6. Test direct tools
# TTS: voxtral-mini-tts-2603
# Image gen, video gen, transcription, X search

# 7. Test MCP compatibility
hermes mcp test <at_least_1_server>
```

## Linked Specs
- xai-workflow-spec.md

## Linked Plan
- ../provider-workflow-master-plan.md

