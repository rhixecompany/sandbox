import Foundation
import Logging

/// Server configuration loaded from environment variables with sensible defaults.
struct ServerConfig: Sendable {
    /// The transport protocol to use (stdio or http).
    let transport: TransportKind

    /// Host address for HTTP transport.
    let host: String

    /// Port for HTTP transport.
    let port: Int

    /// Log level for the server.
    let logLevel: Logger.Level

    /// The server name advertised to MCP clients.
    let serverName: String

    /// The server version advertised to MCP clients.
    let serverVersion: String

    /// Default configuration.
    static let `default` = ServerConfig(
        transport: .stdio,
        host: "127.0.0.1",
        port: 8080,
        logLevel: .info,
        serverName: "swift-mcp-server",
        serverVersion: "1.0.0"
    )

    /// Load configuration from environment variables.
    static func fromEnvironment() -> ServerConfig {
        let env = ProcessInfo.processInfo.environment

        let transport: TransportKind
        if let transportRaw = env["MCP_TRANSPORT"]?.lowercased() {
            transport = TransportKind(rawValue: transportRaw) ?? .stdio
        } else {
            transport = .stdio
        }

        let host = env["MCP_HOST"] ?? "127.0.0.1"
        let port = Int(env["MCP_PORT"] ?? "") ?? 8080

        let logLevel: Logger.Level
        if let levelRaw = env["MCP_LOG_LEVEL"]?.lowercased() {
            logLevel = Logger.Level(rawValue: levelRaw) ?? .info
        } else {
            logLevel = .info
        }

        let serverName = env["MCP_SERVER_NAME"] ?? "swift-mcp-server"
        let serverVersion = env["MCP_SERVER_VERSION"] ?? "1.0.0"

        return ServerConfig(
            transport: transport,
            host: host,
            port: port,
            logLevel: logLevel,
            serverName: serverName,
            serverVersion: serverVersion
        )
    }
}

/// Supported transport kinds for the MCP server.
enum TransportKind: String, Sendable {
    /// Standard input/output transport (for local/cli usage).
    case stdio
    /// HTTP transport for remote connections.
    case http
}
