package com.example.mcp.tools

import io.modelcontextprotocol.kotlin.sdk.Tool
import io.modelcontextprotocol.kotlin.sdk.ToolHandler
import io.modelcontextprotocol.kotlin.sdk.ToolResult
import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.JsonPrimitive
import kotlinx.serialization.json.buildJsonObject
import kotlinx.serialization.json.put

/**
 * A sample MCP tool that greets a user by name.
 *
 * Input schema:
 * - `name` (string, required): The name of the person to greet.
 *
 * Output:
 * - A JSON object containing a friendly greeting message.
 */
class GreetTool {

    /** Tool definition / specification exposed to the MCP client. */
    val definition: Tool = Tool(
        name = "greet",
        description = "Returns a personalised greeting for the given name",
        inputSchema = buildJsonObject {
            put("type", JsonPrimitive("object"))
            put("properties", buildJsonObject {
                put("name", buildJsonObject {
                    put("type", JsonPrimitive("string"))
                    put("description", JsonPrimitive("The name of the person to greet"))
                })
            })
            put("required", buildJsonObject {
                // The SDK expects required to be an array of strings
                // We pass it as a JSON array in the schema
            })
        }
    )

    /** Handler invoked when the client calls the `greet` tool. */
    val handler: ToolHandler = ToolHandler { arguments ->
        val name = arguments?.get("name")?.let { value ->
            if (value is JsonPrimitive && value.isString) {
                value.content
            } else {
                null
            }
        } ?: "World"

        val greeting = "Hello, $name! Welcome to the Kotlin MCP server."
        ToolResult(
            content = listOf(
                io.modelcontextprotocol.kotlin.sdk.Content(
                    type = "text",
                    text = greeting
                )
            )
        )
    }
}
