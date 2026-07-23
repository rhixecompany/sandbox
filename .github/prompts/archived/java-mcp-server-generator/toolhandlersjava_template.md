# ToolHandlers.java Template

> Extracted from `java-mcp-server-generator.prompt.md`.

## ToolHandlers.java Template

```java
package com.example.mcp.tools;

import com.fasterxml.jackson.databind.JsonNode;
import io.mcp.server.McpServer;
import io.mcp.server.tool.ToolResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import reactor.core.publisher.Mono;

public class ToolHandlers {

    private static final Logger log = LoggerFactory.getLogger(ToolHandlers.class);

    public static void register(McpServer server) {
        // Register tool list handler
        server.addToolListHandler(() -> {
            log.debug("Listing available tools");
            return Mono.just(ToolDefinitions.getTools());
        });

        // Register greet handler
        server.addToolHandler("greet", ToolHandlers::handleGreet);

        // Register calculate handler
        server.addToolHandler("calculate", ToolHandlers::handleCalculate);
    }

    private static Mono<ToolResponse> handleGreet(JsonNode arguments) {
        log.info("Greet tool called");

        if (!arguments.has("name")) {
            return Mono.just(ToolResponse.error()
                .message("Missing 'name' parameter")
                .build());
        }

        String name = arguments.get("name").asText();
        String greeting = "Hello, " + name + "! Welcome to MCP.";

        log.debug("Generated greeting for: {}", name);

        return Mono.just(ToolResponse.success()
            .addTextContent(greeting)
            .build());
    }

    private static Mono<ToolResponse> handleCalculate(JsonNode arguments) {
        log.info("Calculate tool called");

        if (!arguments.has("operation") || !arguments.has("a") || !arguments.has("b")) {
            return Mono.just(ToolResponse.error()
                .message("Missing required parameters")
                .build());
        }

        String operation = arguments.get("operation").asText();
        double a = arguments.get("a").asDouble();
        double b = arguments.get("b").asDouble();

        double result;
        switch (operation) {
            case "add":
                result = a + b;
                break;
            case "subtract":
                result = a - b;
                break;
            case "multiply":
                result = a * b;
                break;
            case "divide":
                if (b == 0) {
                    return Mono.just(ToolResponse.error()
                        .message("Division by zero")
                        .build());
                }
                result = a / b;
                break;
            default:
                return Mono.just(ToolResponse.error()
                    .message("Unknown operation: " + operation)
                    .build());
        }

        log.debug("Calculation: {} {} {} = {}", a, operation, b, result);

        return Mono.just(ToolResponse.success()
            .addTextContent("Result: " + result)
            .build());
    }
}
```
