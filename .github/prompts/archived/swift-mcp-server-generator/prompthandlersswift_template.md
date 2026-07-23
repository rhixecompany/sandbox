# PromptHandlers.swift Template

> Extracted from `swift-mcp-server-generator.prompt.md`.

## PromptHandlers.swift Template

```swift
import MCP
import Logging

private let logger = Logger(label: "com.example.mcp-server.prompts")

func registerPromptHandlers(server: Server) async {
    await server.withMethodHandler(ListPrompts.self) { params in
        logger.debug("Listing available prompts")
        return .init(prompts: getPromptDefinitions(), nextCursor: nil)
    }

    await server.withMethodHandler(GetPrompt.self) { params in
        logger.info("Getting prompt", metadata: ["name": .string(params.name)])

        switch params.name {
        case "code-review":
            return handleCodeReviewPrompt(params: params)

        default:
            logger.warning("Unknown prompt requested", metadata: ["name": .string(params.name)])
            throw MCPError.invalidParams("Unknown prompt: \(params.name)")
        }
    }
}

private func handleCodeReviewPrompt(params: GetPrompt.Params) -> GetPrompt.Result {
    guard let language = params.arguments?["language"]?.stringValue else {
        return .init(
            description: "Missing language parameter",
            messages: []
        )
    }

    let focus = params.arguments?["focus"]?.stringValue ?? "general quality"

    let description = "Code review for \(language) with focus on \(focus)"
    let messages: [Prompt.Message] = [
        .user("Please review this \(language) code with focus on \(focus)."),
        .assistant("I'll review the code focusing on \(focus). Please share the code."),
        .user("Here's the code to review: [paste code here]")
    ]

    logger.debug("Generated code review prompt", metadata: [
        "language": .string(language),
        "focus": .string(focus)
    ])

    return .init(description: description, messages: messages)
}
```
