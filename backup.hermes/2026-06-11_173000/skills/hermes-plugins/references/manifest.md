# Plugin Manifest (plugin.yaml)

```yaml
name: my-plugin                    # Required: unique identifier
version: 1.0.0                     # Required: semver
description: "Brief description"   # Required: shown in plugin list
author: "Your Name"                # Optional
license: "MIT"                     # Optional

# Plugin type determines integration point
type: tool                         # model_provider, memory_provider, tool, auth, utility

# Entry point (Python, JS, or shell)
entry_point: main.py               # or index.js, hook.sh

# Optional: JSON Schema for plugin config validation
config_schema:
  type: object
  properties:
    api_key:
      type: string
      description: "API key for service"
    endpoint:
      type: string
      description: "Service endpoint URL"
    timeout:
      type: integer
      description: "Request timeout in seconds"
      default: 30

# For tool plugins: register callable tools
tools:
  - name: my_tool
    description: "What this tool does"
    parameters:
      type: object
      properties:
        query:
          type: string
          description: "Input query"
        max_results:
          type: integer
          default: 10

# For memory providers
memory:
  backend: "honcho"
  config_keys: ["api_key", "endpoint"]

# For model providers
model_provider:
  models_endpoint: "/v1/models"
  chat_endpoint: "/v1/chat/completions"
```

## Field Reference
| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Unique identifier (lowercase, hyphens) |
| `version` | ✅ | Semantic version |
| `description` | ✅ | One-line description |
| `type` | ✅ | Plugin type: model_provider, memory_provider, tool, auth, utility |
| `entry_point` | ✅ | Path to main module |
| `config_schema` | ❌ | JSON Schema for config validation |
| `tools` | ❌ | Tool definitions (for tool plugins) |
| `memory` | ❌ | Memory backend config (for memory providers) |
| `model_provider` | ❌ | Model provider config (for model providers) |

## Discovery
- Plugins scanned at startup from `~/.hermes/plugins/`
- Enabled plugins loaded automatically
- Config from `config.yaml` → `plugins.enabled[]`