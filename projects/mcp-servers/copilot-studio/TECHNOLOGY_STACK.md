# 🏗 Technology Stack Blueprint - mcp-servers/copilot-studio

**Project Path:** `projects/mcp-servers/copilot-studio`
**Generated:** 2026-07-28
**Status:** Active — Power Platform / Copilot Studio MCP Connector

---

## Core Technologies

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Runtime** | Node.js | 18+ | MIT |
| **Language** | TypeScript | ^5.5.0 | Apache-2.0 |
| **Framework** | Express.js | ^4.21.0 | MIT |
| **Transport** | HTTP (Streamable) | Custom | - |
| **Package Manager** | npm | Latest | - |

---

## Architecture

**Pattern:** MCP Server with HTTP/Streamable Transport for Power Platform integration

- **Transport:** HTTP (not STDIO) — enables Copilot Studio connection
- **Auth:** OAuth 2.0 / Managed Identity for Dataverse
- **API:** Microsoft Dataverse Web API

### Project Structure

```
mcp-servers/copilot-studio/
├── src/
│   ├── server.ts              # Express server entry
│   ├── mcp/
│   │   ├── handler.ts         # MCP request handler
│   │   └── tools/             # Tool implementations
│   │       ├── queryDataverse.ts
│   │       └── executeAction.ts
│   └── auth/
│       └── tokenManager.ts    # OAuth token management
├── dist/                      # Compiled output
├── package.json
├── tsconfig.json
└── README.md
```

---

## Dependencies (`package.json`)

### Production

```json
{
  "dependencies": {
    "express": "^4.21.0",
    "cors": "^2.8.5",
    "uuid": "^10.0.0",
    "node-fetch": "^2.7.0"
  }
}
```

### Development

```json
{
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/cors": "^2.8.17",
    "@types/uuid": "^10.0.0",
    "@types/node": "^20.14.0",
    "@types/node-fetch": "^2.6.11",
    "typescript": "^5.5.0",
    "ts-node": "^10.9.2"
  }
}
```

---

## Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| `build` | `tsc` | Compile to `dist/` |
| `start` | `node dist/server.js` | Run production server |
| `dev` | `ts-node src/server.ts` | Development with hot reload |
| `clean` | `rm -rf dist` | Clean build output |

---

## MCP HTTP Transport

Unlike STDIO servers, this uses **HTTP transport** for Copilot Studio:

```
Copilot Studio ──HTTP──▶ Express Server ──MCP Protocol──▶ Dataverse
```

### Endpoints

- `POST /mcp` — MCP protocol messages (initialize, tools/list, tools/call, etc.)
- `GET /health` — Health check
- `GET /.well-known/mcp` — Server discovery

---

## Entry Point (`src/server.ts`)

```typescript
import express from "express";
import cors from "cors";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { registerDataverseTools } from "./mcp/tools/dataverse.js";

const app = express();
app.use(cors());
app.use(express.json());

// MCP endpoint
app.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: () => crypto.randomUUID(),
  });
  
  const server = new McpServer({
    name: "copilot-studio-mcp-server",
    version: "1.0.0",
  });
  
  registerDataverseTools(server);
  
  await server.connect(transport);
  await transport.handleRequest(req, res);
});

// Health check
app.get("/health", (req, res) => res.json({ status: "ok" }));

app.listen(3000, () => console.log("MCP Server listening on :3000"));
```

---

## Dataverse Tools (`src/mcp/tools/dataverse.ts`)

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { getAccessToken } from "../auth/tokenManager.js";

export function registerDataverseTools(server: McpServer) {
  // Query Dataverse
  server.tool(
    "query_dataverse",
    "Execute a FetchXML or OData query against Dataverse",
    {
      query: z.string().describe("FetchXML or OData query"),
      type: z.enum(["fetchxml", "odata"]).default("fetchxml"),
    },
    async ({ query, type }) => {
      const token = await getAccessToken();
      const response = await fetch(`${process.env.DATAVERSE_URL}/api/data/v9.2/...`, {
        method: type === "fetchxml" ? "POST" : "GET",
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json",
          "Prefer": "odata.include-annotations=*",
        },
        body: type === "fetchxml" ? JSON.stringify({ fetchXml: query }) : undefined,
      });
      
      return { content: [{ type: "text", text: await response.text() }] };
    }
  );

  // Execute Action/Function
  server.tool(
    "execute_action",
    "Execute a Dataverse Action or Function",
    {
      actionName: z.string().describe("Name of the Action/Function"),
      parameters: z.record(z.any()).describe("Input parameters"),
    },
    async ({ actionName, parameters }) => {
      // Implementation...
    }
  );
}
```

---

## Authentication (`src/auth/tokenManager.ts`)

```typescript
// Supports: Managed Identity, Client Credentials, Interactive
let tokenCache: { token: string; expiresAt: number } | null = null;

export async function getAccessToken(): Promise<string> {
  if (tokenCache && tokenCache.expiresAt > Date.now() + 60000) {
    return tokenCache.token;
  }
  
  // Azure Managed Identity (preferred in Azure)
  if (process.env.MSI_ENDPOINT) {
    return getManagedIdentityToken();
  }
  
  // Client Credentials flow
  return getClientCredentialsToken();
}

async function getClientCredentialsToken(): Promise<string> {
  const response = await fetch(
    `https://login.microsoftonline.com/${process.env.TENANT_ID}/oauth2/v2.0/token`,
    {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({
        client_id: process.env.CLIENT_ID!,
        client_secret: process.env.CLIENT_SECRET!,
        scope: "https://<org>.crm.dynamics.com/.default",
        grant_type: "client_credentials",
      }),
    }
  );
  
  const data = await response.json();
  tokenCache = { 
    token: data.access_token, 
    expiresAt: Date.now() + data.expires_in * 1000 
  };
  
  return data.access_token;
}
```

---

## Environment Variables

```env
# Required
DATAVERSE_URL=https://<org>.crm.dynamics.com
TENANT_ID=<tenant-guid>
CLIENT_ID=<app-guid>
CLIENT_SECRET=<secret>

# Optional (for Managed Identity)
MSI_ENDPOINT=http://169.254.169.254/metadata/identity/oauth2/token

# Server
PORT=3000
```

---

## Copilot Studio Configuration

1. **Create Custom Connector** in Power Platform
2. **Authentication:** OAuth 2.0 → Azure AD
3. **MCP Definition:** Point to your server `/mcp` endpoint
4. **Actions:** Map MCP tools to connector actions

---

## Commands

```bash
# Install
npm install

# Develop
npm run dev

# Build
npm run build

# Start
npm run start

# Docker (production)
docker build -t copilot-studio-mcp .
docker run -p 3000:3000 --env-file .env copilot-studio-mcp
```

---

## License

MIT

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*
