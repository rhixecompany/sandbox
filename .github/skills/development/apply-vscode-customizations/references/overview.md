# apply_vscode_customizations.py — Overview

## Purpose
Applies VS Code customizations from templates to the user's VS Code settings files. This script reads predefined customization templates (themes, keybindings, editor settings, extension recommendations) and merges them into the VS Code `settings.json` and `keybindings.json` files located in the VS Code user data directory.

## Usage

```bash
python apply_vscode_customizations.py [--template NAME] [--dry-run] [--backup] [--list-templates] [--target PATH]
```

### Options

| Option            | Description                                                   |
|------------------|---------------------------------------------------------------|
| `--template`     | Name of the customization template to apply                  |
| `--list-templates` | List all available customization templates                    |
| `--dry-run`      | Preview changes without modifying files                       |
| `--backup`       | Create a timestamped backup of existing settings              |
| `--target`       | Custom path to VS Code user data directory                    |

## Behavior

- Locates the VS Code user settings directory automatically (Windows: `%APPDATA%\Code\User\`, macOS/Linux: `~/.config/Code/User/`).
- Reads the specified template from the `templates/` subdirectory.
- Merges new settings with existing ones — existing settings are preserved unless explicitly overridden by the template.
- Validates JSON structure before writing to avoid corrupting VS Code settings.
- Supports partial application (only theme, only keybindings, etc.).

## Example

**Apply the standard Hermes customization template:**
```bash
python apply_vscode_customizations.py --template hermes-standard
```

**Preview what would change:**
```bash
python apply_vscode_customizations.py --template dark-theme --dry-run
```

**Backup existing settings first:**
```bash
python apply_vscode_customizations.py --template hermes-standard --backup
```

## Dependencies

- Python 3.7+
- No external package dependencies (uses stdlib `json`, `shutil`, `pathlib`)

## See Also

- VS Code settings documentation: https://code.visualstudio.com/docs/getstarted/settings
- Hermes VS Code integration guide