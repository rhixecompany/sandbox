// swift-tools-version: 6.0
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "swift-mcp-server",
    platforms: [
        .macOS(.v15)
    ],
    dependencies: [
        // MCP Swift SDK — provides the Model Context Protocol server libraries
        .package(url: "https://github.com/swift-server/swift-mcp.git", branch: "main"),
        // Service lifecycle management
        .package(url: "https://github.com/swift-server/swift-service-lifecycle.git", from: "2.0.0"),
        // Logging
        .package(url: "https://github.com/apple/swift-log.git", from: "1.5.0"),
    ],
    targets: [
        // The main executable target
        .executableTarget(
            name: "MyMCPServer",
            dependencies: [
                .product(name: "MCP", package: "swift-mcp"),
                .product(name: "ServiceLifecycle", package: "swift-service-lifecycle"),
                .product(name: "Logging", package: "swift-log"),
            ],
            path: "Sources/MyMCPServer"
        ),
    ]
)
