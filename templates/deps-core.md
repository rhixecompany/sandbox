# Dependencies

Shared dependency patterns for all prompts.

## MCP Server Dependencies

| Server                | Purpose                      | Fallback                        |
| --------------------- | ---------------------------- | ------------------------------- |
| `tavily`              | Web search + URL extraction  | `fetch` → `web_extract`         |
| `fetch`               | Web page content extraction  | `web_extract`                   |
| `filesystem`          | File read/write operations   | native `read_file`/`write_file` |
| `github`              | GitHub API operations        | `gh` CLI                        |
| `memory`              | Persistent memory operations | `session_search`                |
| `sequential-thinking` | Structured reasoning         | —                               |
| `context7`            | Library API docs             | `web_search`                    |
| `ast-grep`            | AST-based code search        | `search_files`                  |
| `playwright`          | Browser automation           | `browser_*` tools               |

## Tool Dependencies

- `delegate_task` — Parallel subagent execution
- `web_search` — Fallback web search
- `web_extract` — Fallback content extraction
- `terminal` — Shell commands
- `search_files` — File content search
