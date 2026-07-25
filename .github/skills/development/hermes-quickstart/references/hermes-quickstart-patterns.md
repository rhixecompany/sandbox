# Hermes Quickstart Patterns

## Installation Verification

```bash
hermes --version
# hermes 1.x.x
```

## Provider Configuration

```bash
hermes config set provider.openrouter.api_key YOUR_KEY
hermes config set provider.openrouter.model anthropic/claude-3.5-sonnet
```

## TUI Launch

```bash
hermes --tui
```

## Slash Commands

| Command | Purpose |
|---------|---------|
| `/help` | Show all commands |
| `/skills` | List/manage skills |
| `/profile` | Switch profiles |
| `/config` | View/edit config |
| `/memory` | View memory files |
| `/session` | Session management |

## Basic Workflow

1. Configure provider: `hermes config set provider.<name>.api_key <key>`
2. Test connection: Send a message in TUI
3. Load skills: `/skill load <name>`
4. Create cron: `/cron create "daily briefing" "0 9 * * *"`
5. Check memory: `/memory view`

## Profile Switching

```bash
hermes profile use code-architect
hermes profile use research-analyst
```

## Config File Location

```
~/.hermes/config.yaml          # Default profile
~/.hermes/profiles/<name>/     # Per-profile config
```

## Error Handling

```python
# Common errors and resolutions
ERRORS = {
    "provider_not_configured": "Run: hermes config set provider.<name>.api_key <key>",
    "model_not_found": "Check model name with: hermes auth list --provider <name>",
    "skill_not_found": "Install skill: hermes skill install <name>",
    "memory_limit_exceeded": "Consolidate MEMORY.md (2200 chars) or USER.md (1375 chars)",
    "profile_not_found": "List profiles: hermes profile list",
}
```

## Platform Detection

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "darwin":
        return "macos"
    elif system == "linux":
        return "linux"
    return "unknown"

# Usage in skills
if get_platform() == "windows":
    # Windows paths: C:\Users\...
    path = r"C:\Users\{username}\AppData\Local\hermes"
else:
    # Unix paths: /home/... or ~/.hermes
    path = "~/.hermes"
```