# Process

> Extracted from `suggest-awesome-github-copilot-instructions.prompt.md`.

## Process

1. **Fetch Available Instructions**: Extract instruction list and descriptions from [awesome-copilot README.instructions.md](https://github.com/github/awesome-copilot/blob/main/docs/README.instructions.md). Must use `#fetch` tool.
2. **Scan Local Instructions**: Discover existing instruction files in `.github/instructions/` folder
3. **Extract Descriptions**: Read front matter from local instruction files to get descriptions and `applyTo` patterns
4. **Fetch Remote Versions**: For each local instruction, fetch the corresponding version from awesome-copilot repository using raw GitHub URLs (e.g., `https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/<filename>`)
5. **Compare Versions**: Compare local instruction content with remote versions to identify:
   - Instructions that are up-to-date (exact match)
   - Instructions that are outdated (content differs)
   - Key differences in outdated instructions (description, applyTo patterns, content)
6. **Analyze Context**: Review chat history, repository files, and current project needs
7. **Compare Existing**: Check against instructions already available in this repository
8. **Match Relevance**: Compare available instructions against identified patterns and requirements
9. **Present Options**: Display relevant instructions with descriptions, rationale, and availability status including outdated instructions
10. **Validate**: Ensure suggested instructions would add value not already covered by existing instructions
11. **Output**: Provide structured table with suggestions, descriptions, and links to both awesome-copilot instructions and similar local instructions **AWAIT** user request to proceed with installation or updates of specific instructions. DO NOT INSTALL OR UPDATE UNLESS DIRECTED TO DO SO.
12. **Download/Update Assets**: For requested instructions, automatically:
    - Download new instructions to `.github/instructions/` folder
    - Update outdated instructions by replacing with latest version from awesome-copilot
    - Do NOT adjust content of the files
    - Use `#fetch` tool to download assets, but may use `curl` using `#runInTerminal` tool to ensure all content is retrieved
    - Use `#todos` tool to track progress
