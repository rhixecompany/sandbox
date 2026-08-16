#!/usr/bin/env bash
# install-pathutil.sh — Copy _pathutil.py into scripts/ and hooks/ directories
# Run after updating the canonical copy bundled with this skill.
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/AppData/Local/hermes}"

if command -v cygpath &>/dev/null; then
    SKILL_DIR=$(cygpath -w "$SKILL_DIR" 2>/dev/null || echo "$SKILL_DIR")
    HERMES_HOME=$(cygpath -w "$HERMES_HOME" 2>/dev/null || echo "$HERMES_HOME")
fi

echo "Installing _pathutil.py..."
cp "$SKILL_DIR/scripts/_pathutil.py" "$HERMES_HOME/scripts/_pathutil.py"
cp "$SKILL_DIR/scripts/_pathutil.py" "$HERMES_HOME/hooks/_pathutil.py"
echo "Installed to scripts/ and hooks/"
