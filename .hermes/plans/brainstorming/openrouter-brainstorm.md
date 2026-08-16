# OpenRouter Provider Workflow — Brainstorming

**Date:** 2026-08-16  
**Provider:** openrouter  
**Status:** draft  

---

## Provider Overview

| Property | Value |
|----------|-------|
| Config key | `openrouter` |
| Default model | nvidia/nemotron-3-ultra-550b-a55b:free |
| Auth type | API key |
| Env var | `OPENROUTER_API_KEY` |
| Base URL | `https://openrouter.ai/api/v1` |
| Models available | 400+ across 70+ providers |
| Credential pool | 1 key (OPENROUTER_API_KEY, env var) |
| Pool strategy | fill_first |
| Role | Primary fallback (2nd in chain after opencode-zen) |
| Response cache | true, TTL: 300s |
| min_coding_score | 0.65 |

---

## What "Repeat the OpenRouter Workflow" Means

OpenRouter IS the template workflow. This is the reference implementation that all other providers should follow. The 8-step OpenRouter workflow:

1. **Credential setup** — OPENROUTER_API_KEY in .env, validated via `hermes auth` / `hermes doctor`
2. **Model selection** — `hermes model` → choose OpenRouter → pick model from 400+ options
3. **Provider routing config** — provider_routing in config.yaml (sort, only, ignore, order, require_parameters, data_collection)
4. **Fallback chain** — 2nd in fallback_providers list
5. **Auxiliary model offload** — cheap models for vision/web extraction (e.g., Gemini Flash on OpenRouter)
6. **MCP server compatibility** — all 21 MCP servers should work
7. **Rate limit / quota management** — single key (no pool backup), response caching (300s TTL)
8. **Verification** — `hermes doctor`, test chat, tool-calling validation

---

## SCAMPER Analysis

### Substitute
- OpenRouter IS the template — other providers adapt this workflow
- Can substitute underlying providers via routing (Anthropic, Google, AWS Bedrock, Together AI)

### Combine
- Response caching (300s TTL) + credential pooling = reduced API calls
- Provider routing + fallback chains = maximum reliability

### Adapt
- This IS the master template — all other 7 providers adapt this 8-step workflow

### Modify
- Only 1 API key in pool (no backup) — consider adding a second key
- No explicit provider_routing config — uses defaults

### Eliminate
- Eliminate rate limit risks by adding credential pool backup

### Reverse
- OpenRouter is 2nd in fallback — should it be 1st for some workloads?

---

## Provider Routing Details

From Hermes docs, OpenRouter provider routing supports:

| Control | Description |
|---------|-------------|
| `sort` | Throughput/price sorting (`:nitro`, `:floor` suffixes) |
| `only` | Restrict to specific underlying providers |
| `ignore` | Exclude specific underlying providers |
| `order` | Priority order for provider selection |
| `require_parameters` | Require specific params |
| `data_collection` | Data sharing preferences |

---

## Key Questions

1. What is the current OPENROUTER_API_KEY tier (free vs paid)?
2. Have there been 429 rate limit incidents?
3. Which underlying OpenRouter providers are routing requests?
4. Should a backup API key be added to the credential pool?

---

## Implementation Artifacts Needed

- `.hermes/plans/specs/openrouter-workflow-spec.md`
- `.hermes/plans/openrouter-workflow.md` (implementation plan)
- `.hermes/plans/results/openrouter-*.txt` (execution results)
