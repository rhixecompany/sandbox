# ToolDefinitions.swift Template

> Extracted from `swift-mcp-server-generator.prompt.md`.

## ToolDefinitions.swift Template

```swift
import MCP

func getToolDefinitions() -> [Tool] {
    [
        Tool(
            name: "greet",
            description: "Generate a greeting message",
            inputSchema: .object([
                "type": .string("object"),
                "properties": .object([
                    "name": .object([
                        "type": .string("string"),
                        "description": .string("Name to greet")
                    ])
                ]),
                "required": .array([.string("name")])
            ])
        ),
        Tool(
            name: "calculate",
            description: "Perform mathematical calculations",
            inputSchema: .object([
                "type": .string("object"),
                "properties": .object([
                    "operation": .object([
                        "type": .string("string"),
                        "enum": .array([
                            .string("add"),
                            .string("subtract"),
                            .string("multiply"),
                            .string("divide")
                        ]),
                        "description": .string("Operation to perform")
                    ]),
                    "a": .object([
                        "type": .string("number"),
                        "description": .string("First operand")
                    ]),
                    "b": .object([
                        "type": .string("number"),
                        "description": .string("Second operand")
                    ])
                ]),
                "required": .array([
                    .string("operation"),
                    .string("a"),
                    .string("b")
                ])
            ])
        )
    ]
}
```
