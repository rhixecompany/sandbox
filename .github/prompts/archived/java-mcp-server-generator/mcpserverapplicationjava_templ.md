# McpServerApplication.java Template

> Extracted from `java-mcp-server-generator.prompt.md`.

## McpServerApplication.java Template

```java
package com.example.mcp;

import com.example.mcp.tools.ToolHandlers;
import com.example.mcp.resources.ResourceHandlers;
import com.example.mcp.prompts.PromptHandlers;
import io.mcp.server.McpServer;
import io.mcp.server.McpServerBuilder;
import io.mcp.server.transport.StdioServerTransport;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import reactor.core.Disposable;

public class McpServerApplication {

    private static final Logger log = LoggerFactory.getLogger(McpServerApplication.class);

    public static void main(String[] args) {
        log.info("Starting MCP Server...");

        try {
            McpServer server = createServer();
            StdioServerTransport transport = new StdioServerTransport();

            // Start server
            Disposable serverDisposable = server.start(transport).subscribe();

            // Graceful shutdown
            Runtime.getRuntime().addShutdownHook(new Thread(() -> {
                log.info("Shutting down MCP server");
                serverDisposable.dispose();
                server.stop().block();
            }));

            log.info("MCP Server started successfully");

            // Keep running
            Thread.currentThread().join();

        } catch (Exception e) {
            log.error("Failed to start MCP server", e);
            System.exit(1);
        }
    }

    private static McpServer createServer() {
        McpServer server = McpServerBuilder.builder()
            .serverInfo("my-mcp-server", "1.0.0")
            .capabilities(capabilities -> capabilities
                .tools(true)
                .resources(true)
                .prompts(true))
            .build();

        // Register handlers
        ToolHandlers.register(server);
        ResourceHandlers.register(server);
        PromptHandlers.register(server);

        return server;
    }
}
```
