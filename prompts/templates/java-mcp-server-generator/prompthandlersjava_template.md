# PromptHandlers.java Template

> Extracted from `java-mcp-server-generator.prompt.md`.

## PromptHandlers.java Template

```java
package com.example.mcp.prompts;

import io.mcp.server.McpServer;
import io.mcp.server.prompt.PromptMessage;
import io.mcp.server.prompt.PromptResult;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import reactor.core.publisher.Mono;

import java.util.List;
import java.util.Map;

public class PromptHandlers {

    private static final Logger log = LoggerFactory.getLogger(PromptHandlers.class);

    public static void register(McpServer server) {
        // Register prompt list handler
        server.addPromptListHandler(() -> {
            log.debug("Listing available prompts");
            return Mono.just(PromptDefinitions.getPrompts());
        });

        // Register prompt get handler
        server.addPromptGetHandler(PromptHandlers::handleCodeReview);
    }

    private static Mono<PromptResult> handleCodeReview(String name, Map<String, String> arguments) {
        log.info("Getting prompt: {}", name);

        if (!name.equals("code-review")) {
            return Mono.error(new IllegalArgumentException("Unknown prompt: " + name));
        }

        String language = arguments.getOrDefault("language", "Java");
        String focus = arguments.getOrDefault("focus", "general quality");

        String description = "Code review for " + language + " with focus on " + focus;

        List<PromptMessage> messages = List.of(
            PromptMessage.user("Please review this " + language + " code with focus on " + focus + "."),
            PromptMessage.assistant("I'll review the code focusing on " + focus + ". Please share the code."),
            PromptMessage.user("Here's the code to review: [paste code here]")
        );

        log.debug("Generated code review prompt for {} ({})", language, focus);

        return Mono.just(PromptResult.builder()
            .description(description)
            .messages(messages)
            .build());
    }
}
```
