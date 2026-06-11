# Plugin Development Templates

## Python Plugin Structure
```
my-plugin/
├── plugin.yaml
├── main.py
└── requirements.txt
```

## Python Template (main.py)
```python
from hermes.plugins import PluginBase, Tool

class MyPlugin(PluginBase):
    name = "my-plugin"
    
    def initialize(self, config: dict):
        """Called once at plugin load. Access config.yaml values."""
        self.api_key = config.get("api_key")
        self.endpoint = config.get("endpoint", "https://api.example.com")
    
    def get_tools(self):
        """Return list of Tool objects this plugin provides."""
        return [
            Tool(
                name="my_tool",
                description="Does something useful",
                parameters={
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Input query"},
                        "max_results": {"type": "integer", "default": 10}
                    }
                },
                handler=self.handle_my_tool
            )
        ]
    
    async def handle_my_tool(self, query: str, max_results: int = 10):
        """Tool handler - implement your logic here."""
        # Your implementation
        return {"result": f"Processed: {query}", "count": max_results}

# For model providers, extend ModelProviderBase
# For memory providers, extend MemoryProviderBase
```

## requirements.txt
```
httpx>=0.25.0
pydantic>=2.0.0
```

## JavaScript/TypeScript Template
```
my-plugin/
├── plugin.yaml
├── index.js
└── package.json
```

**index.js**:
```javascript
class MyPlugin {
    constructor() {
        this.name = "my-plugin";
    }
    
    initialize(config) {
        this.apiKey = config.api_key;
    }
    
    getTools() {
        return [{
            name: "my_tool",
            description: "Does something useful",
            parameters: {
                type: "object",
                properties: {
                    query: { type: "string" }
                }
            },
            handler: async (args) => {
                return { result: `Processed: ${args.query}` };
            }
        }];
    }
}

module.exports = new MyPlugin();
```

**package.json**:
```json
{
  "name": "hermes-plugin-my-plugin",
  "version": "1.0.0",
  "main": "index.js",
  "dependencies": {}
}
```

## Hook-based Plugin (shell)
```bash
#!/usr/bin/env bash
# hook.sh - for hooks, not tool plugins
# Receives JSON on stdin, outputs JSON on stdout
```

## Best Practices
1. **Minimal permissions** — plugins run with same privileges as Hermes
2. **Error handling** — never crash the agent; return structured errors
3. **Config validation** — use JSON Schema in `plugin.yaml`
4. **Logging** — use Hermes logging infrastructure, not print()
5. **Testing** — test with `hermes chat --toolsets <plugin-toolset>`