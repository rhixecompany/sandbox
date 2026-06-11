---
name: mcp-builder-python_mcp_server
description: "Python MCP Server Implementation Guide"
version: 1.0.0
author: Alexa
---
     1|# Python MCP Server Implementation Guide
     2|
     3|## Overview
     4|
     5|This document provides Python-specific best practices and examples for implementing MCP servers using the MCP Python SDK. It covers server setup, tool registration patterns, input validation with Pydantic, error handling, and complete working examples.
     6|
     7|---
     8|
     9|## Quick Reference
    10|
    11|### Key Imports
    12|
    13|```python
    14|from mcp.server.fastmcp import FastMCP
    15|from pydantic import BaseModel, Field, field_validator, ConfigDict
    16|from typing import Optional, List, Dict, Any
    17|from enum import Enum
    18|import httpx
    19|```
    20|
    21|### Server Initialization
    22|
    23|```python
    24|mcp = FastMCP("service_mcp")
    25|```
    26|
    27|### Tool Registration Pattern
    28|
    29|```python
    30|@mcp.tool(name="tool_name", annotations={...})
    31|async def tool_function(params: InputModel) -> str:
    32|    # Implementation
    33|    pass
    34|```
    35|
    36|---
    37|
    38|## MCP Python SDK and FastMCP
    39|
    40|The official MCP Python SDK provides FastMCP, a high-level framework for building MCP servers. It provides:
    41|
    42|- Automatic description and inputSchema generation from function signatures and docstrings
    43|- Pydantic model integration for input validation
    44|- Decorator-based tool registration with `@mcp.tool`
    45|
    46|**For complete SDK documentation, use WebFetch to load:** `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
    47|
    48|## Server Naming Convention
    49|
    50|Python MCP servers must follow this naming pattern:
    51|
    52|- **Format**: `{service}_mcp` (lowercase with underscores)
    53|- **Examples**: `github_mcp`, `jira_mcp`, `stripe_mcp`
    54|
    55|The name should be:
    56|
    57|- General (not tied to specific features)
    58|- Descriptive of the service/API being integrated
    59|- Easy to infer from the task description
    60|- Without version numbers or dates
    61|
    62|## Tool Implementation
    63|
    64|### Tool Naming
    65|
    66|Use snake_case for tool names (e.g., "search_users", "create_project", "get_channel_info") with clear, action-oriented names.
    67|
    68|**Avoid Naming Conflicts**: Include the service context to prevent overlaps:
    69|
    70|- Use "slack_send_message" instead of just "send_message"
    71|- Use "github_create_issue" instead of just "create_issue"
    72|- Use "asana_list_tasks" instead of just "list_tasks"
    73|
    74|### Tool Structure with FastMCP
    75|
    76|Tools are defined using the `@mcp.tool` decorator with Pydantic models for input validation:
    77|
    78|```python
    79|from pydantic import BaseModel, Field, ConfigDict
    80|from mcp.server.fastmcp import FastMCP
    81|
    82|# Initialize the MCP server
    83|mcp = FastMCP("example_mcp")
    84|
    85|# Define Pydantic model for input validation
    86|class ServiceToolInput(BaseModel):
    87|    '''Input model for service tool operation.'''
    88|    model_config = ConfigDict(
    89|        str_strip_whitespace=True,  # Auto-strip whitespace from strings
    90|        validate_assignment=True,    # Validate on assignment
    91|        extra='forbid'              # Forbid extra fields
    92|    )
    93|
    94|    param1: str = Field(..., description="First parameter description (e.g., 'user123', 'project-abc')", min_length=1, max_length=100)
    95|    param2: Optional[int] = Field(default=None, description="Optional integer parameter with constraints", ge=0, le=1000)
    96|    tags: Optional[List[str]] = Field(default_factory=list, description="List of tags to apply", max_items=10)
    97|
    98|@mcp.tool(
    99|    name="service_tool_name",
   100|    annotations={
   101|        "title": "Human-Readable Tool Title",
   102|        "readOnlyHint": True,     # Tool does not modify environment
   103|        "destructiveHint": False,  # Tool does not perform destructive operations
   104|        "idempotentHint": True,    # Repeated calls have no additional effect
   105|        "openWorldHint": False     # Tool does not interact with external entities
   106|    }
   107|)
   108|async def service_tool_name(params: ServiceToolInput) -> str:
   109|    '''Tool description automatically becomes the 'description' field.
   110|
   111|    This tool performs a specific operation on the service. It validates all inputs
   112|    using the ServiceToolInput Pydantic model before processing.
   113|
   114|    Args:
   115|        params (ServiceToolInput): Validated input parameters containing:
   116|            - param1 (str): First parameter description
   117|            - param2 (Optional[int]): Optional parameter with default
   118|            - tags (Optional[List[str]]): List of tags
   119|
   120|    Returns:
   121|        str: JSON-formatted response containing operation results
   122|    '''
   123|    # Implementation here
   124|    pass
   125|```
   126|
   127|## Pydantic v2 Key Features
   128|
   129|- Use `model_config` instead of nested `Config` class
   130|- Use `field_validator` instead of deprecated `validator`
   131|- Use `model_dump()` instead of deprecated `dict()`
   132|- Validators require `@classmethod` decorator
   133|- Type hints are required for validator methods
   134|
   135|```python
   136|from pydantic import BaseModel, Field, field_validator, ConfigDict
   137|
   138|class CreateUserInput(BaseModel):
   139|    model_config = ConfigDict(
   140|        str_strip_whitespace=True,
   141|        validate_assignment=True
   142|    )
   143|
   144|    name: str = Field(..., description="User's full name", min_length=1, max_length=100)
   145|    email: str = Field(..., description="User's email address", pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
   146|    age: int = Field(..., description="User's age", ge=0, le=150)
   147|
   148|    @field_validator('email')
   149|    @classmethod
   150|    def validate_email(cls, v: str) -> str:
   151|        if not v.strip():
   152|            raise ValueError("Email cannot be empty")
   153|        return v.lower()
   154|```
   155|
   156|## Response Format Options
   157|
   158|Support multiple output formats for flexibility:
   159|
   160|```python
   161|from enum import Enum
   162|
   163|class ResponseFormat(str, Enum):
   164|    '''Output format for tool responses.'''
   165|    MARKDOWN = "markdown"
   166|    JSON = "json"
   167|
   168|class UserSearchInput(BaseModel):
   169|    query: str = Field(..., description="Search query")
   170|    response_format: ResponseFormat = Field(
   171|        default=ResponseFormat.MARKDOWN,
   172|        description="Output format: 'markdown' for human-readable or 'json' for machine-readable"
   173|    )
   174|```
   175|
   176|**Markdown format**:
   177|
   178|- Use headers, lists, and formatting for clarity
   179|- Convert timestamps to human-readable format (e.g., "2024-01-15 10:30:00 UTC" instead of epoch)
   180|- Show display names with IDs in parentheses (e.g., "@john.doe (U123456)")
   181|- Omit verbose metadata (e.g., show only one profile image URL, not all sizes)
   182|- Group related information logically
   183|
   184|**JSON format**:
   185|
   186|- Return complete, structured data suitable for programmatic processing
   187|- Include all available fields and metadata
   188|- Use consistent field names and types
   189|
   190|## Pagination Implementation
   191|
   192|For tools that list resources:
   193|
   194|```python
   195|class ListInput(BaseModel):
   196|    limit: Optional[int] = Field(default=20, description="Maximum results to return", ge=1, le=100)
   197|    offset: Optional[int] = Field(default=0, description="Number of results to skip for pagination", ge=0)
   198|
   199|async def list_items(params: ListInput) -> str:
   200|    # Make API request with pagination
   201|    data = await api_request(limit=params.limit, offset=params.offset)
   202|
   203|    # Return pagination info
   204|    response = {
   205|        "total": data["total"],
   206|        "count": len(data["items"]),
   207|        "offset": params.offset,
   208|        "items": data["items"],
   209|        "has_more": data["total"] > params.offset + len(data["items"]),
   210|        "next_offset": params.offset + len(data["items"]) if data["total"] > params.offset + len(data["items"]) else None
   211|    }
   212|    return json.dumps(response, indent=2)
   213|```
   214|
   215|## Character Limits and Truncation
   216|
   217|Add a CHARACTER_LIMIT constant to prevent overwhelming responses:
   218|
   219|```python
   220|# At module level
   221|CHARACTER_LIMIT = 25000  # Maximum response size in characters
   222|
   223|async def search_tool(params: SearchInput) -> str:
   224|    result = generate_response(data)
   225|
   226|    # Check character limit and truncate if needed
   227|    if len(result) > CHARACTER_LIMIT:
   228|        # Truncate data and add notice
   229|        truncated_data = data[:max(1, len(data) // 2)]
   230|        response["data"] = truncated_data
   231|        response["truncated"] = True
   232|        response["truncation_message"] = (
   233|            f"Response truncated from {len(data)} to {len(truncated_data)} items. "
   234|            f"Use 'offset' parameter or add filters to see more results."
   235|        )
   236|        result = json.dumps(response, indent=2)
   237|
   238|    return result
   239|```
   240|
   241|## Error Handling
   242|
   243|Provide clear, actionable error messages:
   244|
   245|```python
   246|def _handle_api_error(e: Exception) -> str:
   247|    '''Consistent error formatting across all tools.'''
   248|    if isinstance(e, httpx.HTTPStatusError):
   249|        if e.response.status_code == 404:
   250|            return "Error: Resource not found. Please check the ID is correct."
   251|        elif e.response.status_code == 403:
   252|            return "Error: Permission denied. You don't have access to this resource."
   253|        elif e.response.status_code == 429:
   254|            return "Error: Rate limit exceeded. Please wait before making more requests."
   255|        return f"Error: API request failed with status {e.response.status_code}"
   256|    elif isinstance(e, httpx.TimeoutException):
   257|        return "Error: Request timed out. Please try again."
   258|    return f"Error: Unexpected error occurred: {type(e).__name__}"
   259|```
   260|
   261|## Shared Utilities
   262|
   263|Extract common functionality into reusable functions:
   264|
   265|```python
   266|# Shared API request function
   267|async def _make_api_request(endpoint: str, method: str = "GET", **kwargs) -> dict:
   268|    '''Reusable function for all API calls.'''
   269|    async with httpx.AsyncClient() as client:
   270|        response = await client.request(
   271|            method,
   272|            f"{API_BASE_URL}/{endpoint}",
   273|            timeout=30.0,
   274|            **kwargs
   275|        )
   276|        response.raise_for_status()
   277|        return response.json()
   278|```
   279|
   280|## Async/Await Best Practices
   281|
   282|Always use async/await for network requests and I/O operations:
   283|
   284|```python
   285|# Good: Async network request
   286|async def fetch_data(resource_id: str) -> dict:
   287|    async with httpx.AsyncClient() as client:
   288|        response = await client.get(f"{API_URL}/resource/{resource_id}")
   289|        response.raise_for_status()
   290|        return response.json()
   291|
   292|# Bad: Synchronous request
   293|def fetch_data(resource_id: str) -> dict:
   294|    response = requests.get(f"{API_URL}/resource/{resource_id}")  # Blocks
   295|    return response.json()
   296|```
   297|
   298|## Type Hints
   299|
   300|Use type hints throughout:
   301|
   302|```python
   303|from typing import Optional, List, Dict, Any
   304|
   305|async def get_user(user_id: str) -> Dict[str, Any]:
   306|    data = await fetch_user(user_id)
   307|    return {"id": data["id"], "name": data["name"]}
   308|```
   309|
   310|## Tool Docstrings
   311|
   312|Every tool must have comprehensive docstrings with explicit type information:
   313|
   314|```python
   315|async def search_users(params: UserSearchInput) -> str:
   316|    '''
   317|    Search for users in the Example system by name, email, or team.
   318|
   319|    This tool searches across all user profiles in the Example platform,
   320|    supporting partial matches and various search filters. It does NOT
   321|    create or modify users, only searches existing ones.
   322|
   323|    Args:
   324|        params (UserSearchInput): Validated input parameters containing:
   325|            - query (str): Search string to match against names/emails (e.g., "john", "@example.com", "team:marketing")
   326|            - limit (Optional[int]): Maximum results to return, between 1-100 (default: 20)
   327|            - offset (Optional[int]): Number of results to skip for pagination (default: 0)
   328|
   329|    Returns:
   330|        str: JSON-formatted string containing search results with the following schema:
   331|
   332|        Success response:
   333|        {
   334|            "total": int,           # Total number of matches found
   335|            "count": int,           # Number of results in this response
   336|            "offset": int,          # Current pagination offset
   337|            "users": [
   338|                {
   339|                    "id": str,      # User ID (e.g., "U123456789")
   340|                    "name": str,    # Full name (e.g., "John Doe")
   341|                    "email": str,   # Email address (e.g., "john@example.com")
   342|                    "team": str     # Team name (e.g., "Marketing") - optional
   343|                }
   344|            ]
   345|        }
   346|
   347|        Error response:
   348|        "Error: <error message>" or "No users found matching '<query>'"
   349|
   350|    Examples:
   351|        - Use when: "Find all marketing team members" -> params with query="team:marketing"
   352|        - Use when: "Search for John's account" -> params with query="john"
   353|        - Don't use when: You need to create a user (use example_create_user instead)
   354|        - Don't use when: You have a user ID and need full details (use example_get_user instead)
   355|
   356|    Error Handling:
   357|        - Input validation errors are handled by Pydantic model
   358|        - Returns "Error: Rate limit exceeded" if too many requests (429 status)
   359|        - Returns "Error: Invalid API authentication" if API key is invalid (401 status)
   360|        - Returns formatted list of results or "No users found matching 'query'"
   361|    '''
   362|```
   363|
   364|## Complete Example
   365|
   366|See below for a complete Python MCP server example:
   367|
   368|```python
   369|#!/usr/bin/env python3
   370|'''
   371|MCP Server for Example Service.
   372|
   373|This server provides tools to interact with Example API, including user search,
   374|project management, and data export capabilities.
   375|'''
   376|
   377|from typing import Optional, List, Dict, Any
   378|from enum import Enum
   379|import httpx
   380|from pydantic import BaseModel, Field, field_validator, ConfigDict
   381|from mcp.server.fastmcp import FastMCP
   382|
   383|# Initialize the MCP server
   384|mcp = FastMCP("example_mcp")
   385|
   386|# Constants
   387|API_BASE_URL = "https://api.example.com/v1"
   388|CHARACTER_LIMIT = 25000  # Maximum response size in characters
   389|
   390|# Enums
   391|class ResponseFormat(str, Enum):
   392|    '''Output format for tool responses.'''
   393|    MARKDOWN = "markdown"
   394|    JSON = "json"
   395|
   396|# Pydantic Models for Input Validation
   397|class UserSearchInput(BaseModel):
   398|    '''Input model for user search operations.'''
   399|    model_config = ConfigDict(
   400|        str_strip_whitespace=True,
   401|        validate_assignment=True
   402|    )
   403|
   404|    query: str = Field(..., description="Search string to match against names/emails", min_length=2, max_length=200)
   405|    limit: Optional[int] = Field(default=20, description="Maximum results to return", ge=1, le=100)
   406|    offset: Optional[int] = Field(default=0, description="Number of results to skip for pagination", ge=0)
   407|    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN, description="Output format")
   408|
   409|    @field_validator('query')
   410|    @classmethod
   411|    def validate_query(cls, v: str) -> str:
   412|        if not v.strip():
   413|            raise ValueError("Query cannot be empty or whitespace only")
   414|        return v.strip()
   415|
   416|# Shared utility functions
   417|async def _make_api_request(endpoint: str, method: str = "GET", **kwargs) -> dict:
   418|    '''Reusable function for all API calls.'''
   419|    async with httpx.AsyncClient() as client:
   420|        response = await client.request(
   421|            method,
   422|            f"{API_BASE_URL}/{endpoint}",
   423|            timeout=30.0,
   424|            **kwargs
   425|        )
   426|        response.raise_for_status()
   427|        return response.json()
   428|
   429|def _handle_api_error(e: Exception) -> str:
   430|    '''Consistent error formatting across all tools.'''
   431|    if isinstance(e, httpx.HTTPStatusError):
   432|        if e.response.status_code == 404:
   433|            return "Error: Resource not found. Please check the ID is correct."
   434|        elif e.response.status_code == 403:
   435|            return "Error: Permission denied. You don't have access to this resource."
   436|        elif e.response.status_code == 429:
   437|            return "Error: Rate limit exceeded. Please wait before making more requests."
   438|        return f"Error: API request failed with status {e.response.status_code}"
   439|    elif isinstance(e, httpx.TimeoutException):
   440|        return "Error: Request timed out. Please try again."
   441|    return f"Error: Unexpected error occurred: {type(e).__name__}"
   442|
   443|# Tool definitions
   444|@mcp.tool(
   445|    name="example_search_users",
   446|    annotations={
   447|        "title": "Search Example Users",
   448|        "readOnlyHint": True,
   449|        "destructiveHint": False,
   450|        "idempotentHint": True,
   451|        "openWorldHint": True
   452|    }
   453|)
   454|async def example_search_users(params: UserSearchInput) -> str:
   455|    '''Search for users in the Example system by name, email, or team.
   456|
   457|    [Full docstring as shown above]
   458|    '''
   459|    try:
   460|        # Make API request using validated parameters
   461|        data = await _make_api_request(
   462|            "users/search",
   463|            params={
   464|                "q": params.query,
   465|                "limit": params.limit,
   466|                "offset": params.offset
   467|            }
   468|        )
   469|
   470|        users = data.get("users", [])
   471|        total = data.get("total", 0)
   472|
   473|        if not users:
   474|            return f"No users found matching '{params.query}'"
   475|
   476|        # Format response based on requested format
   477|        if params.response_format == ResponseFormat.MARKDOWN:
   478|            lines = [f"# User Search Results: '{params.query}'", ""]
   479|            lines.append(f"Found {total} users (showing {len(users)})")
   480|            lines.append("")
   481|
   482|            for user in users:
   483|                lines.append(f"## {user['name']} ({user['id']})")
   484|                lines.append(f"- **Email**: {user['email']}")
   485|                if user.get('team'):
   486|                    lines.append(f"- **Team**: {user['team']}")
   487|                lines.append("")
   488|
   489|            return "\n".join(lines)
   490|
   491|        else:
   492|            # Machine-readable JSON format
   493|            import json
   494|            response = {
   495|                "total": total,
   496|                "count": len(users),
   497|                "offset": params.offset,
   498|                "users": users
   499|            }
   500|            return json.dumps(response, indent=2)
   501|