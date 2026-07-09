---
title: CalculateTool - Technical Documentation
component_path: `projects/mcp-servers/csharp/Tools/CalculateTool.cs`
version: 1.0.0
date_created: 2026-07-09
last_updated: 2026-07-09
owner: CSharpMcpServer (MCP Servers project)
---

# CalculateTool Documentation

`CalculateTool` is a sealed C# class that implements an MCP (Model Context Protocol) tool for performing basic arithmetic operations on two numeric operands. It is part of the `CSharpMcpServer` host, a multi-language MCP server implementation, and is exposed to MCP clients over stdio transport. The class is attribute-driven (`[McpTool]`, `[McpToolParameter]`, `[McpToolMethod]`), requiring no boilerplate wiring beyond assembly auto-discovery.

## 1. Component Overview

### Purpose/Responsibility

- OVR-001: Provide a single, self-contained MCP tool that performs arithmetic (`add`, `subtract`, `multiply`, `divide`, `power`, `modulo`) on two `double` operands and returns a human-readable result string.
- OVR-002: **In scope** — operand binding, operation dispatch, zero-division and unknown-operation error handling, formatted string output. **Out of scope** — transport, server lifecycle, persistence, multi-operand expressions, or non-numeric computation (see `GreetTool` for a sibling non-math tool).
- OVR-003: Consumed by MCP clients (e.g. AI assistants) through the `CSharpMcpServer` host. Registered via `AddToolsFromAssembly()` in `Program.cs`; also explicitly registered as a singleton service.

## 2. Architecture Section

> - ARC-001: The class follows the **Tool/Command pattern** (parameter object + `Execute` method) over the MCP SDK's attribute-based model. It is `sealed` (no inheritance extension point) and acts as a stateless request handler — a Data-Transfer style parameter bag (`A`, `B`, `Operation`) plus a single `Execute()` verb.
> - ARC-002:
>   - **Internal dependencies:** None beyond the parameters it owns.
>   - **External dependencies:**
>     - `ModelContextProtocol` (v0.1.0-preview) — provides `McpTool`, `McpToolParameter`, `McpToolMethod` attributes and the tool execution contract.
>     - `ModelContextProtocol.Server` — server-side tool hosting.
>     - `System.ComponentModel` — provides `Description` attribute for tool/method metadata surfaced to MCP clients.
>     - `System` / `Math.Pow` — BCL arithmetic primitive.

## 3. Interface Documentation

- INT-001: Public surface is entirely attribute-decorated. The MCP SDK reads `[McpTool("calculate")]` to register the tool name, `[McpToolParameter]` properties as tool inputs, and `[McpToolMethod]` `Execute()` as the invocation entry point.
- INT-002: Method/property reference table below.
- INT-003: No events or callbacks; the tool is synchronous and returns a string directly to the caller.

| Member | Purpose | Parameters | Return Type | Usage Notes |
| --- | --- | --- | --- | --- |
| `A` | First operand | — (property, `double`) | `double` | Required; defaults to `0` via `double` default. |
| `B` | Second operand | — (property, `double`) | `double` | Required; divisor in `divide` (must be non-zero). |
| `Operation` | Arithmetic operation selector | — (property, `string`) | `string` | Case-insensitive. Default `"add"`. Accepts aliases: `add`/`sum`, `subtract`/`minus`, `multiply`/`times`, `divide`/`divided by`, `power`/`pow`, `modulo`/`mod`. |
| `Execute()` | Runs the operation and formats output | — | `string` | Returns `"{A} {Operation} {B} = {result}"`. Throws on invalid operation or division by zero. |

## 4. Implementation Details

- IMP-001: `CalculateTool` (`public sealed class`) owns three public auto-properties and one `public string Execute()` method. No subclasses or interfaces — `sealed` signals a terminal, non-extensible tool type.
- IMP-002: No explicit configuration or initialization logic. The tool is instantiated by the MCP host (registered `AddSingleton<CalculateTool>()` in `Program.cs`) and populated by the SDK from client-supplied parameters. `TargetFramework` is `net8.0`; `Nullable` is enabled, so `Operation` defaults to `"add"` and `A`/`B` to `0`.
- IMP-003: `Execute()` uses a C# `switch` expression over `Operation.ToLowerInvariant()`:
  - Arithmetic branch for each operation (`+`, `-`, `*`, `/`, `Math.Pow`, `%`).
  - `divide`/`divided by` short-circuits to `throw new DivideByZeroException(...)` when `B == 0` via a `when` guard.
  - Fallthrough `_` throws `ArgumentException` listing valid operations.
  - Result formatted with interpolated string `$"{A} {Operation} {B} = {result}"`.
