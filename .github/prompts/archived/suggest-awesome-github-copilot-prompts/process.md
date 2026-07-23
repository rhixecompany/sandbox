# Process

> Extracted from `suggest-awesome-github-copilot-prompts.prompt.md`.

## Process

1. **Fetch Available Prompts**: Extract prompt list and descriptions from [awesome-copilot README.prompts.md](https://github.com/github/awesome-copilot/blob/main/docs/README.prompts.md). Must use `#fetch` tool.
2. **Scan Local Prompts**: Discover existing prompt files in `.github/prompts/` folder
3. **Extract Descriptions**: Read front matter from local prompt files to get descriptions
4. **Fetch Remote Versions**: For each local prompt, fetch the corresponding version from awesome-copilot repository using raw GitHub URLs (e.g., `https://raw.githubusercontent.com/github/awesome-copilot/main/prompts/<filename>`)
5. **Compare Versions**: Compare local prompt content with remote versions to identify:
   - Prompts that are up-to-date (exact match)
   - Prompts that are outdated (content differs)
   - Key differences in outdated prompts (tools, description, content)
6. **Analyze Context**: Review chat history, repository files, and current project needs
7. **Compare Existing**: Check against prompts already available in this repository
8. **Match Relevance**: Compare available prompts against identified patterns and requirements
9. **Present Options**: Display relevant prompts with descriptions, rationale, and availability status including outdated prompts
10. **Validate**: Ensure suggested prompts would add value not already covered by existing prompts
11. **Output**: Provide structured table with suggestions, descriptions, and links to both awesome-copilot prompts and similar local prompts **AWAIT** user request to proceed with installation or updates of specific prompts. DO NOT INSTALL OR UPDATE UNLESS DIRECTED TO DO SO.
12. **Download/Update Assets**: For requested prompts, automatically:
    - Download new prompts to `.github/prompts/` folder
    - Update outdated prompts by replacing with latest version from awesome-copilot
    - Do NOT adjust content of the files
    - Use `#fetch` tool to download assets, but may use `curl` using `#runInTerminal` tool to ensure all content is retrieved
    - Use `#todos` tool to track progress
