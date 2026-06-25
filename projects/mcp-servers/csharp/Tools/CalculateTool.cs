using ModelContextProtocol;
using ModelContextProtocol.Server;
using System.ComponentModel;

namespace CSharpMcpServer.Tools;

[McpTool("calculate")]
[Description("Performs a basic arithmetic operation on two numbers.")]
public sealed class CalculateTool
{
    [McpToolParameter]
    [Description("The first operand.")]
    public double A { get; set; }

    [McpToolParameter]
    [Description("The second operand.")]
    public double B { get; set; }

    [McpToolParameter]
    [Description("The arithmetic operation to perform. Valid values: add, subtract, multiply, divide, power, modulo.")]
    public string Operation { get; set; } = "add";

    [McpToolMethod]
    [Description("Executes the calculation and returns the result.")]
    public string Execute()
    {
        var result = Operation.ToLowerInvariant() switch
        {
            "add" => A + B,
            "sum" => A + B,
            "subtract" => A - B,
            "minus" => A - B,
            "multiply" => A * B,
            "times" => A * B,
            "divide" or "divided by" when B == 0
                => throw new DivideByZeroException("Division by zero is not allowed."),
            "divide" => A / B,
            "divided by" => A / B,
            "power" => Math.Pow(A, B),
            "pow" => Math.Pow(A, B),
            "modulo" => A % B,
            "mod" => A % B,
            _ => throw new ArgumentException($"Unknown operation '{Operation}'. Valid operations: add, subtract, multiply, divide, power, modulo.")
        };

        return $"{A} {Operation} {B} = {result}";
    }
}
