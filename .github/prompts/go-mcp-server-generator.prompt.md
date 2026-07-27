---
name: go-mcp-server-generator
title: Go MCP Server Project Generator
description: Generate a complete Go MCP server project with proper structure, dependencies, and
  implementation using the official github.com/modelcontextprotocol/go-sdk.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: ''
tags:
  - backend
  - configuration
  - documentation
  - frontend
  - generator
  - go
  - mcp
  - prompts
  - typescript
trigger: /go-mcp-server-generator
---

# Go MCP Server Project GeneratorGenerate a complete, production-ready Model Context Protocol (MCP) server project in Go.## Project RequirementsYou will create a Go MCP server with:1. **Project Structure**: Proper Go module layout2. **Dependencies**: Official MCP SDK and necessary packages3. **Server Setup**: Configured MCP server with transports4. **Tools**: At least 2-3 useful tools with typed inputs/outputs5. **Error Handling**: Proper error handling and context usage6. **Documentation**: README with setup and usage instructions7. **Testing**: Basic test structure## Template Structure```myserver/├── go.mod├── go.sum├── main.go├── tools/│   ├── tool1.go│   └── tool2.go├── resources/│   └── resource1.go├── config/│   └── config.go├── README.md└── main_test.go```## go.mod Template```gomodule github.com/yourusername/{{PROJECT_NAME}}go 1.23require (    github.com/modelcontextprotocol/go-sdk v1.0.0)```## main.go Template> "github.com/modelcontextprotocol/go-sdk/mcp"> "github.com/yourusername/{{PROJECT_NAME}}/config"> **Full content:** `templates/go-mcp-server-generator/maingo_template.md`## tools/tool1.go Template> "github.com/modelcontextprotocol/go-sdk/mcp"> type Tool1Input struct {> **Full content:** `templates/go-mcp-server-generator/toolstool1go_template.md`## tools/registry.go Template```gopackage toolsimport "github.com/modelcontextprotocol/go-sdk/mcp"func RegisterTools(server *mcp.Server) {    RegisterTool1(server)    RegisterTool2(server)    // Register additional tools here}```## config/config.go Template```gopackage configimport "os"type Config struct {    ServerName string    Version    string    LogLevel   string}func Load() *Config {    return &Config{        ServerName: getEnv("SERVER_NAME", "{{PROJECT_NAME}}"),        Version:    getEnv("VERSION", "v1.0.0"),        LogLevel:   getEnv("LOG_LEVEL", "info"),    }}func getEnv(key, defaultValue string) string {    if value := os.Getenv(key); value != "" {        return value    }    return defaultValue}```## main_test.go Template> "github.com/yourusername/{{PROJECT_NAME}}/tools"> func TestTool1Handler(t *testing.T) {> **Full content:** `templates/go-mcp-server-generator/main_testgo_template.md`## README.md Template```markdown# {{PROJECT_NAME}}A Model Context Protocol (MCP) server built with Go.## Description{{PROJECT_DESCRIPTION}}## Installation\`\`\`bash go mod download go build -o {{PROJECT_NAME}} \`\`\`## UsageRun the server with stdio transport:\`\`\`bash ./{{PROJECT_NAME}} \`\`\`## ConfigurationConfigure via environment variables:- `SERVER_NAME`: Server name (default: "{{PROJECT_NAME}}")- `VERSION`: Server version (default: "v1.0.0")- `LOG_LEVEL`: Logging level (default: "info")## Available Tools### tool1{{TOOL1_DESCRIPTION}}**Input:**- `param1` (string, required): First parameter- `param2` (int, optional): Second parameter**Output:**- `result` (string): Operation result- `status` (string): Status of the operation## DevelopmentRun tests:\`\`\`bash go test ./... \`\`\`Build:\`\`\`bash go build -o {{PROJECT_NAME}} \`\`\`## LicenseMIT```## Generation InstructionsWhen generating a Go MCP server:1. **Initialize Module**: Create `go.mod` with proper module path2. **Structure**: Follow the template directory structure3. **Type Safety**: Use structs with JSON schema tags for all inputs/outputs4. **Error Handling**: Validate inputs, check context, wrap errors5. **Documentation**: Add clear descriptions and examples6. **Testing**: Include at least one test per tool7. **Configuration**: Use environment variables for config8. **Logging**: Use structured logging (log/slog)9. **Graceful Shutdown**: Handle signals properly10. **Transport**: Default to stdio, document alternatives## Best Practices- Keep tools focused and single-purpose- Use descriptive names for types and functions- Include JSON schema documentation in struct tags- Always respect context cancellation- Return descriptive errors- Keep main.go minimal, logic in packages- Write tests for tool handlers- Document all exported functions## Template ReferencesDetailed templates in `templates/go-mcp-server-generator/`:- `main_testgo_template.md`- `maingo_template.md`- `toolstool1go_template.md`