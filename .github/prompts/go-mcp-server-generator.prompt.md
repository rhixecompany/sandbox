---
name: go-mcp-server-generator
title: Go MCP Server Project Generator
description: 'Generate a complete Go MCP server project with proper structure, dependencies, and implementation using the official github.com/modelcontextprotocol/go-sdk.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: 'None'
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
dependencies: []
metadata:
  hermes: {}
---

## Goal

Generate a complete Go MCP server project with proper structure, dependencies, and implementation using the official github.com/modelcontextprotocol/go-sdk.

# Go MCP Server Project GeneratorGenerate a complete, production-ready Model Context Protocol (MCP) server project in Go.

## Project Requirements

You will create a Go MCP server with:1. **Project Structure**: Proper Go module layout2. **Dependencies**: Official MCP SDK and necessary packages3. **Server Setup**: Configured MCP server with transports4. **Tools**: At least 2-3 useful tools with typed inputs/outputs5. **Error Handling**: Proper error handling and context usage6. **Documentation**: README with setup and usage instructions7. **Testing**: Basic test structure

## Template Structure

```
myserver/├── go.mod├── go.sum├── main.go├── tools/│   ├── tool1.go│   └── tool2.go├── resources/│   └── resource1.go├── config/│   └── config.go├── README.md└── main_test.go
```

## go.mod Template

```go
module github.com/yourusername/

{PROJECT_NAME}}go 1.23require (    github.com/modelcontextprotocol/go-sdk v1.0.0)
```

## main.go Template

> "github.com/modelcontextprotocol/go-sdk/mcp"
> "github.com/yourusername/{{PROJECT_NAME}}/config"
> **Full content:**

## tools/tool1.go Template

> "github.com/modelcontextprotocol/go-sdk/mcp"
> type Tool1Input struct {
> **Full content:**

## tools/registry.go Template

```go
package toolsimport "github.com/modelcontextprotocol/go-sdk/mcp"func RegisterTools(server *mcp.Server) {    RegisterTool1(server)    RegisterTool2(server)    // Register additional tools here}
```

## config/config.go Template

```go
package configimport "os"type Config struct {    ServerName string    Version    string    LogLevel   string}func Load() *Config {    return &Config{        ServerName: getEnv("SERVER_NAME", "

{PROJECT_NAME}}"),        Version:    getEnv("VERSION", "v1.0.0"),        LogLevel:   getEnv("LOG_LEVEL", "info"),    }}func getEnv(key, defaultValue string) string {    if value := os.Getenv(key); value != "" {        return value    }    return defaultValue}
```

## main_test.go Template

> "github.com/yourusername/{{PROJECT_NAME}}/tools"
> func TestTool1Handler(t *testing.T) {
> **Full content:**

## README.md Template

```markdown
#

{PROJECT_NAME}}A Model Context Protocol (MCP) server built with Go.

## Description

{{PROJECT_DESCRIPTION}}

## Installation

\`\`\`bash go mod download go build -o

{PROJECT_NAME}} \`\`\`

## Usage

Run the server with stdio transport:\`\`\`bash ./{{PROJECT_NAME}} \`\`\`

## Configuration

Configure via environment variables:

- `SERVER_NAME`: Server name (default: "{{PROJECT_NAME}}")- `VERSION`: Server version (default: "v1.0.0")- `LOG_LEVEL`: Logging level (default: "info")

## Available Tools

### tool1

{TOOL1_DESCRIPTION}}**Input:**

- `param1` (string, required): First parameter- `param2` (int, optional): Second parameter**Output:**- `result` (string): Operation result- `status` (string): Status of the operation

## Development

Run tests:\`\`\`bash go test ./... \`\`\`Build:\`\`\`bash go build -o

{PROJECT_NAME}} \`\`\`

## License

MIT
```

## Generation Instructions

When generating a Go MCP server:1. **Initialize Module**: Create `go.mod` with proper module path2. **Structure**: Follow the template directory structure3. **Type Safety**: Use structs with JSON schema tags for all inputs/outputs4. **Error Handling**: Validate inputs, check context, wrap errors5. **Documentation**: Add clear descriptions and examples6. **Testing**: Include at least one test per tool7. **Configuration**: Use environment variables for config8. **Logging**: Use structured logging (log/slog)9. **Graceful Shutdown**: Handle signals properly10. **Transport**: Default to stdio, document alternatives

## Best Practices

- Keep tools focused and single-purpose
- Use descriptive names for types and functions
- Include JSON schema documentation in struct tags
- Always respect context cancellation
- Return descriptive errors
- Keep main.go minimal, logic in packages
- Write tests for tool handlers
- Document all exported functions

## Template References

Detailed templates in `templates/go-mcp-server-generator/`:- `main_testgo_template.md`- `maingo_template.md`- `toolstool1go_template.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.

## Phases

### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings clearly.
- Stop once the requested result is delivered.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Related Prompts

Other language variants of this MCP server generator:

| Language | Prompt |
| ---------- | -------- |
| TypeScript | [`typescript-mcp-server-generator.prompt.md`](typescript-mcp-server-generator.prompt.md) |
| Python | [`python-mcp-server-generator.prompt.md`](python-mcp-server-generator.prompt.md) |
| Rust | [`rust-mcp-server-generator.prompt.md`](rust-mcp-server-generator.prompt.md) |
| Swift | [`swift-mcp-server-generator.prompt.md`](swift-mcp-server-generator.prompt.md) |
| Kotlin | [`kotlin-mcp-server-generator.prompt.md`](kotlin-mcp-server-generator.prompt.md) |
| Java | [`java-mcp-server-generator.prompt.md`](java-mcp-server-generator.prompt.md) |
| C# | [`csharp-mcp-server-generator.prompt.md`](csharp-mcp-server-generator.prompt.md) |
| PHP | [`php-mcp-server-generator.prompt.md`](php-mcp-server-generator.prompt.md) |
| Ruby | [`ruby-mcp-server-generator.prompt.md`](ruby-mcp-server-generator.prompt.md) |
