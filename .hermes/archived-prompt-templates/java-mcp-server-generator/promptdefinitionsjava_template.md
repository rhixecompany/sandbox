# PromptDefinitions.java Template

> Extracted from `java-mcp-server-generator.prompt.md`.

## PromptDefinitions.java Template

```java
package com.example.mcp.prompts;

import io.mcp.server.prompt.Prompt;
import io.mcp.server.prompt.PromptArgument;

import java.util.List;

public class PromptDefinitions {

    public static List<Prompt> getPrompts() {
        return List.of(
            Prompt.builder()
                .name("code-review")
                .description("Generate a code review prompt")
                .argument(PromptArgument.builder()
                    .name("language")
                    .description("Programming language")
                    .required(true)
                    .build())
                .argument(PromptArgument.builder()
                    .name("focus")
                    .description("Review focus area")
                    .required(false)
                    .build())
                .build()
        );
    }
}
```
