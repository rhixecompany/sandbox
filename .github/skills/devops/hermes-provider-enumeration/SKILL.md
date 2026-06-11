---
name: hermes-provider-enumeration
title: "Hermes Provider Enumeration"
description: "Accurately enumerate all configured Hermes providers by cross-referencing config.yaml provider blocks with .env credential keys. Determines which providers are active, which have credentials, and the full fallback chain."
author: Alexa
created: 2026-05-27
tags:
  - hermes
  - configuration
  - diagnostics
  - providers
---

# Hermes Provider Enumeration

## Why This Exists

`hermes auth list` only shows credentials loaded in the provider pool — it does NOT show which provider blocks exist in config.yaml, which have matching `.env` keys, or the active/fallback chain. Complete enumeration requires cross-referencing **4 data sources**.

## The Four-Source Cross-Reference Pattern

### Source 1: Active Provider

The active model is at the top of config.yaml:

```bash
grep -A 3 "^model:" ~/AppData/Local/hermes/config.yaml
```

Expected shape:
```yaml
model:
  default: <model-name>
  provider: <provider-name>
  base_url: <url>
  api_mode: chat_completions
```

### Source 2: Defined Provider Blocks

The `providers:` section defines all registered providers:

```bash
grep -A 2 "^  [a-z]" ~/AppData/Local/hermes/config.yaml | grep -E "^\s+\w+:"
```

### Source 3: .env Credential Keys

Use `grep` to list available credential keys (values remain hidden — `.env` is Hermes-protected from direct reads):

```bash
grep -oP '^[A-Z_]+_KEY[^=]*|^[A-Z_]+_TOKEN[^=]*' ~/AppData/Local/hermes/.env | sort -u
```

Match each key to its provider:
- `OPENROUTER_API_KEY` → openrouter
- `GOOGLE_API_KEY` → google-gemini
- `OPENCODE_ZEN_API_KEY` → opencode-zen
- `COPILOT_GITHUB_TOKEN` → github-copilot
- `GITHUB_TOKEN` → gh CLI / curl (not a provider)
- `TAVILY_API_KEY` → web search (tavily backend), not a chat provider

### Source 4: Fallback Chain

```bash
grep -A 10 "^fallback_providers:" ~/AppData/Local/hermes/config.yaml
```

### Assembly

Combine all four into a single table:

| Provider | Where Defined | Env Key | Key Present | Role |
|----------|-------------|---------|-------------|------|
| opencode-zen | `model.provider:` | OPENCODE_ZEN_API_KEY | ✓/✗ | active primary |
| openrouter | `providers:` | OPENROUTER_API_KEY | ✓/✗ | configured fallback |
| google-gemini | `providers:` | GOOGLE_API_KEY | ✓/✗ | configured fallback |
| github-copilot | `fallback_providers:` | COPILOT_GITHUB_TOKEN | ✓/✗ | inlined fallback |

## Model Probing & Availability Testing

After enumerating which providers are configured, you may need to probe what models are actually reachable and their capabilities (knowledge cutoff, speed, cost tier). Use the Hermes CLI for live testing.

### Pattern: Single-Model Probe

```bash
# Quiet mode (-Q) suppresses banner/tool previews, making output capture easier
hermes chat -q "Reply with ONLY 'CUTOFF: YYYY-MM'. What is your cutoff?" -m "<model-id>" --provider <provider> -Q
```

**Key flags:**
- `-q "<prompt>"` — single query, non-interactive
- `-m <model>` — model ID (must match provider's naming scheme)
- `--provider <provider>` — which provider to route through
- `-Q` — quiet mode (suppresses banner/spinner; response becomes the first non-whitespace line after the reasoning box)

**Output parsing:** In quiet mode, the response appears after the reasoning box (if any). Grep for the response prefix (e.g. `'^CUTOFF:'`) to extract clean output.

### Fallback: Direct API Probe

When Hermes CLI routing fails, probe directly via curl/Python HTTP. This bypasses Hermes' internal routing and reveals more detailed error messages:

```python
import json, urllib.request
payload = json.dumps({"model": "model-id", "messages": [...], "max_tokens": 80})
req = urllib.request.Request(url, data=payload.encode(), headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=30) as resp:
    data = json.loads(resp.read())
```

For OAuth-only providers (no raw API key), only Hermes CLI probing works — direct calls return `Missing API key` / `Invalid API key`.

### Rate Limiting & WAF

Some providers (notably OpenCode Zen behind Cloudflare) return **HTTP 403 error code 1010** on rapid automated requests. This is Cloudflare's WAF sliding-window limiter, not a credential issue.

**Mitigations:**
- Insert 2-3 second delays between sequential requests to the same provider
- If 403 persists 60+ seconds, the IP hit the rate limit — wait 30-60 seconds before retrying
- `hermes chat -q` auto-retries 3 times with exponential backoff
- Direct HTTP requests do NOT auto-retry — handle 403 with sleep-and-retry logic

### Reference

See `references/opencode-zen-free-tiers.md` for a worked example: model probing across OpenCode Zen's free tier including observed cutoffs, Cloudflare rate limit diagnostics, and API key validation.

## Common Pitfalls

- **Provider block exists, key missing**: The provider is registered in config but will 401 at runtime. The block is necessary but not sufficient.
- **Commented providers ≠ configured**: Config files often list zai, kimi-coding, minimax, bedrock as comments/documentation. These are NOT configured unless uncommented with actual keys.
- **`hermes auth list` may disagree** with config.yaml state if credentials were loaded from a different source or the pool uses a timed rotation strategy.
- **`COPILOT_GITHUB_TOKEN` vs `GITHUB_TOKEN`**: Different tokens for different purposes. Copilot auth uses its own token; gh CLI may use a separate GITHUB_TOKEN or OAuth.

## Verification

After enumerating, confirm with:

```bash
hermes auth list
hermes doctor
```

## When to Use

- When performing hermes provider enumeration operations or tasks
- When managing hermes provider enumeration infrastructure or configurations
- When automating or debugging hermes provider enumeration workflows
- **Triggers**: "set up devops/hermes-provider-enumeration", "configure hermes provider enumeration", "debug hermes provider enumeration issue"

## Workflow

### Phase 1: Setup

Verify prerequisites and ensure required dependencies are available.

### Phase 2: Execute

Perform the hermes provider enumeration operations following the instructions in this skill.

### Phase 3: Verify

Confirm the output meets expectations and address any issues.

### Phase 4: Document

Record any changes, configurations, or decisions made during execution.

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Hermes Provider Enumeration operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Overview

Hermes Provider Enumeration is a skill for handling hermes provider enumeration tasks and automation workflows. Use this skill when you need to perform hermes provider enumeration operations efficiently.

