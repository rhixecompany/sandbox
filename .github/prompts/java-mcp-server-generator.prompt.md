---
name: java-mcp-server-generator
title: Java MCP Server Generator
description: Generate a complete Model Context Protocol server project in Java using the official MCP Java SDK with reactive streams and optional Spring Boot integration.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
  - web
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - backend
  - frontend
  - generator
  - java
  - mcp
  - ml
  - prompts
  - typescript
trigger: /java-mcp-server-generator
dependencies: []
metadata:
  hermes: {}
---

## Goal

Generate a complete Model Context Protocol server project in Java using the official MCP Java SDK with reactive streams and optional Spring Boot integration.

# Java MCP Server GeneratorGenerate a complete, production-ready MCP server in Java using the official Java SDK with Maven or Gradle.

## Project Generation

> When asked to create a Java MCP server, generate a complete project with this st
> ├── pom.xml (or build.gradle.kts)
> **Full content:**

## Maven pom.xml Template

> <?xml version="1.0" encoding="UTF-8"?>
> <project xmlns="<http://maven.apache.org/POM/4.0.0>"
> **Full content:**

## Gradle build.gradle.kts Template

> group = "com.example"
> sourceCompatibility = JavaVersion.VERSION_17
> **Full content:**

## McpServerApplication.java Template

> package com.example.mcp;
> import com.example.mcp.tools.ToolHandlers;
> **Full content:**

## ToolDefinitions.java Template

> package com.example.mcp.tools;
> import io.mcp.json.JsonSchema;
> **Full content:**

## ToolHandlers.java Template

> package com.example.mcp.tools;
> import com.fasterxml.jackson.databind.JsonNode;
> **Full content:**

## ResourceDefinitions.java Template

```java
package com.example.mcp.resources;

import io.mcp.server.resource.Resource;

import java.util.List;

public class ResourceDefinitions {

    public static List<Resource> getResources() {
        return List.of(
            Resource.builder()
                .name("Example Data")
                .uri("resource://data/example")
                .description("Example resource data")
                .mimeType("application/json")
                .build(),
            Resource.builder()
                .name("Configuration")
                .uri("resource://config")
                .description("Server configuration")
                .mimeType("application/json")
                .build()
        );
    }
}
```
> getResources() {        return List.of(            Resource.builder()                .name("Example Data")                .uri("resource://data/example")                .description("Example resource data")                .mimeType("application/json")                .build(),            Resource.builder()                .name("Configuration")                .uri("resource://config")                .description("Server configuration")                .mimeType("application/json")                .build()        );    }}```

## ResourceHandlers.java Template

> package com.example.mcp.resources;
> import io.mcp.server.McpServer;
> **Full content:**

## PromptDefinitions.java Template

> package com.example.mcp.prompts;
> import io.mcp.server.prompt.Prompt;
> **Full content:**

## PromptHandlers.java Template

> package com.example.mcp.prompts;
> import io.mcp.server.McpServer;
> **Full content:**

## McpServerTest.java Template

> package com.example.mcp;
> import com.fasterxml.jackson.databind.ObjectMapper;
> **Full content:**

## README.md Template

````markdown

# My MCP Server

A Model Context Protocol server built with Java and the official MCP Java SDK.

## Feature

s- ✅ Tools: greet, calculate- ✅ Resources: example data, configuration- ✅ Prompts: code-review- ✅ Reactive Streams with Project Reactor- ✅ Structured logging with SLF4J- ✅ Full test coverage

## Requirements

- Java 17 or later
- Maven 3.6+ or Gradle 7+

## Build

### Maven

```

bashmvn clean package````
```

### Gradle

```

bash./gradlew build
```

## Run

### Maven

```

bashjava -jar target/my-mcp-server-1.0.0.jar
```

### Gradle

```

bash./gradlew run
```

## Test

ing

### Maven

```

bashmvn test
```

### Gradle

```

bash./gradlew test
```

## Integration with Claude Desktop

Add to `claude_desktop_config.json`:```json{  "mcpServers": {    "my-mcp-server": {      "command": "java",      "args": ["-jar", "/path/to/my-mcp-server-1.0.0.jar"]    }  }}```

## License

MIT```

## Generation Instructions

1. **Ask for project name and package**
2. **Choose build tool** (Maven or Gradle)
3. **Generate all files** with proper package structure
4. **Use Reactive Streams** for async handlers
5. **Include comprehensive logging** with SLF4J
6. **Add tests** for all handlers
7. **Follow Java conventions** (camelCase, PascalCase)
8. **Include error handling** with proper responses
9. **Document public APIs** with Javadoc
1
0. **Provide both sync and async** examples```

## Template References

Detailed section templates in `templates/java-mcp-server-generator/`:- `gradle_buildgradlekts_template.md`- `maven_pomxml_template.md`- `mcpserverapplicationjava_templ.md`- `mcpservertestjava_template.md`- `project_generation.md`- `promptdefinitionsjava_template.md`- `prompthandlersjava_template.md`- `resourcehandlersjava_template.md`- `tooldefinitionsjava_template.md`- `toolhandlersjava_template.md`

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

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

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
| Kotlin | [`kotlin-mcp-server-generator.prompt.md`](kotlin-mcp-server-generator.prompt.md) |
| C# | [`csharp-mcp-server-generator.prompt.md`](csharp-mcp-server-generator.prompt.md) |
| PHP | [`php-mcp-server-generator.prompt.md`](php-mcp-server-generator.prompt.md) |
| Ruby | [`ruby-mcp-server-generator.prompt.md`](ruby-mcp-server-generator.prompt.md) |
