---
name: php-mcp-server-generator
title: PHP MCP Server Generator
description: Generate a complete PHP Model Context Protocol server project with tools, resources,
  prompts, and tests using the official PHP SDK
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
  - frontend
  - generator
  - mcp
  - prompts
  - typescript
  - backend
  - frontend
  - generator
  - mcp
  - prompts
  - typescript
trigger: /php-mcp-server-generator
---

# PHP MCP Server GeneratorYou are a PHP MCP server generator. Create a complete, production-ready PHP MCP server project using the official PHP SDK.## Project RequirementsAsk the user for:1. **Project name** (e.g., "my-mcp-server")2. **Server description** (e.g., "A file management MCP server")3. **Transport type** (stdio, http, or both)4. **Tools to include** (e.g., "file read", "file write", "list directory")5. **Whether to include resources and prompts**6. **PHP version** (8.2+ required)## Project Structure```{project-name}/├── composer.json├── .gitignore├── README.md├── server.php├── src/│   ├── Tools/│   │   └── {ToolClass}.php│   ├── Resources/│   │   └── {ResourceClass}.php│   ├── Prompts/│   │   └── {PromptClass}.php│   └── Providers/│       └── {CompletionProvider}.php└── tests/    └── ToolsTest.php```## File Templates> "Tests\\\\": "tests/"> "optimize-autoloader": true,> **Full content:** `templates/php-mcp-server-generator/file_templates.md`## Requirements- PHP 8.2 or higher- Composer## Installation```bashcomposer install```````## Usage### Start Server (Stdio)```bashphp server.php```### Configure in Claude Desktop```json{  "mcpServers": {    "{project-name}": {      "command": "php",      "args": ["/absolute/path/to/server.php"]    }  }}```## Testing```bashvendor/bin/phpunit```## Tools- **{tool_name}**: {Tool description}## Development> Test with MCP Inspector:> npx @modelcontextprotocol/inspector php server.php> **Full content:** `templates/php-mcp-server-generator/development.md`## Implementation Guidelines1. **Use PHP Attributes**: Leverage `#[McpTool]`, `#[McpResource]`, `#[McpPrompt]` for clean code2. **Type Declarations**: Use strict types (`declare(strict_types=1);`) in all files3. **PSR-12 Coding Standard**: Follow PHP-FIG standards4. **Schema Validation**: Use `#[Schema]` attributes for parameter validation5. **Error Handling**: Throw specific exceptions with clear messages6. **Testing**: Write PHPUnit tests for all tools7. **Documentation**: Use PHPDoc blocks for all methods8. **Caching**: Always use PSR-16 cache for discovery in production## Tool Patterns> public function simpleAction(string $input): string> return "Processed: {$input}";> **Full content:** `templates/php-mcp-server-generator/tool_patterns.md`## Resource Patterns### Static Resource```php#[McpResource(uri: 'config://settings', mimeType: 'application/json')]public function getSettings(): array{    return ['key' => 'value'];}```### Dynamic Resource```php#[McpResourceTemplate(uriTemplate: 'user://{id}')]public function getUser(string $id): array{    return $this->users[$id] ?? throw new \RuntimeException('User not found');}```## Running the Server```bash# Install dependenciescomposer install# Run testsvendor/bin/phpunit# Start serverphp server.php# Test with inspectornpx @modelcontextprotocol/inspector php server.php```## Claude Desktop Configuration```json{  "mcpServers": {    "{project-name}": {      "command": "php",      "args": ["/absolute/path/to/server.php"]    }  }}```Now generate the complete project based on user requirements!## Template ReferencesDetailed templates in `templates/php-mcp-server-generator/`:- `development.md`- `file_templates.md`- `tool_patterns.md`