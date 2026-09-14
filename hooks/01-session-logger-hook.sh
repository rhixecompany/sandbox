#!/usr/bin/env bash
# session-logger hook — thin wrapper, delegates to async Python.
set -euo pipefail
# Resolve hook directory without `dirname` (external command may be off PATH
# in Hermes's hook execution environment on Windows). Pure bash builtins.
HOOK_DIR="${BASH_SOURCE[0]%/*}"
if command -v cygpath &>/dev/null; then
    HOOK_DIR=$(cygpath -w "$HOOK_DIR" 2>/dev/null || echo "$HOOK_DIR")
elif pwd -W &>/dev/null; then
    HOOK_DIR="$( cd "$HOOK_DIR" &>/dev/null && pwd -W )"
fi
HOOK_DIR=${HOOK_DIR//\\//}
# Locate python: PATH first, then Hermes venv as absolute fallback.
if command -v python3 &>/dev/null; then
    PY=python3
elif command -v python &>/dev/null; then
    PY=python
elif [ -x "/c/Users/Alexa/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe" ]; then
    PY="/c/Users/Alexa/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe"
else
    echo "[ERROR] session-logger: python3/python not found on PATH" >&2
    exit 1
fi
exec "$PY" "$HOOK_DIR/hook.py"
