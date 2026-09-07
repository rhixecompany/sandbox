---
name: kotlin-mcp-server-generator
title: Kotlin MCP Server Project Generator
description: Generate a complete Kotlin MCP server project with proper structure, dependencies, and implementation
  using the official io.modelcontextprotocol:kotlin-sdk library.
version: 1.0.0
license: MIT
author: Hermes Agent
trigger: /kotlin-mcp-server-generator
toolsets:
- file
- terminal
skills: []
dependencies: []
formatter: default
metadata:
  hermes:
    profile: code-architect
    mcp_servers: []
    context_size: large
  copilot:
    context_size: large
    extensions: []
    keybinding: null
  opencode:
    command: opencode /kotlin-mcp-server-generator
    flags: {}
    help: Generate a complete Kotlin MCP server project with proper structure, dependen...
  codex:
    model_override: null
    system_prompt_id: null
    temperature: null
    max_tokens: null
tags:
- agent-type:hermes
- backend
- frontend
- generator
- mcp
- prompts
- typescript
- configuration
scripts: []
## Goal

Generate a complete Kotlin MCP server project with proper structure, dependencies, and implementation using the official io.modelcontextprotocol:kotlin-sdk library.

# Kotlin MCP Server Project GeneratorGenerate a complete, production-ready Model Context Protocol (MCP) server project in Kotlin.

## Project Requirements

You will create a Kotlin MCP server with:1. **Project Structure**: Gradle-based Kotlin project layout2. **Dependencies**: Official MCP SDK, Ktor, and kotlinx libraries3. **Server Setup**: Configured MCP server with transports4. **Tools**: At least 2-3 useful tools with typed inputs/outputs5. **Error Handling**: Proper exception handling and validation6. **Documentation**: README with setup and usage instructions7. **Testing**: Basic test structure with coroutines

## Template Structure

```

myserver/├── build.gradle.kts├── settings.gradle.kts├── gradle.properties├── src/│   ├── main/│   │   └── kotlin/│   │       └── com/example/myserver/│   │           ├── Main.kt│   │           ├── Server.kt│   │           ├── config/│   │           │   └── Config.kt│   │           └── tools/│   │               ├── Tool1.kt│   │               └── Tool2.kt│   └── test/│       └── kotlin/│           └── com/example/myserver/│               └── ServerTest.kt└── README.md
```

## build.gradle.kts Template

> kotlin("jvm") version "2.1.0"
> kotlin("plugin.serialization") version "2.1.0"
> **Full content:**

## settings.gradle.kts Template

```kotlin

rootProject.name = "

{PROJECT_NAME}}"
```

## Main.kt Template

```kotlin

package com.example.myserverimport io.modelcontextprotocol.kotlin.sdk.server.StdioServerTransportimport kotlinx.coroutines.runBlockingimport io.github.oshai.kotlinlogging.KotlinLoggingprivate val logger = KotlinLogging.logger

}fun main() = runBlocking {    logger.info { "Starting MCP server..." }    val config = loadConfig()    val server = createServer(config)    // Use stdio transport    val transport = StdioServerTransport()    logger.info { "Server '${config.name}' v${config.version} ready" }    server.connect(transport)}
```

## Server.kt Template

> package com.example.myserver
> import io.modelcontextprotocol.kotlin.sdk.server.Server
> **Full content:**

## Config.kt Template

```kotlin

package com.example.myserver.configimport kotlinx.serialization.Serializable@Serializabledata class Config(    val name: String = "

{PROJECT_NAME}}",    val version: String = "1.0.0",    val description: String = "{{PROJECT_DESCRIPTION}}")fun loadConfig(): Config {    return Config(        name = System.getenv("SERVER_NAME") ?: "{{PROJECT_NAME}}",        version = System.getenv("VERSION") ?: "1.0.0",        description = System.getenv("DESCRIPTION") ?: "{{PROJECT_DESCRIPTION}}"    )}
```

## Tool1.kt Template

> package com.example.myserver.tools
> import io.modelcontextprotocol.kotlin.sdk.server.Server
> **Full content:**

## tools/ToolRegistry.kt Template

```kotlin
package com.example.myserver.tools

import io.modelcontextprotocol.kotlin.sdk.server.Server

fun Server.registerTools() {
    registerTool1()
    registerTool2()
    // Register additional tools here
}
```

