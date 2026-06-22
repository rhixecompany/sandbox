# Process

> Extracted from `suggest-awesome-github-copilot-skills.prompt.md`.

## Process

1. **Fetch Available Skills**: Extract skills list and descriptions from [awesome-copilot README.skills.md](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md). Must use `#fetch` tool.
2. **Scan Local Skills**: Discover existing skill folders in `.github/skills/` folder
3. **Extract Descriptions**: Read front matter from local `SKILL.md` files to get `name` and `description`
4. **Fetch Remote Versions**: For each local skill, fetch the corresponding `SKILL.md` from awesome-copilot repository using raw GitHub URLs (e.g., `https://raw.githubusercontent.com/github/awesome-copilot/main/skills/<skill-name>/SKILL.md`)
5. **Compare Versions**: Compare local skill content with remote versions to identify:
   - Skills that are up-to-date (exact match)
   - Skills that are outdated (content differs)
   - Key differences in outdated skills (description, instructions, bundled assets)
6. **Analyze Context**: Review chat history, repository files, and current project needs
7. **Compare Existing**: Check against skills already available in this repository
8. **Match Relevance**: Compare available skills against identified patterns and requirements
9. **Present Options**: Display relevant skills with descriptions, rationale, and availability status including outdated skills
10. **Validate**: Ensure suggested skills would add value not already covered by existing skills
11. **Output**: Provide structured table with suggestions, descriptions, and links to both awesome-copilot skills and similar local skills **AWAIT** user request to proceed with installation or updates of specific skills. DO NOT INSTALL OR UPDATE UNLESS DIRECTED TO DO SO.
12. **Download/Update Assets**: For requested skills, automatically:
    - Download new skills to `.github/skills/` folder, preserving the folder structure
    - Update outdated skills by replacing with latest version from awesome-copilot
    - Download both `SKILL.md` and any bundled assets (scripts, templates, data files)
    - Do NOT adjust content of the files
    - Use `#fetch` tool to download assets, but may use `curl` using `#runInTerminal` tool to ensure all content is retrieved
    - Use `#todos` tool to track progress
