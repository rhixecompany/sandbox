# .github/plugins/ — Not Hermes Plugins

## Summary
The `.github/plugins/` directory contains **46 Copilot agent configurations**, not Hermes plugins. They lack the required `plugin.yaml` manifest and contain Copilot-specific structures (`agents/`, `commands/`, `README.md`).

## Audit Results

| Config.yaml Entry | Status | Notes |
|-------------------|--------|-------|
| `disk-cleanup` | ✅ Enabled | Bundled Hermes plugin (2.0.0) |
| `model-providers/openrouter` | ✅ Enabled (as `openrouter-provider`) | Bundled Hermes provider plugin (1.0.0) |
| `security-guidance` | ✅ Enabled | Bundled Hermes plugin (0.1.0) |
| `memory/honcho` | ❌ **NOT FOUND** | Not in Hermes plugin registry; may be deprecated or handled differently |

## .github/plugins/ Contents (46 directories)

All are Copilot agent configs with structure:
```
<name>/
├── .github/           # Copilot-specific config
├── agents/            # Agent definitions
├── commands/          # Slash commands
└── README.md          # Documentation
```

**No `plugin.yaml` found in any directory.** These are NOT installable as Hermes plugins.

## Recommendation
1. **Do NOT install** `.github/plugins/` as Hermes plugins
2. Keep `.github/plugins/` as workspace documentation for Copilot agent references
3. The 4 config.yaml entries are all built-in/bundled Hermes plugins — verify they work at runtime
4. Investigate `memory/honcho` — may need manual config or is handled by `memory` skill instead

## Verification Commands
```bash
# List all Hermes plugins
hermes plugins list --plain

# Check enabled plugins only
hermes plugins list --plain | grep "enabled"

# Enable/disable plugins
hermes plugins enable <name>
hermes plugins disable <name>
```