# Complete MCP Configuration Examples

## Pattern 1: Local Project Assistant
```yaml
mcp_servers:
  fs:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/project"]
    tools:
      include: [list_files, read_file, write_file]
      prompts: false
      resources: false
  
  git:
    command: "uvx"
    args: ["mcp-server-git", "--repository", "/home/user/project"]
    tools:
      include: [git_status, git_log, git_diff]
      prompts: false
      resources: false
```

## Pattern 2: GitHub Triage Assistant
```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
    tools:
      include: [list_issues, create_issue, update_issue, search_code]
      prompts: false
      resources: false
```

## Pattern 3: Internal API Assistant
```yaml
mcp_servers:
  internal_api:
    url: "https://mcp.internal.example.com"
    headers:
      Authorization: "Bearer ${INTERNAL_API_TOKEN}"
    tools:
      include: [query_db, call_service]
```

## Pattern 4: Linear Issue Management
```yaml
mcp_servers:
  linear:
    url: "https://mcp.linear.app/mcp"
    auth: oauth
    tools:
      include: [find_issues, get_issue, create_issue]
      prompts: false
      resources: false
```

## Pattern 5: Stripe (with Blacklist)
```yaml
mcp_servers:
  stripe:
    url: "https://mcp.stripe.com"
    headers:
      Authorization: "Bearer ${STRIPE_API_KEY}"
    tools:
      exclude: [delete_customer, refund_payment]
```

## Complete Schema
```yaml
mcp_servers:
  <server_name>:
    # Stdio (local subprocess)
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
    env:
      ENV_VAR: "value"
    
    # HTTP (remote)
    # url: "https://mcp.example.com/mcp"
    # headers:
    #   Authorization: "Bearer ***"
    
    # OAuth
    # auth: "oauth"
    
    # Tool filtering
    tools:
      include: [tool1, tool2]      # Whitelist (recommended)
      # exclude: [tool3, tool4]     # Blacklist
      prompts: true                # Enable prompt wrappers
      resources: true              # Enable resource wrappers
```