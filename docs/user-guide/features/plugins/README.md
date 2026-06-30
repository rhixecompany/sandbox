# Hermes Agent Plugins — Comprehensive Summary

> **Source:** https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins

---

## Overview

Plugins extend Hermes Agent's core functionality beyond built-in features. They can add new tools, memory providers, model providers, authentication methods, and more.

---

## Plugin Architecture

- **Location:** `~/AppData/Local/hermes/plugins/` (user) + bundled in Hermes install
- **Config:** `config.yaml` → `plugins.enabled[]` / `plugins.disabled[]`
- **Format:** Each plugin is a directory with `plugin.yaml` manifest + code
- **Discovery:** Scanned at startup; enabled plugins loaded automatically

---

## Plugin Configuration (`config.yaml`)

```yaml
plugins:
  enabled:
    - disk-cleanup
    - model-providers/openrouter
    - security-guidance
  disabled:
    - some-unwanted-plugin
```

---

## Built-in Plugins

| Plugin | Status | Purpose |
|--------|--------|---------|
| `disk-cleanup` | ✅ enabled | Disk cleanup utilities |
| `model-providers/openrouter` | ✅ enabled | OpenRouter model provider |
| `security-guidance` | ✅ enabled | Security guidance |

---

## Plugin Types

| Type | Description | Example |
|------|-------------|---------|
| **Model Provider** | Adds new LLM provider integration | `openrouter`, `anthropic`, `bedrock` |
| **Memory Provider** | Alternative memory backend | `honcho` (cross-session) |
| **Tool** | Adds new callable tools | Custom API integrations |
| **Authentication** | New auth methods for platforms | OAuth providers |
| **Utility** | Helper functions, maintenance | `disk-cleanup` |

---

## Installing Plugins

### From Catalog (Future)
```bash
# Planned: hermes plugin install <name>
```

### Manual Installation
```bash
# 1. Clone or download plugin to ~/AppData/Local/hermes/plugins/
git clone https://github.com/example/hermes-plugin-xyz ~/AppData/Local/hermes/plugins/xyz

# 2. Enable in config.yaml
plugins:
  enabled:
    - xyz

# 3. Restart Hermes
```

### Development Installation
```bash
# For local development
ln -s /path/to/your/plugin ~/AppData/Local/hermes/plugins/my-plugin
```

---

## Plugin Manifest (`plugin.yaml`)

```yaml
name: my-plugin
version: 1.0.0
description: "Brief description"
author: "Your Name"
license: "MIT"

type: model_provider  # or: memory_provider, tool, auth, utility

entry_point: main.py  # or: index.js, hook.sh
config_schema:        # Optional: JSON Schema for plugin config
  type: object
  properties:
    api_key:
      type: string
      description: "API key for service"

# For tool plugins
tools:
  - name: my_tool
    description: "What this tool does"
    parameters:
      type: object
      properties:
        query:
          type: string

# For memory providers
memory:
  backend: "honcho"
  config_keys: ["api_key", "endpoint"]
```

---

## Writing a Plugin

### Python Plugin Template
```
my-plugin/
├── plugin.yaml
├── main.py
└── requirements.txt
```

**main.py:**
```python
from hermes.plugins import PluginBase, Tool

class MyPlugin(PluginBase):
    name = "my-plugin"
    
    def initialize(self, config: dict):
        self.api_key = config.get("api_key")
    
    def get_tools(self):
        return [
            Tool(
                name="my_tool",
                description="Does something useful",
                parameters={"type": "object", "properties": {"query": {"type": "string"}}},
                handler=self.handle_my_tool
            )
        ]
    
    async def handle_my_tool(self, query: str):
        # Your logic here
        return {"result": f"Processed: {query}"}
```

### JavaScript/TypeScript Plugin
Plugin system supports JS/TS via Node.js entry points.

---

## Memory Provider Plugins

### Honcho (Cross-Session Memory)
```yaml
plugins:
  enabled:
    - memory/honcho
```

**Config:**
```yaml
memory:
  provider: honcho
  honcho:
    api_key: "${HONCHO_API_KEY}"
    workspace: "my-project"
```

---

## Model Provider Plugins

### OpenRouter
```yaml
plugins:
  enabled:
    - model-providers/openrouter
```

**Config:**
```yaml
model:
  provider: openrouter
  openrouter:
    api_key: "${OPENROUTER_API_KEY}"
    model: "anthropic/claude-3.5-sonnet"
```

---

## Security Guidance Plugin

Provides automated security review capabilities:
- Secret detection in prompts/files
- Dependency vulnerability scanning
- Code pattern analysis

---

## Disk Cleanup Plugin

Automated maintenance:
- Cleans old logs (`~/AppData/Local/hermes/logs/`)
- Removes temp files
- Prunes old session data
- Configurable retention policies

---

## Plugin Management Commands

```bash
# List installed plugins
hermes plugins list

# Enable plugin
hermes plugins enable <name>

# Disable plugin
hermes plugins disable <name>

# Show plugin info
hermes plugins info <name>
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Plugin not loading | Check `config.yaml` enabled list; verify `plugin.yaml` syntax |
| Import errors | Ensure dependencies in `requirements.txt` / `package.json` installed |
| Config not applied | Restart Hermes after config changes |
| Tool not appearing | Verify tool registration in `get_tools()`; check toolset config |
| Memory provider not working | Check `memory.provider` in config; verify credentials |

---

## Best Practices

1. **Minimal permissions** — plugins run with same privileges as Hermes
2. **Error handling** — never crash the agent; return structured errors
3. **Config validation** — use JSON Schema in `plugin.yaml`
4. **Logging** — use Hermes logging infrastructure, not print()
5. **Testing** — test with `hermes chat --toolsets <plugin-toolset>`

---

## Related Documentation

- [Adding Tools (Developer Guide)](/docs/developer-guide/adding-tools)
- [Model Providers](/docs/user-guide/configuration#model-providers)
- [Memory Providers](/docs/user-guide/features/memory)

---

**Source:** [Hermes Agent Docs - Plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)  
**Extracted:** 2026-06-08