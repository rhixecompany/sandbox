# Chroma MCP Server — Comprehensive Summary

## Overview

**Repository:** [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp)
**License:** Apache 2.0
**Language:** Python

A **Model Context Protocol (MCP) server** implementation that provides **Chroma database capabilities** to LLM applications. It enables AI models to create collections over generated data and user inputs, and retrieve that data using **vector search, full text search, metadata filtering**, and more.

> "The Model Context Protocol (MCP) is an open protocol designed for effortless integration between LLM applications and external data sources or tools, offering a standardized framework to seamlessly provide LLMs with the context they require."

---

## Key Features

### Flexible Client Types
- **Persistent client** — uses a local data directory
- **Cloud client** — connects to `api.trychroma.com` via SSL
- **HTTP client** — connects to a self-hosted Chroma instance

### Supported Tools (13 total)

| Tool | Purpose |
|---|---|
| `chroma_list_collections` | List all collections |
| `chroma_create_collection` | Create a new collection |
| `chroma_peek_collection` | Peek at collection contents |
| `chroma_get_collection_info` | Get collection metadata |
| `chroma_get_collection_count` | Get document count |
| `chroma_modify_collection` | Modify collection properties |
| `chroma_delete_collection` | Delete a collection |
| `chroma_add_documents` | Add documents to a collection |
| `chroma_query_documents` | Query documents (vector/full-text/metadata) |
| `chroma_get_documents` | Retrieve documents by ID/filter |
| `chroma_update_documents` | Update existing documents |
| `chroma_delete_documents` | Delete documents from a collection |

### Supported Embedding Functions
- `default`
- `cohere`
- `openai`
- `jina`
- `voyageai`
- `roboflow`

> **Note:** Embedding function persistence was added in **Chroma v1.0.0**. Collections created with **version <= 0.6.3** do not support this feature.

---

## Usage with Claude Desktop

### Persistent Client (Local)
```json
// claude_desktop_config.json
{
  "mcpServers": {
    "chroma": {
      "command": "chroma-mcp",
      "args": ["--client-type", "persistent", "--data-dir", "/path/to/data"]
    }
  }
}
```

### Cloud Client
```json
// claude_desktop_config.json
{
  "mcpServers": {
    "chroma": {
      "command": "chroma-mcp",
      "args": ["--client-type", "cloud", "--api-key", "your-api-key"]
    }
  }
}
```

### HTTP Client (Self-Hosted)
```json
// claude_desktop_config.json
{
  "mcpServers": {
    "chroma": {
      "command": "chroma-mcp",
      "args": ["--client-type", "http", "--host", "localhost", "--port", "8000"]
    }
  }
}
```

### Custom Environment File Path
```json
"args": ["chroma-mcp", "--dotenv-path", "/custom/path/.env"]
```

---

## Environment Variable Configuration

The server loads variables from:
1. A `.env` file at the path specified by `--dotenv-path` (defaults to `.chroma_env` in the working directory)
2. System environment variables

> **Precedence:** Command-line arguments > Environment variables > `.env` file

### Embedding Function API Keys

Follow the naming convention:
```
CHROMA_<PROVIDER>_API_KEY="<key>"
```

**Example:**
```
CHROMA_COHERE_API_KEY="your-cohere-key"
CHROMA_OPENAI_API_KEY="your-openai-key"
```

Use the `CHROMA_DOTENV_PATH` environment variable or `--dotenv-path` flag to securely point to your `.env` file.

---

## Repository Structure

```
chroma-mcp/
├── .github/workflows/     # CI/CD workflows
├── src/chroma_mcp/        # Main source code
├── tests/                 # Test suite
├── CHANGELOG.md           # Version history
├── Dockerfile             # Docker support
├── LICENSE                # Apache 2.0
├── README.md              # Documentation
├── SECURITY.md            # Security policy
├── pyproject.toml         # Python project config
├── smithery.yaml          # Smithery deployment config
├── glama.json             # Glama configuration
├── uv.lock                # Dependency lock file
└── .python-version        # Python version specifier
```

---

## Key Links

- **Chroma Homepage:** [trychroma.com](https://www.trychroma.com/)
- **Documentation:** [docs.trychroma.com](https://docs.trychroma.com/)
- **MCP Docs (Claude integration):** [Chroma MCP Docs](https://docs.trychroma.com/integrations/frameworks/anthropic-mcp#using-chroma-with-claude)
- **Discord:** [Join here](https://discord.gg/MMeYNTmh3x)
- **Smithery:** [@chroma-core/chroma-mcp](https://smithery.ai/server/@chroma-core/chroma-mcp)
- **Package Search repo:** [chroma-core/package-search](https://github.com/chroma-core/package-search)

---

## Important Notes

- This server is for **self-hosting** access to Chroma via MCP.
- For **Package Search** functionality, use the separate [package-search repository](https://github.com/chroma-core/package-search).
- API keys passed in arguments are acceptable on **local devices**, but using `--dotenv-path` with a `.env` file is recommended for security.
