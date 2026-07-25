# Toolset Mapping Reference (VS Code/Help → Hermes)

## Known Hermes Toolset Palette

```python
{
    "web", "browser", "terminal", "file", "code_execution",
    "vision", "image_gen", "moa", "tts", "skills", "todo",
    "memory", "context_engine", "session_search", "clarify",
    "delegation", "cronjob"
}
```

NOTE: `search` is NOT a valid Hermes toolset. Use `web` instead. Prompts imported from some sources carry `search` in their toolsets — fix as part of normalization.

## Common VS Code / Copilot Tool Names → Hermes Equivalents

| VS Code Pattern | Hermes | Notes |
|----------------|--------|-------|
| `search` (bare) | `web` | Legacy toolset name; found en masse in prompt imports. Replace with `web`. |
| `edit/editFiles`, `createFile`, `editFiles` | `file` | |
| `web/fetch`, `fetch`, `openSimpleBrowser` | `web` | |
| `runCommands`, `terminalCommand`, `runInTerminal` | `terminal` | |
| `execute/runInTerminal`, `execute/getTerminalOutput` | `terminal` | |
| `runCommands/runInTerminal`, `runCommands/getTerminalOutput` | `terminal` | |
| `runCommands/terminalLastCommand`, `runCommands/terminalSelection` | `terminal` | |
| `search/codebase`, `codebase`, `search/changes` | `file` | `search_files` is a file tool |
| `read/readFile`, `read/problems` | `file` | |
| `playwright/*`, `io.github.chromedevtools/chrome-devtools-mcp/*` | `browser` | |
| `microsoft.docs.mcp` | `fetch` or `web` | Use MCP fetch for doc lookups |
| `context7/*`, `nextjs-docs-mcp/*` | `fetch` | Third-party MCP servers |
| `neondatabase/mcp-server-neon/*` | `terminal` | SQL queries via terminal |
| `prisma.prisma/*` | `terminal` | DB migration commands |
| `ms-azuretools.vscode-containers/containerToolsConfig` | `terminal` | Docker via terminal |
| `pylanceRunCodeSnippet` | `code_execution` | Python execution |
| `azure_get_schema_for_Bicep`, `bicepschema` | `terminal` | Azure CLI |
| `githubRepo`, `github`, `github/*` | — | Remove; GitHub operations use MCP `github` server, not a toolset |
| `vscode.vscodeAPI`, `extensions`, `usages` | — | Remove – VS Code internal |
| `problems`, `todos`, `changes`, `testFailure` | — | Remove – IDE widget |
| `vscode.mermaid-chat-features/renderMermaidDiagram` | — | Remove – feature-specific |
| `search/searchResults`, `findTestFiles`, `runTests`, `runTasks` | — | Remove – VS Code internals |
| `think` | — | Not a Hermes toolset |
| `agent` | — | Not a toolset |
| `new` | — | Not a toolset |

## Heuristic for Default

If after filtering all entries are removed, default to `[terminal, file]` — these are universally available on any Hermes host and cover 90%+ of prompt workflows.
