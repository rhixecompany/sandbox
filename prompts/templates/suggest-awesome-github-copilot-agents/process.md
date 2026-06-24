# Process

> Extracted from `suggest-awesome-github-copilot-agents.prompt.md`.

## Process

1. **Fetch Available Custom Agents**: Extract Custom Agents list and descriptions from [awesome-copilot README.agents.md](https://github.com/github/awesome-copilot/blob/main/docs/README.agents.md). Must use `fetch` tool.
2. **Scan Local Custom Agents**: Discover existing custom agent files in `.github/agents/` folder
3. **Extract Descriptions**: Read front matter from local custom agent files to get descriptions
4. **Fetch Remote Versions**: For each local agent, fetch the corresponding version from awesome-copilot repository using raw GitHub URLs (e.g., `https://raw.githubusercontent.com/github/awesome-copilot/main/agents/<filename>`)
5. **Compare Versions**: Compare local agent content with remote versions to identify:
   - Agents that are up-to-date (exact match)
   - Agents that are outdated (content differs)
   - Key differences in outdated agents (tools, description, content)
6. **Analyze Context**: Review chat history, repository files, and current project needs
7. **Match Relevance**: Compare available custom agents against identified patterns and requirements
8. **Present Options**: Display relevant custom agents with descriptions, rationale, and availability status including outdated agents
9. **Validate**: Ensure suggested agents would add value not already covered by existing agents
10. **Output**: Provide structured table with suggestions, descriptions, and links to both awesome-copilot custom agents and similar local custom agents **AWAIT** user request to proceed with installation or updates of specific custom agents. DO NOT INSTALL OR UPDATE UNLESS DIRECTED TO DO SO.
11. **Download/Update Assets**: For requested agents, automatically:
    - Download new agents to `.github/agents/` folder
    - Update outdated agents by replacing with latest version from awesome-copilot
    - Do NOT adjust content of the files
    - Use `#fetch` tool to download assets, but may use `curl` using `#runInTerminal` tool to ensure all content is retrieved
    - Use `#todos` tool to track progress