## ServerTest.kt Template

> package com.example.myserver
> import kotlinx.coroutines.test.runTest
> **Full content:**

## README.md Template

```markdown

#

{PROJECT_NAME}}A Model Context Protocol (MCP) server built with Kotlin.

## Description

{{PROJECT_DESCRIPTION}}

## Requirements

- Java 17 or higher
- Kotlin 2.1.0

## Installation

Build the project:\`\`\`bash ./gradlew build \`\`\`

## Usage

Run the server with stdio transport:\`\`\`bash ./gradlew run \`\`\`Or build and run the jar:\`\`\`bash ./gradlew installDist ./build/install/{{PROJECT_NAME}}/bin/{{PROJECT_NAME}} \`\`\`

## Configuration

Configure via environment variables:

- `SERVER_NAME`: Server name (default: "{{PROJECT_NAME}}")- `VERSION`: Server version (default: "1.0.0")- `DESCRIPTION`: Server description

## Available Tools

### tool1

{TOOL1_DESCRIPTION}}**Input:**

- `param1` (string, required): First parameter- `param2` (integer, optional): Second parameter**Output:**- Text result of the operation

## Development

Run tests:\`\`\`bash ./gradlew test \`\`\`Build:\`\`\`bash ./gradlew build \`\`\`Run with auto-reload (development):\`\`\`bash ./gradlew run --continuous \`\`\`

## Multiplatform

This project uses Kotlin Multiplatform and can target JVM, Wasm, and iOS. See `build.gradle.kts` for platform configuration.

## License

MIT
```

## Generation Instructions

When generating a Kotlin MCP server:1. **Gradle Setup**: Create proper `build.gradle.kts` with all dependencies2. **Package Structure**: Follow Kotlin package conventions3. **Type Safety**: Use data classes and kotlinx.serialization4. **Coroutines**: All operations should be suspending functions5. **Error Handling**: Use Kotlin exceptions and validation6. **JSON Schemas**: Use `buildJsonObject` for tool schemas7. **Testing**: Include coroutine test utilities8. **Logging**: Use kotlin-logging for structured logging9. **Configuration**: Use data classes and environment variables10. **Documentation**: KDoc comments for public APIs

## Best Practices

- Use suspending functions for all async operations
- Leverage Kotlin's null safety and type system
- Use data classes for structured data
- Apply kotlinx.serialization for JSON handling
- Use sealed classes for result types
- Implement proper error handling with Result/Either patterns
- Write tests using kotlinx-coroutines-test
- Use dependency injection for testability
- Follow Kotlin coding conventions
- Use meaningful names and KDoc comments

## Transport Options

### Stdio Transport

```

kotlinval transport = StdioServerTransport()server.connect(transport)

```

### SSE Transport (Ktor)

```

kotlinembeddedServer(Netty, port = 8080) {    mcp {        Server(/*...*/) { "Description" }    }}.start(wait = true)

```

## Multiplatform Configuration

For multiplatform projects, add to `build.gradle.kts`:```kotlinkotlin {    jvm()    js(IR) { nodejs() }    wasmJs()    sourceSets {        commonMain.dependencies {            implementation("io.modelcontextprotocol:kotlin-sdk:0.7.2")        }    }}```

## Template References

Detailed templates in `templates/kotlin-mcp-server-generator/`:- `buildgradlekts_template.md`- `serverkt_template.md`- `servertestkt_template.md`- `tool1kt_template.md`

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

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

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
| Go | [`go-mcp-server-generator.prompt.md`](go-mcp-server-generator.prompt.md) |
| Swift | [`swift-mcp-server-generator.prompt.md`](swift-mcp-server-generator.prompt.md) |
| Java | [`java-mcp-server-generator.prompt.md`](java-mcp-server-generator.prompt.md) |
| C# | [`csharp-mcp-server-generator.prompt.md`](csharp-mcp-server-generator.prompt.md) |
| PHP | [`php-mcp-server-generator.prompt.md`](php-mcp-server-generator.prompt.md) |
| Ruby | [`ruby-mcp-server-generator.prompt.md`](ruby-mcp-server-generator.prompt.md) |

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section