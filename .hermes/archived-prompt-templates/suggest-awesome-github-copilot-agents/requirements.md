# Requirements

> Extracted from `suggest-awesome-github-copilot-agents.prompt.md`.

## Requirements

- Use `githubRepo` tool to get content from awesome-copilot repository agents folder
- Scan local file system for existing agents in `.github/agents/` directory
- Read YAML front matter from local agent files to extract descriptions
- Compare local agents with remote versions to detect outdated agents
- Compare against existing agents in this repository to avoid duplicates
- Focus on gaps in current agent library coverage
- Validate that suggested agents align with repository's purpose and standards
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot agents and similar local agents
- Clearly identify outdated agents with specific differences noted
- Don't provide any additional information or context beyond the table and the analysis
