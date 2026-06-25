import Foundation
import MCP
import Logging

/// Handles execution of MCP tool calls.
///
/// Each function corresponds to a tool defined in `ToolDefinitions` and
/// returns a `ToolResult` containing the result content.
struct ToolHandlers {
    private let logger: Logger

    init(logger: Logger) {
        self.logger = logger
    }

    /// Handle the `greet` tool.
    /// - Parameter arguments: Tool arguments from the MCP request.
    /// - Returns: A greeting text content.
    func handleGreet(arguments: [String: AnyValue]) throws -> ToolResult {
        guard case .string(let name) = arguments["name"] else {
            throw MCPError.invalidParameters("Missing required argument: name")
        }

        let title: String
        if case .string(let t) = arguments["title"] {
            title = t
        } else {
            title = ""
        }

        let greeting: String
        if title.isEmpty {
            greeting = "Hello, \(name)! Welcome to the Swift MCP Server."
        } else {
            greeting = "Hello, \(title) \(name)! Welcome to the Swift MCP Server."
        }

        logger.info("Greeted user: \(title) \(name)")
        return ToolResult(content: [.text(greeting)])
    }

    /// Handle the `calculate` tool.
    /// - Parameter arguments: Tool arguments from the MCP request.
    /// - Returns: The calculation result as text content.
    func handleCalculate(arguments: [String: AnyValue]) throws -> ToolResult {
        guard case .string(let operation) = arguments["operation"] else {
            throw MCPError.invalidParameters("Missing required argument: operation")
        }
        guard case .number(let a) = arguments["a"] else {
            throw MCPError.invalidParameters("Missing required argument: a")
        }
        guard case .number(let b) = arguments["b"] else {
            throw MCPError.invalidParameters("Missing required argument: b")
        }

        let result: Double
        switch operation {
        case "add":
            result = a + b
        case "subtract":
            result = a - b
        case "multiply":
            result = a * b
        case "divide":
            guard b != 0 else {
                throw MCPError.invalidParameters("Division by zero is not allowed.")
            }
            result = a / b
        default:
            throw MCPError.invalidParameters("Unknown operation: \(operation). Supported: add, subtract, multiply, divide.")
        }

        // Format: strip trailing zeros for clean output
        let formatted: String
        if result == floor(result) {
            formatted = String(format: "%.0f", result)
        } else {
            formatted = String(format: "%.4f", result)
        }

        logger.info("Calculated: \(a) \(operation) \(b) = \(formatted)")
        return ToolResult(content: [.text("\(formatted)")])
    }
}

// MARK: - Supporting Types

/// Errors that can occur during tool handling.
enum MCPError: Error, LocalizedError {
    case invalidParameters(String)

    var errorDescription: String? {
        switch self {
        case .invalidParameters(let message):
            return message
        }
    }
}
