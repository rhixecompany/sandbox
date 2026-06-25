package com.example.mcp;

import com.example.mcp.config.Config;
import com.example.mcp.tools.ToolDefinitions;
import com.example.mcp.tools.ToolHandlers;
import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpServerFeatures;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.spec.McpSchema;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;

/**
 * Main entry point for the Java MCP Server.
 * <p>
 * This server implements the Model Context Protocol (MCP) and provides
 * tools that can be discovered and invoked by MCP clients (e.g., AI assistants).
 * It communicates via STDIO transport.
 */
public class McpServerApplication {

    private static final Logger logger = LoggerFactory.getLogger(McpServerApplication.class);

    public static void main(String[] args) {
        logger.info("Starting Java MCP Server...");

        // Load configuration
        Config config = Config.load();
        logger.info("Server name: {}", config.getServerName());
        logger.info("Server version: {}", config.getServerVersion());

        try {
            // Create server info
            McpSchema.ServerCapabilities capabilities = McpSchema.ServerCapabilities.builder()
                    .tools(true) // Signal that this server supports tools
                    .build();

            McpSchema.Implementation serverInfo = new McpSchema.Implementation(
                    config.getServerName(),
                    config.getServerVersion()
            );

            // Build the server with STDIO transport
            McpServer server = McpServer.using(new StdioServerTransport())
                    .capabilities(capabilities)
                    .serverInfo(serverInfo)
                    .build();

            // Register tool definitions
            List<McpServerFeatures.SyncToolRegistration> tools = ToolDefinitions.getDefinitions();
            for (McpServerFeatures.SyncToolRegistration tool : tools) {
                server.addTool(tool);
                logger.info("Registered tool: {}", tool.tool().name());
            }

            // Register tool handlers
            ToolHandlers handlers = new ToolHandlers();
            handlers.register(server);

            logger.info("Java MCP Server is ready and listening on STDIO.");
            logger.info("Available tools: greet, echo");

            // Keep the main thread alive
            Thread.currentThread().join();

        } catch (Exception e) {
            logger.error("Fatal error running MCP server", e);
            System.exit(1);
        }
    }
}
