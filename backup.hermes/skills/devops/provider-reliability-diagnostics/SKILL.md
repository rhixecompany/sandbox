---
name: provider-reliability-diagnostics
title: Provider Reliability Diagnostics — Chain Tracing, ACPX Validation, Auxiliary Fallback
description: "Diagnose and fix provider chain failures in Hermes: trace failures across main → fallback → auxiliary → aggregator layers, validate provider health via ACPX exec, fix MCP transport mismatches, and configure auxiliary fallbacks."
author: Hermes Agent
version: 1.0.0
tags: [hermes, diagnostics, providers, reliability, mcp, fallback]
trigger: |
  • User says "provider not working", "API failing", "model not responding"
  • errors.log shows repeated provider failure patterns (ConnectionError, 402, 429, 401)
  • Multiple provider retries visible in logs
  • Vision/compression/title gen silently failing
  • MCP server connection failures at startup
  • User asks "why did my session fail?"
---

# Provider Reliability Diagnostics

## When to Use

- Provider connection failures in errors.log
- Fallback chain not activating as expected
- Auxiliary features (vision, compression, title gen) silently failing
- MCP server "Connection closed" at gateway startup
- Session abort mid-conversation with provider error
- After model/provider config changes

## Verification Checklist

- [ ] Provider chain fully mapped (main → fallback → auxiliary)
- [ ] Each provider in chain passes health check
- [ ] Auxiliary providers configured explicitly (not `auto` when OpenRouter has no credits)
- [ ] MCP servers with transport mismatch disabled or fixed
- [ ] Gateway restart picks up all changes

## The Provider Chain

Hermes attempts providers in this exact order when processing a request:

```
1. Main provider  ─── model.provider + model.default
   ↓ (fails: ConnectionError, 402, 429, timeout)
2. Fallback providers ─── fallback_providers[] (in order)
   ↓ (all fail)
3. Auxiliary aggregator ─── auxiliary.*.provider
   ↓ (fails: 402, auth error, or not configured)
4. Silent failure ─── session aborts or feature degrades
```

Each layer leaves distinct signatures in errors.log.

## Phase 1: Quick Health Sweep

Run all three ACPX provider checks in parallel:

```bash
acpx copilot exec "Reply with exactly: COPILOT_ALIVE"
acpx qwen exec "Reply with exactly: QWEN_ALIVE"
opencode run "Reply with exactly: OPENCODE_ALIVE" --model opencode/big-pickle 2>&1 | tail -3
```

**Healthy response:** Each returns the exact string.
**Failure patterns:**
- Copilot: "Authentication required" → re-auth GitHub token
- Qwen: "401" or timeout → check OpenRouter API key + credits
- OpenCode: cost-guard banner then valid response → cosmetic only

## Phase 2: Log Trace — Identify the Broken Link

```bash
# 1. Pull WARNING/ERROR lines mentioning providers
grep -E "WARNING|ERROR" /c/Users/Alexa/AppData/Local/hermes/logs/errors.log \
  | grep -i "provider\|api_call\|retry\|credits\|auth" | tail -40

# 2. Classify the failure layer
```

### Failure Signature Reference

| Log Line | Layer | Problem |
|----------|-------|---------|
| `API call failed ... provider=<main> ... Connection error` | **Main** | Primary API unreachable (network, endpoint down, etc.) |
| `Retrying API call ... (attempt 1/3)` | **Main retry** | Auto-retry running — wait for all 3 attempts |
| `API call failed after 3 retries. Connection error. \| msgs=80 tokens=~66,270` | **Main exhausted** | All retries failed. Fallback should activate. |
| `API call failed ... provider=copilot-acp ... Authentication required` | **Fallback** | Fallback also failing (auth issue) |
| `Non-retryable client error: Copilot ACP session/new failed` | **Fallback dead** | Fallback unrecoverable. Chain moves to auxiliary. |
| `Title generation failed: Error code: 402 - Insufficient credits` | **Auxiliary** | OpenRouter credits exhausted. Features silently degrade. |
| `Failed to generate context summary: Error code: 402` | **Auxiliary compression** | Summary generation dead. Session may hit context limit. |
| `Vision auto-detect: skipping main provider ... aggregator chain` | **Auxiliary vision** | Main provider has no vision. Falls through to aggregator (often OpenRouter). |
| `Stream drop ... incomplete chunked read` | **Main unstable** | Partial response received but connection closed mid-stream. Provider load issue. |
| `MCP server '<name>' failed initial connection after 3 attempts` | **MCP startup** | MCP server transport or startup failure. |

