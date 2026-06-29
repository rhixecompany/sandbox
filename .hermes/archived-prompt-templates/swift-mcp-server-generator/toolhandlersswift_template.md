# ToolHandlers.swift Template

> Extracted from `swift-mcp-server-generator.prompt.md`.

## ToolHandlers.swift Template

```swift
import MCP
import Logging

private let logger = Logger(label: "com.example.mcp-server.tools")

func registerToolHandlers(server: Server) async {
    await server.withMethodHandler(ListTools.self) { _ in
        logger.debug("Listing available tools")
        return .init(tools: getToolDefinitions())
    }

    await server.withMethodHandler(CallTool.self) { params in
        logger.info("Tool called", metadata: ["name": .string(params.name)])

        switch params.name {
        case "greet":
            return handleGreet(params: params)

        case "calculate":
            return handleCalculate(params: params)

        default:
            logger.warning("Unknown tool requested", metadata: ["name": .string(params.name)])
            return .init(
                content: [.text("Unknown tool: \(params.name)")],
                isError: true
            )
        }
    }
}

private func handleGreet(params: CallTool.Params) -> CallTool.Result {
    guard let name = params.arguments?["name"]?.stringValue else {
        return .init(
            content: [.text("Missing 'name' parameter")],
            isError: true
        )
    }

    let greeting = "Hello, \(name)! Welcome to MCP."
    logger.debug("Generated greeting", metadata: ["name": .string(name)])

    return .init(
        content: [.text(greeting)],
        isError: false
    )
}

private func handleCalculate(params: CallTool.Params) -> CallTool.Result {
    guard let operation = params.arguments?["operation"]?.stringValue,
          let a = params.arguments?["a"]?.doubleValue,
          let b = params.arguments?["b"]?.doubleValue else {
        return .init(
            content: [.text("Missing or invalid parameters")],
            isError: true
        )
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
            return .init(
                content: [.text("Division by zero")],
                isError: true
            )
        }
        result = a / b
    default:
        return .init(
            content: [.text("Unknown operation: \(operation)")],
            isError: true
        )
    }

    logger.debug("Calculation performed", metadata: [
        "operation": .string(operation),
        "result": .string("\(result)")
    ])

    return .init(
        content: [.text("Result: \(result)")],
        isError: false
    )
}
```
