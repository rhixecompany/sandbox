# TypeScript MCP Server

A production-ready [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server written in TypeScript, providing **greeting** and **calculator** tools over stdio transport.

## Features

- ✅ **Greeting tool** — Generate personalized greetings with configurable tone (friendly, formal, enthusiastic)
- ✅ **Calculator tool** — Perform arithmetic operations (add, subtract, multiply, divide, power, modulo)
- ✅ **TypeScript** — Strict mode, ES modules, full type safety
- ✅ **Zod validation** — Runtime input validation with descriptive error messages
- ✅ **Error handling** — Proper MCP error codes and structured error responses
- ✅ **stdio transport** — Lightweight, composable with any MCP client

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) >= 18.x
- npm (comes with Node.js) or [bun](https://bun.sh/)

### Installation

```bash
# Clone or navigate to the project directory
cd projects/mcp-servers/typescript

# Install dependencies
npm install

# Build the TypeScript source
npm run build
```

### Running the Server

```bash
# Start the server (stdio transport)
npm start
```

Or with hot-reload during development:

```bash
npm run dev
```

### Testing the Server

You can test the server with any MCP client (e.g., the [MCP Inspector](https://github.com/modelcontextprotocol/inspector)):

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

Or test manually from another shell by piping JSON-RPC messages:

```bash
# List available tools
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | node dist/index.js

# Call the greeting tool
echo '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"greeting","arguments":{"name":"Alice","tone":"enthusiastic"}}}' | node dist/index.js

# Call the calculator tool
echo '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"calculator","arguments":{"operation":"multiply","a":6,"b":7}}}' | node dist/index.js
```

## Tools Reference

### `greeting`

Generate a personalized greeting message.

| Parameter | Type   | Required | Default     | Description                             |
|-----------|--------|----------|-------------|-----------------------------------------|
| `name`    | string | Yes      | —           | The name of the person to greet         |
| `title`   | string | No       | `""`        | Optional title (e.g., Dr., Prof., Esq.) |
| `tone`    | string | No       | `"friendly"`| One of: `friendly`, `formal`, `enthusiastic` |

### `calculator`

Perform basic arithmetic operations.

| Parameter   | Type   | Required | Description                                    |
|-------------|--------|----------|------------------------------------------------|
| `operation` | string | Yes      | One of: `add`, `subtract`, `multiply`, `divide`, `power`, `modulo` |
| `a`         | number | Yes      | First operand                                  |
| `b`         | number | Yes      | Second operand                                 |

## Project Structure

```
typescript/
├── package.json          # Dependencies and scripts
├── tsconfig.json         # TypeScript configuration (strict, ES modules)
├── README.md             # This file
└── src/
    ├── index.ts          # Server entry point — stdio transport, tool handlers
    └── tools/
        ├── greeting.ts   # Greeting tool: schema + logic
        └── calculator.ts # Calculator tool: schema + logic
```

## Error Handling

The server uses structured MCP error codes:

- **InvalidParams** — Missing or incorrectly typed arguments
- **MethodNotFound** — Request for a non-existent tool
- **InternalError** — Unexpected runtime failures

All errors are returned as properly formatted MCP error responses, making them easy to handle on the client side.

## License

MIT
