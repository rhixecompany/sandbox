# Source: <https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp>

# MCP (Model Context Protocol) — Hermes Agent (Nous Research)

Key purpose: MCP lets Hermes Agent connect to external tool servers so Hermes can use tools hosted outside Hermes (GitHub, DBs, filesystems, internal APIs, etc.). Use MCP to let Hermes use existing external tools.

---

## Key excerpts & code snippets (original formatting)

Quick start — install and enable MCP support:

```
cd ~/.hermes/hermes-agent
uv pip install -e ".[mcp]"
```

Example config (stdio MCP):

```
~/.hermes/config.yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
```

Run Hermes chat:

```
hermes chat
```

Catalog / one-click install:

```
hermes mcp           # interactive picker (default)
hermes mcp catalog   # plain-text list, scriptable
hermes mcp install n8n  # install a catalog entry by name
```

Picker example rows:

```
n8n available Manage and inspect n8n workflows from Hermes
linear enabled Linear issue/project management (remote OAuth)
github installed (disabled) GitHub repo + PR tools
```

Install-time tool selection (checklist):

```
Select tools for 'linear' (SPACE toggle, ENTER confirm)
 [x] find_issues Find issues matching a query
 [x] get_issue Get a single issue
 [x] create_issue Create a new issue
 [ ] delete_workspace Delete a Linear workspace
 ...
```

Manifest / trust notes:

- Manifests live at `optional-mcps/<name>/manifest.yaml` in the hermes-agent GitHub repo.
- Inspect `source:` and `install.bootstrap:` before installing.

Manifest compatibility warning:

```
⚠ '<name>' requires a newer Hermes
hermes update
```

Runtime environment substitution:

- `${VAR}` in manifest fields (`transport.command`, `transport.args`, `transport.url`, `headers`) resolved at server-connect time using environment variables (including `~/.hermes/.env`).
- `${INSTALL_DIR}` is substituted at install-time (path where catalog repo was cloned).

Reconfigure later:

```
hermes mcp configure <name>
hermes mcp install <name>   # to refresh a manifest
```

Two MCP server types — stdio and HTTP:

Stdio example:

```
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
```

HTTP example:

```
mcp_servers:
  remote_api:
    url: "https://mcp.example.com/mcp"
    headers:
      Authorization: "Bearer ***"
```

OAuth (dynamic client registration, PKCE, token caching):

```
mcp_servers:
  linear:
    url: "https://mcp.linear.app/mcp"
    auth: oauth
```

Token cache: `~/.hermes/mcp-tokens/<server>.json` (0o600 perms)

Google Drive / Atlassian pitfall — supply pre-registered client:

```
mcp_servers:
  googledrive:
    url: "https://drivemcp.googleapis.com/mcp/v1"
    auth: oauth
    oauth:
      client_id: "<your-oauth-client-id>"
      client_secret: "<your-oauth-client-secret>"
```

mTLS / client certs — three shapes accepted:

Combined PEM path:

```
client_cert: "~/.certs/mcp-client.pem"
```

Separate cert/key:

```
client_cert: ["~/.certs/mcp-client.crt", "~/.certs/mcp-client.key"]
```

Cert/key/password:

```
client_cert: ["~/.certs/mcp-client.crt", "~/.certs/mcp-client.key", "${MCP_KEY_PASSWORD}"]
```

Minimal stdio example:

```
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
```

Minimal HTTP example:

```
mcp_servers:
  company_api:
    url: "https://mcp.internal.example.com"
    headers:
      Authorization: "Bearer ***"
```

Preset example (Codex):

```
# Add Codex CLI as an MCP server in one line
hermes mcp add codex --preset codex
```

Equivalent config written:

```
mcp_servers:
  codex:
    command: "codex"
    args: ["mcp-server"]
```

Tool registration naming:

- Hermes prefixes MCP tools to avoid collisions:
  - Format: `mcp_<server_name>_<tool_name>`
  - Example: `mcp_filesystem_read_file`, `mcp_github_create_issue`, `mcp_my_api_query_data`

Utility wrappers (when supported):

- `list_resources`, `read_resource`, `list_prompts`, `get_prompt`
- Registered as `mcp_<server>_<utility>` (e.g. `mcp_github_list_resources`)

Filtering examples:

Disable server:

```
mcp_servers:
  legacy:
    url: "https://mcp.legacy.internal"
    enabled: false
```

Whitelist tools:

```
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
    tools:
      include: [create_issue, list_issues]
```

Blacklist tools:

```
mcp_servers:
  stripe:
    url: "https://mcp.stripe.com"
    tools:
      exclude: [delete_customer]
```

Include vs exclude precedence: include wins.

Filter utility wrappers:

```
mcp_servers:
  docs:
    url: "https://mcp.docs.example.com"
    tools:
      prompts: false
      resources: false
```

Full example (combined):

```
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
    tools:


[... summary truncated for context management ...]
```
