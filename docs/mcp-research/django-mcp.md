# Django MCP Server

**Source:** https://github.com/gts360/django-mcp-server

## Overview

**Django MCP Server** is a Django extension implementing the **Model Context Protocol (MCP)** that allows **MCP Clients** and **AI agents** to interact with **any Django application** seamlessly.

### Key Highlights

- 🚀 **Django-style declarative tools** for AI agents and MCP clients
- 🚀 **Expose Django models** for AI querying in 2 lines of code (safely)
- 🚀 **Convert DRF APIs to MCP tools** with one annotation
- ✅ Works on **both WSGI and ASGI** without infrastructure changes
- ✅ **Validated as Remote Integration** with Claude AI
- 🤖 Compatible with any MCP client: Google ADK, Claude AI, Claude Desktop, etc.

**License:** MIT | **Maintained by:** Smart GTS Software Engineering

## Quick Start

### 1. Installation

```bash
pip install django-mcp-server
# Or from GitHub:
pip install git+https://github.com/gts360/django-mcp-server.git
```

### 2. Configure Django

**settings.py:**
```python
INSTALLED_APPS = [
    # ...
    'mcp_server',
]
```

**urls.py:**
```python
from django.urls import path, include

urlpatterns = [
    # ...
    path('mcp/', include('mcp_server.urls')),
]
```
> Default MCP endpoint: `/mcp`

### 3. Define MCP Tools

Create `mcp.py` in your app:

```python
# Expose Django models for querying
from mcp_server.toolsets import ModelQueryToolset
from myapp.models import MyModel

class MyModelToolset(ModelQueryToolset):
    model = MyModel
    # Optional: fields to expose, filters, etc.

# Or create generic tools
from mcp_server.toolsets import MCPToolset

class MyCustomToolset(MCPToolset):
    def my_tool(self, param: str) -> str:
        """Tool description for the AI"""
        return f"Result: {param}"
    
    def _private_method(self):  # Not published (starts with _)
        pass
```

### 4. Verify with MCP Inspect

```bash
python manage.py mcp_inspect
```

### 5. Test with Python MCP SDK

```python
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def test():
    async with streamablehttp_client("http://localhost:8000/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(tools)

asyncio.run(test())
```

## Advanced Topics

### Publish DRF APIs as MCP Tools

```python
from mcp_server.decorators import (
    drf_publish_create_mcp_tool,
    drf_publish_update_mcp_tool,
    drf_publish_delete_mcp_tool,
    drf_publish_list_mcp_tool,
)
from rest_framework import viewsets
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

@drf_publish_list_mcp_tool()
@drf_publish_create_mcp_tool()
@drf_publish_update_mcp_tool()
@drf_publish_delete_mcp_tool()
class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    """
    This docstring becomes instructions for the AI model.
    """
```

**Important Notes:**
- Built-in authentication, filter_backends, permission_classes, and pagination_class are **disabled by default** (MCP auth used instead)
- `self.paginator` will be `None` - account for this in existing paginated views
- For older DRF versions without schema generation, provide schema manually

### DRF Serializer Integration

```python
from mcp_server.decorators import drf_serialize_output
from myapp.serializers import MySerializer

class MyToolset(MCPToolset):
    @drf_serialize_output(MySerializer)
    def my_tool(self) -> dict:
        return {"data": "serialized output"}
```

### Low-Level MCP Server Annotations

```python
from mcp_server.server import mcp_server

@mcp_server.tool()
def my_custom_tool(param: str) -> str:
    return f"Result: {param}"

@mcp_server.resource("resource://my-resource")
def my_resource() -> str:
    return "Resource content"
```

⚠️ **Important:** State preservation across calls doesn't work in WSGI deployments with `@mcp_server.tool()` due to Django's thread-per-request architecture.

## Configuration Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `DJANGO_MCP_GLOBAL_SERVER_CONFIG` | `{}` | Config dict passed to `MCPServer` initialization |
| `DJANGO_MCP_AUTHENTICATION_CLASSES` | `[]` | List of DRF authentication classes for main MCP view |
| `DJANGO_MCP_GET_SERVER_INSTRUCTIONS_TOOL` | `True` | Offer tool to get global instructions |
| `DJANGO_MCP_ENDPOINT` | `"mcp"` | URL endpoint (use `"mcp/"` for trailing slash) |

### Example settings.py

```python
# OAuth2 Authentication (recommended per MCP Spec 2025-03-26)
DJANGO_MCP_AUTHENTICATION_CLASSES = [
    'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
]

# Global server config
DJANGO_MCP_GLOBAL_SERVER_CONFIG = {
    "stateless": True,  # Make server stateless
}

# Custom endpoint
DJANGO_MCP_ENDPOINT = "mcp/"
```

## Session Management

- **Default:** Stateful using Django sessions (`request.session`)
- **Stateless:** Set `DJANGO_MCP_GLOBAL_SERVER_CONFIG = {"stateless": True}`
- **WSGI:** Sessions don't persist across workers — consider stateless mode

## Hermes Integration

For Hermes Agent (STDIO mode for local Django dev):

```yaml
mcp_servers:
  django-dev:
    command: "python"
    args: ["manage.py", "mcp_stdio"]  # Requires custom management command
    # OR for HTTP mode (run Django server separately):
    # url: "http://localhost:8000/mcp"
    # transport: "streamable-http"
    tools:
      include: [model_query, drf_list, drf_create, drf_update, drf_delete]
```

Then run:
```bash
hermes mcp test django-dev
/reload-mcp
```

## References

- GitHub: https://github.com/gts360/django-mcp-server
- PyPI: https://pypi.org/project/django-mcp-server
- django-ai-boost: https://github.com/vintasoftware/django-ai-boost