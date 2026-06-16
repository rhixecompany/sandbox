# Gemini API Docs MCP Server

**Source:** https://github.com/google-gemini/gemini-api-mcp-server *(community)*  
**Official Gemini Docs:** https://ai.google.dev/docs  
**Python SDK:** https://github.com/google-gemini/generative-ai-python

## Overview

Exposes **Google Gemini API** capabilities to MCP-compatible AI agents. Allows agents to invoke Gemini models for text generation, multimodal processing, embeddings, and code execution — as well as search Gemini's official documentation.

As of 2025, there is no single official Gemini MCP server package from Google, but several community implementations exist, and Google's `@google/generative-ai` SDK is easily wrapped as MCP tools.

## Key Features

- Call Gemini models (gemini-1.5-pro, gemini-1.5-flash, etc.) from agent workflows
- Multimodal: text + image + video inputs
- Embedding generation with `text-embedding-004`
- Code execution via Gemini Code Execution tool
- Document (PDF) processing
- Search Gemini API documentation

## Tools to Expose as MCP

| Tool | Description |
|------|-------------|
| `generate_text` | Generate text using a Gemini model |
| `generate_with_image` | Multimodal generation with image input |
| `create_embedding` | Generate text embeddings |
| `execute_code` | Use Gemini's code execution capability |
| `search_docs` | Search Gemini API documentation |

## Installation

### Python SDK

```bash
pip install google-generativeai
```

### FastMCP Wrapper

```python
from mcp.server.fastmcp import FastMCP
import google.generativeai as genai
import os

mcp = FastMCP("gemini-api")
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

@mcp.tool()
def generate_text(prompt: str) -> str:
    """Generate text using Gemini 1.5 Flash."""
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    mcp.run()
```

### Node.js SDK

```bash
npm install @google/generative-ai @modelcontextprotocol/sdk
```

## Hermes Config

```yaml
mcp_servers:
  gemini-api:
    command: python3
    args: ["/path/to/gemini_mcp_server.py"]
    env:
      GEMINI_API_KEY: "AIza..."
```

## API Key Setup

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key for your project
3. Set `GEMINI_API_KEY` environment variable
4. Never commit the key to source control

## Available Models (2025)

| Model | Context | Best For |
|-------|---------|----------|
| `gemini-1.5-pro` | 2M tokens | Complex reasoning, long documents |
| `gemini-1.5-flash` | 1M tokens | Fast responses, multimodal |
| `gemini-2.0-flash` | 1M tokens | Latest, fastest |
| `text-embedding-004` | 2K tokens | Semantic search, RAG |

## Related Resources

- [Google AI for Developers](https://ai.google.dev/)
- [Gemini API Python SDK](https://github.com/google-gemini/generative-ai-python)
- [Gemini API Cookbook](https://github.com/google-gemini/cookbook)
- [Google AI Studio](https://aistudio.google.com/)
- [FastMCP for Python](https://github.com/jlowin/fastmcp)
