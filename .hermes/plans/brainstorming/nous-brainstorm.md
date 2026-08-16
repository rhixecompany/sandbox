# Nous Portal Provider Workflow — Brainstorming

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

## What "Repeat the OpenRouter Workflow" Means for Nous

Adapting the 8-step template to Nous Portal:

1. **Credential verification** — Verify OAuth token via `hermes auth list nous`
2. **Model selection** — `hermes model` → Nous Portal → pick from 300+ models (currently: upstage/solar-pro4:free)
3. **Config.yaml validation** — Verify model.base_url, model.provider
4. **Fallback chain position** — Not in fallback chain; serves as the model foundation (base_url)
5. **MCP compatibility** — Test MCP servers with nous backing model
6. **Rate limit / quota management** — Document portal rate limits and usage
7. **Model catalog access** — Verify model_catalog.json accessibility
8. **Verification** — `hermes doctor`, test chat

---

## Key Insight

Nous Portal is the **current active provider** for the default profile (upstage/solar-pro4:free). This is interesting because:
- The config.yaml shows opencode-zen as the primary provider with deepseek-v4-flash-free
- But `hermes model` shows Nous Portal / solar-pro4 as active
- This suggests the running session has overridden the config, or the config hasn't been applied

Nous Portal serves as the **base_url foundation** — the model section references `https://inference-api.nousresearch.com/v1` as the inference endpoint.

---

## SCAMPER Analysis

### Substitute
- Nous Portal vs OpenRouter — both aggregate multiple models, different backing infrastructure
- solar-pro4:free vs deepseek-v4-flash-free — different models on different providers

### Combine
- Nous Portal OAuth + opencode-zen API key = multi-provider primary setup
- Model catalog (300+ models) + bundled tool use = comprehensive capability

### Adapt
- Adapt 8-step template — Nous-specific: OAuth auth, portal URL, model catalog URL

### Modify
- Current active model is solar-pro4:free via Nous Portal — different from config.yaml's opencode-zen/deepseek-v4-flash-free
- This discrepancy needs investigation

### Eliminate
- Eliminate if OAuth token is expired or portal access is unavailable

### Reverse
- Nous Portal as primary (already the case for default profile) — opencode-zen is the config default but not the active session model

---

## Key Questions

1. Why does `hermes model` show Nous Portal as active instead of opencode-zen?
2. Is the OAuth token still valid?
3. What models are available via the portal right now?
4. Should Nous Portal be in the fallback chain?

---

## Implementation Artifacts Needed

- `.hermes/plans/specs/nous-workflow-spec.md`
- `.hermes/plans/nous-workflow.md` (implementation plan)
- `.hermes/plans/results/nous-*.txt` (execution results)
