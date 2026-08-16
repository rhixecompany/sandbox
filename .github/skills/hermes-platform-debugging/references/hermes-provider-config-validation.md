---
name: hermes-provider-config-validation
title: "Hermes Provider Config Validation"
description: "Validate Hermes provider support before switching models."
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - hermes
  - provider
  - auth
  - validation
  - configuration
---

# Hermes Provider Config Validation

## Overview

Class-level workflow for validating provider support, API key permissions, and Hermes configuration before switching models or adding credentials. Prevents misconfigured providers, unsupported chat backends, and silent auth failures.

## When to Use

- Adding a new API key to Hermes (`hermes auth add` or `.env`)
- Changing `model.provider`, `model.default`, or `model.base_url`
- Validating whether a provider supports chat completions in Hermes
- Debugging 403/401 errors after adding a new key
- Auditing provider support before recommending a model switch

## When NOT to Use

- OAuth-only providers that require browser flow (`hermes auth` handles these)
- STT/TTS-only provider config (`stt.provider`, `tts.provider`)
- MCP server configuration (use `hermes-mcp` skills)

## Workflow

### 1. Check Hermes Provider Support

1. Inspect `hermes-agent` source for provider routing:
   - `agent/models_dev.py` — provider id mapping
   - `agent/agent_init.py` — provider-specific init branches
   - `.env.example` — documented env vars and supported providers
2. Confirm the provider id is accepted by `hermes auth add <provider>`
3. If `hermes auth add <provider>` returns `Unknown provider`, the provider is not wired for auth even if the API endpoint exists

### 2. Validate API Key Permissions

Always test the key against the provider's public model endpoint before configuring Hermes:

```bash
# Generic pattern
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer $API_KEY" \
  "$PROVIDER_BASE_URL/v1/models"
```

Or via Python:

```python
import requests
r = requests.get(
    f"{base_url}/v1/models",
    headers={"Authorization": f"Bearer {api_key}"},
    timeout=20,
)
print(r.status_code, r.json().get("data", [])[:5])
```

Interpret results:
- `200` + model list → key is valid and has model-read permissions
- `403` + permission-denied → key is rejected or the team/account lacks credits/licenses
- `401` → key is invalid or expired
- Timeout → network/DNS issue, not a key issue

### 3. Configure Hermes

Only after steps 1 and 2 pass:

1. Add credential:
   ```bash
   hermes auth add <provider> --type api-key --api-key "$API_KEY"
   ```
2. Update `config.yaml`:
   ```yaml
   model:
     provider: <provider>
     default: <model-id>
     base_url: <base-url>
   ```
3. Verify with a test query:
   ```bash
   hermes chat -q "TEST_OK" -m <model-id>
   ```

## Provider-Specific Findings

### Groq

- **Hermes support:** STT/TTS only, not a general chat provider
- **Env var:** `GROQ_API_KEY`
- **Chat config:** Do NOT set `model.provider: groq` for chat; Hermes will not route chat through Groq
- **Use case:** Voice transcription only (`stt.provider: groq`)

### xAI / Grok

- **Hermes support:** Yes, via `xai` or `xai-oauth` provider
- **Env var:** `XAI_API_KEY`
- **Key validation:** `/v1/models` may return 403 even with a syntactically valid key if the team/account has no credits or licenses
- **Chat config:** Only configure after confirming the key can list models and complete a chat completion
- **Error signature:** `{"code":"permission-denied","error":"Your newly created team doesn't have any credits or licenses yet..."}`

## Pitfalls

- **Do not assume endpoint availability = chat support:** A provider may expose `/v1/models` but Hermes may only support it for STT/TTS
- **`hermes auth add` is not generic:** It rejects providers not in the auth registry, even if the underlying API works
- **403 with valid key format:** Means permission/credit issue, not key syntax issue
- **Store keys even if provider is unusable:** If the key is valid but provider support is missing, store in `.env` for future use but do not route chat through it
- **Never echo raw keys in logs:** Use `***` redaction in all reports and skill references

## Verification Checklist

- [ ] Provider id confirmed in Hermes source or `hermes auth add --help`
- [ ] API key returns 200 from `/v1/models` or chat completions endpoint
- [ ] No 403 credit/license errors from provider
- [ ] `hermes auth add <provider>` succeeds
- [ ] `config.yaml` model section updated
- [ ] Test query completes successfully
- [ ] Keys stored in `.env`, not in config.yaml

## References

- `references/provider-support-matrix.md` — Hermes provider id mapping, STT/TTS-only providers, env var names
- `references/api-validation-recipes.md` — Curl/Python snippets for validating keys against live endpoints
- `references/groq-xai-findings.md` — Session-specific findings for Groq and xAI/Grok auth behavior