## Phase 3: Apply Fix at the Broken Link

### Fix Main Provider Instability
If opencode-zen is flaky (intermittent connection errors, chunked read drops):
```bash
# Check if issue persists
curl -s -o /dev/null -w "%{http_code}" https://opencode.ai/zen/v1/models
# If endpoint is down, fallback should auto-activate.
# The fallback chain is configured in config.yaml:
#   fallback_providers:
#   - provider: copilot-acp
#     model: claude-sonnet-4.6
```
No fix needed on your side — the provider endpoint was temporarily unstable (Cloudflare-routed). Fallback handles it.

### Fix Fallback Auth Failure
If copilot-acp says "Authentication required":
```bash
# Re-authenticate
gh auth status
copilot --version
```
Usually a transient GH token issue. Re-auth resolves it.

### Fix Auxiliary 402 (OpenRouter Credits)
If auxiliary features fail with HTTP 402:
```bash
# 1. Check OpenRouter credit status
# Visit: https://openrouter.ai/settings/credits

# 2. Immediate workaround — set auxiliary to working provider
hermes config set auxiliary.vision.provider copilot-acp
hermes config set auxiliary.vision.model claude-sonnet-4.6
hermes config set auxiliary.compression.provider copilot-acp
hermes config set auxiliary.compression.model claude-sonnet-4.6
hermes config set auxiliary.title_generation.provider copilot-acp
hermes config set auxiliary.title_generation.model claude-sonnet-4.6
```

### Fix MCP Transport Mismatch
If an MCP server uses a Docker/HTTP gateway command but Hermes connects via stdio:
```bash
# 1. Verify the MCP command type
# If it starts a long-running HTTP server, it's not stdio-compatible

# 2. Disable the misconfigured server
hermes config set mcp_servers.<name>.enabled false

# 3. Verify it's gone from startup
hermes mcp list 2>&1 | grep <name> || echo "✓ Removed from active MCP servers"
```

## Phase 4: Verify Fix

```bash
# 1. Confirm config changes
grep -A2 "auxiliary" /c/Users/Alexa/AppData/Local/hermes/config.yaml

# 2. Re-run provider health check
acpx copilot exec "Reply with exactly: COPILOT_ALIVE"

# 3. Confirm MCP servers load cleanly (no Docker warnings)
tail -20 /c/Users/Alexa/AppData/Local/hermes/logs/gateway.log | grep "MCP"

# 4. Restart gateway to pick up all changes
hermes gateway run --replace
```

## Pitfalls

### α Provider works in VS Code but fails in Hermes
Hermes gateway loads credentials from `.env` + `config.yaml`. VS Code extensions use their own credential store. The two are independent — a provider working in VS Code does not mean it's configured for Hermes.

### α Error chain is deep — don't fix the wrong layer
When you see "system failure: all providers exhausted" in a session, the actual root cause is often just one broken link. Trace back through the chain: was it the main provider? The fallback? The auxiliary? Fix that one link.

### α "auto" auxiliary provider is not magic
`auxiliary.*.provider: auto` does NOT auto-detect a working provider. It tries the main provider first, then falls through to the OpenRouter aggregator pool. If OpenRouter has zero credits, everything after the main provider is dead.

### α MCP "Connection closed" does not mean Docker is down
`docker mcp gateway run` starts an HTTP/SSE server. Hermes connects via stdio MCP protocol. The "connection closed" is a transport mismatch, not a Docker failure. Docker Desktop may be running fine.

## Best Practices

1. Run provider health check weekly or after any config change
2. Set auxiliary providers explicitly if OpenRouter credits are limited
3. Keep fallback_providers configured even if main provider is stable — outages happen
4. After diagnosing a chain failure, add a reference file documenting the specific provider issue for faster triage next time
5. Restart gateway after any config change: `hermes gateway run --replace`

## Related Skills

- `hermes-agent-diagnostics-configuration` — General Hermes health checks and config verification
- `log-analysis-and-triage` — General log file triage methodology
- `acpx-agent-routing` — ACPX agent selection by task type

## Reference Files

- `references/provider-chain-diagnostics.md` — Session-specific diagnostic details, error transcripts, and reproduction recipes
