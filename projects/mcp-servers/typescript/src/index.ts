import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ErrorCode,
  McpError,
} from "@modelcontextprotocol/sdk/types.js";

import {
  GreetingInputSchema,
  generateGreeting,
} from "./tools/greeting.js";
import {
  CalculatorInputSchema,
  calculate,
} from "./tools/calculator.js";

/**
 * TypeScript MCP Server
 *
 * Provides two tools:
 *  - `greeting`: Generate a personalized greeting with configurable tone
 *  - `calculator`: Perform basic arithmetic operations
 *
 * Uses stdio transport for MCP communication.
 */
const server = new Server(
  {
    name: "typescript-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

/**
 * Handler that lists available tools and their schemas.
 */
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "greeting",
      description: "Generate a personalized greeting message",
      inputSchema: {
        type: "object",
        properties: {
          name: {
            type: "string",
            description: "The name of the person to greet",
          },
          title: {
            type: "string",
            description: "Optional title (e.g., Dr., Prof., Esq.)",
          },
          tone: {
            type: "string",
            enum: ["friendly", "formal", "enthusiastic"],
            description: "The tone of the greeting",
          },
        },
        required: ["name"],
      },
    },
    {
      name: "calculator",
      description: "Perform basic arithmetic operations (add, subtract, multiply, divide, power, modulo)",
      inputSchema: {
        type: "object",
        properties: {
          operation: {
            type: "string",
            enum: ["add", "subtract", "multiply", "divide", "power", "modulo"],
            description: "The arithmetic operation to perform",
          },
          a: {
            type: "number",
            description: "First operand",
          },
          b: {
            type: "number",
            description: "Second operand",
          },
        },
        required: ["operation", "a", "b"],
      },
    },
  ],
}));

/**
 * Handler that processes tool call requests.
 * Validates input with Zod, executes the tool, and returns a formatted response.
 */
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case "greeting": {
        if (args == null) {
          throw new McpError(ErrorCode.InvalidParams, "Arguments are required");
        }
        const input = GreetingInputSchema.parse(args);
        const greeting = generateGreeting(input);
        return {
          content: [
            {
              type: "text",
              text: greeting,
            },
          ],
        };
      }

      case "calculator": {
        if (args == null) {
          throw new McpError(ErrorCode.InvalidParams, "Arguments are required");
        }
        const input = CalculatorInputSchema.parse(args);
        const result = calculate(input);
        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      default:
        throw new McpError(
          ErrorCode.MethodNotFound,
          `Unknown tool: ${name}`
        );
    }
  } catch (error) {
    if (error instanceof McpError) {
      throw error;
    }

    // Zod validation errors
    if (error instanceof Error) {
      throw new McpError(ErrorCode.InvalidParams, error.message);
    }

    throw new McpError(
      ErrorCode.InternalError,
      "An unexpected error occurred"
    );
  }
});

/**
 * Main entry point.
 * Connects the server to stdio transport, logs startup info to stderr
 * (so as not to interfere with MCP communication on stdout).
 */
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);

  // Log to stderr so it doesn't interfere with stdout MCP protocol
  console.error("✅ typescript-mcp-server running on stdio transport");
  console.error("   Tools available: greeting, calculator");
}

main().catch((error: unknown) => {
  console.error("Fatal error starting server:", error);
  process.exit(1);
});
