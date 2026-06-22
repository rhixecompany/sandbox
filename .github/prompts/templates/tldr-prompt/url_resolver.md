# URL Resolver

> Extracted from `tldr-prompt.prompt.md`.

## URL Resolver

### Ambiguous Queries

When no specific URL or file is provided, but instead raw data relevant to working with Copilot, resolve to:

1. **Identify topic category**:
   - Workspace files → Search ${workspaceFolder} for .prompt.md, .agent.md, .instructions.md, .collections.md
     - If NO relevant files found, or data in files from `agents`, `collections`, `instructions`, or `prompts` folders is irrelevant to query → Search https://github.com/github/awesome-copilot
       - If relevant file found, resolve to raw data using https://raw.githubusercontent.com/github/awesome-copilot/refs/heads/main/{{folder}}/{{filename}} (e.g., https://raw.githubusercontent.com/github/awesome-copilot/refs/heads/main/prompts/java-junit.prompt.md)
   - MCP servers → https://modelcontextprotocol.io/ or https://code.visualstudio.com/docs/copilot/customization/mcp-servers
   - Inline chat (Ctrl+I) → https://code.visualstudio.com/docs/copilot/inline-chat
   - Chat tools/agents → https://code.visualstudio.com/docs/copilot/chat/
   - General Copilot → https://code.visualstudio.com/docs/copilot/ or https://docs.github.com/en/copilot/

2. **Search strategy**:
   - For workspace files: Use search tools to find matching files in ${workspaceFolder}
   - For GitHub awesome-copilot: Fetch raw content from https://raw.githubusercontent.com/github/awesome-copilot/refs/heads/main/
   - For documentation: Use fetch tool with the most relevant URL from above

3. **Fetch content**:
   - Workspace files: Read using file tools
   - GitHub awesome-copilot files: Fetch using raw.githubusercontent.com URLs
   - Documentation URLs: Fetch using fetch tool

4. **Evaluate and respond**:
   - Use the fetched content as the reference for completing the request
   - Adapt response verbosity based on chat context

### Unambiguous Queries

If the user **DOES** provide a specific URL or file, skip searching and fetch/read that directly.

### Optional

- **Help output** - Raw data matching `-h`, `--help`, `/?`, `--tldr`, `--man`, etc.
