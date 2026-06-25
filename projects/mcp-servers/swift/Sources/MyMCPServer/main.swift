import Foundation
import Logging
import ServiceLifecycle

// MARK: - Entry Point

/// The entry point for the Swift MCP Server.
///
/// Initializes logging, loads configuration from the environment,
/// creates the server, and runs it within a ServiceLifecycle group
/// for graceful shutdown.
@main
enum Main {
    static func main() async {
        // Bootstrap logging system
        LoggingSystem.bootstrap { label in
            var handler = StreamLogHandler.standardOutput(label: label)
            handler.logLevel = .info
            return handler
        }

        let logger = Logger(label: "com.swift-mcp-server")

        // Load configuration
        let config = ServerConfig.fromEnvironment()
        logger.logLevel = config.logLevel

        logger.info("========================================")
        logger.info("  Swift MCP Server")
        logger.info("  Name:    \(config.serverName)")
        logger.info("  Version: \(config.serverVersion)")
        logger.info("  Transport: \(config.transport.rawValue)")
        logger.info("========================================")

        // Create the server
        let server = MCPServer(config: config)

        // Run with graceful shutdown via ServiceLifecycle
        let serviceGroup = ServiceGroup(
            configuration: ServiceGroupConfiguration(
                services: [server],
                gracefulShutdownSignals: [.sigterm, .sigint],
                logger: logger
            )
        )

        do {
            try await serviceGroup.run()
        } catch {
            logger.error("Server terminated with error: \(error.localizedDescription)")
            exit(1)
        }
    }
}
