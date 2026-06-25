import Foundation
import MCP
import Logging
import ServiceLifecycle

/// The main MCP server responsible for configuration, tool registration, and transport.
final class MCPServer: Service {
    private let config: ServerConfig
    private let logger: Logger
    private let toolHandlers: ToolHandlers
    private var mcpServer: MCP.Server?

    init(config: ServerConfig) {
        self.config = config
        self.logger = Logger(label: "com.swift-mcp-server")
        self.logger.logLevel = config.logLevel
        self.toolHandlers = ToolHandlers(logger: logger)
    }

    /// Conforms to ServiceLifecycle's `Service` protocol.
    /// Starts the MCP server using the configured transport.
    func run() async throws {
        logger.info("Starting Swift MCP Server v\(config.serverVersion)")
        logger.info("Transport: \(config.transport.rawValue)")

        // Build the MCP server with tool definitions
        let serverInfo = ServerInfo(
            name: config.serverName,
            version: config.serverVersion
        )

        let mcpServer = MCP.Server(
            info: serverInfo,
            capabilities: .init(tools: .init(listChanged: true))
        )

        // Register tool definitions and handlers
        for tool in ToolDefinitions.all {
            mcpServer.registerTool(tool) { [weak self] arguments in
                guard let self = self else {
                    return ToolResult(content: [.text("Server shutting down")])
                }
                return try await self.handleToolCall(toolName: tool.name, arguments: arguments)
            }
        }

        self.mcpServer = mcpServer

        logger.info("Starting transport: \(config.transport.rawValue)")
        switch config.transport {
        case .stdio:
            try await mcpServer.runStdio()
        case .http:
            try await mcpServer.runHTTP(host: config.host, port: config.port)
        }
    }

    // MARK: - Private

    /// Route a tool call to the appropriate handler.
    private func handleToolCall(toolName: String, arguments: [String: AnyValue]) async throws -> ToolResult {
        logger.debug("Handling tool call: \(toolName)")

        switch toolName {
        case "greet":
            return try toolHandlers.handleGreet(arguments: arguments)
        case "calculate":
            return try toolHandlers.handleCalculate(arguments: arguments)
        default:
            throw MCPError.invalidParameters("Unknown tool: \(toolName)")
        }
    }
}
