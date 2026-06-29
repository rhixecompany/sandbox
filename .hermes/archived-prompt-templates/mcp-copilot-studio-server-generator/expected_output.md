# Expected Output

> Extracted from `mcp-copilot-studio-server-generator.prompt.md`.

## Expected Output

Generate:

1. **apiDefinition.swagger.json** with:
   - Proper `x-ms-agentic-protocol: mcp-streamable-1.0`
   - MCP endpoint at POST `/mcp`
   - Compliant schema definitions (no reference types)
   - McpResponse and McpErrorResponse definitions

2. **apiProperties.json** with:
   - Connector metadata and branding
   - Authentication configuration
   - Policy templates if needed

3. **script.csx** with:
   - Custom C# code for request/response transformations
   - MCP JSON-RPC message handling logic
   - Data validation and processing functions
   - Error handling and logging capabilities

4. **MCP Server Code** with:
   - JSON-RPC 2.0 request handler
   - Tool registration and execution
   - Resource management (as tool outputs)
   - Proper error handling
   - Copilot Studio compatibility checks

5. **Individual Tools** that:
   - Accept only primitive type inputs
   - Return structured outputs
   - Include resources as outputs when needed
   - Provide clear descriptions for Copilot Studio

6. **Deployment Configuration** for:
   - Power Platform environment
   - Copilot Studio agent integration
   - Testing and validation
