# ResourceHandlers.swift Template

> Extracted from `swift-mcp-server-generator.prompt.md`.

## ResourceHandlers.swift Template

```swift
import MCP
import Logging
import Foundation

private let logger = Logger(label: "com.example.mcp-server.resources")

actor ResourceState {
    private var subscriptions: Set<String> = []

    func addSubscription(_ uri: String) {
        subscriptions.insert(uri)
    }

    func removeSubscription(_ uri: String) {
        subscriptions.remove(uri)
    }

    func isSubscribed(_ uri: String) -> Bool {
        subscriptions.contains(uri)
    }
}

private let state = ResourceState()

func registerResourceHandlers(server: Server) async {
    await server.withMethodHandler(ListResources.self) { params in
        logger.debug("Listing available resources")
        return .init(resources: getResourceDefinitions(), nextCursor: nil)
    }

    await server.withMethodHandler(ReadResource.self) { params in
        logger.info("Reading resource", metadata: ["uri": .string(params.uri)])

        switch params.uri {
        case "resource://data/example":
            let jsonData = """
            {
                "message": "Example resource data",
                "timestamp": "\(Date())"
            }
            """
            return .init(contents: [
                .text(jsonData, uri: params.uri, mimeType: "application/json")
            ])

        case "resource://config":
            let config = """
            {
                "serverName": "MyMCPServer",
                "version": "1.0.0"
            }
            """
            return .init(contents: [
                .text(config, uri: params.uri, mimeType: "application/json")
            ])

        default:
            logger.warning("Unknown resource requested", metadata: ["uri": .string(params.uri)])
            throw MCPError.invalidParams("Unknown resource URI: \(params.uri)")
        }
    }

    await server.withMethodHandler(ResourceSubscribe.self) { params in
        logger.info("Client subscribed to resource", metadata: ["uri": .string(params.uri)])
        await state.addSubscription(params.uri)
        return .init()
    }

    await server.withMethodHandler(ResourceUnsubscribe.self) { params in
        logger.info("Client unsubscribed from resource", metadata: ["uri": .string(params.uri)])
        await state.removeSubscription(params.uri)
        return .init()
    }
}
```
