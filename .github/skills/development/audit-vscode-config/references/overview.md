# audit_vscode_config.py — Overview

## Purpose
Audits VS Code configuration files (`settings.json`, `keybindings.json`, `extensions.json`) for issues, inconsistencies, and compliance with best practices. This script checks for deprecated settings, misconfigured values, missing recommended extensions, and conflicts between user and workspace settings.

## Usage

```bash
python audit_vscode_config.py [--config-dir PATH] [--output FORMAT] [--report FILE] [--check-extensions] [--verbose]
```

### Options

| Option              | Description                                                   |
|--------------------|---------------------------------------------------------------|
| `--config-dir`     | Path to VS Code user config directory (auto-detected if omitted) |
| `--output`         | Output format: `terminal`, `json`, `markdown`              |
| `--report`        | Save the audit report to a file                               |
| `--check-extensions` | Verify installed extensions against a recommended list        |
| `--verbose`       | Show detailed per-setting analysis                            |

## Behavior

- Locates VS Code config directory automatically (Windows: `%APPDATA%\Code\User\`, macOS: `~/Library/Application Support/Code/User/`, Linux: `~/.config/Code/User/`).
- Parses `settings.json` and validates values against known types and ranges.
- Detects deprecated settings (settings removed in recent VS Code versions).
- Flags settings that conflict with Hermes recommended defaults.
- When `--check-extensions` is active, compares installed extensions against a reference list and reports missing or unneeded extensions.
- Outputs a categorized summary by severity.

## Example

**Basic audit with terminal output:**
```bash
python audit_vscode_config.py
```

**Full audit with extension check and JSON report:**
```bash
python audit_vscode_config.py --check-extensions --output json --report vscode_audit.json
```

**Audit a custom config directory:**
```bash
python audit_vscode_config.py --config-dir ./config/Code/User
```

## Dependencies

- Python 3.7+
- No external dependencies (uses stdlib `json`, `pathlib`)

## See Also

- VS Code settings reference: https://code.visualstudio.com/docs/reference/settings/
- `apply-vscode-customizations` skill