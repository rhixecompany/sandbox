# 🏗 Technology Stack Blueprint - mcp-servers/java

**Project Path:** `projects/mcp-servers/java`
**Generated:** 2026-07-28
**Status:** Active — Java MCP Server Reference Implementation

---

## Core Technologies

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Language** | Java | 17 | GPL-2.0-with-classpath-exception |
| **Build** | Maven | 3.9+ | Apache-2.0 |
| **MCP SDK** | io.modelcontextprotocol:mcp | 0.8.0 | MIT |
| **Logging** | SLF4J + slf4j-simple | 2.0.16 | MIT |
| **Packaging** | maven-shade-plugin | 3.6.0 | Apache-2.0 |

---

## Architecture

**Pattern:** MCP (Model Context Protocol) Server
- **Transport:** STDIO
- **Packaging:** Fat JAR (uber-jar with all dependencies)

### Project Structure
```
mcp-servers/java/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/mcp/
│   │   │       ├── McpServerApplication.java
│   │   │       ├── tools/
│   │   │       │   └── GreetTool.java
│   │   │       └── resources/
│   │   └── resources/
│   │       └── logback.xml
│   └── test/
│       └── java/
└── README.md
```

---

## Dependencies (`pom.xml`)

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example.mcp</groupId>
    <artifactId>java-mcp-server</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>
    
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <mcp.sdk.version>0.8.0</mcp.sdk.version>
    </properties>
    
    <dependencies>
        <!-- MCP Java SDK -->
        <dependency>
            <groupId>io.modelcontextprotocol</groupId>
            <artifactId>mcp</artifactId>
            <version>${mcp.sdk.version}</version>
        </dependency>
        
        <!-- Logging -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-simple</artifactId>
            <version>2.0.16</version>
        </dependency>
    </dependencies>
    
    <build>
        <finalName>java-mcp-server</finalName>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>17</source>
                    <target>17</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.6.0</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals><goal>shade</goal></goals>
                        <configuration>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.example.mcp.McpServerApplication</mainClass>
                                </transformer>
                            </transformers>
                            <filters>
                                <filter>
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                            </filters>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

---

## Entry Point (`McpServerApplication.java`)

```java
package com.example.mcp;

import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import com.example.mcp.tools.GreetTool;

public class McpServerApplication {
    public static void main(String[] args) throws Exception {
        // Create server
        McpServer server = McpServer.builder("java-mcp-server", "1.0.0")
            .addTool(new GreetTool())
            .build();
        
        // Run with STDIO transport
        StdioServerTransport transport = new StdioServerTransport();
        server.run(transport);
    }
}
```

---

## Tool Implementation (`tools/GreetTool.java`)

```java
package com.example.mcp.tools;

import io.modelcontextprotocol.server.McpServerTool;
import io.modelcontextprotocol.spec.McpSchema;
import java.util.Map;

public class GreetTool implements McpServerTool {
    
    @Override
    public String getName() {
        return "greet";
    }
    
    @Override
    public String getDescription() {
        return "Greet a person by name";
    }
    
    @Override
    public McpSchema.Tool.InputSchema getInputSchema() {
        return McpSchema.Tool.InputSchema.builder()
            .type("object")
            .properties(Map.of(
                "name", McpSchema.Tool.Property.builder()
                    .type("string")
                    .description("The name of the person to greet")
                    .build()
            ))
            .required(List.of("name"))
            .build();
    }
    
    @Override
    public McpSchema.CallToolResult handle(Map<String, Object> arguments) {
        String name = (String) arguments.getOrDefault("name", "World");
        return McpSchema.CallToolResult.builder()
            .content(List.of(
                McpSchema.TextContent.builder()
                    .text("Hello, " + name + "!")
                    .build()
            ))
            .build();
    }
}
```

---

## Commands

```bash
# Compile
mvn compile

# Package (creates fat JAR)
mvn package

# Run
java -jar target/java-mcp-server.jar

# Run with Maven exec plugin
mvn exec:java -Dexec.mainClass="com.example.mcp.McpServerApplication"

# Test
mvn test

# Clean
mvn clean

# Verify
mvn verify

# Dependency tree
mvn dependency:tree

# Update dependencies
mvn versions:display-dependency-updates
```

---

## Quality Gates

| Check | Command |
|-------|---------|
| **Compile** | `mvn compile` |
| **Tests** | `mvn test` |
| **Package** | `mvn package` |
| **Format** | `mvn spotless:check` (if configured) |
| **Lint** | `mvn checkstyle:check` (if configured) |

---

## Java 17+ Features Used

- **Records** for immutable DTOs (if applicable)
- **Sealed classes** for type hierarchies
- **Pattern matching** for instanceof
- **Text blocks** for multi-line strings
- **Switch expressions** for concise logic

---

## License

MIT / Apache-2.0

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*