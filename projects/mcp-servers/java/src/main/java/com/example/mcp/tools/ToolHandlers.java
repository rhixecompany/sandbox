package com.example.mcp.tools;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerFeatures;
import io.modelcontextprotocol.spec.McpSchema;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;

/**
 * Registers tool call handlers with the MCP server.
 * <p>
 * Handlers are invoked when a client calls a tool. This class wires the
 * tool definitions (schemas) together with their implementations.
 */
public class ToolHandlers {

    private static final Logger logger = LoggerFactory.getLogger(ToolHandlers.class);

    /**
     * Registers all tool handlers on the given MCP server instance.
     *
     * @param server the MCP server to register handlers on
     */
    public void register(McpServer server) {
        List<McpServerFeatures.SyncToolRegistration> tools = ToolDefinitions.getDefinitions();

        for (McpServerFeatures.SyncToolRegistration tool : tools) {
            String toolName = tool.tool().name();
            logger.debug("Attaching handler for tool: {}", toolName);
            // The handler is already embedded in the SyncToolRegistration via the lambda,
            // but we add it explicitly to the server here.
            server.addTool(tool);
        }

        logger.info("Registered {} tool handler(s)", tools.size());
    }

    /**
     * Handles a "greet" call.
     *
     * @param name the name to greet
     * @return a greeting message
     */
    public McpSchema.CallToolResult handleGreet(String name) {
        String greeting = "Hello, " + name + "! Welcome to the Java MCP Server.";
        logger.info("Greet tool called with name: {}", name);
        return new McpSchema.CallToolResult(
                List.of(new McpSchema.TextContent(greeting)),
                false
        );
    }

    /**
     * Handles an "echo" call.
     *
     * @param message the message to echo
     * @return the echoed message
     */
    public McpSchema.CallToolResult handleEcho(String message) {
        String response = "Echo: " + message;
        logger.info("Echo tool called with message: {}", message);
        return new McpSchema.CallToolResult(
                List.of(new McpSchema.TextContent(response)),
                false
        );
    }
}
