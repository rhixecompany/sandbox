# Version Comparison Process

> Extracted from `suggest-awesome-github-copilot-instructions.prompt.md`.

## Version Comparison Process

1. For each local instruction file, construct the raw GitHub URL to fetch the remote version:
   - Pattern: `https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/<filename>`
2. Fetch the remote version using the `#fetch` tool
3. Compare entire file content (including front matter and body)
4. Identify specific differences:
   - **Front matter changes** (description, applyTo patterns)
   - **Content updates** (guidelines, examples, best practices)
5. Document key differences for outdated instructions
6. Calculate similarity to determine if update is needed
