# DRY Best Practices — OpenCode / OMO Workspace

## Principles
- Don't Repeat Yourself: One source of truth for model config (`.opencode/opencode.json` + `.omo/config.json`)
- Shared plugin array: Plugins listed in `.opencode/opencode.json` plugin array and `.omo/config.json` plugins.enabled must stay in sync
- Use `.omo/templates/` for reusable patterns
- Config inheritance: `.hermes.md` → `.opencode/opencode.json` → `.omo/config.json`

## Model Routing (DRY)
Primary: openrouter/nvidia/nemotron-3-ultra-550b-a55b:free (best for accuracy)
Reasoning: openrouter/thinkingmachines/inkling:free (deep reasoning)
Fast: openrouter/deepseek/deepseek-v4-flash-free (speed)

## Context & Compaction (DRY)
- `.opencode/opencode.json` defines `context_size`, `compaction`
- `.omo/config.json` references the same values; keep in sync
- Never duplicate settings — import/reference instead

## Plugin Management (DRY)
- Plugin spec in `.opencode/opencode.json` `plugin` array
- Plugin list in `.omo/config.json` `plugins.enabled`
- Use `.omo/templates/` for common plugin patterns
