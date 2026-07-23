# ToolDefinitions.java Template

> Extracted from `java-mcp-server-generator.prompt.md`.

## ToolDefinitions.java Template

```java
package com.example.mcp.tools;

import io.mcp.json.JsonSchema;
import io.mcp.server.tool.Tool;

import java.util.List;

public class ToolDefinitions {

    public static List<Tool> getTools() {
        return List.of(
            createGreetTool(),
            createCalculateTool()
        );
    }

    private static Tool createGreetTool() {
        return Tool.builder()
            .name("greet")
            .description("Generate a greeting message")
            .inputSchema(JsonSchema.object()
                .property("name", JsonSchema.string()
                    .description("Name to greet")
                    .required(true)))
            .build();
    }

    private static Tool createCalculateTool() {
        return Tool.builder()
            .name("calculate")
            .description("Perform mathematical calculations")
            .inputSchema(JsonSchema.object()
                .property("operation", JsonSchema.string()
                    .description("Operation to perform")
                    .enumValues(List.of("add", "subtract", "multiply", "divide"))
                    .required(true))
                .property("a", JsonSchema.number()
                    .description("First operand")
                    .required(true))
                .property("b", JsonSchema.number()
                    .description("Second operand")
                    .required(true)))
            .build();
    }
}
```
