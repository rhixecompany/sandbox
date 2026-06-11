# Plugin Commands Reference

## Management
```bash
hermes plugins list           # List installed plugins
hermes plugins enable <name>  # Enable plugin
hermes plugins disable <name> # Disable plugin
hermes plugins info <name>    # Show plugin info
```

## Configuration (config.yaml)
```yaml
plugins:
  enabled:
    - disk-cleanup
    - model-providers/openrouter
    - security-guidance
    - memory/honcho
  disabled: []
```

## Model Provider (OpenRouter)
```yaml
model:
  provider: openrouter
  openrouter:
    api_key: "${OPENROUTER_API_KEY}"
    model: "anthropic/claude-3.5-sonnet"
```

## Memory Provider (Honcho)
```yaml
memory:
  provider: honcho
  honcho:
    api_key: "${HONCHO_API_KEY}"
    workspace: "my-project"
```

## Manual Installation
```bash
git clone https://github.com/example/hermes-plugin-xyz ~/.hermes/plugins/xyz
# Add to config.yaml enabled list
# Restart Hermes
```

## Development Installation
```bash
ln -s /path/to/your/plugin ~/.hermes/plugins/my-plugin
```