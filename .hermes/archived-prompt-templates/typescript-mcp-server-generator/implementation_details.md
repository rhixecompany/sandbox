# Implementation Details

> Extracted from `typescript-mcp-server-generator.prompt.md`.

## Implementation Details

### Project Setup

- Initialize with `npm init` and create package.json
- Install dependencies: `@modelcontextprotocol/sdk`, `zod@3`, and transport-specific packages
- Configure TypeScript with ES modules: `"type": "module"` in package.json
- Add dev dependencies: `tsx` or `ts-node` for development
- Create proper .gitignore file

### Server Configuration

- Use `McpServer` class for high-level implementation
- Set server name and version
- Choose appropriate transport (StreamableHTTPServerTransport or StdioServerTransport)
- For HTTP: set up Express with proper middleware and error handling
- For stdio: use StdioServerTransport directly

### Tool Implementation

- Use `registerTool()` method with descriptive names
- Define schemas using zod for input and output validation
- Provide clear `title` and `description` fields
- Return both `content` and `structuredContent` in results
- Implement proper error handling with try-catch blocks
- Support async operations where appropriate

### Resource/Prompt Setup (Optional)

- Add resources using `registerResource()` with ResourceTemplate for dynamic URIs
- Add prompts using `registerPrompt()` with argument schemas
- Consider adding completion support for better UX

### Code Quality

- Use TypeScript for type safety
- Follow async/await patterns consistently
- Implement proper cleanup on transport close events
- Use environment variables for configuration
- Add inline comments for complex logic
- Structure code with clear separation of concerns
