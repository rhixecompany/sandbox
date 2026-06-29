# ResourceHandlers.java Template

> Extracted from `java-mcp-server-generator.prompt.md`.

## ResourceHandlers.java Template

```java
package com.example.mcp.resources;

import io.mcp.server.McpServer;
import io.mcp.server.resource.ResourceContent;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import reactor.core.publisher.Mono;

import java.time.Instant;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class ResourceHandlers {

    private static final Logger log = LoggerFactory.getLogger(ResourceHandlers.class);
    private static final Map<String, Boolean> subscriptions = new ConcurrentHashMap<>();

    public static void register(McpServer server) {
        // Register resource list handler
        server.addResourceListHandler(() -> {
            log.debug("Listing available resources");
            return Mono.just(ResourceDefinitions.getResources());
        });

        // Register resource read handler
        server.addResourceReadHandler(ResourceHandlers::handleRead);

        // Register resource subscribe handler
        server.addResourceSubscribeHandler(ResourceHandlers::handleSubscribe);

        // Register resource unsubscribe handler
        server.addResourceUnsubscribeHandler(ResourceHandlers::handleUnsubscribe);
    }

    private static Mono<ResourceContent> handleRead(String uri) {
        log.info("Reading resource: {}", uri);

        switch (uri) {
            case "resource://data/example":
                String jsonData = String.format(
                    "{\"message\":\"Example resource data\",\"timestamp\":\"%s\"}",
                    Instant.now()
                );
                return Mono.just(ResourceContent.text(jsonData, uri, "application/json"));

            case "resource://config":
                String config = "{\"serverName\":\"my-mcp-server\",\"version\":\"1.0.0\"}";
                return Mono.just(ResourceContent.text(config, uri, "application/json"));

            default:
                log.warn("Unknown resource requested: {}", uri);
                return Mono.error(new IllegalArgumentException("Unknown resource URI: " + uri));
        }
    }

    private static Mono<Void> handleSubscribe(String uri) {
        log.info("Client subscribed to resource: {}", uri);
        subscriptions.put(uri, true);
        return Mono.empty();
    }

    private static Mono<Void> handleUnsubscribe(String uri) {
        log.info("Client unsubscribed from resource: {}", uri);
        subscriptions.remove(uri);
        return Mono.empty();
    }
}
```
