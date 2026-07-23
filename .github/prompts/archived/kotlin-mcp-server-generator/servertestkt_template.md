# ServerTest.kt Template

> Extracted from `kotlin-mcp-server-generator.prompt.md`.

## ServerTest.kt Template

```kotlin
package com.example.myserver

import kotlinx.coroutines.test.runTest
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse

class ServerTest {

    @Test
    fun `test server creation`() = runTest {
        val config = Config(
            name = "test-server",
            version = "1.0.0",
            description = "Test server"
        )

        val server = createServer(config)

        assertEquals("test-server", server.serverInfo.name)
        assertEquals("1.0.0", server.serverInfo.version)
    }

    @Test
    fun `test tool1 execution`() = runTest {
        val config = Config()
        val server = createServer(config)

        // Test tool execution
        // Note: You'll need to implement proper testing utilities
        // for calling tools in the server
    }
}
```
