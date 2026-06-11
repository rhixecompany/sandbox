# Provider Chain Debug — Session 2026-05-30

## Reproduction Recipe: Provider Chain Failure

### Scenario
Main provider (opencode-zen) intermittently drops connections. Fallback (copilot-acp) 
has intermittent auth. OpenRouter auxiliary has 0 credits (402). Result: session degrades
silently.

### Symptoms in errors.log (timestamp 21:31-21:53)

```
1. [opencode-zen] API call failed (3/3) → Connection error
2. [copilot-acp] API call failed (1/3) → Authentication required (non-retryable)
3. [auxiliary] Title generation failed → 402 Insufficient credits
4. [auxiliary] Vision auto-detect: skipping opencode-zen → aggregator chain
5. [auxiliary] Failed to generate context summary → 402 Insufficient credits
```

### Root Cause Chain
```
opencode-zen outage (Cloudflare) 
  → copilot-acp also failing (auth) 
    → OpenRouter fallback has 0 credits (402) 
      → ALL auxiliary features silently broken
```

### Applied Fixes

1. **Auxiliary fallback bypass** — Set vision/compression/title_generation to copilot-acp:
   ```
   hermes config set auxiliary.vision.provider copilot-acp
   hermes config set auxiliary.vision.model claude-sonnet-4.6
   hermes config set auxiliary.compression.provider copilot-acp
   hermes config set auxiliary.compression.model claude-sonnet-4.6
   hermes config set auxiliary.title_generation.provider copilot-acp
   hermes config set auxiliary.title_generation.model claude-sonnet-4.6
   ```

2. **MCP Docker disabled** — Transport mismatch (SSE/stdio):
   ```
   hermes config set mcp_servers.mcp-docker.enabled false
   ```

### OpenCode Cost-Guard NDJSON Pollution
When running `opencode run "prompt"`, the output includes a preamble line:
```
[cost-guard] Active — limit: $20.0000 | warn at: 80% | mode: warn
```
This non-JSON line causes NDJSON parse warnings when used via ACPX pipeline.
The actual response follows on the next lines. Workaround: pipe through `tail -n +2`
or just accept the warning — the response is still valid.

### Provider Health Validation Results (post-fix)
| Provider | Command | Result |
|----------|---------|--------|
| Copilot ACP | `acpx copilot exec "Reply with: COPILOT_ALIVE"` | ✅ COPILOT_ALIVE |
| Qwen Code | `acpx qwen exec "Reply with: QWEN_ALIVE"` | ✅ QWEN_ALIVE |
| OpenCode | `opencode run "Reply with: OPENCODE_ALIVE"` | ✅ OPENCODE_ALIVE (with cost-guard banner) |

### Gateway Restart Sequence
```bash
# Graceful restart picks up config changes
hermes gateway run --replace
```
After restart: verify clean MCP startup in gateway.log.
