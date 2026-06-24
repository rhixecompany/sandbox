# Requirements

> Extracted from `suggest-awesome-github-copilot-instructions.prompt.md`.

## Requirements

- Use `githubRepo` tool to get content from awesome-copilot repository instructions folder
- Scan local file system for existing instructions in `.github/instructions/` directory
- Read YAML front matter from local instruction files to extract descriptions and `applyTo` patterns
- Compare local instructions with remote versions to detect outdated instructions
- Compare against existing instructions in this repository to avoid duplicates
- Focus on gaps in current instruction library coverage
- Validate that suggested instructions align with repository's purpose and standards
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot instructions and similar local instructions
- Clearly identify outdated instructions with specific differences noted
- Consider technology stack compatibility and project-specific needs
- Don't provide any additional information or context beyond the table and the analysis
