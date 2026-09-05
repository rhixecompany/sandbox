# Smithery MCP Setup and Connection Management

## Goal

Configure Smithery MCP connections for Hermes/OpenCode, handling OAuth flows, API key configuration, token management, and multi-user namespace setup.

## Reference Documentation

Full documentation index: https://smithery.ai/docs/llms.txt

Use this to discover all available pages before exploring further.

## Core Concepts

### Namespaces

- Globally unique identifier grouping connections
- One namespace per application/environment
- Auto-created if not specified

### Connections

- Long-lived sessions to MCP servers
- Store credentials securely (write-only)
- Include custom metadata for filtering
- Return serverInfo with name/version

### Authentication Methods

- **API Key**: Backend only, full namespace access
- **Service Token**: Browser/mobile/agents, scoped access
- **OAuth Flow**: Managed by Smithery, no redirect URI config needed

## Quick Start

### CLI

```bash
# 1. Log in to Smithery
smithery auth login

# 2. Connect to an MCP server
smithery mcp add exa --id exa

# 3. List available tools
smithery tool list exa

# 4. Call a tool
smithery tool call exa search '{"query": "latest news about MCP"}'
```

### TypeScript SDK

```typescript
import { createMCPClient } from '@ai-sdk/mcp';
import { createConnection } from '@smithery/api/mcp';

const { transport } = await createConnection({
  mcpUrl: 'https://mcp.exa.ai',
});

const mcpClient = await createMCPClient({ transport });
const tools = await mcpClient.tools();
```

## Server Configuration

### With API Keys

```bash
smithery mcp add \
  '@browserbasehq/mcp-browserbase?browserbaseProjectId=your-project-id' \
  --id my-browserbase \
  --headers '{"browserbaseApiKey": "your-api-key"}'
```

### OAuth-Enabled Servers

```bash
# Returns auth_required with setup URL
smithery mcp add github
# Visit the setup URL to authorize
```

## Multi-User Setup

1. Create connections with `userId` in metadata
2. Filter connections by metadata
3. Aggregate tools across all user connections

```bash
smithery mcp add github \
  --id user-123-github \
  --metadata '{"userId": "user-123"}'
```

## Namespace MCP Endpoint

Bundle all namespace connections behind one endpoint:

```
https://mcp.smithery.run/{namespace}
```

Tool names prefixed with connection ID for uniqueness.

## Connection Status

| Status           | Description                                                                 |
|| ---------------- | --------------------------------------------------------------------------- ||
| `connected`      | Ready to use                                                                 |
| `auth_required`  | OAuth needed; includes `setupUrl`                                           |
| `input_required` | Needs configuration; includes `setupUrl`, `http` schema, `missing` fields  |
| `error`          | Failed; includes error `message`                                            |

## Execution Rules

- Never expose API keys to untrusted clients
- Use scoped service tokens for browser/mobile
- Store credentials only via Smithery managed flow
- Report auth failures with setup URLs
- LF-only Markdown writes
