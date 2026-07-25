# VS Code Config Audit Scripts

## ESLint Mismatch Detection (Monorepo-Wide)

Detects `settings.json` files that have `source.fixAll.eslint` in `codeActionsOnSave` but don't have `dbaeumer.vscode-eslint` in their `extensions.json` recommendations.

```python
import os, json

sandbox_root = r"C:/Users/Alexa/Desktop/SandBox"
mismatches = []

for root, dirs, files in os.walk(sandbox_root):
    if ".git" in root or "node_modules" in root:
        continue
    if ".vscode" not in dirs:
        continue
    
    vscode_path = os.path.join(root, ".vscode")
    settings_path = os.path.join(vscode_path, "settings.json")
    ext_path = os.path.join(vscode_path, "extensions.json")
    
    if not os.path.exists(settings_path):
        continue
    
    with open(settings_path) as f:
        settings = json.load(f)
    
    cas = settings.get("editor", {}).get("codeActionsOnSave", {})
    if "source.fixAll.eslint" not in cas:
        continue
    
    has_eslint_ext = False
    if os.path.exists(ext_path):
        with open(ext_path) as f:
            exts = json.load(f)
        recs = exts.get("recommendations", [])
        has_eslint_ext = any("eslint" in r for r in recs)
    
    if not has_eslint_ext:
        rel = os.path.relpath(settings_path, sandbox_root)
        mismatches.append(rel)

for m in mismatches:
    print(f"MISMATCH: {m}")
print(f"\nTotal: {len(mismatches)}")
```

## JSON Validation (All .vscode Files)

```python
import os, json

sandbox_root = r"C:/Users/Alexa/Desktop/SandBox"
errors = []

for root, dirs, files in os.walk(sandbox_root):
    if ".git" in root:
        continue
    if ".vscode" not in dirs:
        continue
    vscode_path = os.path.join(root, ".vscode")
    for f in os.listdir(vscode_path):
        if not f.endswith(".json"):
            continue
        fp = os.path.join(vscode_path, f)
        try:
            with open(fp) as fh:
                json.load(fh)
        except json.JSONDecodeError as e:
            errors.append(f"{fp}: {e}")

if errors:
    for e in errors:
        print(f"INVALID: {e}")
else:
    print("All JSON files valid")
```

## Key Pitfall: Audit Script Stale Data

When writing audit scripts that check file contents AFTER edits, always re-read the file from disk. Do NOT cache file content in variables and re-use the cached version after writing changes. The `read_file` tool also deduplicates — if you call it on the same unchanged file multiple times, it returns a "BLOCKED" error. Workaround: use `terminal` + `python3 -c "..."` or `grep` to extract specific sections instead.