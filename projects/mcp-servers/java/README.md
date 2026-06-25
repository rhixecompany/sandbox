# Java MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server implementation in Java.

This server provides tools that can be discovered and invoked by MCP clients (e.g., AI assistants like Claude). It communicates via STDIO transport.

## Features

- **Greet tool** — Returns a personalized greeting for a given name
- **Echo tool** — Echoes back any message you send (useful for connectivity testing)
- Environment-based configuration
- Maven build with shaded (fat) JAR

## Prerequisites

- **Java 17+** (JDK)
- **Apache Maven 3.8+** (or use the Maven wrapper — see below)

## Quick Start

### Using the Maven Wrapper

```bash
# On Linux/macOS
./mvnw clean package

# On Windows
mvnw.cmd clean package
```

### Using a system Maven installation

```bash
mvn clean package
```

### Run the server

```bash
java -jar target/java-mcp-server.jar
```

The server listens on **STDIO** by default. It is designed to be launched by an MCP client (e.g., Claude Desktop or the MCP CLI).

## Configuration

All configuration is through environment variables:

| Variable               | Default            | Description                     |
|------------------------|--------------------|---------------------------------|
| `MCP_SERVER_NAME`      | `java-mcp-server`  | Server name reported to clients |
| `MCP_SERVER_VERSION`   | `1.0.0`            | Server version reported to clients |
| `MCP_LOG_LEVEL`        | `INFO`             | Logging level (DEBUG, INFO, WARN, ERROR) |
| `MCP_PORT`             | `8080`             | Port (reserved for future SSE transport) |
| `MCP_STDIO_TRANSPORT`  | `true`             | Use STDIO transport (default) |

## Project Structure

```
java-mcp-server/
├── pom.xml                        # Maven build file
├── .gitignore                     # Git ignore rules
├── README.md                      # This file
├── .mvn/
│   └── wrapper/
│       └── maven-wrapper.properties
└── src/
    └── main/
        └── java/
            └── com/
                └── example/
                    └── mcp/
                        ├── McpServerApplication.java    # Main entry point
                        ├── config/
                        │   └── Config.java              # Environment-based config
                        └── tools/
                            ├── ToolDefinitions.java     # Tool schemas & default handlers
                            └── ToolHandlers.java        # Tool handler registration
```

## Testing with the MCP CLI

You can test the server using the [MCP CLI tool](https://github.com/modelcontextprotocol/cli):

```bash
npx @modelcontextprotocol/cli inspect java -jar target/java-mcp-server.jar
```

## Building

```bash
# Build the shaded JAR
mvn clean package

# The output JAR will be at: target/java-mcp-server.jar
```

## License

This project is provided as an example. See the LICENSE file (if present) for details.
