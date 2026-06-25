package com.example.mcp

import com.example.mcp.config.Config
import com.example.mcp.tools.GreetTool
import io.modelcontextprotocol.kotlin.sdk.StdioServerTransport
import kotlinx.coroutines.runBlocking
import mu.KotlinLogging

private val logger = KotlinLogging.logger {}

/**
 * Entry point for the Kotlin MCP server.
 *
 * Parses configuration, builds the server, and starts listening
 * on STDIO transport (designed to be launched by an MCP host
 * such as Claude Desktop or Cursor).
 */
fun main() {
    val config = Config.fromEnvironment()
    logger.info { "Starting ${config.name} v${config.version}" }

    val transport = StdioServerTransport()

    val server = createServer(config)

    runBlocking {
        try {
            server.start(transport)
            logger.info { "Server running on stdio transport" }
        } catch (e: Exception) {
            logger.error(e) { "Server terminated with error" }
            System.exit(1)
        }
    }
}
