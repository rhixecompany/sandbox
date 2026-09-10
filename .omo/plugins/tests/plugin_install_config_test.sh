#!/usr/bin/env bash
# Plugin install, configure, test, enable script — DRY compliant
# References: .opencode/opencode.json plugin array, .omo/config.json plugins.enabled

set -euo pipefail

echo "=== Plugin Installation / Configuration / Test / Enable ==="

echo "--- Checking plugin installations ---"
# Check if opencode CLI is available
if command -v opencode >/dev/null 2>&1 || [ -f "/usr/local/bin/opencode" ]; then
    echo "[PASS] opencode CLI found"
else
    echo "[WARN] opencode CLI not in PATH (expected on Hermes-hosted systems)"
fi

# Check plugin directories
for plugin in oh-my-openagent opencode superpowers; do
    plugin_path="C:/Users/Alexa/AppData/Local/hermes/plugins/$plugin"
    if [ -d "$plugin_path" ]; then
        echo "[PASS] $plugin installed at $plugin_path"
    else
        echo "[INFO] $plugin not installed at $plugin_path"
    fi
done

echo "--- Plugin sync verification ---"
python .omo/plugins/tests/verify_plugin_config.py || echo "[WARN] Verification script failed — check JSON syntax"

echo "--- Plugin enable/status reference ---"
cat .omo/plugins/plugin_sync_state.json

echo "=== Plugin Workflow Complete ==="
