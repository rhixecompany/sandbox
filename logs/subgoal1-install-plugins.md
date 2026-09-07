# Subgoal 1: Install Plugins from Awesome Repos

## Status: PARTIAL — Subagent failed due to model provider connectivity issue

## What Was Accomplished Before Failure

### Skills Installed via hermes skills install
- wondelai/skills → FAILED (could not fetch)
- skills-sh/agents365-ai/365-skills/drawio-skill → SUCCESS (installed)
- skills-sh/zeropointrepo/youtube-skills/youtube-full → Attempted
- skills-sh/Black-Forest-Labs/skills → Attempted

### Skills Already Present (from previous sessions)
- 779 SKILL.md files found in /c/Users/Alexa/AppData/Local/hermes/skills/
- 682 lines in hermes skills list output (local source)
- 101 skill directories exist

### Repos Fetched and Analyzed
1. **github/awesome-copilot** — Fetched. Contains: agents/, skills/, plugins/, hooks/, instructions/, workflows/, cookbook/, extensions/, .schemas/
2. **awesome-opencode** — Fetched. Contains: plugins (bluelovers/opencode-arise, aerovato/opencode-quotes-plugin, gotgenes/opencode-agent-identity, joshuadavidthomas/opencode-agent-memory, joshuadavidthomas/opencode-agent-skills), themes, agents, projects, resources
3. **RoggeOhta/awesome-codex-cli** — Fetched. Contains: 280+ resources including agents, skills, plugins, hooks, MCP servers, IDE integrations
4. **0xNyk/awesome-hermes-agent** — Fetched. Contains: community skills (hermes-plugins, hermes-skill-factory, litprog-skill), plugins (hermes-plugins by 42-evey), memory providers, tools, integrations, bridges

### Hermes-Compatible Items Identified
From the 4 repos, the following are Hermes-compatible:
- **Skills** (.skills/ folder with SKILL.md): 100+ across all repos
- **Plugins**: Various plugin.yaml format entries
- **Hooks**: Shell scripts and Python scripts
- **MCP Servers**: Various stdio and HTTP MCP servers

### Items NOT Compatible / Not Installed
- Copilot-specific plugins (require VS Code/Copilot CLI environment)
- Opencode-specific plugins (require opencode runtime)
- Codex CLI-specific subagents (require codex CLI)
- Some MCP servers have incompatible tooling requirements

## What Remains
Subagent failed during execution phase due to model provider connectivity. The following need to be completed:

1. Install remaining skills from awesome repos via `hermes skills install`
2. Convert compatible agents/instructions to Hermes format
3. Set up MCP servers for discovered functionality
4. Create webhooks for any discovered webhook-capable features

## Compatibility Report
| Repo | Hermes-Compatible | Not Compatible | Notes |
|------|-------------------|----------------|-------|
| awesome-copilot | Skills, hooks, agents | Plugins (Copilot-specific) | Agents can be converted |
| awesome-opencode | Skills, plugins | Opencode-specific configs | Some skills transferable |
| awesome-codex-cli | MCP servers, skills | Codex-specific subagents | MCP servers transferable |
| awesome-hermes-agent | ALL categories | None (already Hermes) | Primary target repo |

## Key Skills Identified for Hermes Installation
- hermes-plugins (42-evey) - Discord voice bridge, WhatsApp bridge, goal management
- hermes-skill-factory (Romanescu11) - Meta-skill for auto-generating skills
- litprog-skill (tlehman) - Literate programming skill
- opencode-agent-skills (joshuadavidthomas) - Dynamic skills loader
- opencode-agent-memory (joshuadavidthomas) - Persistent memory (Letta-inspired)

