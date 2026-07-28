# 🏗 Technology Stack Blueprint - mcp-servers/kotlin

**Project Path:** `projects/mcp-servers/kotlin`
**Generated:** 2026-07-28
**Status:** Active — Kotlin MCP Server Reference Implementation

---

## Core Technologies

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Language** | Kotlin | 1.9.22 | Apache-2.0 |
| **Runtime** | JVM | 17+ | GPL-2.0-with-classpath-exception |
| **Build** | Gradle | 8.x (Kotlin DSL) | Apache-2.0 |
| **MCP SDK** | io.modelcontextprotocol:kotlin-sdk | 0.3.0 | MIT |
| **HTTP Client** | Ktor | 2.3.7 | Apache-2.0 |
| **Serialization** | kotlinx.serialization | 1.6.2 | Apache-2.0 |
| **Coroutines** | kotlinx.coroutines | 1.7.3 | Apache-2.0 |
| **Logging** | Logback + kotlin-logging | 1.4.14 / 3.0.5 | EPL-1.0 / Apache-2.0 |

---

## Architecture

**Pattern:** MCP (Model Context Protocol) Server
- **Transport:** STDIO
- **Packaging:** Fat JAR (via custom Gradle task)

### Project Structure
```
mcp-servers/kotlin/
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── src/
│   ├── main/
│   │   ├── kotlin/
│   │   │   └── com/example/mcp/
│   │   │       ├── Main.kt
│   │   │       ├── tools/
│   │   │       │   └── GreetTool.kt
│   │   │       └── resources/
│   │   └── resources/
│   │       └── logback.xml
│   └── test/
│       └── kotlin/
└── README.md
```

---

## Dependencies (`build.gradle.kts`)

```kotlin
plugins {
    kotlin("jvm") version "1.9.22"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    // Kotlin MCP SDK
    implementation("io.modelcontextprotocol:kotlin-sdk:0.3.0")

    // Ktor client for HTTP transport needs
    implementation("io.ktor:ktor-client-core:2.3.7")
    implementation("io.ktor:ktor-client-cio:2.3.7")

    // Serialization
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.6.2")

    // Coroutines
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-jdk8:1.7.3")

    // Logging
    implementation("ch.qos.logback:logback-classic:1.4.14")
    implementation("io.github.microutils:kotlin-logging-jvm:3.0.5")
}

application {
    mainClass.set("com.example.mcp.MainKt")
}

kotlin {
    jvmToolchain(17)
}

tasks.named<Jar>("jar") {
    manifest {
        attributes["Main-Class"] = "com.example.mcp.MainKt"
    }
}

tasks.register<Jar>("fatJar") {
    dependsOn(tasks.named("compileKotlin"))
    from(configurations.runtimeClasspath.get().map { if (it.isDirectory) it else zipTree(it) })
    from(tasks.named("processResources"))
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
    manifest {
        attributes["Main-Class"] = "com.example.mcp.MainKt"
    }
    archiveClassifier.set("all")
}
```

---

## Entry Point (`Main.kt`)

```kotlin
package com.example.mcp

import io.modelcontextprotocol.server.McpServer
import io.modelcontextprotocol.server.transport.StdioServerTransport
import io.modelcontextprotocol.spec.McpSchema
import kotlinx.coroutines.runBlocking
import mu.KLogging

private val logger = KotlinLogging.logger {}

fun main() = runBlocking {
    val server = McpServer.builder("kotlin-mcp-server", "1.0.0")
        .addTool(
            McpSchema.Tool.builder()
                .name("greet")
                .description("Greet a person by name")
                .inputSchema(McpSchema.Tool.InputSchema(
                    type = "object",
                    properties = mapOf(
                        "name" to McpSchema.Tool.Property(
                            type = "string",
                            description = "The name of the person to greet"
                        )
                    ),
                    required = listOf("name")
                ))
                .build()
        ) { exchange, args ->
            val name = args["name"] as String
            McpSchema.CallToolResult.builder()
                .content(listOf(
                    McpSchema.TextContent.builder()
                        .text("Hello, $name!")
                        .build()
                ))
                .build()
        }
        .build()

    val transport = StdioServerTransport()
    server.run(transport)
    logger.info("Kotlin MCP Server running...")
}
```

---

## Commands

```bash
# Build
./gradlew build

# Run
./gradlew run

# Build fat JAR
./gradlew fatJar

# Run fat JAR
java -jar build/libs/kotlin-mcp-server-all.jar

# Test
./gradlew test

# Clean
./gradlew clean

# Format (if ktlint configured)
./gradlew ktlintFormat

# Dependency updates
./gradlew dependencyUpdates
```

---

## Quality Gates

| Check | Command |
|-------|---------|
| **Compile** | `./gradlew compileKotlin` |
| **Tests** | `./gradlew test` |
| **Fat JAR** | `./gradlew fatJar` |
| **Format** | `./gradlew ktlintCheck` |

---

## Kotlin 1.9+ Features Used

- **Sealed classes** for type-safe hierarchies
- **Data classes** for immutable DTOs
- **Coroutines** for async programming
- **Serialization** with kotlinx.serialization
- **Extension functions** for clean APIs

---

## License

MIT / Apache-2.0

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*