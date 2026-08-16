# OpenCode-Zen Provider Workflow — Brainstorming

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

## What "Repeat the OpenRouter Workflow" Means for OpenCode-Zen

The OpenRouter workflow template adapted for OpenCode-Zen:

1. **Credential verification** — Confirm OPENCODE_ZEN_API_KEY in .env + backup key in opencode auth.json
2. **Model selection** — `hermes model` → verify opencode-zen provider → pick deepseek-v4-flash-free
3. **Config.yaml validation** — Verify model.base_url, model.provider, credential_pool_strategies
4. **Fallback chain position** — Confirm opencode-zen is 1st in fallback_providers chain
5. **MCP compatibility** — Test MCP servers with opencode-zen backing model
6. **Rate limit management** — Document rate limits for deepseek-v4-flash-free, credential rotation
7. **Auxiliary model offload** — Check if opencode-zen used for auxiliary tasks
8. **Verification** — `hermes doctor`, test chat, tool-calling validation

---

## SCAMPER Analysis

### Substitute
- Can deepseek-v4-flash-free be substituted with another opencode-zen model? → laguna-s-2.1-free, nemotron-3-ultra-free
- Can the credential pool be substituted with a single key? → Yes but loses rotation resilience

### Combine
- Combine opencode-zen credential verification with doctor check
- Combine model selection with MCP testing

### Adapt
- Adapt the OpenRouter 8-step workflow template to opencode-zen's specific auth (API key + manual backup)

### Modify
- The fill_first strategy means both keys tried before fallback — this is different from round_robin

### Eliminate
- Eliminate the interactive `hermes model` picker — use config.yaml directly for non-interactive setup

### Reverse
- Instead of testing model first, test MCP connectivity first (github MCP already confirmed working)

---

## Key Questions

1. Are both API keys in the pool currently valid?
2. Has deepseek-v4-flash-free ever hit a rate limit?
3. Why does `hermes model` show Nous Portal as active instead of opencode-zen?
4. Should the fallback chain be reordered?

---

## Implementation Artifacts Needed

- `.hermes/plans/specs/opencode-zen-workflow-spec.md`
- `.hermes/plans/opencode-zen-workflow.md` (implementation plan)
- `.hermes/plans/results/opencode-zen-*.txt` (execution results)
