# Provider Documentation Research Template

**Provider**: {{PROVIDER_NAME}}
**Research Date**: {{TIMESTAMP}}
**Researcher**: {{RESEARCHER}}
**Session**: {{SESSION_ID}}

## Provider Overview

| Field | Value |
|---|---|
| Provider Name | {{PROVIDER_NAME}} |
| Auth Method | {{AUTH_METHOD}} |
| Base URL | {{BASE_URL}} |
| API Documentation URL | {{API_DOCS_URL}} |
| Model List URL | {{MODEL_LIST_URL}} |
| Pricing Page | {{PRICING_URL}} |
| Status Page | {{STATUS_URL}} |
| Community/Discord | {{COMMUNITY_URL}} |

## Authentication Configuration for Hermes

### Credential Setup

```yaml
# Example credential configuration for {{PROVIDER_NAME}}
providers:
  {{PROVIDER_NAME}}:
    api_key: "{{ENV_VAR_NAME}}"
    # or
    oauth:
      client_id: "{{CLIENT_ID}}"
      client_secret: "{{CLIENT_SECRET}}"
```

### Environment Variables Required

| Variable | Description | Required |
|---|---|---|
| {{ENV_VAR_1}} | {{ENV_VAR_1_DESC}} | {{ENV_VAR_1_REQ}} |
| {{ENV_VAR_2}} | {{ENV_VAR_2_DESC}} | {{ENV_VAR_2_REQ}} |

### Hermes Config Example

```yaml
providers:
  {{PROVIDER_NAME}}:
    default_model: "{{DEFAULT_MODEL}}"
    models:
      - "{{MODEL_1}}"
      - "{{MODEL_2}}"
    base_url: "{{BASE_URL}}"
```

## Discovered :free Models

### From Official Documentation

| Model ID | Context Window | Max Output | Vision | Reasoning | Notes | Source URL |
|---|---|---|---|---|---|---|
| {{MODEL_1}} | {{CTX_1}} | {{OUT_1}} | {{VIS_1}} | {{REAS_1}} | {{NOTES_1}} | {{SRC_1}} |
| {{MODEL_2}} | {{CTX_2}} | {{OUT_2}} | {{VIS_2}} | {{REAS_2}} | {{NOTES_2}} | {{SRC_2}} |
| {{MODEL_3}} | {{CTX_3}} | {{OUT_3}} | {{VIS_3}} | {{REAS_3}} | {{NOTES_3}} | {{SRC_3}} |

### From Community/Third-Party Sources

| Model ID | Context Window | Max Output | Vision | Reasoning | Notes | Source URL |
|---|---|---|---|---|---|---|
| {{COMM_MODEL_1}} | {{COMM_CTX_1}} | {{COMM_OUT_1}} | {{COMM_VIS_1}} | {{COMM_REAS_1}} | {{COMM_NOTES_1}} | {{COMM_SRC_1}} |

## Configuration Best Practices

### Rate Limits

| Tier | Requests/Minute | Tokens/Minute | Concurrent |
|---|---|---|---|
| Free | {{FREE_RPM}} | {{FREE_TPM}} | {{FREE_CONC}} |
| Paid | {{PAID_RPM}} | {{PAID_TPM}} | {{PAID_CONC}} |

### Known Issues / Gotchas

1. {{ISSUE_1}}
2. {{ISSUE_2}}
3. {{ISSUE_3}}

### Recommended Settings for Hermes

```yaml
# Recommended provider-specific settings
providers:
  {{PROVIDER_NAME}}:
    timeout: {{RECOMMENDED_TIMEOUT}}
    max_retries: {{RECOMMENDED_RETRIES}}
    # Provider-specific options
    {{PROVIDER_SPECIFIC_OPTIONS}}
```

## Web Research Sources

| Query | Result URL | Relevance | Extracted |
|---|---|---|---|
| "{{QUERY_1}}" | {{URL_1}} | High/Med/Low | Yes/No |
| "{{QUERY_2}}" | {{URL_2}} | High/Med/Low | Yes/No |
| "{{QUERY_3}}" | {{URL_3}} | High/Med/Low | Yes/No |

## Saved Markdown Files

- `provider_docs/{{PROVIDER_NAME}}-api-docs.md`
- `provider_docs/{{PROVIDER_NAME}}-models.md`
- `provider_docs/{{PROVIDER_NAME}}-pricing.md`
- `provider_docs/{{PROVIDER_NAME}}-best-practices.md`

## Gaps / Follow-up Needed

- [ ] {{GAP_1}}
- [ ] {{GAP_2}}
- [ ] {{GAP_3}}

---

*Fill in all {{PLACEHOLDERS}} during Phase 2 execution. Save completed template as `provider_docs/{{PROVIDER_NAME}}-research.md`*