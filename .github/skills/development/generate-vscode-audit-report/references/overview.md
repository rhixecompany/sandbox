# generate_vscode_audit_report.py — Overview

## Purpose
Generates comprehensive visual audit reports for VS Code configurations. This script takes the output of VS Code configuration audits and produces formatted reports (HTML, Markdown, or JSON) with visualized issue breakdowns, severity summaries, and actionable recommendations.

## Usage

```bash
python generate_vscode_audit_report.py [--audit-file PATH] [--output FORMAT] [--report FILE] [--html] [--open] [--style THEME] [--filter SEVERITY] [--group-by CATEGORY]
```

### Options

| Option         | Description                                                    |
|---------------|----------------------------------------------------------------|
| `--audit-file`| Path to the audit data JSON file (from `audit_vscode_config.py`) |
| `--output`    | Output format: `html`, `markdown`, `json`, `pdf`               |
| `--report`   | Path to save the generated report                              |
| `--html`     | Shortcut for HTML output (equivalent to `--output html`)       |
| `--open`     | Open the report in the default browser after generation         |
| `--style`    | Report theme: `light`, `dark`, `minimal` (default: `light`)     |
| `--group-by`  | Group issues by: `category`, `severity`, `file` (default: `category`) |
| `--verbose` | Include detailed per-setting recommendations in the report        |

## Behavior

- Reads the audit data from a JSON file produced by `audit_vscode_config.py` or `audit_vscode_config_v2.py`.
- Organizes findings into groups (deprecations, misconfigurations, missing extensions, etc.).
- Generates a visual report with summary tables, severity heatmaps, and per-section breakdowns.
- Markdown output uses readable tables and checklists suitable for PRs or documentation.
- HTML output includes collapsible sections, color-coded severity indicators, and optional auto-open in browser.
- Includes a recommendations section with links to VS Code docs for each issue type.

## Example

**Generate an HTML report from an audit file:**
```bash
python generate_vscode_audit_report.py --input-file vscode_audit.json --html --report vscode_report.html --open
```

**Generate a Markdown report for documentation:**
```bash
python generate_vscode_audit_report.py --input-file vscode_audit.json --output markdown --report vscode_audit_report.md
```

**Group issues by severity with dark theme:**
```bash
python generate_vscode_audit_report.py --input-file audit.json --html --style dark --group-by severity
```

## Dependencies

- Python 3.7+
- No external dependencies for Markdown/JSON output
- For HTML/PDF output: `jinja2` (recommended)

## See Also

- `audit-vscode-config` and `audit-vscode-config-v2` skills
- VS Code configuration best practices