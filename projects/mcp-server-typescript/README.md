# TypeScript MCP Server

A production-ready [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server built with TypeScript, featuring tools and resources over stdio transport using `@modelcontextprotocol/sdk`.

## Features

- **Stdio transport** — Communicates via standard input/output
- **Two example tools**:
    - `greet` — Friendly greeting with style/customization options
    - `calculator` — Arithmetic operations with edge-case handling
- **One system resource** — `mcp://system/info` exposing runtime diagnostics
- **Schema validation** — All tools validated with Zod
- **TypeScript + ES modules** — Strict mode, declaration maps, source maps

## Quick Start

```bash
# Install dependencies
npm install

# Build
npm run build

# Run (stdio transport)
npm start

# Or run in dev mode (no build step)
npm run dev
```

## MCP Inspector (Recommended for testing)

```bash
# With built output
npm run inspect

# Or directly with dev server
npm run inspect:dev
```

Then open the Inspector URL in your browser (default: http://localhost:6274).

## Connect from an MCP Client

```json
{
  "mcpServers": {
    "typescript-server": {
      "command": "node",
      "args": ["dist/index.js"],
      "cwd": "/path/to/projects/mcp-server-typescript"
    }
  }
}
```

Or with `tsx` (no build step):

```json
{
  "mcpServers": {
    "typescript-server": {
      "command": "tsx",
      "args": ["src/index.ts"],
      "cwd": "/path/to/projects/mcp-server-typescript"
    }
  }
}
```

## Available Tools

### `greet`

Greet a user with a friendly message.

**Arguments:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Name of the person to greet |
| `title` | string | No | Optional title (Mr., Ms., Dr., etc.) |
| `style` | enum | No | `"casual"` (default), `"formal"`, `"enthusiastic"` |

**Example:**

```json
{
  "name": "Hermes",
  "title": "Dr.",
  "style": "formal"
}
```

### `calculator`

Perform arithmetic operations on two numbers.

**Arguments:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `a` | number | Yes | First operand |
| `b` | number | Yes | Second operand |
| `operation` | enum | Yes | `"add"`, `"subtract"`, `"multiply"`, `"divide"`, `"power"`, `"modulo"` |

**Example:**

```json
{
  "a": 10,
  "b": 3,
  "operation": "divide"
}
```

## Available Resources

### `mcp://system/info`

System and runtime information (read-only).

**Returns:** JSON with:

- Hostname, platform, OS type/release, architecture
- Node.js version
- Uptime (seconds)
- Memory: total, free, used bytes + free percentage
- CPU: model, core count, speed (MHz)
- Timestamp (ISO 8601)

## Project Structure

```
projects/mcp-server-typescript/
├── package.json
├── tsconfig.json
├── README.md
├── src/
│   ├── index.ts              # Server entry point & registration
│   ├── tools/
│   │   ├── hello-world.ts    # greet tool
│   │   └── calculator.ts     # calculator tool
│   └── resources/
│       └── system-info.ts    # system-info resource
└── dist/                     # Compiled output (after npm run build)
```

## Adding a New Tool

1. Create `src/tools/my-tool.ts` with a Zod schema + handler
2. Export `MyToolArgsSchema` and `myTool` handler
3. Import and register in `src/index.ts`:

   ```typescript
   import { myTool, MyToolArgsSchema } from "./tools/my-tool.js";
   
   const tools: ToolEntry[] = [
     // ...existing tools
     {
       definition: { name: "my-tool", description: "...", inputSchema: {...} },
       handler: myTool,
       schema: MyToolArgsSchema,
     },
   ];
   ```

## Adding a New Resource

1. Create `src/resources/my-resource.ts` with handler + metadata
2. Import and register in `src/index.ts`:

   ```typescript
   import { myResourceRead, myResource } from "./resources/my-resource.js";
   
   const resources: ResourceEntry[] = [
     // ...existing resources
     { definition: myResource, handler: myResourceRead },
   ];
   ```

## Scripts

| Command | Description |
|---------|-------------|
| `npm run build` | Compile TypeScript to `dist/` |
| `npm start` | Run built server (stdio) |
| `npm run dev` | Run with `tsx` (no build) |
| `npm run inspect` | Open MCP Inspector with built server |
| `npm run inspect:dev` | Open MCP Inspector with dev server |
| `npm run typecheck` | Type-check without emitting |
| `npm run clean` | Remove `dist/` |

## Requirements

- Node.js 18+ (ESM support)
- npm / pnpm / yarn

## License

MIT
