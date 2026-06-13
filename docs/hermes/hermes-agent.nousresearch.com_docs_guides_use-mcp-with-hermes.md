# Source: <https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes>

# Use MCP with Hermes — Summary

Source: <https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes>

A concise, scannable guide to using MCP (Model Context Protocol) with Hermes Agent: when to use it, setup steps, filtering/security, WSL2 browser bridging, common patterns, a short tutorial, troubleshooting, and recommended first servers.

---

## Key excerpts (original format)

Installation (when extras not installed):

```
cd ~/.hermes/hermes-agentuv pip install -e ".[mcp]"
```

Example: add a single safe filesystem server

```
mcp_servers:
  project_fs:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/my-project"]
```

Verify / reload:

```
hermes chat
/reload-mcp
```

Example: whitelist GitHub tools

```
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
    tools:
      include: [list_issues, create_issue, search_code]
```

WSL2 -> Windows Chrome bridge (recommended server example)

```
hermes mcp add chrome-devtools-win --command cmd.exe --args /c npx -y chrome-devtools-mcp@latest --autoConnect --no-usage-statistics
hermes mcp test chrome-devtools-win
/reload-mcp
```

Example: blacklist dangerous actions

```
mcp_servers:
  stripe:
    url: "https://mcp.stripe.com"
    headers:
      Authorization: "Bearer ***"
    tools:
      exclude: [delete_customer, refund_payment]
```

Example: disable utility wrappers

```
mcp_servers:
  docs:
    url: "https://mcp.docs.example.com"
    tools:
      prompts: false
      resources: false
```

Disable/keep config without connecting:

```
enabled: false
```

Typical WSL2 mental model (quote)

> Hermes (WSL) -> MCP stdio bridge -> Windows Chrome

Typical MCP browser prompt (original text)

```
调用 MCP 工具 mcp_chrome_devtools_win_list_pages，列出当前浏览器标签页。
```

---

## When to use MCP (summary)

Use MCP when:

- a tool already exists in MCP form and you don't want to write a native Hermes tool
- you need a clean RPC adapter to local or remote systems
- you want per-server, fine-grained exposure control
- you need to connect Hermes to internal APIs/databases without modifying Hermes core

Do NOT use MCP when:

- a built-in Hermes tool already suffices
- the server exposes a large dangerous surface you cannot filter
- you only need one narrow integration where a native tool would be simpler/smaller risk

---

## Mental model

- MCP = adapter layer: Hermes is the agent; MCP servers contribute tools.
- Hermes discovers MCP servers at startup/reload; the model can call those tools like normal tools.
- Crucial: control visibility per-server — connect the right thing with the smallest useful surface.

---

## Quick setup steps

1. Install MCP support
   - Standard installer includes MCP (`uv pip install -e ".[all]"`).
   - If installed without extras, add MCP:

     ```
     cd ~/.hermes/hermes-agentuv pip install -e ".[mcp]"
     ```

   - For npm servers ensure Node.js and `npx` are available; for Python servers `uvx` is recommended.

2. Add one safe server first (example: project-limited filesystem) — see filesystem snippet above.
   Start Hermes: `hermes chat` and try a concrete prompt:
   `Inspect this project and summarize the repo layout.`

3. Verify MCP loaded
   - Hermes banner/status shows MCP integration
   - Ask Hermes what tools it has
   - Use `/reload-mcp` after config changes
   - Check logs if connection fails
   - Practical test prompt: `Tell me which MCP-backed tools are available right now.`

4. Start filtering immediately — prefer allowlists for sensitive systems.

---

## Filtering: what it affects

Two categories:

1. Server-native MCP tools — filtered by:
   - `tools.include`
   - `tools.exclude`

2. Hermes-added utility wrappers — filtered by:
   - `tools.resources`
   - `tools.prompts`

Common utility wrappers (appear only if supported and enabled):

- Resources: `list_resources`, `read_resource`
- Prompts: `list_prompts`, `get_prompt`

---

## WSL2: bridging Hermes in WSL to Windows Chrome

When useful:

- Hermes runs in WSL2 but you want to control your signed-in Windows Chrome (preserve profile/cookies/logins).
- Hermes starts a local stdio MCP server launched via Windows interop which attaches to the live Windows Chrome.

Recommended server: `chrome-devtools-mcp`
Use the add/test commands shown above. Then `/reload-mcp` or restart Hermes.

When `/browser connect` is wrong:

- WSL may not reach Windows-hosted debugging endpoints
- New Chrome live-debugging flows differ from classic ws://localhost:9222
- Use a Windows-side helper (MCP) to attach

Known pitfalls:

- Starting Hermes from Windows-mounted paths (e.g., /mnt/c/Users/...) with Windows stdio executables can cause UNC warnings.
- If `--autoConnect` times out while enumerating pages, reduce frozen/background tabs in Chrome and retry.

---

## Common patterns (config + example prompts)

1. Local project assistant (scoped filesystem/git)

```
mcp_servers

[... summary truncated for context management ...]
```

Recommended server: `chrome-devtools-mcp`
Use the add/test commands shown above. Then `/reload-mcp` or restart Hermes.

When `/browser connect` is wrong:

- WSL may not reach Windows-hosted debugging endpoints
- New Chrome live-debugging flows differ from classic ws://localhost:9222
- Use a Windows-side helper (MCP) to attach

Known pitfalls:

- Starting Hermes from Windows-mounted paths (e.g., /mnt/c/Users/...) with Windows stdio executables can cause UNC warnings.
- If `--autoConnect` times out while enumerating pages, reduce frozen/background tabs in Chrome and retry.

---

## Common patterns (config + example prompts)

1. Local project assistant (scoped filesystem/git)

```
mcp_servers

[... summary truncated for context management ...]
```
