---
name: hermes-plugins-manager
title: Hermes Plugins Manager
description: "Create, update, delete, test, debug, enhance and manage Hermes plugins. Use when working with plugins in ~/AppData/Local/hermes/plugins/. Triggers: plugin, plugins, hermes-plugin, create plugin, update plugin, delete plugin, test plugin, debug plugin, enhance plugin, manage plugins, enable plugin, disable plugin."
category: devops
version: 1.1.0
author: Alexa
license: MIT
tags: [plugins, hermes, management, testing, debugging, enable, disable]
---

# Hermes Plugins Manager

Full lifecycle management of Hermes plugins: create, update, delete, test, debug, enhance, and verify.

## Two Plugin Systems

**CRITICAL DISTINCTION:** There are two completely separate plugin systems:

### 1. Hermes-Native Plugins (Bundled)
- Shipped with Hermes, NOT in the `plugins/` directory
- Configured in `config.yaml` under `plugins.enabled[]` / `plugins.disabled[]`
- Provide tools, hooks, and model providers directly to the Hermes agent
- Managed via `hermes plugins list`, `hermes plugins enable/disable <name>`
- Current bundled plugins: `disk-cleanup`, `model-providers/openrouter`, `security-guidance`, `google_meet`, `spotify`, `teams_pipeline`

### 2. Copilot CLI Plugins (in `plugins/` directory)
- 46 community plugins from `awesome-copilot` in `~/AppData/Local/hermes/plugins/`
- Provide slash commands, agents, and skills for **GitHub Copilot CLI** — NOT Hermes agent tools
- NOT managed via `hermes plugins` commands — managed via `copilot plugin install`
- Each plugin has its own directory with `README.md`, and optionally `agents/`, `commands/`, `skills/` subdirectories
- Skills are **nested** (e.g., `skills/copilot-sdk/SKILL.md`, not flat `skills/SKILL.md`)
- `hermes-achievements` is special: it's a runtime state directory (JSON state files), not a content plugin

## Plugin Directory Structure

```
~/AppData/Local/hermes/plugins/
├── awesome-copilot/              # Meta-prompts for discovering Copilot assets
├── azure-cloud-development/      # Azure cloud development tools
├── cast-imaging/                 # CAST Imaging software analysis agents
├── context-engineering/          # Context engineering patterns
├── copilot-sdk/                  # Copilot SDK integration (has nested skills/)
├── csharp-dotnet-development/    # C#/.NET development
├── database-data-management/     # Database management tools
├── devops-oncall/                # DevOps on-call workflows
├── edge-ai-tasks/                # Edge AI task automation
├── frontend-web-dev/             # Frontend web development
├── gem-team/                     # Multi-agent orchestration team
├── go-mcp-development/           # Go MCP server development
├── hermes-achievements/          # Runtime state ONLY (no README, no content)
├── java-development/             # Java development
├── ... (46 total)
```

## Plugin Configuration

Only Hermes-native plugins are configured in `config.yaml`:

```yaml
plugins:
  enabled:
  - disk-cleanup
  - model-providers/openrouter
  - security-guidance
  disabled:
  - model-providers/anthropic
  - model-providers/copilot
  - model-providers/copilot-acp
  - model-providers/custom
  - model-providers/openai-codex
  - model-providers/xai
  - web/brave_free
  - web/xai
```

Copilot CLI plugins are NOT listed in config.yaml — they're always "installed" by virtue of existing in the `plugins/` directory.

## When to Use

- Creating a new plugin
- Updating/enhancing an existing plugin
- Deleting a plugin
- Enabling/disabling plugins
- Testing plugin functionality
- Debugging plugin failures
- Reviewing plugin contents
- Adding new capabilities to existing plugins

## When NOT TO Use

- Managing hooks (use hermes-hooks-manager skill)
- Managing skills (use skill management skills)
- Managing profile files (use profile-maintenance skill)

## Workflow

### Phase 1: Discover

1. List all plugins: `ls ~/AppData/Local/hermes/plugins/`
2. Check enabled/disabled status in `config.yaml` (Hermes-native only)
3. Read plugin contents: each plugin is a directory with its own structure
4. Check plugin type by examining directory contents:
   - `agents/` subdirectory → agent definitions (.md files)
   - `commands/` subdirectory → slash command definitions (.md files)
   - `skills/` subdirectory → skill definitions (nested: `skills/<name>/SKILL.md`)
   - `hooks/` subdirectory → hook definitions
   - Only `.json` state files → runtime state directory (not a content plugin)
