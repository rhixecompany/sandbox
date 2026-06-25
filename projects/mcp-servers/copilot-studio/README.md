# Copilot Studio MCP Server

A **Model Context Protocol (MCP)** server for **Microsoft Copilot Studio**, implementing a Power Platform–compatible connector with **streamable HTTP transport**, **JSON-RPC 2.0** compliance, and **generative orchestration** support.

---

## Overview

This server exposes customer management tools via the [Model Context Protocol](https://modelcontextprotocol.io) (MCP), making them directly consumable by Copilot Studio's generative AI orchestration layer as **agentic plugin actions**.

### How it works

```
Copilot Studio  ─── POST /mcp ──►  MCP Server  ──► Tool Handlers
     │              (JSON-RPC 2.0)        │
     │  ◄── inline JSON or SSE stream ────┘
     │
     └── GET /mcp/openapi.json  ──►  OpenAPI spec for connector registration
     └── GET /mcp/health        ──►  Health check
```

### Key features

| Feature | Detail |
|---------|--------|
| **Protocol** | MCP (Model Context Protocol) v2025-03-26 |
| **Transport** | Streamable HTTP (inline + SSE streaming) |
| **RPC Format** | JSON-RPC 2.0 |
| **Copilot Studio** | `x-ms-agentic-protocol` header, `x-ms-agentic-model` metadata |
| **Tools** | Declarative tool registry with JSON Schema input validation |
| **Streaming** | SSE (`text/event-stream`) for long-running tool executions |

---

## Prerequisites

- **Node.js** >= 18.x
- **npm** or **yarn**
- (Optional) **Power Platform CLI** for connector registration

---

## Installation

```bash
# Navigate to the project directory
cd projects/mcp-servers/copilot-studio

# Install dependencies
npm install

# Build TypeScript
npm run build

# Start the server
npm start
```

The server starts on **http://localhost:3121** by default.  
Override with `PORT` and `HOST` environment variables:

```bash
PORT=8080 HOST=127.0.0.1 npm start
```

---

## API Endpoints

### `POST /mcp` — MCP JSON-RPC 2.0 endpoint

Accepts MCP method calls. Supports both inline and SSE streaming responses.

**Request headers:**

| Header | Value | Required |
|--------|-------|----------|
| `Content-Type` | `application/json` | Yes |
| `x-ms-agentic-protocol` | `mcp` | Yes |
| `Accept` | `application/json` or `text/event-stream` | No (default: `application/json`) |

**Supported MCP methods:**

| Method | Description |
|--------|-------------|
| `initialize` | Protocol handshake; returns server capabilities |
| `tools/list` | Lists all available tools with their input schemas |
| `tools/call` | Invokes a tool by name with provided arguments |
| `notifications/initialized` | Client notification that initialization is complete |
| `notifications/tools/list_changed` | Notification that the tool list has changed |

### `GET /mcp/health` — Health check

Returns server status and registered tool count.

### `GET /mcp/openapi.json` — OpenAPI specification

Returns the `apiDefinition.swagger.json` spec for use with Power Platform connector registration.

---

## Tools

### `search_customers`

Search for customers by name, email, or phone.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search query |
| `limit` | integer | No | Max results (1–50, default: 10) |
| `status` | string | No | Filter: `active`, `inactive`, `lead`, `any` |

### `get_customer_details`

Get detailed profile for a specific customer.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `customer_id` | string | Yes | Customer ID (e.g. `CUST-001`) |
| `include_interactions` | boolean | No | Include recent interaction history (default: true) |

---

## Usage Examples

### Initialize (handshake)

```bash
curl -X POST http://localhost:3121/mcp \
  -H "Content-Type: application/json" \
  -H "x-ms-agentic-protocol: mcp" \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "initialize",
    "params": {}
  }'
```

### List tools

```bash
curl -X POST http://localhost:3121/mcp \
  -H "Content-Type: application/json" \
  -H "x-ms-agentic-protocol: mcp" \
  -d '{
    "jsonrpc": "2.0",
    "id": "2",
    "method": "tools/list"
  }'
```

### Call a tool (inline)

```bash
curl -X POST http://localhost:3121/mcp \
  -H "Content-Type: application/json" \
  -H "x-ms-agentic-protocol: mcp" \
  -d '{
    "jsonrpc": "2.0",
    "id": "3",
    "method": "tools/call",
    "params": {
      "name": "search_customers",
      "arguments": {
        "query": "acme",
        "status": "active"
      }
    }
  }'
```

### Call a tool (streaming)

```bash
curl -X POST http://localhost:3121/mcp \
  -H "Content-Type: application/json" \
  -H "x-ms-agentic-protocol: mcp" \
  -H "Accept: text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": "4",
    "method": "tools/call",
    "params": {
      "name": "get_customer_details",
      "arguments": {
        "customer_id": "CUST-001"
      }
    }
  }'
```

---

## Registering with Copilot Studio

1. In Copilot Studio, navigate to **Settings > Generative AI > Actions**.
2. Add a new **Connector** and point it to your MCP server URL.
3. The OpenAPI spec is auto-discovered at `http://your-server:3121/mcp/openapi.json`.
4. Copilot Studio's generative orchestration will:
   - Read the `x-ms-agentic-protocol` extension to enable MCP mode
   - Call `tools/list` to discover available tools
   - Invoke `tools/call` when the AI decides to use a tool

---

## Project Structure

```
copilot-studio/
├── apiDefinition.swagger.json   # OpenAPI 3.0 spec with MCP extensions
├── package.json                 # Node.js project manifest
├── tsconfig.json                # TypeScript configuration
├── server.ts                    # Express server + MCP protocol handler
├── tools/
│   ├── search-customers.ts      # Customer search tool
│   └── get-customer-details.ts  # Customer details tool
└── README.md                    # This file
```

---

## Extending with New Tools

1. Create a new file in `tools/` (e.g. `tools/create-order.ts`).
2. Export `definition` and `handler` matching the `ToolDefinition` and `ToolHandler` types.
3. In `server.ts`, import and register it:

```typescript
import { registerTool } from './server';
import { definition as createOrderDef, handler as createOrderHandler } from './tools/create-order';

registerTool(createOrderDef, createOrderHandler);
```

4. Rebuild and restart.

---

## License

Internal use — Power Platform / Copilot Studio connector template.
