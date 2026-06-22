# McpServerTest.java Template

> Extracted from `java-mcp-server-generator.prompt.md`.

## McpServerTest.java Template

```java
package com.example.mcp;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import io.mcp.server.McpServer;
import io.mcp.server.McpSyncServer;
import io.mcp.server.tool.ToolResponse;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class McpServerTest {

    private McpSyncServer syncServer;
    private ObjectMapper objectMapper;

    @BeforeEach
    void setUp() {
        McpServer server = createTestServer();
        syncServer = server.toSyncServer();
        objectMapper = new ObjectMapper();
    }

    private McpServer createTestServer() {
        // Same setup as main application
        McpServer server = McpServerBuilder.builder()
            .serverInfo("test-server", "1.0.0")
            .capabilities(cap -> cap.tools(true))
            .build();

        // Register handlers
        ToolHandlers.register(server);

        return server;
    }

    @Test
    void testGreetTool() {
        ObjectNode args = objectMapper.createObjectNode();
        args.put("name", "Java");

        ToolResponse response = syncServer.callTool("greet", args);

        assertFalse(response.isError());
        assertEquals(1, response.getContent().size());
        assertTrue(response.getContent().get(0).getText().contains("Java"));
    }

    @Test
    void testCalculateTool() {
        ObjectNode args = objectMapper.createObjectNode();
        args.put("operation", "add");
        args.put("a", 5);
        args.put("b", 3);

        ToolResponse response = syncServer.callTool("calculate", args);

        assertFalse(response.isError());
        assertTrue(response.getContent().get(0).getText().contains("8"));
    }

    @Test
    void testDivideByZero() {
        ObjectNode args = objectMapper.createObjectNode();
        args.put("operation", "divide");
        args.put("a", 10);
        args.put("b", 0);

        ToolResponse response = syncServer.callTool("calculate", args);

        assertTrue(response.isError());
    }
}
```