5. **Note:** MCP filesystem tool is sandboxed to workspace. Use `terminal` tool to read plugin files outside workspace.

### Phase 2: Create / Update

1. For new plugins: create directory under `~/AppData/Local/hermes/plugins/<plugin-name>/`
2. Plugin structure varies by type — examine existing plugins for patterns
3. For Copilot CLI plugins: add `README.md`, `agents/`, `commands/`, `skills/` as needed
4. For Hermes-native plugins: update `config.yaml` to enable/disable
5. For model provider plugins: add to `model-providers/` subdirectory
6. For web plugins: add to `web/` subdirectory

### Phase 3: Enable / Disable

**For Hermes-native plugins** — edit `config.yaml`:

```yaml
plugins:
  enabled:
  - my-new-plugin        # Add to enable
  disabled:
  - my-old-plugin         # Add to disable
```

**Rules:**
- A plugin is active ONLY if it appears in `enabled:` AND NOT in `disabled:`
- To enable: move from `disabled:` to `enabled:`
- To disable: move from `enabled:` to `disabled:`
- Plugins not listed in either section are inactive by default

**For Copilot CLI plugins** — they're always "installed" if the directory exists. No config.yaml entry needed.

### Phase 4: Test

1. After enabling a Hermes-native plugin, verify it loads: `hermes plugins list`
2. Test plugin-specific functionality
3. Check for conflicts with other enabled plugins
4. Verify config.yaml syntax is valid YAML (use `python3 -c "import yaml; yaml.safe_load(open('config.yaml'))"`)

### Phase 5: Debug

| Symptom | Cause | Fix |
|---|---|---|
| Plugin not loading | Not in `enabled:` list | Add to `plugins.enabled` in config.yaml |
| Plugin conflict | Two plugins provide same capability | Disable one of them |
| Config syntax error | Invalid YAML | Validate YAML syntax, check indentation |
| Plugin directory missing | Deleted or moved | Restore directory or remove from config |
| Model provider not working | Missing API key | Add key to `.env` file |
| Can't read plugin files | MCP filesystem sandboxed | Use `terminal` tool instead of MCP filesystem |

### Phase 6: Delete

1. Disable the plugin first (move to `disabled:` or remove from `enabled:`)
2. Remove the plugin directory: `rm -rf ~/AppData/Local/hermes/plugins/<name>/`
3. Clean up `config.yaml` references
4. Verify Hermes still starts cleanly

## Plugin Categories

| Category | Examples | Purpose |
|---|---|---|
| `model-providers/*` | openrouter, anthropic, copilot | AI model provider integrations (Hermes-native) |
| `web/*` | brave_free, xai | Web search providers (Hermes-native) |
| `disk-cleanup` | — | Disk cleanup utilities (Hermes-native) |
| `security-guidance` | — | Security guidance (Hermes-native) |
| Copilot CLI plugins | awesome-copilot, cast-imaging, 44 others | Third-party Copilot commands/agents/skills |

## Pitfalls

- **Never delete a plugin directory** without first disabling it in `config.yaml`
- **Never edit `config.yaml`** without validating YAML syntax afterward
- **Never enable conflicting plugins** (e.g., two model providers for the same model)
- **Never commit `.env` files** that may contain API keys for plugins
- **Always test after enabling** a new plugin — check logs for errors
- **Always use `hermes plugins`** CLI command for Hermes-native plugin operations
- **MCP filesystem tool is sandboxed** — it cannot read files outside the workspace. Use `terminal` tool to read plugin files in `~/AppData/Local/hermes/plugins/`
- **Skills are nested** — plugin skills live in `skills/<name>/SKILL.md`, not `skills/SKILL.md`. Count subdirectories, not flat files.
- **`hermes-achievements` is not a content plugin** — it's a runtime state directory with JSON files. Don't expect agents/commands/skills in it.
- **Copilot CLI plugins ≠ Hermes plugins** — the 46 directories in `plugins/` are for Copilot CLI, not Hermes agent tools. They don't appear in `config.yaml`.
