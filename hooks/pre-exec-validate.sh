#!/usr/bin/env bash
# pre-exec-validate — Syntax/formatting validation hook
# Runs before file writes to catch malformed output early.
# Source this from other hooks or invoke directly with file paths.
set -euo pipefail

validate_python() {
    local file="$1"
    if python3 -c "import py_compile; py_compile.compile('$file', doraise=True)" 2>/dev/null; then
        return 0
    else
        echo "[VALIDATE] Python syntax error in $file" >&2
        python3 -m py_compile "$file" 2>&1 | head -5 >&2
        return 1
    fi
}

validate_json() {
    local file="$1"
    if python3 -c "import json; json.load(open('$file'))" 2>/dev/null; then
        return 0
    else
        echo "[VALIDATE] JSON parse error in $file" >&2
        python3 -c "import json; json.load(open('$file'))" 2>&1 | head -3 >&2
        return 1
    fi
}

validate_yaml() {
    local file="$1"
    if python3 -c "import yaml; yaml.safe_load(open('$file'))" 2>/dev/null; then
        return 0
    else
        echo "[VALIDATE] YAML parse error in $file" >&2
        python3 -c "import yaml; yaml.safe_load(open('$file'))" 2>&1 | head -3 >&2
        return 1
    fi
}

# If invoked with a file argument, validate it
if [[ $# -gt 0 ]]; then
    file="$1"
    case "$file" in
        *.py) validate_python "$file" ;;
        *.json) validate_json "$file" ;;
        *.yaml|*.yml) validate_yaml "$file" ;;
        *)
            # Unrecognized extension — skip validation
            exit 0
            ;;
    esac
fi
