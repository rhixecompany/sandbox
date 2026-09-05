# Provider Inventory Template

**Generated**: {{TIMESTAMP}}
**Session**: {{SESSION_ID}}
**Operator**: {{OPERATOR}}

## Hermes Auth List Output

```text
{{AUTH_LIST_OUTPUT}}
```

## Hermes Config Show Output

```text
{{CONFIG_SHOW_OUTPUT}}
```

## Hermes Profile List Output

```text
{{PROFILE_LIST_OUTPUT}}
```

## Parsed Provider Inventory

| Provider | Credential Status | Auth Method | Base URL (from config) | Docs URL (researched) | Current Default Model | Notes |
|---|---|---|---|---|---|---|
| nous | {{NOUS_CRED_STATUS}} | device_code | {{NOUS_BASE_URL}} | {{NOUS_DOCS_URL}} | {{NOUS_DEFAULT_MODEL}} | |
| opencode-zen | {{OPENCODE_ZEN_CRED_STATUS}} | api_key + oauth | {{OPENCODE_ZEN_BASE_URL}} | {{OPENCODE_ZEN_DOCS_URL}} | {{OPENCODE_ZEN_DEFAULT_MODEL}} | |
| openrouter | {{OPENROUTER_CRED_STATUS}} | api_key | {{OPENROUTER_BASE_URL}} | {{OPENROUTER_DOCS_URL}} | {{OPENROUTER_DEFAULT_MODEL}} | |
| ollama-cloud | {{OLLAMA_CLOUD_CRED_STATUS}} | api_key | {{OLLAMA_CLOUD_BASE_URL}} | {{OLLAMA_CLOUD_DOCS_URL}} | {{OLLAMA_CLOUD_DEFAULT_MODEL}} | |
| gemini | {{GEMINI_CRED_STATUS}} | api_key | {{GEMINI_BASE_URL}} | {{GEMINI_DOCS_URL}} | {{GEMINI_DEFAULT_MODEL}} | |
| deepseek | {{DEEPSEEK_CRED_STATUS}} | api_key | {{DEEPSEEK_BASE_URL}} | {{DEEPSEEK_DOCS_URL}} | {{DEEPSEEK_DEFAULT_MODEL}} | |
| xai | {{XAI_CRED_STATUS}} | api_key | {{XAI_BASE_URL}} | {{XAI_DOCS_URL}} | {{XAI_DEFAULT_MODEL}} | Auth failed |
| openai-api | {{OPENAI_API_CRED_STATUS}} | api_key | {{OPENAI_API_BASE_URL}} | {{OPENAI_API_DOCS_URL}} | {{OPENAI_API_DEFAULT_MODEL}} | Exhausted (402) |
| openai-codex | {{OPENAI_CODEX_CRED_STATUS}} | oauth | {{OPENAI_CODEX_BASE_URL}} | {{OPENAI_CODEX_DOCS_URL}} | {{OPENAI_CODEX_DEFAULT_MODEL}} | Rate limited |

## Current Fallback Chain

```yaml
fallback_providers: {{CURRENT_FALLBACK_PROVIDERS}}
```

## Primary Model

```yaml
model:
  provider: {{CURRENT_MODEL_PROVIDER}}
  default: {{CURRENT_MODEL_DEFAULT}}
  base_url: {{CURRENT_MODEL_BASE_URL}}
  api_mode: {{CURRENT_MODEL_API_MODE}}
```

## Provider Models from Config

{{PROVIDER_MODELS_TABLE}}

---

*Fill in all {{PLACEHOLDERS}} during Phase 1 execution.*