# Error Handling

> Extracted from `tldr-prompt.prompt.md`.

## Error Handling

### Missing Required Parameters

**User**

```bash
/tldr-prompt
```

**Agent Response when NO Required Data**

```text
Error: Missing required input.

You MUST provide one of the following:
1. A Copilot file: /tldr-prompt #file:{{name.prompt.md | name.agent.md | name.instructions.md | name.collections.md}}
2. A URL: /tldr-prompt #fetch {{https://example.com/docs}}
3. A search query: /tldr-prompt "{{topic}}" (e.g., "MCP servers", "inline chat", "chat tools")

Please retry with one of these inputs.
```

### AMBIGUOUS QUERIES

#### Workspace Search

> [!NOTE] First attempt to resolve using workspace files. If found, generate output. If no relevant files found, resolve using GitHub awesome-copilot as specified in **URL Resolver** section.

**User**

```bash
/tldr-prompt "Prompt files relevant to Java"
```

**Agent Response when Relevant Workspace Files Found**

```text
I'll search ${workspaceFolder} for Copilot customization files (.prompt.md, .agent.md, .instructions.md, .collections.md) relevant to Java.
From the search results, I'll produce a tldr output for each file found.
```

**Agent Response when NO Relevant Workspace Files Found**

```text
I'll check https://github.com/github/awesome-copilot
Found:
- https://github.com/github/awesome-copilot/blob/main/prompts/java-docs.prompt.md
- https://github.com/github/awesome-copilot/blob/main/prompts/java-junit.prompt.md

Now let me fetch the raw content:
- https://raw.githubusercontent.com/github/awesome-copilot/refs/heads/main/prompts/java-docs.prompt.md
- https://raw.githubusercontent.com/github/awesome-copilot/refs/heads/main/prompts/java-junit.prompt.md

I'll create a tldr summary for each prompt file.
```

### UNAMBIGUOUS QUERIES

#### File Query

**User**

```bash
/tldr-prompt #file:typescript-mcp-server-generator.prompt.md
```

**Agent**

```text
I'll read the file typescript-mcp-server-generator.prompt.md and create a tldr summary.
```

#### Documentation Query

**User**

```bash
/tldr-prompt "How do MCP servers work?" #fetch https://code.visualstudio.com/docs/copilot/customization/mcp-servers
```

**Agent**

```text
I'll fetch the MCP server documentation from https://code.visualstudio.com/docs/copilot/customization/mcp-servers
and create a tldr summary of how MCP servers work.
```
