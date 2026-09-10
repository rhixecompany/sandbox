# DRY Best Practices — Workspace Enhancement

## Reference Config Mapping

| Config Layer | Source of Truth | References |
|---|---|---|
| Workspace global | `.opencode/opencode.json` | Plugins, models, context, compaction |
| OMO layer | `.omo/config.json` | Agent routing, plugins, performance, quality |
| Plugin sync | `.omo/plugins/plugin_sync_state.json` | Non-destructive verification |
| References | `.omo/templates/reference_config.json` | All settings at a glance |

## DRY In Practice

- **One plugin array** → `.opencode/opencode.json` `plugin` array is canonical; `.omo/config.json` references it.
- **One model definition** → `.opencode/opencode.json` `model` / `small_model`; `.omo/config.json` uses same providers.
- **One verification script** → `.omo/plugins/tests/verify_plugin_config.py` covers both config files.
- **One verification bash script** → `.omo/plugins/tests/verify_plugins.sh` runs syntax checks non-destructively.
- **No duplicated settings** → Context, compaction, quality, performance settings live in `.opencode/` and are referenced by `.omo/`.
- **Reference docs** → `.omo/templates/DRY_BEST_PRACTICES.md` explains the inheritance rules.

## Plugin Enablement Checklist

For each plugin in the `plugin_sync_state.json`:
- [x] Listed in `.opencode/opencode.json`
- [x] Referenced in `.omo/config.json` `plugins.enabled`
- [x] Verify command exists in `plugin_sync_state.json`
- [x] Non-destructive test script verifies load (`verify_plugin_config.py`)
- [x] Plugin state tracked (`plugin_sync_state.json`)

## Model Routing (Single Source)

- `primary`: openrouter/nvidia/nemotron-3-ultra-550b-a55b:free
- `reasoning`: openrouter/thinkingmachines/inkling:free
- `fast`: openrouter/deepseek/deepseek-v4-flash-free
- `vision`: openrouter/nvidia/nemotron-3-ultra-550b-a55b:free

This routing is defined once in `.omo/config.json` and aligns with `.opencode/opencode.json`.
