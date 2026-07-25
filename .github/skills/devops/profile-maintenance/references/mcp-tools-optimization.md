# MCP Server Tools Optimization Guide

**Purpose:** Document the Strict Rule #2 — ALWAYS prefer MCP server tools over native equivalents for token efficiency.

---

## Rule Definition (from SOUL.md)

> **Rule 2: MCP Server Tools Rule**
> ALWAYS use MCP server tools when available to reduce token usage:
> - Use `filesystem` MCP for file read/write/search instead of native tools
> - Use `github` MCP for GitHub operations instead of `gh` CLI or web search
> - Use `ast-grep` MCP for code pattern searching instead of grep/rg
> - Use `memory` MCP for persistent memory operations
> - Use `playwright` MCP for browser automation
> - Use `sequential-thinking` MCP for structured reasoning
> - Use `cli` MCP for built-in CLI tools
> - Use `code-sandbox` MCP for Node.js code execution
> - Use `fetch` MCP for web content fetching
> - Use `mcp-docker` MCP for Docker container management
> Prefer MCP tools over equivalent native tools — they are more token-efficient and integrated.

---

## MCP Server Inventory (from code-architect config)

| Server | Native Alternative | Token Advantage |
|--------|-------------------|-----------------|
| `filesystem` | `read_file`, `write_file`, `search_files`, `terminal` (ls/cat/grep) | Structured responses, no shell overhead |
| `github` | `gh` CLI, `terminal` (curl), `web_search` | Direct API, paginated, authenticated |
| `ast-grep` | `search_files` (grep/rg), `terminal` (ast-grep CLI) | AST-aware patterns, precise matches |
| `memory` | `memory` tool, `terminal` (file ops) | Integrated with MCP protocol |
| `playwright` | `browser_*` tools | Native MCP, better session handling |
| `sequential-thinking` | Manual reasoning, `execute_code` | Structured, auditable reasoning traces |
| `cli` | All native tools | Unified interface |
| `code-sandbox` | `execute_code`, `terminal` (node) | Isolated, reproducible Node.js |
| `fetch` | `web_extract`, `web_search`, `terminal` (curl) | Streaming, structured extraction |
| `mcp-docker` | `terminal` (docker CLI) | Profile-aware, env-managed |

---

## Decision Matrix: When to Use MCP vs Native

| Task | Use MCP | Use Native |
|------|---------|------------|
| Read/write/search files in workspace | `filesystem` MCP | Quick one-off, no MCP connection |
| GitHub API (repos, issues, PRs, actions) | `github` MCP | Simple `gh` CLI if already in shell |
| Code pattern search (AST-based) | `ast-grep` MCP | Simple text grep/rg |
| Persistent memory ops | `memory` MCP | `memory` tool for quick add/remove |
| Browser automation (complex) | `playwright` MCP | `browser_*` for simple nav/extract |
| Structured multi-step reasoning | `sequential-thinking` MCP | In-line thinking |
| CLI commands (grep, find, jq, etc) | `cli` MCP | `terminal` for complex pipelines |
| Node.js execution | `code-sandbox` MCP | `execute_code` (Python), `terminal` (node) |
| Web content fetch/extract | `fetch` MCP | `web_extract` for simple pages |
| Docker operations | `mcp-docker` MCP | `terminal` (docker CLI) for admin |

---

## Token Efficiency Rationale

1. **Structured responses** — MCP returns JSON, not raw terminal output
2. **No shell invocation overhead** — Direct process communication
3. **Protocol-level filtering** — Server-side include/exclude reduces payload
4. **Session reuse** — MCP servers maintain state (e.g., Playwright browser)
5. **Authentication handled** — GitHub MCP uses configured auth, no token passing

---

## Verification Checklist

When auditing SOUL.md for MCP rule compliance:

- [ ] All 10 MCP servers listed in rule
- [ ] Rule text identical across all 7 profiles
- [ ] No profile-specific exceptions without justification
- [ ] `.hermes.md` and `AGENTS.md` reference the rule
- [ ] User corrections about token usage captured

---

## Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| Using `terminal` for `ls`, `cat`, `grep` in workspace | Use `filesystem` MCP |
| Using `gh` CLI or `curl` for GitHub API | Use `github` MCP |
| Using `search_files` for code patterns | Use `ast-grep` MCP |
| Using `browser_*` for complex automation | Use `playwright` MCP |
| Manual reasoning without structure | Use `sequential-thinking` MCP |

---

## Integration with Profile Maintenance

When running `profile-maintenance`:
1. Verify MCP rule present in all 7 SOUL.md files
2. Verify MCP server config in `code-architect` config.yaml matches rule list
3. Update reference if new MCP servers added/removed