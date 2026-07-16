# VS Code Configuration Audit Report

## Summary
- Workspace: `C:\Users\Alexa\Desktop\SandBox`
- Formatter conflicts: 0
- Hardcoded paths: 0
- Missing configs: 0
- Stack mismatches: 0

## Validation
- `audit_vscode_config.py`: passed with 0 issues.
- `validate_vscode_configs.py`: passed, 127 files scanned, 0 failures.
- `validate_vscode_json.py`: passed, 127 files scanned, 0 failures.

## Notes
- Warnings reported by `validate_vscode_configs.py` are formatter-preference suggestions, not syntax errors.
- `node_modules/` paths are excluded from the validation scripts so dependency vendor files do not cause false failures.
- The audit script bug that produced false ESLint mismatches was fixed in `C:\Users\Alexa\AppData\Local\hermes\scripts\audit_vscode_config.py`.
