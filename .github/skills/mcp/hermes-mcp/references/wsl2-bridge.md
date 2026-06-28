# WSL2 → Windows Chrome Bridge

## When to Use
Hermes runs in WSL2, Chrome runs on Windows.

## Setup
```bash
# Add the bridge server
hermes mcp add chrome-devtools-win \
  --command cmd.exe \
  --args "/c npx -y chrome-devtools-mcp@latest --autoConnect --no-usage-statistics"

# Test connection
hermes mcp test chrome-devtools-win

# Reload in Hermes
/reload-mcp
```

## Mental Model
```
Hermes (WSL) → MCP stdio bridge → Windows Chrome
```

## Typical Prompt
> `调用 MCP 工具 mcp_chrome_devtools_win_list_pages，列出当前浏览器标签页。`

## When `/browser connect` Fails
- Use `/browser connect` for **same-environment** setups
- Use MCP bridge for **WSL→Windows** browser access

## Known Pitfalls
| Issue | Solution |
|-------|----------|
| Path mapping (`/mnt/c/Users/...` vs `C:\Users\...`) | Use `chrome-devtools-mcp --autoConnect` |
| UNC paths | Avoid; use local Windows paths |
| WSL root (`/root`) vs home (`/home/...`) | Ensure server runs in correct context |

## Config.yaml Entry
```yaml
mcp_servers:
  chrome-devtools-win:
    command: "cmd.exe"
    args: ["/c", "npx", "-y", "chrome-devtools-mcp@latest", "--autoConnect", "--no-usage-statistics"]
    tools:
      include: [list_pages, navigate, evaluate]
      prompts: false
      resources: false
```

## Verification
```bash
# In Hermes chat
/reload-mcp
# Then: "List browser tabs via MCP"
```