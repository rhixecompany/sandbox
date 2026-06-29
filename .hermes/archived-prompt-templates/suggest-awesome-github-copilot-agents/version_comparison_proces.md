# Version Comparison Process

> Extracted from `suggest-awesome-github-copilot-agents.prompt.md`.

## Version Comparison Process

1. For each local agent file, construct the raw GitHub URL to fetch the remote version:
   - Pattern: `https://raw.githubusercontent.com/github/awesome-copilot/main/agents/<filename>`
2. Fetch the remote version using the `fetch` tool
3. Compare entire file content (including front matter, tools array, and body)
4. Identify specific differences:
   - **Front matter changes** (description, tools)
   - **Tools array modifications** (added, removed, or renamed tools)
   - **Content updates** (instructions, examples, guidelines)
5. Document key differences for outdated agents
6. Calculate similarity to determine if update is needed
