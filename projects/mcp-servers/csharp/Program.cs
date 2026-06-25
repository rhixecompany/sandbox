using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

// Register MCP server with a name
builder.Services.AddMcpServer(options =>
{
    options.ServerInfo = new ServerInfo
    {
        Name = "CSharpMcpServer",
        Version = "1.0.0"
    };
})
.AddToolsFromAssembly();

// Register the tools explicitly (optional, AddToolsFromAssembly auto-discovers)
builder.Services.AddSingleton<CSharpMcpServer.Tools.GreetTool>();
builder.Services.AddSingleton<CSharpMcpServer.Tools.CalculateTool>();

var host = builder.Build();

// Start the MCP server using stdio transport
await host.RunAsync();
