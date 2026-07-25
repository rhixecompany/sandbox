# audit_vscode_config_v2.py — Overview

## Purpose
Enhanced version of the VS Code configuration audit with extended checks, deeper analysis, and improved reporting. This script audits `settings.json`, `keybindings.json`, and VS Code workspace files with additional capabilities: theme compliance, telemetry settings audit, security configuration validation, and extension marketplace compliance.

## Usage

```bash
python audit_vscode_config_v2.py [--config-dir PATH] [--workspace-dir PATH] [--output FORMAT] [--report FILE] [--full] [--policy FILE] [--ci]
```

### Options

| Option           | Description                                                    |
|----------------|----------------------------------------------------------------|
| `--config-dir` | Path to VS Code user config directory                          |
| `--workspace-dir` | Path to workspace `.vscode/` directory to audit workspace configs |
| `--output`     | Output format: `terminal`, `json`, `html`, `markdown`         |
| `--report`     | Save the full report to a file                                 |
| `--full`       | Run all audit checks (takes longer but more thorough)             |
| `--check`      | Path to a custom compliance policy YAML file                    |
| `--ci`         | CI mode — exit with non-zero code if any issues found          |

## Behavior

- All checks from the v1 audit are included, plus the following enhancements:
- Cross-workspace setting drift detection — flags when active workspace settings diverge from user defaults.
- Telemetry and privacy configuration check (verifies `telemetry.enableCrashReporter`, `telemetry.telemetryLevel`).
- Extension recommendation verification — compares against a curated list of AI/developer tools.
- Security audit of `security.workspace.trust`, `security.allowedUNCHosts`, and similar.
- Reports JSON and HTML with severity drill-downs suitable for team dashboards.

## Example

**Full audit with all checks:**
```bash
python audit_vscode_config_v2.py --full
```

**CI pipeline usage:**
```bash
python audit_vscode_config_v2.py --ci --workspace-dir .vscode --output json --report audit_report.json
```

**Audit with a custom compliance policy:**
```bash
python audit_vscode_config_v2.py --check team-compliance.yaml
```

## Dependencies

- Python 3.8+
- `pyyaml` (for compliance policy parsing)

## See Also

- VS Code security settings: https://code.visualstudio.com/docs/editor/workspace-trust
- `audit-vscode-config` skill (v1)