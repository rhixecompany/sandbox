package com.example.mcp.tools;

import io.modelcontextprotocol.server.McpServerFeatures;
import io.modelcontextprotocol.spec.McpSchema;

import java.util.List;

/**
 * Defines the MCP tools exposed by this server.
 * Each tool has a name, description, and input schema.
 */
public final class ToolDefinitions {

    private ToolDefinitions() {
        // Utility class - prevent instantiation
    }

    /**
     * Returns the list of tool registrations for this server.
     */
    public static List<McpServerFeatures.SyncToolRegistration> getDefinitions() {
        return List.of(
                defineGreetTool(),
                defineEchoTool()
        );
    }

    /**
     * Defines the "greet" tool.
     * Greets a user by their name.
     */
    private static McpServerFeatures.SyncToolRegistration defineGreetTool() {
        McpSchema.Tool tool = new McpSchema.Tool(
                "greet",
                "Greets a user with a friendly message. Provide a name and receive a personalized greeting.",
                new McpSchema.JsonSchema(
                        "object",
                        java.util.Map.of(
                                "name", new McpSchema.JsonSchema(
                                        "string",
                                        "The name of the person to greet"
                                )
                        ),
                        List.of("name") // required fields
                )
        );

        return new McpServerFeatures.SyncToolRegistration(tool, args -> {
            String name = (String) args.get("name");
            String greeting = "Hello, " + name + "! Welcome to the Java MCP Server.";
            return new McpSchema.CallToolResult(
                    List.of(new McpSchema.TextContent(greeting)),
                    false // isError
            );
        });
    }

    /**
     * Defines the "echo" tool.
     * Echoes back the provided message.
     */
    private static McpServerFeatures.SyncToolRegistration defineEchoTool() {
        McpSchema.Tool tool = new McpSchema.Tool(
                "echo",
                "Echoes back the message you provide. Useful for testing connectivity and verifying the server is responding.",
                new McpSchema.JsonSchema(
                        "object",
                        java.util.Map.of(
                                "message", new McpSchema.JsonSchema(
                                        "string",
                                        "The message to echo back"
                                )
                        ),
                        List.of("message") // required fields
                )
        );

        return new McpServerFeatures.SyncToolRegistration(tool, args -> {
            String message = (String) args.get("message");
            String response = "Echo: " + message;
            return new McpSchema.CallToolResult(
                    List.of(new McpSchema.TextContent(response)),
                    false // isError
            );
        });
    }
}
