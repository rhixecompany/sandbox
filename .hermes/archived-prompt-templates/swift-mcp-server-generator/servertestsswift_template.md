# ServerTests.swift Template

> Extracted from `swift-mcp-server-generator.prompt.md`.

## ServerTests.swift Template

```swift
import XCTest
@testable import MyMCPServer

final class ServerTests: XCTestCase {
    func testGreetTool() async throws {
        let params = CallTool.Params(
            name: "greet",
            arguments: ["name": .string("Swift")]
        )

        let result = handleGreet(params: params)

        XCTAssertFalse(result.isError ?? true)
        XCTAssertEqual(result.content.count, 1)

        if case .text(let message) = result.content[0] {
            XCTAssertTrue(message.contains("Swift"))
        } else {
            XCTFail("Expected text content")
        }
    }

    func testCalculateTool() async throws {
        let params = CallTool.Params(
            name: "calculate",
            arguments: [
                "operation": .string("add"),
                "a": .number(5),
                "b": .number(3)
            ]
        )

        let result = handleCalculate(params: params)

        XCTAssertFalse(result.isError ?? true)
        XCTAssertEqual(result.content.count, 1)

        if case .text(let message) = result.content[0] {
            XCTAssertTrue(message.contains("8"))
        } else {
            XCTFail("Expected text content")
        }
    }

    func testDivideByZero() async throws {
        let params = CallTool.Params(
            name: "calculate",
            arguments: [
                "operation": .string("divide"),
                "a": .number(10),
                "b": .number(0)
            ]
        )

        let result = handleCalculate(params: params)

        XCTAssertTrue(result.isError ?? false)
    }
}
```
