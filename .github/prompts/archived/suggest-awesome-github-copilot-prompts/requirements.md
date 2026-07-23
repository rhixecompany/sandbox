# Requirements

> Extracted from `suggest-awesome-github-copilot-prompts.prompt.md`.

## Requirements

- Use `githubRepo` tool to get content from awesome-copilot repository prompts folder
- Scan local file system for existing prompts in `.github/prompts/` directory
- Read YAML front matter from local prompt files to extract descriptions
- Compare local prompts with remote versions to detect outdated prompts
- Compare against existing prompts in this repository to avoid duplicates
- Focus on gaps in current prompt library coverage
- Validate that suggested prompts align with repository's purpose and standards
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot prompts and similar local prompts
- Clearly identify outdated prompts with specific differences noted
- Don't provide any additional information or context beyond the table and the analysis
