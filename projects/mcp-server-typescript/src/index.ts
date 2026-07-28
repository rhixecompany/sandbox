#!/usr/bin/env node

/**
 * MCP Server — TypeScript
 *
 * A Model Context Protocol server exposing tools and resources
 * over stdio transport using @modelcontextprotocol/sdk.
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListResourcesRequestSchema,
  ListToolsRequestSchema,
  ReadResourceRequestSchema,
  ErrorCode,
  McpError,
} from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";

// ── Tool implementations ─────────────────────────────────────────────────────

import { greetTool, GreetArgsSchema } from "./tools/hello-world.js";
import { calculatorTool, CalculatorArgsSchema } from "./tools/calculator.js";

// ── Resource implementations ─────────────────────────────────────────────────

import { systemInfoResource, systemInfoRead } from "./resources/system-info.js";

// ── Tool registry ────────────────────────────────────────────────────────────

interface ToolEntry {
  definition: {
    name: string;
    description: string;
    inputSchema: Record<string, unknown>;
  };
  handler: (args: Record<string, unknown>) => Promise<{
    content: Array<{ type: string; text: string }>;
    isError?: boolean;
  }>;
  schema: z.ZodType<unknown>;
}

const tools: ToolEntry[] = [
  {
    definition: {
      name: "greet",
      description: "Greet a user with a friendly message. Supports optional title and emoji style.",
      inputSchema: {
        type: "object",
        properties: {
          name: { type: "string", description: "Name of the person to greet" },
          title: {
            type: "string",
            description: "Optional title (Mr., Ms., Dr., etc.)",
          },
          style: {
            type: "string",
            enum: ["casual", "formal", "enthusiastic"],
            description: "Greeting style",
          },
        },
        required: ["name"],
      },
    },
    handler: greetTool,
    schema: GreetArgsSchema,
  },
  {
    definition: {
      name: "calculator",
      description: "Perform arithmetic operations on two numbers.",
      inputSchema: {
        type: "object",
        properties: {
          a: { type: "number", description: "First operand" },
          b: { type: "number", description: "Second operand" },
          operation: {
            type: "string",
            enum: ["add", "subtract", "multiply", "divide", "power", "modulo"],
            description: "The arithmetic operation to perform",
          },
        },
        required: ["a", "b", "operation"],
      },
    },
    handler: calculatorTool,
    schema: CalculatorArgsSchema,
  },
];

// ── Resource registry ────────────────────────────────────────────────────────

interface ResourceEntry {
  definition: {
    uri: string;
    name: string;
    description: string;
    mimeType?: string;
  };
  handler: (uri: string) => Promise<{
    contents: Array<{ uri: string; mimeType?: string; text: string }>;
    isError?: boolean;
  }>;
}

const resources: ResourceEntry[] = [
  {
    definition: {
      uri: "mcp://system/info",
      name: "System Information",
      description: "Current system and runtime information including platform, memory, and CPU details",
      mimeType: "application/json",
    },
    handler: systemInfoRead,
  },
];

// ── Server initialisation ────────────────────────────────────────────────────

const server = new Server(
  {
    name: "typescript-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
      resources: {},
    },
  },
);

// ── Tool handlers ────────────────────────────────────────────────────────────

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: tools.map((t) => t.definition),
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const tool = tools.find((t) => t.definition.name === request.params.name);
  if (!tool) {
    throw new McpError(
      ErrorCode.MethodNotFound,
      `Unknown tool: ${request.params.name}`,
    );
  }

  try {
    const parsed = tool.schema.parse(request.params.arguments ?? {}) as Record<string, unknown>;
    const result = await tool.handler(parsed);
    return result;
  } catch (error) {
    if (error instanceof z.ZodError) {
      throw new McpError(
        ErrorCode.InvalidParams,
        `Invalid arguments: ${error.errors.map((e) => `${e.path.join(".")}: ${e.message}`).join("; ")}`,
      );
    }
    throw new McpError(
      ErrorCode.InternalError,
      error instanceof Error ? error.message : "Unknown error occurred",
    );
  }
});

// ── Resource handlers ────────────────────────────────────────────────────────

server.setRequestHandler(ListResourcesRequestSchema, async () => ({
  resources: resources.map((r) => r.definition),
}));

server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const resource = resources.find((r) => r.definition.uri === request.params.uri);
  if (!resource) {
    throw new McpError(
      ErrorCode.InvalidRequest,
      `Unknown resource: ${request.params.uri}`,
    );
  }

  try {
    return await resource.handler(request.params.uri);
  } catch (error) {
    throw new McpError(
      ErrorCode.InternalError,
      error instanceof Error ? error.message : "Unknown error reading resource",
    );
  }
});

// ── Start ────────────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCP server running on stdio transport");
}

main().catch((error) => {
  console.error("Server failed to start:", error);
  process.exit(1);
});
