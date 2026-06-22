# tools/tool1.go Template

> Extracted from `go-mcp-server-generator.prompt.md`.

## tools/tool1.go Template

```go
package tools

import (
    "context"
    "fmt"

    "github.com/modelcontextprotocol/go-sdk/mcp"
)

type Tool1Input struct {
    Param1 string `json:"param1" jsonschema:"required,description=First parameter"`
    Param2 int    `json:"param2,omitempty" jsonschema:"description=Optional second parameter"`
}

type Tool1Output struct {
    Result string `json:"result" jsonschema:"description=The result of the operation"`
    Status string `json:"status" jsonschema:"description=Operation status"`
}

func Tool1Handler(ctx context.Context, req *mcp.CallToolRequest, input Tool1Input) (
    *mcp.CallToolResult,
    Tool1Output,
    error,
) {
    // Validate input
    if input.Param1 == "" {
        return nil, Tool1Output{}, fmt.Errorf("param1 is required")
    }

    // Check context
    if ctx.Err() != nil {
        return nil, Tool1Output{}, ctx.Err()
    }

    // Perform operation
    result := fmt.Sprintf("Processed: %s", input.Param1)

    return nil, Tool1Output{
        Result: result,
        Status: "success",
    }, nil
}

func RegisterTool1(server *mcp.Server) {
    mcp.AddTool(server,
        &mcp.Tool{
            Name:        "tool1",
            Description: "Description of what tool1 does",
        },
        Tool1Handler,
    )
}
```
