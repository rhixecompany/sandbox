# Subgoal 2: Code-Rabbit CLI, MCP, and Webhook Setup

## Installation Status

### CLI Installation
- **Status**: ✅ INSTALLED
- **Package**: CodeRabbit CLI v0.7.6 (native Windows binary)
- **Install Path**: `C:\Users\Alexa\.local\bin\coderabbit`
- **Alias**: `cr` (at `C:\Users\Alexa\.local\bin\cr`)
- **Installation Method**: Downloaded from `https://cli.coderabbit.ai/releases/latest/coderabbit-windows-x64.zip` via Python (PowerShell/curl had SSL/connectivity issues)
- **Doctor Check**: 7 passed, 2 warnings (auth not signed in, not in a git repo)
- **PATH**: Not yet added to hermes config PATH — need to add `C:\Users\Alexa\.local\bin`

### MCP Server
- **coderabbit-cli-mcp**: ✅ ALREADY INSTALLED and ENABLED
  - Transport: `npx -y coderabbit-cli-mcp@latest`
  - Tool: `run_review` (1 tool)
  - Test Result: ✅ Connected (4006ms), 1 tool discovered (`run_review`)
- **Standalone `code-rabbit` npm/pip package**: ❌ NOT FOUND (404 on both registries)

### Webhooks
- **Status**: ✅ CONFIGURED (Express server created)
- **Location**: `C:\Users\Alexa\Desktop\SandBox\coderabbit_webhooks\`
- **Server**: `coderabbit_webhooks.js` — Express server on port 3456
- **Endpoints**: 4 routes configured
- **Dependencies**: express, cors, dotenv installed

## Files Created/Modified

| File | Action | Description |
|------|--------|-------------|
| `C:\Users\Alexa\.local\bin\coderabbit` | Created | Installed CLI binary v0.7.6 |
| `C:\Users\Alexa\.local\bin\cr` | Created | Short alias |
| `C:\Users\Alexa\Desktop\SandBox\coderabbit_webhooks\package.json` | Modified | Updated dependencies |
| `C:\Users\Alexa\Desktop\SandBox\coderabbit_webhooks\node_modules\` | Modified | Added cors, dotenv |
| `C:\Users\Alexa\Desktop\SandBox\coderabbit_webhooks\coderabbit_webhooks.js` | Pre-existing | Webhook server (4 endpoints) |

## MCP Configuration (from config.yaml)

```yaml
coderabbit-cli-mcp:
  args:
    - -y
    - coderabbit-cli-mcp@latest
  command: npx
  enabled: true
```

## Webhook Routes

| Method | Path | Function |
|--------|------|----------|
| POST | `/webhooks/coderabbit/review` | Trigger review on push events |
| POST | `/webhooks/coderabbit/pr` | Trigger review on PR events |
| GET | `/webhooks/coderabbit/auth/status` | Check auth status |
| POST | `/webhooks/coderabbit/bootstrap` | Bootstrap CLI if missing |

## Issues Encountered

1. **PowerShell SSL**: `Invoke-WebRequest` fails with SSL/TLS channel error — used Python `urllib` instead
2. **curl in MSYS2**: Fails to write to Windows paths — used Python download approach
3. **`code-rabbit` package not found**: No such package on npm or pip — actual product is `coderabbit` CLI
4. **CLI not in PATH**: `C:\Users\Alexa\.local\bin` needs to be added to hermes config

## Next Steps (Optional)

1. Add `C:\Users\Alexa\.local\bin` to hermes `config.yaml` PATH
2. Start the webhook server: `cd coderabbit_webhooks && node coderabbit_webhooks.js`
3. Authenticate: `coderabbit auth login`
4. Add `coderabbit` binary to hermes `mcp_servers` if a native CLI MCP is desired
5. Run webhook tests

## Test Results

- MCP `coderabbit-cli-mcp`: ✅ Connected, `run_review` tool available
- CLI `coderabbit --version`: ✅ Returns `0.7.6`
- CLI `coderabbit doctor`: ✅ 7/9 checks passed
- Webhook server: ⏳ Not yet started (needs `node coderabbit_webhooks.js`)
