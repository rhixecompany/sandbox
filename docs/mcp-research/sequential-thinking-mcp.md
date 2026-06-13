# Sequential Thinking MCP Server

**Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking

## Overview

An MCP server implementation providing a **structured thinking tool** for dynamic, reflective problem-solving through step-by-step reasoning processes.

## Tool: `sequential_thinking`

Facilitates detailed, step-by-step thinking for problem-solving and analysis.

### Input Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `thought` | string | The current thinking step |
| `nextThoughtNeeded` | boolean | Whether another thought step is required |
| `thoughtNumber` | number | Current step number |
| `totalThoughts` | number | Estimated total steps |
| `isRevision` | boolean | Whether this revises a previous thought |
| `revisesThought` | number | Which thought number this revises |
| `branchFromThought` | number | Branch point for alternative reasoning |
| `branchId` | string | Identifier for reasoning branch |
| `needsMoreThoughts` | boolean | Whether additional thoughts needed beyond estimate |

## Use Cases

The tool excels at:

- **Database migrations** — *"Plan a database migration from PostgreSQL 14 to 16, list risks, and revise the plan if downtime exceeds 5 minutes."*
- **Production debugging** — *"Debug why this deployment only fails in production and show your reasoning step by step."*
- **Architecture comparison** — *"Compare three architecture options for a file sync engine and branch if one assumption turns out to be wrong."*

## How It Works

1. **Connect** the server to an MCP-aware host (Claude Desktop, VS Code, Codex CLI)
2. **Ask** the model to think through a problem step by step
3. **Host calls** `sequential_thinking` repeatedly during reasoning
4. **Observe** tool activity showing:
   - `thought`, `thoughtNumber`, `totalThoughts`, `nextThoughtNeeded`
   - Revision fields: `isRevision`, `revisesThought`
   - Branching fields: `branchFromThought`, `branchId`

## Configuration

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sequentialthinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

**Windows:** Use `cmd /c npx` instead of `npx`

**Docker:**
```json
{
  "mcpServers": {
    "sequentialthinking": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "mcp/sequentialthinking"]
    }
  }
}
```

**Environment Variable:** Set `DISABLE_THOUGHT_LOGGING=true` to disable thought logging

### VS Code

#### Quick Install Buttons

| Method | VS Code | VS Code Insiders |
|--------|---------|------------------|
| **NPX** | [![Install](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-sequential-thinking%22%5D%7D) | [![Install](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-sequential-thinking%22%5D%7D&quality=insiders) |
| **Docker** | [![Install](https://img.shields.io/badge/VS_Code-Docker-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22--rm%22%2C%22-i%22%2C%22mcp%2Fsequentialthinking%22%5D%7D) | [![Install](https://img.shields.io/badge/VS_Code_Insiders-Docker-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22--rm%22%22%2C%22-i%22%2C%22mcp%2Fsequentialthinking%22%5D%7D&quality=insiders) |

#### Manual Configuration

**Method 1: User Configuration (Recommended)**
1. Open Command Palette: `Ctrl + Shift + P`
2. Run: `MCP: Open User Configuration`
3. Add to `mcp.json`:

```json
{
  "servers": {
    "sequentialthinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

**Windows NPX:**
```json
{
  "command": "cmd",
  "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-sequential-thinking"]
}
```

**Docker:**
```json
{
  "command": "docker",
  "args": ["run", "--rm", "-i", "mcp/sequentialthinking"]
}
```

**Method 2: Workspace Configuration**
Create `.vscode/mcp.json` in your workspace for team sharing.

> **Reference:** [VS Code MCP Documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)

### Codex CLI

```bash
# NPX
codex mcp add sequential-thinking npx -y @modelcontextprotocol/server-sequential-thinking

# Docker
codex mcp add sequential-thinking docker run --rm -i mcp/sequentialthinking
```

### Copilot CLI

```bash
copilot mcp add sequential-thinking npx -y @modelcontextprotocol/server-sequential-thinking
```

### Hermes Integration

For Hermes Agent, add to `config.yaml`:

```yaml
mcp_servers:
  sequential-thinking:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    # Windows:
    # command: "cmd"
    # args: ["/c", "npx", "-y", "@modelcontextprotocol/server-sequential-thinking"]
    env:
      DISABLE_THOUGHT_LOGGING: "false"
    tools:
      include: [sequential_thinking]
```

Then run:
```bash
hermes mcp test sequential-thinking
/reload-mcp
```

## Alternative Implementation

There's also an alternative Python-based implementation at: https://github.com/arben-adm/mcp-sequential-thinking

```bash
# Using uv
claude mcp add sequential-thinking -- uv run --directory /path/to/mcp-sequential-thinking -m mcp_sequential_thinking.server
```

## References

- GitHub (Official): https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- mcpservers.org: https://mcpservers.org/servers/modelcontextprotocol/sequentialthinking
- Alternative: https://github.com/arben-adm/mcp-sequential-thinking