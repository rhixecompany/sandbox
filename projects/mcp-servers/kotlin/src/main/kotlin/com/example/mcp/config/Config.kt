package com.example.mcp.config

/**
 * Holds server identity and configuration values.
 *
 * Values can be overridden via environment variables:
 * - `MCP_SERVER_NAME`    → server name (default: "kotlin-mcp-server")
 * - `MCP_SERVER_VERSION` → server version (default: "1.0.0")
 */
data class Config(
    val name: String,
    val version: String
) {
    companion object {
        /** Default configuration used when environment variables are not set. */
        fun defaults(): Config = Config(
            name = "kotlin-mcp-server",
            version = "1.0.0"
        )

        /**
         * Loads configuration from environment variables, falling back
         * to default values for any missing variable.
         */
        fun fromEnvironment(): Config {
            val envName = System.getenv("MCP_SERVER_NAME")
            val envVersion = System.getenv("MCP_SERVER_VERSION")
            val defaults = defaults()
            return Config(
                name = envName ?: defaults.name,
                version = envVersion ?: defaults.version
            )
        }
    }
}