- IMP-004: Performance is O(1) and allocation-light (single string interpolation). No I/O, no loops, no state. Bottlenecks: none at this scale.

## 5. Usage Examples

### Basic Usage

```csharp
// Basic usage — two operands with default "add"
var tool = new CalculateTool { A = 2, B = 3 };
string result = tool.Execute();   // "2 add 3 = 5"
```

### Advanced Usage

```csharp
// Advanced — power operation, aliased keyword, zero-division guard
var power = new CalculateTool { A = 2, B = 10, Operation = "pow" };
power.Execute();                  // "2 pow 10 = 1024"

var bad = new CalculateTool { A = 5, B = 0, Operation = "divide" };
// bad.Execute();                // throws DivideByZeroException("Division by zero is not allowed.")

// Invoked through the MCP host (Program.cs), not directly:
// builder.Services.AddSingleton<CSharpMcpServer.Tools.CalculateTool>();
// clients call the "calculate" tool with JSON { "A": 2, "B": 3, "Operation": "add" }
```

- USE-001: Provide operands `A`/`B` and an `Operation` string; call `Execute()`.
- USE-002: Aliases (`sum`, `minus`, `times`, `divided by`, `pow`, `mod`) are interchangeable with canonical names.
- USE-003: Always guard against `B == 0` before a `divide` call in client code; prefer canonical operation names for forward-compatibility.

## 6. Quality Attributes

- QUA-001 (Security): No authentication/authorization inside the tool; trust is delegated to the MCP host's transport layer. No data persistence — operands and results are ephemeral. Inputs are typed (`double`/`string`); the SDK validates parameter presence.
- QUA-002 (Performance): O(1), no allocation beyond the result string, no async — suitable for high-frequency tool calls. `double` arithmetic has standard IEEE-754 rounding/precision characteristics.
- QUA-003 (Reliability): Explicit, descriptive exceptions (`DivideByZeroException`, `ArgumentException`) provide clear failure signals. No retries or recovery logic (not needed for pure computation).
- QUA-004 (Maintainability): `sealed` + attribute metadata makes the contract explicit and discoverable. `ImplicitUsings` and `Nullable` enabled reduce boilerplate. No tests found in the repository for this component (gap — see REF-003).
- QUA-005 (Extensibility): `sealed` prevents subclassing; extension is via new sibling tool classes (e.g. `GreetTool`) or adding branches to the `switch`. New operations require a code change, not configuration.

## 7. Reference Information

- REF-001: Dependencies (from `CSharpMcpServer.csproj`):
  | Package | Version | Purpose |
  | --- | --- | --- |
  | `ModelContextProtocol` | `0.1.0-preview` | MCP tool attributes & hosting |
  | `Microsoft.Extensions.Hosting` | `8.0.0` | Generic host / DI / `RunAsync` |
  | .NET runtime | `net8.0` | Target framework |

- REF-002: Configuration options — none at the component level. Server name/version configured in `Program.cs` (`ServerInfo { Name = "CSharpMcpServer", Version = "1.0.0" }`).
- REF-003: Testing guidelines — no existing tests located. Recommended: unit-test `Execute()` across each branch (including aliases), assert `DivideByZeroException` for `B == 0`, and `ArgumentException` for unknown operations. Mock-free; the class is a plain object.
- REF-004: Troubleshooting:
  | Symptom | Cause | Fix |
  | --- | --- | --- |
  | `ArgumentException: Unknown operation '...'` | `Operation` not in valid set | Use `add/sum`, `subtract/minus`, `multiply/times`, `divide/divided by`, `power/pow`, `modulo/mod` |
  | `DivideByZeroException` | `Operation` is divide and `B == 0` | Ensure `B != 0` before divide |
  | Tool not discovered by server | Assembly not scanned | Confirm `AddToolsFromAssembly()` or explicit `AddSingleton<CalculateTool>()` in `Program.cs` |

- REF-005: Related docs — `GreetTool.cs` (sibling MCP tool), `Program.cs` (host/registration), project `AGENTS.md` and `architecture.md` under `projects/mcp-servers/`.
- REF-006: Change history — initial version `1.0.0` (net8.0, MCP SDK 0.1.0-preview). No migration notes.

---

### Verification Note
Artifact generated from real source: `projects/mcp-servers/csharp/Tools/CalculateTool.cs` (48 lines), corroborated by `Program.cs`, `GreetTool.cs`, and `CSharpMcpServer.csproj`. All facts (attributes, operations, exceptions, versions) are traced to source. Skipped template reference `templates/create-oo-component-documentation/2_architecture_section.md` — path does not exist in workspace (ERR), so inline content was authored per the prompt's embedded section spec.
