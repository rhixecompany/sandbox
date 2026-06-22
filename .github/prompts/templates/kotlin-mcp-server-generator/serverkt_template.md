# Server.kt Template

> Extracted from `kotlin-mcp-server-generator.prompt.md`.

## Server.kt Template

```kotlin
package com.example.myserver

import io.modelcontextprotocol.kotlin.sdk.server.Server
import io.modelcontextprotocol.kotlin.sdk.server.ServerOptions
import io.modelcontextprotocol.kotlin.sdk.Implementation
import io.modelcontextprotocol.kotlin.sdk.ServerCapabilities
import com.example.myserver.tools.registerTools

fun createServer(config: Config): Server {
    val server = Server(
        serverInfo = Implementation(
            name = config.name,
            version = config.version
        ),
        options = ServerOptions(
            capabilities = ServerCapabilities(
                tools = ServerCapabilities.Tools(),
                resources = ServerCapabilities.Resources(
                    subscribe = true,
                    listChanged = true
                ),
                prompts = ServerCapabilities.Prompts(listChanged = true)
            )
        )
    ) {
        config.description
    }

    // Register all tools
    server.registerTools()

    return server
}
```
