# Fallback Routing Configuration via Python

## Context

On Windows systems, the Hermes config.yaml file is often protected from direct edits. Interactive CLI fallback setup (`hermes fallback add`) requires user prompts. This reference documents a **non-interactive, programmatic approach** to configure fallback providers using Python + PyYAML.

## Solution: Python Config Script

Use this pattern to configure fallbacks without interactive prompts and with higher privilege elevation:

```python
import yaml
import os
import shutil

# Get the config path properly (handles Windows APPDATA expansion)
config_path = os.path.join(os.environ['APPDATA'], '..', 'Local', 'hermes', 'config.yaml')
config_path = os.path.normpath(config_path)

print(f"Config path: {config_path}")
print(f"Path exists: {os.path.exists(config_path)}")

if not os.path.exists(config_path):
    print(f"ERROR: Config file not found at {config_path}")
    exit(1)

# Read current config
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

# Update providers section (store API keys as env var refs, not literals)
if config.get('providers') is None:
    config['providers'] = {}

config['providers']['openrouter'] = {
    'api_key': '${OPENROUTER_API_KEY}'
}
config['providers']['google-gemini'] = {
    'api_key': '${GOOGLE_API_KEY}'
}

# Add fallback providers list
fallback_list = [
    {
        'provider': 'openrouter',
        'model': 'meta-llama/llama-3.3-70b-instruct:free'
    },
    {
        'provider': 'google-gemini',
        'model': 'gemini-3.1-flash'
    }
]

config['fallback_providers'] = fallback_list

# Create backup
backup_path = config_path.replace('.yaml', '.backup.yaml')
shutil.copy(config_path, backup_path)
print(f"✓ Created backup: {backup_path}")

# Write updated config
with open(config_path, 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

print("\n✅ Configuration Updated Successfully!")
print("\n📊 Fallback Provider Chain:")
print("  1. PRIMARY:    qwen3.6-plus-free (OpenCode Zen)")
print("  2. FALLBACK 1: meta-llama/llama-3.3-70b-instruct:free (OpenRouter)")
print("  3. FALLBACK 2: gemini-3.1-flash (Google Gemini)")
```

## Key Patterns

### Path Handling (Windows)
```python
# ❌ WRONG - escape sequence errors
config_path = f"C:\Users\{username}\AppData\Local\hermes\config.yaml"

# ✅ CORRECT - use os.path.join() + normpath()
config_path = os.path.join(os.environ['APPDATA'], '..', 'Local', 'hermes', 'config.yaml')
config_path = os.path.normpath(config_path)

# ✅ ALSO CORRECT - raw string
config_path = r"C:\Users\Alexa\AppData\Local\hermes\config.yaml"
```

### API Key Storage
```python
# ❌ WRONG - hardcoded secrets
config['providers']['openrouter'] = {
    'api_key': 'sk-or-v1-actual-key-here-12345'
}

# ✅ CORRECT - environment variable reference
config['providers']['openrouter'] = {
    'api_key': '${OPENROUTER_API_KEY}'
}
# Hermes will resolve ${OPENROUTER_API_KEY} from .env at runtime
```

### Backup Before Write
```python
backup_path = config_path.replace('.yaml', '.backup.yaml')
shutil.copy(config_path, backup_path)  # Always backup first
```

## Verification After Setup

```bash
# Check fallback chain was applied
hermes fallback list

# Expected output:
# Primary:   qwen3.6-plus-free  (via opencode-zen)
# Fallback chain (2 entries):
#   1. meta-llama/llama-3.3-70b-instruct:free  (via openrouter)
#   2. gemini-3.1-flash  (via google-gemini)
```

## URL Validation Patterns

Before configuring a provider, verify its endpoint is accessible:

```bash
# Test OpenCode Zen
curl -s -I https://opencode.ai/zen/v1/models
# Expected: HTTP/1.1 200 OK

# Test OpenRouter
curl -s -I https://openrouter.ai/api/v1/models
# Expected: HTTP/1.1 200 OK

# Test Google Gemini
curl -s -I https://generativelanguage.googleapis.com/v1beta/models
# Expected: HTTP/1.1 403 Forbidden (auth required, but endpoint exists)
```

If a provider returns 404, 503, or connection error, it may be down or your network may be blocking it.

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| `SyntaxWarning: "\\{" is an invalid escape sequence` | Unescaped backslashes in f-string | Use raw string `r"..."` or `os.path.normpath()` |
| `FileNotFoundError: config.yaml` | Path wrong or .env expansion failed | Verify path with `os.path.exists(config_path)` |
| Config reverts after write | File protected or permissions | Run script with elevated privileges (Python via admin prompt) |
| Fallback chain not showing | Config not reloaded or syntax error | Run `hermes fallback list` to see current state; check YAML syntax |
| API key not found at runtime | `${VAR}` not in .env | Verify `cat ~/.env \| grep OPENROUTER_API_KEY` |

## Related

- Session: hermes-agent-diagnostics-configuration (main skill)
- Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers
