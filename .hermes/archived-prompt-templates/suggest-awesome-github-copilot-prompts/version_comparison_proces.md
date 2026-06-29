# Version Comparison Process

> Extracted from `suggest-awesome-github-copilot-prompts.prompt.md`.

## Version Comparison Process

1. For each local prompt file, construct the raw GitHub URL to fetch the remote version:
   - Pattern: `https://raw.githubusercontent.com/github/awesome-copilot/main/prompts/<filename>`
2. Fetch the remote version using the `#fetch` tool
3. Compare entire file content (including front matter and body)
4. Identify specific differences:
   - **Front matter changes** (description, tools, mode)
   - **Tools array modifications** (added, removed, or renamed tools)
   - **Content updates** (instructions, examples, guidelines)
5. Document key differences for outdated prompts
6. Calculate similarity to determine if update is needed
