package com.example.mcp

import com.example.mcp.config.Config
import com.example.mcp.tools.GreetTool
import io.modelcontextprotocol.kotlin.sdk.McpServer
import io.modelcontextprotocol.kotlin.sdk.ServerCapabilities
import io.modelcontextprotocol.kotlin.sdk.ServerInfo
import mu.KotlinLogging

private val logger = KotlinLogging.logger {}

/**
 * Builds and returns the configured MCP server with all tools registered.
 */
fun createServer(config: Config): McpServer {
    logger.info { "Creating MCP server: ${config.name} v${config.version}" }

    return McpServer(
        serverInfo = ServerInfo(
            name = config.name,
            version = config.version
        ),
        capabilities = ServerCapabilities(
            tools = true
        )
    ) {
        // Register all tools
        val greetTool = GreetTool()
        tool(greetTool.definition, greetTool.handler)
    }
}
