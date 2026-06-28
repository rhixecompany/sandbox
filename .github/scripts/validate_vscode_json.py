import os
import json
import glob

# Find all .vscode folders and JSON files
sandbox_root = r"C:/Users/Alexa/Desktop/SandBox"

def validate_json(file_path):
    """Validate a JSON file and return errors"""
    errors = []
    try:
        with open(file_path) as f:
            content = f.read()
        # Try to parse - will fail if comments in strict JSON
        try:
            json.loads(content)
        except json.JSONDecodeError as e:
            errors.append(f"JSON parse error: {e}")
    except Exception as e:
        errors.append(f"Read error: {e}")
    return errors

# Find all .vscode JSON files
results = []
for root, dirs, files in os.walk(sandbox_root):
    # Skip .git and node_modules
    if ".git" in root or "node_modules" in root:
        continue
    if ".vscode" in dirs:
        vscode_path = os.path.join(root, ".vscode")
        for f in os.listdir(vscode_path):
            if f.endswith(".json"):
                file_path = os.path.join(vscode_path, f)
                rel_path = os.path.relpath(file_path, sandbox_root)
                errors = validate_json(file_path)
                status = "✓ VALID" if not errors else "✗ INVALID"
                results.append((rel_path, status, errors))
                print(f"{status}: {rel_path}")

# Summary
valid_count = sum(1 for r in results if r[1] == "✓ VALID")
invalid_count = len(results) - valid_count
print(f"\n{'='*50}")
print(f"Total: {len(results)} JSON files")
print(f"Valid: {valid_count}")
print(f"Invalid: {invalid_count}")

if invalid_count > 0:
    print("\nInvalid files need correction:")
    for rel_path, status, errors in results:
        if status == "✗ INVALID":
            for err in errors:
                print(f"  {rel_path}: {err}")