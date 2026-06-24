# Requirements

> Extracted from `suggest-awesome-github-copilot-skills.prompt.md`.

## Requirements

- Use `fetch` tool to get content from awesome-copilot repository skills documentation
- Use `githubRepo` tool to get individual skill content for download
- Scan local file system for existing skills in `.github/skills/` directory
- Read YAML front matter from local `SKILL.md` files to extract names and descriptions
- Compare local skills with remote versions to detect outdated skills
- Compare against existing skills in this repository to avoid duplicates
- Focus on gaps in current skill library coverage
- Validate that suggested skills align with repository's purpose and technology stack
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot skills and similar local skills
- Clearly identify outdated skills with specific differences noted
- Consider bundled asset requirements and compatibility
- Don't provide any additional information or context beyond the table and the analysis
