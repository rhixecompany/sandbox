using ModelContextProtocol;
using ModelContextProtocol.Server;
using System.ComponentModel;

namespace CSharpMcpServer.Tools;

[McpTool("greet")]
[Description("Greets a user by name and returns a friendly message.")]
public sealed class GreetTool
{
    [McpToolParameter]
    [Description("The name of the person to greet.")]
    public string Name { get; set; } = string.Empty;

    [McpToolParameter]
    [Description("Optional title (e.g., Mr., Ms., Dr.).")]
    public string? Title { get; set; }

    [McpToolMethod]
    [Description("Generates a personalized greeting message.")]
    public string Execute()
    {
        var prefix = string.IsNullOrWhiteSpace(Title) ? string.Empty : $"{Title} ";
        return $"Hello, {prefix}{Name}! Welcome to C# MCP Server. The current time is {DateTime.Now:HH:mm:ss} UTC.";
    }
}
