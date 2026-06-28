# Cross-Platform Agent Inventory (Class Pattern)

For environments with multiple AI coding platforms where agent definitions need discovery, audit, and cross-reference.

**Important:** Each platform has a **CLI root** (config, plugins, sessions) separate from its **workspace agent definitions**. Always verify by probing the filesystem — don't assume paths from documentation alone.

## 5-Phase Inventory Model

1. **DISCOVER** — For each platform, locate agent definitions and CLI root
2. **INVENTORY** — Per platform: agent name, format, path, purpose, tools/permissions, model, mode
3. **CROSS-REFERENCE** — Map agents by function across platforms
4. **AUDIT INCONSISTENCIES** — Check for missing cross-refs, divergent naming, format differences
5. **FIX & DOCUMENT** — Create cross-reference document, update platform instructions

## Root Discovery Table (Windows 11)

| Platform | CLI Root (config, session, plugins) | Agent Definitions (workspace) | Verification |
|----------|--------------------------------------|-------------------------------|-------------|
| Copilot | `~/.copilot/` (`config.json`, `settings.json`, `session-store.db`, `plugins/`, `logs/`) | `.github/agents/*.agent.md` | `command -v copilot` → resolved path |
| Codex | `~/.codex/` (`config.toml`, agents/, skills/) | `~/.codex/agents/*.toml` | `ls ~/.codex/` |
| Hermes | `~/AppData/Local/hermes/` (`config.yaml`, profiles/, skills/, plugins/, hooks/) | `~/AppData/Local/hermes/profiles/*/` | `ls ~/AppData/Local/hermes/` |

### Copilot CLI Binary Location
On Windows, installed via VS Code extension or WinGet:
- VS Code: `~/AppData/Roaming/Code/User/globalStorage/github.copilot-chat/copilotCli/copilot`
- WinGet: `~/AppData/Local/Microsoft/WinGet/Links/copilot`

### Inventory Template

| Platform | Agent | Format | File | Purpose | Cross-Ref |
|----------|-------|--------|------|---------|-----------|
| Copilot | `architect` | `.agent.md` | `.github/agents/` | Architecture planning | → Hermes: code-architect |
| Hermes | `code-architect` | profile | `profiles/` | Code, debug, refactor | → Copilot: architect |
| Codex | `architect-reviewer` | `.toml` | `~/.codex/agents/` | Architecture review | → Copilot: architect |

## Pitfalls
- Global config files may be absent in project root — check user home config
- Agent file patterns differ per platform: Copilot uses `.agent.md`, Codex uses `.toml`, Hermes uses profile dirs
- The workspace `.github/` dir holds Copilot's agent/instruction definitions but is NOT the CLI root — the CLI root is `~/.copilot/`
- Some agents use `mode: primary`, others `mode: subagent`
- Hermes plugins may disable a provider plugin even when the active profile uses it
- On Windows, Hermes lives at `~/AppData/Local/hermes/`, NOT `~/.hermes/` (which is used on Linux/macOS)
- Running `which copilot` or `command -v copilot` may return multiple installs (VS Code bundled + WinGet) — check both
