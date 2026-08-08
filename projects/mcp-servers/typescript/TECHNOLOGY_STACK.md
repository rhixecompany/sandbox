# 🏗 Technology Stack Blueprint - mcp-servers/typescript

**Project Path:** `projects/mcp-servers/typescript`
**Generated:** 2026-07-28
**Status:** Active — TypeScript MCP Server Reference Implementation

---

## Core Technologies

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Runtime** | Node.js | 18+ | MIT |
| **Language** | TypeScript | ^5.8.3 | Apache-2.0 |
| **MCP SDK** | @modelcontextprotocol/sdk | ^1.9.0 | MIT |
| **Validation** | zod | ^3.24.4 | MIT |
| **Build System** | TypeScript (tsc) | ^5.8.3 | Apache-2.0 |
| **Dev Runtime** | tsx | ^4.19.4 | MIT |

---

## Architecture

**Pattern:** MCP (Model Context Protocol) Server

- **Transport:** STDIO (stdio transport)
- **Tools:** Greeting + Calculation tools
- **Resources:** File system / configuration access

### Project Structure

```
mcp-servers/typescript/
├── src/
│   ├── index.ts              # Entry point
│   ├── tools/                # Tool implementations
│   │   ├── greeting.ts
│   │   └── calculator.ts
│   └── resources/            # Resource implementations
├── dist/                     # Compiled output (gitignored)
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
    "@modelcontextprotocol/sdk": "^1.9.0",
    "zod": "^3.24.4"
  }
}
```

### Development

```json
{
  "devDependencies": {
    "typescript": "^5.8.3",
    "@types/node": "^22.14.1",
    "tsx": "^4.19.4"
  }
}
```

---

## TypeScript Configuration (`tsconfig.json`)

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "resolveJsonModule": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

---

## Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| `build` | `tsc` | Compile TypeScript to `dist/` |
| `start` | `node dist/index.js` | Run compiled server |
| `dev` | `tsx watch src/index.ts` | Run with hot reload |
| `inspect` | `bunx @modelcontextprotocol/inspector node dist/index.js` | Debug with MCP Inspector |
| `inspect:dev` | `bunx @modelcontextprotocol/inspector tsx src/index.ts` | Debug without build |
| `clean` | `rm -rf dist` | Remove build output |
| `typecheck` | `tsc --noEmit` | Type check only |

---

## Entry Point (`src/index.ts`)

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { registerGreetingTool } from "./tools/greeting.js";
import { registerCalculatorTool } from "./tools/calculator.js";

const server = new McpServer({
  name: "typescript-mcp-server",
  version: "1.0.0",
});

// Register tools
registerGreetingTool(server);
registerCalculatorTool(server);

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
console.error("TypeScript MCP Server running on stdio");
```

---

## Tool Implementation (`src/tools/greeting.ts`)

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

export function registerGreetingTool(server: McpServer) {
  server.tool(
    "greet",
    "Greet a person by name",
    {
      name: z.string().describe("The name of the person to greet"),
    },
    async ({ name }) => ({
      content: [{ type: "text", text: `Hello, ${name}!` }],
    })
  );
}
```

---

## Tool Implementation (`src/tools/calculator.ts`)

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

export function registerCalculatorTool(server: McpServer) {
  server.tool(
    "calculate",
    "Perform basic arithmetic operations",
    {
      operation: z.enum(["add", "subtract", "multiply", "divide"]),
      a: z.number(),
      b: z.number(),
    },
    async ({ operation, a, b }) => {
      let result: number;
      switch (operation) {
        case "add": result = a + b; break;
        case "subtract": result = a - b; break;
        case "multiply": result = a * b; break;
        case "divide": 
          if (b === 0) throw new Error("Division by zero");
          result = a / b; 
          break;
      }
      return {
        content: [{ type: "text", text: `Result: ${result}` }],
      };
    }
  );
}
```

---

## Commands

```bash
# Install dependencies
bun install

# Development (hot reload)
bun run dev

# Type check
bun run typecheck

# Build
bun run build

# Start production
bun run start

# Debug with Inspector
bun run inspect:dev

# Clean
bun run clean
```

---

## Quality Gates

| Check | Command |
|-------|---------|
| **Type Check** | `bun run typecheck` |
| **Build** | `bun run build` |
| **Format** | `bunx prettier --check .` (if configured) |
| **Lint** | `bunx eslint .` (if configured) |

---

## License

MIT

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*
