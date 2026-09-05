# Hermes Config Target Template

**Config Date**: {{TIMESTAMP}}
**Session**: {{SESSION_ID}}
**Configurator**: {{CONFIGURATOR}}

## Target Configuration State

### Model Configuration

```yaml
model:
  base_url: "{{TARGET_BASE_URL}}"
  default: "{{TARGET_DEFAULT_MODEL}}"
  provider: "{{TARGET_PROVIDER}}"
  api_mode: "{{TARGET_API_MODE}}"
```

### Provider Configurations

```yaml
providers:
  {{PROVIDER_1}}:
    default_model: "{{PROVIDER_1_MODEL}}"
    models:
      - "{{PROVIDER_1_MODEL}}"
      {{PROVIDER_1_EXTRA_MODELS}}
    base_url: "{{PROVIDER_1_BASE_URL}}"
  
  {{PROVIDER_2}}:
    default_model: "{{PROVIDER_2_MODEL}}"
    models:
      - "{{PROVIDER_2_MODEL}}"
      {{PROVIDER_2_EXTRA_MODELS}}
    base_url: "{{PROVIDER_2_BASE_URL}}"
  
  {{PROVIDER_3}}:
    default_model: "{{PROVIDER_3_MODEL}}"
    models:
      - "{{PROVIDER_3_MODEL}}"
      {{PROVIDER_3_EXTRA_MODELS}}
    base_url: "{{PROVIDER_3_BASE_URL}}"
  
  {{PROVIDER_4}}:
    default_model: "{{PROVIDER_4_MODEL}}"
    models:
      - "{{PROVIDER_4_MODEL}}"
      {{PROVIDER_4_EXTRA_MODELS}}
    base_url: "{{PROVIDER_4_BASE_URL}}"
  
  {{PROVIDER_5}}:
    default_model: "{{PROVIDER_5_MODEL}}"
    models:
      - "{{PROVIDER_5_MODEL}}"
      {{PROVIDER_5_EXTRA_MODELS}}
    base_url: "{{PROVIDER_5_BASE_URL}}"
```

### Fallback Chain

```yaml
fallback_providers:
  - "{{FALLBACK_1}}"
  - "{{FALLBACK_2}}"
  - "{{FALLBACK_3}}"
  - "{{FALLBACK_4}}"
  - "{{FALLBACK_5}}"
```

### Auxiliary Models

```yaml
auxiliary:
  free_only: true
  openrouter_model: "{{AUX_OPENROUTER_MODEL}}"
  vision:
    provider: "{{VISION_PROVIDER}}"
    model: "{{VISION_MODEL}}"
    timeout: {{VISION_TIMEOUT}}
    download_timeout: {{VISION_DOWNLOAD_TIMEOUT}}
```

### Credential Pool Strategies

```yaml
credential_pool_strategies:
  {{PROVIDER_1}}: fill_first
  {{PROVIDER_2}}: fill_first
  {{PROVIDER_3}}: fill_first
  {{PROVIDER_4}}: fill_first
  {{PROVIDER_5}}: fill_first
  copilot: fill_first
  deepseek: fill_first
  gemini: fill_first
  huggingface: fill_first
  ollama-cloud: fill_first
  openai-api: least_used
  openai-codex: least_used
  xai: fill_first
```

## Commands to Apply

```bash
# Primary model
hermes config set model.provider "{{TARGET_PROVIDER}}"
hermes config set model.default "{{TARGET_DEFAULT_MODEL}}"
hermes config set model.base_url "{{TARGET_BASE_URL}}"
hermes config set model.api_mode "{{TARGET_API_MODE}}"

# Fallback chain (MUST be YAML list)
hermes config set fallback_providers '["{{FALLBACK_1}}","{{FALLBACK_2}}","{{FALLBACK_3}}","{{FALLBACK_4}}","{{FALLBACK_5}}"]

# Provider default models
hermes config set providers.{{FALLBACK_1}}.default_model "{{FALLBACK_1_MODEL}}"
hermes config set providers.{{FALLBACK_2}}.default_model "{{FALLBACK_2_MODEL}}"
hermes config set providers.{{FALLBACK_3}}.default_model "{{FALLBACK_3_MODEL}}"
hermes config set providers.{{FALLBACK_4}}.default_model "{{FALLBACK_4_MODEL}}"
hermes config set providers.{{FALLBACK_5}}.default_model "{{FALLBACK_5_MODEL}}"

# Auxiliary
hermes config set auxiliary.vision.provider "{{VISION_PROVIDER}}"
hermes config set auxiliary.vision.model "{{VISION_MODEL}}"
hermes config set auxiliary.openrouter_model "{{AUX_OPENROUTER_MODEL}}"
```

## Verification Commands

```bash
# Verify config structure
hermes config check

# Verify fallback_providers is a list
python -c "import yaml,os; c=yaml.safe_load(open(os.environ['LOCALAPPDATA']+'/hermes/config.yaml')); assert isinstance(c['fallback_providers'], list), 'fallback_providers must be a list'; print('OK:', c['fallback_providers'])"

# Verify each provider has working default_model
hermes profile list
```

## Expected Verification Output

```
fallback_providers: ['{{FALLBACK_1}}', '{{FALLBACK_2}}', '{{FALLBACK_3}}', '{{FALLBACK_4}}', '{{FALLBACK_5}}']
model.provider: {{TARGET_PROVIDER}}
model.default: {{TARGET_DEFAULT_MODEL}}
```

## Current vs Target Diff

| Setting | Current | Target | Match |
|---|---|---|---|
| model.provider | {{CURR_PROVIDER}} | {{TARGET_PROVIDER}} | {{MATCH_PROVIDER}} |
| model.default | {{CURR_DEFAULT}} | {{TARGET_DEFAULT}} | {{MATCH_DEFAULT}} |
| model.base_url | {{CURR_BASE_URL}} | {{TARGET_BASE_URL}} | {{MATCH_BASE_URL}} |
| fallback_providers | {{CURR_FALLBACK}} | {{TARGET_FALLBACK}} | {{MATCH_FALLBACK}} |
| providers.{{FALLBACK_1}}.default_model | {{CURR_FB1_MODEL}} | {{FALLBACK_1_MODEL}} | {{MATCH_FB1}} |
| providers.{{FALLBACK_2}}.default_model | {{CURR_FB2_MODEL}} | {{FALLBACK_2_MODEL}} | {{MATCH_FB2}} |
| providers.{{FALLBACK_3}}.default_model | {{CURR_FB3_MODEL}} | {{FALLBACK_3_MODEL}} | {{MATCH_FB3}} |
| auxiliary.vision.model | {{CURR_VISION}} | {{VISION_MODEL}} | {{MATCH_VISION}} |

---

*Fill in during Phase 5 execution. Save as `config/hermes-config-target-{{TIMESTAMP}}.md`*