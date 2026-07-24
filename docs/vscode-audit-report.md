# VS Code Configuration Audit Report

## Summary
- Workspace: `C:\Users\Alexa\Desktop\SandBox`
- Formatter conflicts: 0 (96 intentional formatter-override warnings — global + per-language pattern)
- Hardcoded paths: 0
- Missing configs: 0
- Stack mismatches: 0

## Validation (2026-07-24)
- `audit_vscode_config.py`: passed with 0 issues.
- `validate_vscode_configs.py`: passed, 119 files scanned, 0 failures, 96 warnings (expected).
- `validate_vscode_json.py`: passed, 119 files scanned, 0 failures.

## Notes
- Warnings reported by `validate_vscode_configs.py` are formatter-preference suggestions, not syntax errors.
- The 96 warnings are intentional: each `settings.json` uses a global default formatter with per-language overrides (e.g., `[json]`/`[jsonc]` use `vscode.json-language-features`, not Prettier). This is the recommended VS Code pattern.
- `node_modules/` paths are excluded from validation scripts to avoid vendor-file false failures.
- All 21 subdirectories have `.vscode/` with `settings.json`, `extensions.json`, `launch.json`, `tasks.json` (plus `mcp.json` at root).
