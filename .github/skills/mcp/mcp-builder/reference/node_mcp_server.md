---
name: mcp-builder-node_mcp_server
description: "Node/TypeScript MCP Server Implementation Guide"
version: 1.0.0
author: Alexa
---
     1|# Node/TypeScript MCP Server Implementation Guide
     2|
     3|## Overview
     4|
     5|This document provides Node/TypeScript-specific best practices and examples for implementing MCP servers using the MCP TypeScript SDK. It covers project structure, server setup, tool registration patterns, input validation with Zod, error handling, and complete working examples.
     6|
     7|---
     8|
     9|## Quick Reference
    10|
    11|### Key Imports
    12|
    13|```typescript
    14|import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
    15|import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
    16|import { z } from "zod";
    17|import axios, { AxiosError } from "axios";
    18|```
    19|
    20|### Server Initialization
    21|
    22|```typescript
    23|const server = new McpServer({
    24|  name: "service-mcp-server",
    25|  version: "1.0.0"
    26|});
    27|```
    28|
    29|### Tool Registration Pattern
    30|
    31|```typescript
    32|server.registerTool("tool_name", { ...config }, async params => {
    33|  // Implementation
    34|});
    35|```
    36|
    37|---
    38|
    39|## MCP TypeScript SDK
    40|
    41|The official MCP TypeScript SDK provides:
    42|
    43|- `McpServer` class for server initialization
    44|- `registerTool` method for tool registration
    45|- Zod schema integration for runtime input validation
    46|- Type-safe tool handler implementations
    47|
    48|See the MCP SDK documentation in the references for complete details.
    49|
    50|## Server Naming Convention
    51|
    52|Node/TypeScript MCP servers must follow this naming pattern:
    53|
    54|- **Format**: `{service}-mcp-server` (lowercase with hyphens)
    55|- **Examples**: `github-mcp-server`, `jira-mcp-server`, `stripe-mcp-server`
    56|
    57|The name should be:
    58|
    59|- General (not tied to specific features)
    60|- Descriptive of the service/API being integrated
    61|- Easy to infer from the task description
    62|- Without version numbers or dates
    63|
    64|## Project Structure
    65|
    66|Create the following structure for Node/TypeScript MCP servers:
    67|
    68|```
    69|{service}-mcp-server/
    70|├── package.json
    71|├── tsconfig.json
    72|├── README.md
    73|├── src/
    74|│   ├── index.ts          # Main entry point with McpServer initialization
    75|│   ├── types.ts          # TypeScript type definitions and interfaces
    76|│   ├── tools/            # Tool implementations (one file per domain)
    77|│   ├── services/         # API clients and shared utilities
    78|│   ├── schemas/          # Zod validation schemas
    79|│   └── constants.ts      # Shared constants (API_URL, CHARACTER_LIMIT, etc.)
    80|└── dist/                 # Built JavaScript files (entry point: dist/index.js)
    81|```
    82|
    83|## Tool Implementation
    84|
    85|### Tool Naming
    86|
    87|Use snake_case for tool names (e.g., "search_users", "create_project", "get_channel_info") with clear, action-oriented names.
    88|
    89|**Avoid Naming Conflicts**: Include the service context to prevent overlaps:
    90|
    91|- Use "slack_send_message" instead of just "send_message"
    92|- Use "github_create_issue" instead of just "create_issue"
    93|- Use "asana_list_tasks" instead of just "list_tasks"
    94|
    95|### Tool Structure
    96|
    97|Tools are registered using the `registerTool` method with the following requirements:
    98|
    99|- Use Zod schemas for runtime input validation and type safety
   100|- The `description` field must be explicitly provided - JSDoc comments are NOT automatically extracted
   101|- Explicitly provide `title`, `description`, `inputSchema`, and `annotations`
   102|- The `inputSchema` must be a Zod schema object (not a JSON schema)
   103|- Type all parameters and return values explicitly
   104|
   105|```typescript
   106|import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
   107|import { z } from "zod";
   108|
   109|const server = new McpServer({
   110|  name: "example-mcp",
   111|  version: "1.0.0"
   112|});
   113|
   114|// Zod schema for input validation
   115|const UserSearchInputSchema = z
   116|  .object({
   117|    query: z
   118|      .string()
   119|      .min(2, "Query must be at least 2 characters")
   120|      .max(200, "Query must not exceed 200 characters")
   121|      .describe("Search string to match against names/emails"),
   122|    limit: z
   123|      .number()
   124|      .int()
   125|      .min(1)
   126|      .max(100)
   127|      .default(20)
   128|      .describe("Maximum results to return"),
   129|    offset: z
   130|      .number()
   131|      .int()
   132|      .min(0)
   133|      .default(0)
   134|      .describe("Number of results to skip for pagination"),
   135|    response_format: z
   136|      .nativeEnum(ResponseFormat)
   137|      .default(ResponseFormat.MARKDOWN)
   138|      .describe(
   139|        "Output format: 'markdown' for human-readable or 'json' for machine-readable"
   140|      )
   141|  })
   142|  .strict();
   143|
   144|// Type definition from Zod schema
   145|type UserSearchInput = z.infer<typeof UserSearchInputSchema>;
   146|
   147|server.registerTool(
   148|  "example_search_users",
   149|  {
   150|    title: "Search Example Users",
   151|    description: `Search for users in the Example system by name, email, or team.
   152|
   153|This tool searches across all user profiles in the Example platform, supporting partial matches and various search filters. It does NOT create or modify users, only searches existing ones.
   154|
   155|Args:
   156|  - query (string): Search string to match against names/emails
   157|  - limit (number): Maximum results to return, between 1-100 (default: 20)
   158|  - offset (number): Number of results to skip for pagination (default: 0)
   159|  - response_format ('markdown' | 'json'): Output format (default: 'markdown')
   160|
   161|Returns:
   162|  For JSON format: Structured data with schema:
   163|  {
   164|    "total": number,           // Total number of matches found
   165|    "count": number,           // Number of results in this response
   166|    "offset": number,          // Current pagination offset
   167|    "users": [
   168|      {
   169|        "id": string,          // User ID (e.g., "U123456789")
   170|        "name": string,        // Full name (e.g., "John Doe")
   171|        "email": string,       // Email address
   172|        "team": string,        // Team name (optional)
   173|        "active": boolean      // Whether user is active
   174|      }
   175|    ],
   176|    "has_more": boolean,       // Whether more results are available
   177|    "next_offset": number      // Offset for next page (if has_more is true)
   178|  }
   179|
   180|Examples:
   181|  - Use when: "Find all marketing team members" -> params with query="team:marketing"
   182|  - Use when: "Search for John's account" -> params with query="john"
   183|  - Don't use when: You need to create a user (use example_create_user instead)
   184|
   185|Error Handling:
   186|  - Returns "Error: Rate limit exceeded" if too many requests (429 status)
   187|  - Returns "No users found matching '<query>'" if search returns empty`,
   188|    inputSchema: UserSearchInputSchema,
   189|    annotations: {
   190|      readOnlyHint: true,
   191|      destructiveHint: false,
   192|      idempotentHint: true,
   193|      openWorldHint: true
   194|    }
   195|  },
   196|  async (params: UserSearchInput) => {
   197|    try {
   198|      // Input validation is handled by Zod schema
   199|      // Make API request using validated parameters
   200|      const data = await makeApiRequest<any>(
   201|        "users/search",
   202|        "GET",
   203|        undefined,
   204|        {
   205|          q: params.query,
   206|          limit: params.limit,
   207|          offset: params.offset
   208|        }
   209|      );
   210|
   211|      const users = data.users || [];
   212|      const total = data.total || 0;
   213|
   214|      if (!users.length) {
   215|        return {
   216|          content: [
   217|            {
   218|              type: "text",
   219|              text: `No users found matching '${params.query}'`
   220|            }
   221|          ]
   222|        };
   223|      }
   224|
   225|      // Format response based on requested format
   226|      let result: string;
   227|
   228|      if (params.response_format === ResponseFormat.MARKDOWN) {
   229|        // Human-readable markdown format
   230|        const lines: string[] = [
   231|          `# User Search Results: '${params.query}'`,
   232|          ""
   233|        ];
   234|        lines.push(`Found ${total} users (showing ${users.length})`);
   235|        lines.push("");
   236|
   237|        for (const user of users) {
   238|          lines.push(`## ${user.name} (${user.id})`);
   239|          lines.push(`- **Email**: ${user.email}`);
   240|          if (user.team) {
   241|            lines.push(`- **Team**: ${user.team}`);
   242|          }
   243|          lines.push("");
   244|        }
   245|
   246|        result = lines.join("\n");
   247|      } else {
   248|        // Machine-readable JSON format
   249|        const response: any = {
   250|          total,
   251|          count: users.length,
   252|          offset: params.offset,
   253|          users: users.map((user: any) => ({
   254|            id: user.id,
   255|            name: user.name,
   256|            email: user.email,
   257|            ...(user.team ? { team: user.team } : {}),
   258|            active: user.active ?? true
   259|          }))
   260|        };
   261|
   262|        // Add pagination info if there are more results
   263|        if (total > params.offset + users.length) {
   264|          response.has_more = true;
   265|          response.next_offset = params.offset + users.length;
   266|        }
   267|
   268|        result = JSON.stringify(response, null, 2);
   269|      }
   270|
   271|      return {
   272|        content: [
   273|          {
   274|            type: "text",
   275|            text: result
   276|          }
   277|        ]
   278|      };
   279|    } catch (error) {
   280|      return {
   281|        content: [
   282|          {
   283|            type: "text",
   284|            text: handleApiError(error)
   285|          }
   286|        ]
   287|      };
   288|    }
   289|  }
   290|);
   291|```
   292|
   293|## Zod Schemas for Input Validation
   294|
   295|Zod provides runtime type validation:
   296|
   297|```typescript
   298|import { z } from "zod";
   299|
   300|// Basic schema with validation
   301|const CreateUserSchema = z
   302|  .object({
   303|    name: z
   304|      .string()
   305|      .min(1, "Name is required")
   306|      .max(100, "Name must not exceed 100 characters"),
   307|    email: z.string().email("Invalid email format"),
   308|    age: z
   309|      .number()
   310|      .int("Age must be a whole number")
   311|      .min(0, "Age cannot be negative")
   312|      .max(150, "Age cannot be greater than 150")
   313|  })
   314|  .strict(); // Use .strict() to forbid extra fields
   315|
   316|// Enums
   317|enum ResponseFormat {
   318|  MARKDOWN = "markdown",
   319|  JSON = "json"
   320|}
   321|
   322|const SearchSchema = z.object({
   323|  response_format: z
   324|    .nativeEnum(ResponseFormat)
   325|    .default(ResponseFormat.MARKDOWN)
   326|    .describe("Output format")
   327|});
   328|
   329|// Optional fields with defaults
   330|const PaginationSchema = z.object({
   331|  limit: z
   332|    .number()
   333|    .int()
   334|    .min(1)
   335|    .max(100)
   336|    .default(20)
   337|    .describe("Maximum results to return"),
   338|  offset: z
   339|    .number()
   340|    .int()
   341|    .min(0)
   342|    .default(0)
   343|    .describe("Number of results to skip")
   344|});
   345|```
   346|
   347|## Response Format Options
   348|
   349|Support multiple output formats for flexibility:
   350|
   351|```typescript
   352|enum ResponseFormat {
   353|  MARKDOWN = "markdown",
   354|  JSON = "json"
   355|}
   356|
   357|const inputSchema = z.object({
   358|  query: z.string(),
   359|  response_format: z
   360|    .nativeEnum(ResponseFormat)
   361|    .default(ResponseFormat.MARKDOWN)
   362|    .describe(
   363|      "Output format: 'markdown' for human-readable or 'json' for machine-readable"
   364|    )
   365|});
   366|```
   367|
   368|**Markdown format**:
   369|
   370|- Use headers, lists, and formatting for clarity
   371|- Convert timestamps to human-readable format
   372|- Show display names with IDs in parentheses
   373|- Omit verbose metadata
   374|- Group related information logically
   375|
   376|**JSON format**:
   377|
   378|- Return complete, structured data suitable for programmatic processing
   379|- Include all available fields and metadata
   380|- Use consistent field names and types
   381|
   382|## Pagination Implementation
   383|
   384|For tools that list resources:
   385|
   386|```typescript
   387|const ListSchema = z.object({
   388|  limit: z.number().int().min(1).max(100).default(20),
   389|  offset: z.number().int().min(0).default(0)
   390|});
   391|
   392|async function listItems(params: z.infer<typeof ListSchema>) {
   393|  const data = await apiRequest(params.limit, params.offset);
   394|
   395|  const response = {
   396|    total: data.total,
   397|    count: data.items.length,
   398|    offset: params.offset,
   399|    items: data.items,
   400|    has_more: data.total > params.offset + data.items.length,
   401|    next_offset:
   402|      data.total > params.offset + data.items.length
   403|        ? params.offset + data.items.length
   404|        : undefined
   405|  };
   406|
   407|  return JSON.stringify(response, null, 2);
   408|}
   409|```
   410|
   411|## Character Limits and Truncation
   412|
   413|Add a CHARACTER_LIMIT constant to prevent overwhelming responses:
   414|
   415|```typescript
   416|// At module level in constants.ts
   417|export const CHARACTER_LIMIT = 25000; // Maximum response size in characters
   418|
   419|async function searchTool(params: SearchInput) {
   420|  let result = generateResponse(data);
   421|
   422|  // Check character limit and truncate if needed
   423|  if (result.length > CHARACTER_LIMIT) {
   424|    const truncatedData = data.slice(0, Math.max(1, data.length / 2));
   425|    response.data = truncatedData;
   426|    response.truncated = true;
   427|    response.truncation_message =
   428|      `Response truncated from ${data.length} to ${truncatedData.length} items. ` +
   429|      `Use 'offset' parameter or add filters to see more results.`;
   430|    result = JSON.stringify(response, null, 2);
   431|  }
   432|
   433|  return result;
   434|}
   435|```
   436|
   437|## Error Handling
   438|
   439|Provide clear, actionable error messages:
   440|
   441|```typescript
   442|import axios, { AxiosError } from "axios";
   443|
   444|function handleApiError(error: unknown): string {
   445|  if (error instanceof AxiosError) {
   446|    if (error.response) {
   447|      switch (error.response.status) {
   448|        case 404:
   449|          return "Error: Resource not found. Please check the ID is correct.";
   450|        case 403:
   451|          return "Error: Permission denied. You don't have access to this resource.";
   452|        case 429:
   453|          return "Error: Rate limit exceeded. Please wait before making more requests.";
   454|        default:
   455|          return `Error: API request failed with status ${error.response.status}`;
   456|      }
   457|    } else if (error.code === "ECONNABORTED") {
   458|      return "Error: Request timed out. Please try again.";
   459|    }
   460|  }
   461|  return `Error: Unexpected error occurred: ${error instanceof Error ? error.message : String(error)}`;
   462|}
   463|```
   464|
   465|## Shared Utilities
   466|
   467|Extract common functionality into reusable functions:
   468|
   469|```typescript
   470|// Shared API request function
   471|async function makeApiRequest<T>(
   472|  endpoint: string,
   473|  method: "GET" | "POST" | "PUT" | "DELETE" = "GET",
   474|  data?: any,
   475|  params?: any
   476|): Promise<T> {
   477|  try {
   478|    const response = await axios({
   479|      method,
   480|      url: `${API_BASE_URL}/${endpoint}`,
   481|      data,
   482|      params,
   483|      timeout: 30000,
   484|      headers: {
   485|        "Content-Type": "application/json",
   486|        Accept: "application/json"
   487|      }
   488|    });
   489|    return response.data;
   490|  } catch (error) {
   491|    throw error;
   492|  }
   493|}
   494|```
   495|
   496|## Async/Await Best Practices
   497|
   498|Always use async/await for network requests and I/O operations:
   499|
   500|```typescript
   501|