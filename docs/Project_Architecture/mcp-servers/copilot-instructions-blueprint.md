# GitHub Copilot Instructions — mcp-servers

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Multi-language** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability and consistency across languages** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **TypeScript** — check `typescript/package.json` and `tsconfig.json`
   - **Python** — check `python/pyproject.toml` or `requirements.txt`
   - **Go** — check `go/go.mod`
   - **Rust** — check `rust/Cargo.toml`
   - **Java** — check `java/pom.xml` or `build.gradle`
   - **Kotlin** — check `kotlin/pom.xml` or `build.gradle.kts`
   - **PHP** — check `php/composer.json`
   - **Ruby** — check `ruby/Gemfile`
   - **Swift** — check `swift/Package.swift`
   - **C#** — check `csharp/*.csproj`

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **MCP Server SDK** — the common framework across all language implementations
   - Language-specific web server frameworks as detected

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - Each language directory is self-contained with its own build system
   - Respect version constraints from each language's package manager

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **folder-structure.md**: Project organization guidelines

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files in the same language directory
2. Analyze patterns for:
   - **MCP protocol implementation**: How the Model Context Protocol is implemented
   - **Server structure**: How each language organizes its MCP server
   - **Transport handling**: How transport layer is configured
   - **Tool/Resource definitions**: How tools and resources are defined
   - **Error handling**: Consistent patterns across language implementations
3. Follow the most consistent patterns found in the codebase for each language
4. When conflicting patterns exist, prioritize patterns in newer files
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow each language's idiomatic conventions
- Maintain consistency across language implementations where the MCP protocol allows
- Respect each language's standard tooling and build systems

## Documentation Requirements

- Match the level and style of comments found in existing code
- Document according to patterns observed in the codebase
- Follow existing patterns for documenting MCP-specific concepts

## Testing Approach

- Match the exact structure and style of existing tests
- Follow the testing patterns established in each language directory

## Technology-Specific Guidelines

### MCP Protocol
- Implement MCP specification for each language ecosystem
- Follow established patterns for server, transport, tool, and resource definitions
- Maintain consistency in protocol handling across languages

### Language Patterns
- Each language directory is self-contained with its own build config, source, and tests
- Follow language-specific best practices and idioms
- Use the language's standard package manager and build tools

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Follow the same approach to testing as seen in the codebase

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Multi-language MCP server implementations across 10 programming languages
- Each `<language>/` directory is self-contained with its own source, tests, and build config
- Shared patterns across implementations allow cross-language reference
- Refer to each subdirectory's README for language-specific setup
