---
name: hermes-plugins
description: Plugin architecture, configuration, development templates, and built-in plugins
version: 1.0.0
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [hermes, plugins, extensibility]
    category: plugins
    requires_toolsets: [terminal, file, skills]
    config:
      - key: hermes.skill.plugins.enabled
        description: "Enable plugins skill"
        default: "true"
---

# Hermes Plugins Skill

## When to Use
- Configuring built-in plugins (disk-cleanup, OpenRouter, security-guidance)
- Developing custom plugins (model providers, memory providers, tools, auth, utilities)
- Managing plugin lifecycle (enable, disable, update)

## Procedure
1. **Built-in Plugins** (config.yaml):
   ```yaml
   plugins:
     enabled:
       - disk-cleanup
       - model-providers/openrouter
       - security-guidance
       - memory/honcho  # Cross-session memory
     disabled: []
   ```

2. **Plugin Types**:
   | Type | Description | Example |
   |------|-------------|---------|
   | Model Provider | New LLM provider integration | openrouter, anthropic, bedrock |
   | Memory Provider | Alternative memory backend | honcho (cross-session) |
   | Tool | New callable tools | Custom API integrations |
   | Authentication | New auth methods | OAuth providers |
   | Utility | Helper functions, maintenance | disk-cleanup |

3. **Install Plugin**:
   ```bash
   # Manual installation
   git clone https://github.com/example/hermes-plugin-xyz ~/.hermes/plugins/xyz
   
   # Enable in config.yaml
   plugins:
     enabled:
       - xyz
   
   # Development installation
   ln -s /path/to/your/plugin ~/.hermes/plugins/my-plugin
   
   # Restart Hermes
   ```

4. **Plugin Manifest** (plugin.yaml):
   ```yaml
   name: my-plugin
   version: 1.0.0
   description: "Brief description"
   author: "Your Name"
   license: "MIT"
   type: tool  # model_provider, memory_provider, tool, auth, utility
   entry_point: main.py  # or index.js, hook.sh
   config_schema:
     type: object
     properties:
       api_key:
         type: string
         description: "API key for service"
   
   # For tool plugins:
   tools:
     - name: my_tool
       description: "What this tool does"
       parameters:
         type: object
         properties:
           query:
             type: string
   
   # For memory providers:
   memory:
     backend: "honcho"
     config_keys: ["api_key", "endpoint"]
   ```

5. **Python Plugin Template**:
   ```
   my-plugin/
   ├── plugin.yaml
   ├── main.py
   └── requirements.txt
   ```
   
   **main.py**:
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
           return {"result": f"Processed: {query}"}
   ```

6. **Model Provider Config** (OpenRouter):
   ```yaml
   model:
     provider: openrouter
     openrouter:
       api_key: "${OPENROUTER_API_KEY}"
       model: "anthropic/claude-3.5-sonnet"
   ```

7. **Memory Provider Config** (Honcho):
   ```yaml
   memory:
     provider: honcho
     honcho:
       api_key: "${HONCHO_API_KEY}"
       workspace: "my-project"
   ```

8. **Management Commands**:
   ```bash
   hermes plugins list
   hermes plugins enable <name>
   hermes plugins disable <name>
   hermes plugins info <name>
   ```

## Pitfalls
- **Plugin not loading** → Check `config.yaml` enabled list; verify `plugin.yaml` syntax
- **Import errors** → Ensure dependencies in `requirements.txt` / `package.json` installed
- **Config not applied** → Restart Hermes after config changes
- **Tool not appearing** → Verify tool registration in `get_tools()`; check toolset config
- **Memory provider not working** → Check `memory.provider` in config; verify credentials

## Verification
- `hermes plugins list` shows enabled plugins
- Custom tool available via `/my_tool`
- Model provider works with `hermes chat`
- Memory persists across sessions

## References
- `references/commands.md` — CLI commands
- `references/manifest.md` — plugin.yaml specification
- `references/plugin-template.md` — Python/JS templates