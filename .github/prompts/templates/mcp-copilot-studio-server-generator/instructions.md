# Instructions

> Extracted from `mcp-copilot-studio-server-generator.prompt.md`.

## Instructions

Create a complete MCP server implementation that:

1. **Uses Copilot Studio MCP Pattern:**
   - Implement `x-ms-agentic-protocol: mcp-streamable-1.0`
   - Support JSON-RPC 2.0 communication protocol
   - Provide streamable HTTP endpoint at `/mcp`
   - Follow Power Platform connector structure

2. **Schema Compliance Requirements:**
   - **NO reference types** in tool inputs/outputs (filtered by Copilot Studio)
   - **Single type values only** (not arrays of multiple types)
   - **Avoid enum inputs** (interpreted as string, not enum)
   - Use primitive types: string, number, integer, boolean, array, object
   - Ensure all endpoints return full URIs

3. **MCP Components to Include:**
   - **Tools**: Functions for the language model to call (✅ Supported in Copilot Studio)
   - **Resources**: File-like data outputs from tools (✅ Supported in Copilot Studio - must be tool outputs to be accessible)
   - **Prompts**: Predefined templates for specific tasks (❌ Not yet supported in Copilot Studio)

4. **Implementation Structure:**
   ```
   /apiDefinition.swagger.json  (Power Platform connector schema)
   /apiProperties.json         (Connector metadata and configuration)
   /script.csx                 (Custom code transformations and logic)
   /server/                    (MCP server implementation)
   /tools/                     (Individual MCP tools)
   /resources/                 (MCP resource handlers)
   ```
