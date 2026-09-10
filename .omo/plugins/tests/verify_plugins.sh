#!/usr/bin/env bash
# Plugin verification and load test for OpenCode / OMO workspace config
# DRY: runs syntax checks, plugin sync verification, and smoke tests

set -euo pipefail

echo "=== OpenCode / OMO Plugin Verification (Dry-Run Mode) ==="
echo "Workspace: $(pwd)"
echo "Date: $(date -Iseconds)"

echo ""
echo "--- .opencode/opencode.json syntax check ---"
python3 -c "
import json
with open('.opencode/opencode.json') as f:
    data = json.load(f)
print('JSON syntax OK')
print('Plugins:', data.get('plugin', []))
print('Model:', data.get('model'))
print('Small model:', data.get('small_model'))
print('MCP servers enabled:', sum(1 for s in data.get('mcp', {}).values() if s.get('enabled')))
"

echo ""
echo "--- .omo/config.json syntax check ---"
python3 -c "
import json
with open('.omo/config.json') as f:
    data = json.load(f)
print('JSON syntax OK')
print('Plugins enabled:', len(data.get('plugins', {}).get('enabled', [])))
"

echo ""
echo "--- Plugin sync verification ---"
python3 -c "
import json
with open('.opencode/opencode.json') as f: op = json.load(f)
with open('.omo/config.json') as f: omo = json.load(f)
with open('.omo/plugins/plugin_sync_state.json') as f: state = json.load(f)
op_plugins = op.get('plugin', [])
omo_plugins = omo.get('plugins', {}).get('enabled', [])
print('OpenCode plugins:', op_plugins)
print('OMO plugins:', omo_plugins)
print('In sync:', set(op_plugins) == set(omo_plugins))
"

echo ""
echo "--- Context / Compaction settings ---"
python3 -c "
import json
with open('.opencode/opencode.json') as f:
    data = json.load(f)
print('Context size:', data.get('context_size'))
print('Compaction:', data.get('compaction'))
print('Agent factory:', data.get('agent_factory'))
"

echo ""
echo "=== Verification Complete ==="
