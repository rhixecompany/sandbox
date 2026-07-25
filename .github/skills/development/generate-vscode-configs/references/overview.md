# generate_vscode_configs.py — Overview

## Purpose
Generates VS Code configuration files from templates. This script creates or regenerates `settings.json`, `keybindings.json`, and `extensions.json` files using predefined templates that align with Hermes agent workflow preferences and development best practices.

## Usage

```bash
python generate_vscode_configs.py [--template NAME] [--output-dir PATH] [--format FORMAT] [--include] [--dry-run] [--list-templates] [--overwrite]
```

### Options

| Option          | Description                                                    |
|----------------|----------------------------------------------------------------|
| `--template`   | Configuration template to use (e.g., `hermes-dev`, `minimal`, `full`) |
| `--output-dir` | Output directory (default: VS Code user config dir)            |
| `--format`     | Config file format: `json`, `jsonc` (default: `json`)          |
| `--include`    | Which configs to generate: `settings`, `keybindings`, `extensions`, `all` (default: `all`) |
| `--dry-run`    | Show what files would be generated without writing them        |
| `--list-templates` | List available configuration templates                    |
| `--overwrite`  | Overwrite existing config files without prompting              |

## Behavior

- Locates the VS Code user config directory automatically (cross-platform).
- Supports multiple templates: `hermes-agent` (preferred for Hermes users), `minimal` (bare essentials), `full` (all settings with descriptions).
- For each config type, generates a properly formatted JSON/JSONC file with extensive in-line comments (JSONC format) or readme-only (JSON format).
- Settings include: editor font, theme, format-on-save, auto-completion, terminal config, and language-specific overrides.
- Extensions generate a recommended extensions list that can be used with VS Code's `extensions.json`.
- Backs up any existing config before overwriting (unless `--overwrite` is set).

## Example

**Generate Hermes-agent template for VS Code:**
```bash
python generate_vscode_configs.py --template hermes-agent
```

**Generate only settings to a custom directory:**
```bash
python generate_vscode_configs.py --template minimal --include settings --output-dir ./vscode-config
```

**List available templates:**
```bash
python generate_vscode_configs.py --list-templates
```

## Dependencies

- Python 3.7+
- No external dependencies

## See Also

- `apply-vscode-customizations` — apply generated configs
- `audit-vscode-config` — audit existing configs for issues