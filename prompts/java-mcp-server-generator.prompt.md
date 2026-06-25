---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Java MCP Server Generator
name: java-mcp-server-generator
description: "Generate a complete Model Context Protocol server project in Java using the official MCP Java SDK with reactive streams and optional Spring Boot integration."
---

# Java MCP Server Generator

Generate a complete, production-ready MCP server in Java using the official Java SDK with Maven or Gradle.

## Project Generation

> When asked to create a Java MCP server, generate a complete project with this st
> ├── pom.xml (or build.gradle.kts)

> **Full content:** `templates/java-mcp-server-generator/project_generation.md`

## Maven pom.xml Template

> <?xml version="1.0" encoding="UTF-8"?>
> <project xmlns="http://maven.apache.org/POM/4.0.0"

> **Full content:** `templates/java-mcp-server-generator/maven_pomxml_template.md`

## Gradle build.gradle.kts Template

> group = "com.example"
> sourceCompatibility = JavaVersion.VERSION_17

> **Full content:** `templates/java-mcp-server-generator/gradle_buildgradlekts_template.md`

## McpServerApplication.java Template

> package com.example.mcp;
> import com.example.mcp.tools.ToolHandlers;

> **Full content:** `templates/java-mcp-server-generator/mcpserverapplicationjava_templ.md`

## ToolDefinitions.java Template

> package com.example.mcp.tools;
> import io.mcp.json.JsonSchema;

> **Full content:** `templates/java-mcp-server-generator/tooldefinitionsjava_template.md`

## ToolHandlers.java Template

> package com.example.mcp.tools;
> import com.fasterxml.jackson.databind.JsonNode;

> **Full content:** `templates/java-mcp-server-generator/toolhandlersjava_template.md`

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

## ResourceHandlers.java Template

> package com.example.mcp.resources;
> import io.mcp.server.McpServer;

> **Full content:** `templates/java-mcp-server-generator/resourcehandlersjava_template.md`

## PromptDefinitions.java Template

> package com.example.mcp.prompts;
> import io.mcp.server.prompt.Prompt;

> **Full content:** `templates/java-mcp-server-generator/promptdefinitionsjava_template.md`

## PromptHandlers.java Template

> package com.example.mcp.prompts;
> import io.mcp.server.McpServer;

> **Full content:** `templates/java-mcp-server-generator/prompthandlersjava_template.md`

## McpServerTest.java Template

> package com.example.mcp;
> import com.fasterxml.jackson.databind.ObjectMapper;

> **Full content:** `templates/java-mcp-server-generator/mcpservertestjava_template.md`

## README.md Template

````markdown
# My MCP Server

A Model Context Protocol server built with Java and the official MCP Java SDK.

## Features

- ✅ Tools: greet, calculate
- ✅ Resources: example data, configuration
- ✅ Prompts: code-review
- ✅ Reactive Streams with Project Reactor
- ✅ Structured logging with SLF4J
- ✅ Full test coverage

## Requirements

- Java 17 or later
- Maven 3.6+ or Gradle 7+

## Build

### Maven

```bash
mvn clean package
```
````

### Gradle

```bash
./gradlew build
```

## Run

### Maven

```bash
java -jar target/my-mcp-server-1.0.0.jar
```

### Gradle

```bash
./gradlew run
```

## Testing

### Maven

```bash
mvn test
```

### Gradle

```bash
./gradlew test
```

## Integration with Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "java",
      "args": ["-jar", "/path/to/my-mcp-server-1.0.0.jar"]
    }
  }
}
```

## License

MIT

```

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
10. **Provide both sync and async** examples
```

## Template References

Detailed section templates in `templates/java-mcp-server-generator/`:
- `gradle_buildgradlekts_template.md`
- `maven_pomxml_template.md`
- `mcpserverapplicationjava_templ.md`
- `mcpservertestjava_template.md`
- `project_generation.md`
- `promptdefinitionsjava_template.md`
- `prompthandlersjava_template.md`
- `resourcehandlersjava_template.md`
- `tooldefinitionsjava_template.md`
- `toolhandlersjava_template.md`
