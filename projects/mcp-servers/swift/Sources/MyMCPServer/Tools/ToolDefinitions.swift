import MCP

/// Defines all tools provided by this MCP server.
///
/// Each tool is defined as a static property returning an `MCPTool` instance
/// with its name, description, and input schema.
enum ToolDefinitions {
    // MARK: - greet

    /// Tool: greet — Greets a user by name.
    static let greet = MCPTool(
        name: "greet",
        description: "Greet a person by name with an optional title.",
        inputSchema: .object([
            "name": .object([
                "type": .string,
                "description": "The name of the person to greet.",
            ]),
            "title": .object([
                "type": .string,
                "description": "An optional title (e.g., Mr., Ms., Dr.).",
            ]),
        ]),
        required: ["name"]
    )

    // MARK: - calculate

    /// Tool: calculate — Performs a basic arithmetic operation.
    static let calculate = MCPTool(
        name: "calculate",
        description: "Perform a basic arithmetic operation on two numbers.",
        inputSchema: .object([
            "operation": .object([
                "type": .string,
                "description": "The operation to perform: add, subtract, multiply, divide.",
                "enum": ["add", "subtract", "multiply", "divide"],
            ]),
            "a": .object([
                "type": .number,
                "description": "The first operand.",
            ]),
            "b": .object([
                "type": .number,
                "description": "The second operand.",
            ]),
        ]),
        required: ["operation", "a", "b"]
    )

    /// All tools registered by this server.
    static let all: [MCPTool] = [greet, calculate]
}
