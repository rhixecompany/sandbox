# Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins

# Hermes Agent Plugins — Comprehensive Summary

## Quick Overview

Hermes uses a **plugin system** for adding custom tools, hooks, and integrations without modifying core code. Plugins are directories dropped into `~/.hermes/plugins/` with a `plugin.yaml` manifest and Python code.

### Plugin Structure
```
~/.hermes/plugins/my-plugin/
├── plugin.yaml          # manifest
├── __init__.py          # register() — wires schemas to handlers
├── schemas.py           # tool schemas (what the LLM sees)
└── tools.py             # tool handlers (what runs when called)
```

**Project-local plugins** under `./.hermes/plugins/` are **disabled by default**. Enable with:
```bash
HERMES_ENABLE_PROJECT_PLUGINS=true
```

---

## Minimal Working Example

### `plugin.yaml`
```yaml
name: hello-world
version: "1.0"
description: A minimal example plugin
```

### `__init__.py`
```python
"""Minimal Hermes plugin — registers a tool and a hook."""

import json

def register(ctx):
    # --- Tool: hello_world ---
    schema = {
        "name": "hello_world",
        "description": "Returns a friendly greeting for the given name.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name to greet",
                }
            },
            "required": ["name"],
        },
    }

    def handle_hello(params, **kwargs):
        del kwargs
        name = params.get("name", "World")
        return json.dumps({"success": True, "greeting": f"Hello, {name}!"})

    ctx.register_tool(
        name="hello_world",
        toolset="hello_world",
        schema=schema,
        handler=handle_hello,
        description="Return a friendly greeting for the given name.",
    )

    # --- Hook: log every tool call ---
    def on_tool_call(tool_name, params, result):
        print(f"[hello-world] tool called: {tool_name}")

    ctx.register_hook("post_tool_call", on_tool_call)
```

**Usage:** Drop both files into `~/.hermes/plugins/hello-world/`, restart Hermes → model can immediately call `hello_world`.

---

## What Plugins Can Do

All `ctx.*` APIs are available inside a plugin's `register(ctx)` function.

| Capability | API |
|------------|-----|
| **Add tools** | `ctx.register_tool(name=..., toolset=..., schema=..., handler=...)` |
| **Add hooks** | `ctx.register_hook("post_tool_call", callback)` |
| **Add slash commands** | `ctx.register_command(name, handler, description)` — adds `/name` in CLI/gateway |
| **Dispatch tools from commands** | `ctx.dispatch_tool(name, args)` — invokes registered tool with parent-agent context |
| **Add CLI commands** | `ctx.register_cli_command(name, help, setup_fn, handler_fn)` — adds `hermes <plugin> <subcommand>` |
| **Inject messages** | `ctx.inject_message(content, role="user")` — see [Injecting Messages](#injecting-messages) |
| **Ship data files** | `Path(__file__).parent / "data" / "file.yaml"` |
| **Bundle skills** | `ctx.register_skill(name, path)` — namespaced as `plugin:skill`, loaded via `skill_view("plugin:skill")` |
| **Gate on env vars** | `requires_env: [API_KEY]` in `plugin.yaml` — prompted during `hermes plugins install` |
| **Distribute via pip** | `[project.entry-points."hermes_agent.plugins"]` |
| **Register gateway platform** | `ctx.register_platform(name, label, adapter_factory, check_fn, ...)` |
| **Register image-gen backend** | `ctx.register_image_gen_provider(provider)` |
| **Register video-gen backend** | `ctx.register_video_gen_provider(provider)` |
| **Register context-compression engine** | `ctx.register_context_engine(engine)` |
| **Register memory backend** | Subclass `MemoryProvider` in `plugins/memory/<name>/__init__.py` |
| **Run host-owned LLM call** | `ctx.llm.complete(...)` / `ctx.llm.complete_structured(...)` — borrow user's active model + auth |
| **Register inference backend (LLM provider)** | `register_provider(ProviderProfile(...))` in `plugins/model-providers/<name>/__init__.py` |

---

## Plugin Discovery

### Discovery Sources (priority order — later overrides earlier)

| Source | Path | Use Case |
|--------|------|----------|
| **Bundled** | `<repo>/plugins/` | Ships with Hermes |
| **User** | `~/.hermes/plugins/` | Personal plugins |
| **Project** | `.hermes/plugins/` | Project-specific (requires `HERMES_ENABLE_PROJECT_PLUGINS=true`) |
| **pip** | `hermes_agent.plugins` entry_points | Distributed packages |
| **Nix** | `services.hermes-agent.extraPlugins` / `extraPythonPackages` | NixOS declarative installs |

### Plugin Sub-Categories

| Sub-Directory | What It Holds | Discovery System |
|---------------|---------------|------------------|
| `plugins/` (root) | General plugins — tools, hooks, slash commands, CLI commands, bundled skills | `PluginManager` (kind: `standalone` or `backend`) |
| `plugins/platforms/<name>/` | Gateway channel adapters (`ctx.register_platform()`) | `PluginManager` (kind: `platform`) |
| `plugins/image_gen/<name>/` | Image generation backends | `PluginManager` (kind: `image_gen`) |
| `plugins/video_gen/<name>/` | Video generation backends | `PluginManager` (kind: `video_gen`) |
| `plugins/memory/<name>/` | Memory backends (subclass `MemoryProvider`) | `MemoryManager` |
| `plugins/model-providers/<name>/` | LLM provider backends | `ProviderRegistry` |

---

## plugin.yaml Schema

```yaml
name: my-plugin
version: "1.0.0"
description: What this plugin does
author: Your Name
license: MIT
requires_env:
  - MY_API_KEY  # Optional: env vars required for install
# Optional: minimum Hermes version
min_hermes_version: "0.12.0"
# Optional: python version constraint
python: ">=3.10"
```

---

## Common Patterns

### Tool with Config
```python
def register(ctx):
    # Access config via ctx.config
    api_key = ctx.config.get("my-plugin.api_key")
    base_url = ctx.config.get("my-plugin.base_url", "https://api.example.com")
```

Config in `~/.hermes/config.yaml`:
```yaml
my-plugin:
  api_key: "secret"
  base_url: "https://api.example.com"
```

### Skill Bundle
```python
def register(ctx):
    ctx.register_skill(
        name="my-skill",
        path=Path(__file__).parent / "skills" / "my-skill"
    )
```

Accessed as: `skill_view("my-plugin:my-skill")`

### CLI Command
```python
def register(ctx):
    def setup(parser):
        parser.add_argument("target", help="Target to process")

    def handler(args):
        print(f"Processing {args.target}")
        return {"processed": args.target}

    ctx.register_cli_command(
        name="process",
        help="Process a target",
        setup_fn=setup,
        handler_fn=handler,
    )
```

Usage: `hermes my-plugin process my-target`

---

## Installing & Managing Plugins

```bash
# Browse available plugins
hermes plugins browse

# Install from hub
hermes plugins install owner/plugin-name

# Install from local path
hermes plugins install ./my-plugin

# List installed
hermes plugins list

# Update
hermes plugins update [name]

# Uninstall
hermes plugins uninstall name

# Check for issues
hermes plugins check
```

---

## Security Notes

- Plugins run **in the same process** as Hermes — they have full access to your environment
- Only install plugins from trusted sources
- Run `hermes plugins check` before installing third-party plugins
- Project plugins (`.hermes/plugins/`) require explicit opt-in via `HERMES_ENABLE_PROJECT_PLUGINS=true`