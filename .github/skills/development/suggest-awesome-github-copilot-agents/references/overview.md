# GitHub Copilot Custom Agents — Reference Overview

## Key Concepts

- **GitHub Copilot Custom Agents** are specialized AI personas defined in `.agent.md` files. Each agent has a YAML frontmatter with `name`, `description`, and `tools` array specifying which MCP tools the agent can use. Agents enable targeted, role-specific AI assistance for different development tasks.
- **The awesome-copilot Repository** at https://github.com/github/awesome-copilot hosts a community-curated collection of Custom Agents in its `agents/` directory. The README at `docs/README.agents.md` provides a discoverable catalog. Agents cover use cases like feature flag cleanup, experimentation, principal engineering guidance, and security review.
- **Version Drift** — Custom Agents evolve as tool configurations and best practices change. A local agent file may differ from its remote counterpart in the awesome-copilot repository. Regular comparison is needed to detect changes in the `tools` array, `description`, or body instructions.
- **File Structure** — Agents live in `.github/agents/` for repository-specific use. Each file follows the naming convention `<name>.agent.md` and contains both frontmatter (tools, description) and body (instructions for the agent's behavior).
- **Agent Discovery** — The agent runtime scans `.github/agents/` for `*.agent.md` files and makes them available for use. Custom agents augment the built-in agent capabilities with domain-specific knowledge and tool access patterns.