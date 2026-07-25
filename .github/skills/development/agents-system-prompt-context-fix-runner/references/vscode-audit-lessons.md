# VS Code audit lessons from mixed-workspace runs

## Verified lesson
When walking a workspace for `.vscode` JSON files, exclude generated/vendor trees before validation:
- `node_modules`
- `.git`
- `.next`
- `dist`
- `build`
- `coverage`
- `out`
- `.venv`
- `venv`
- `__pycache__`

Without this filter, vendored dependency trees can produce false failures unrelated to the workspace’s real configs.

## Validation rule
Treat formatter mismatches as warnings unless the task explicitly asks for a strict policy. Fail only on invalid JSON or missing required files.

## Mixed-workspace doc layout
When generating architecture/folder/tech-stack blueprints for many projects, namespace per-project docs by relative project path under `docs/Project_Architecture/` so root-level and nested projects do not collide.

## Verified commands
- `python "C:/Users/Alexa/AppData/Local/hermes/scripts/audit_vscode_config.py" --workspace "C:/Users/Alexa/Desktop/SandBox"`
- `python "C:/Users/Alexa/AppData/Local/hermes/scripts/validate_vscode_configs.py" --workspace "C:/Users/Alexa/Desktop/SandBox"`
- `python "C:/Users/Alexa/AppData/Local/hermes/scripts/validate_vscode_json.py" --workspace "C:/Users/Alexa/Desktop/SandBox"`
