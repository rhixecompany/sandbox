# Local Agent Discovery Process

> Extracted from `suggest-awesome-github-copilot-agents.prompt.md`.

## Local Agent Discovery Process

1. List all `*.agent.md` files in `.github/agents/` directory
2. For each discovered file, read front matter to extract `description`
3. Build comprehensive inventory of existing agents
4. Use this inventory to avoid suggesting duplicates
