---
name: mcp-builder-mcp_best_practices
description: "MCP Server Development Best Practices and Guidelines"
version: 1.0.0
author: Alexa
---
     1|# MCP Server Development Best Practices and Guidelines
     2|
     3|## Overview
     4|
     5|This document compiles essential best practices and guidelines for building Model Context Protocol (MCP) servers. It covers naming conventions, tool design, response formats, pagination, error handling, security, and compliance requirements.
     6|
     7|---
     8|
     9|## Quick Reference
    10|
    11|### Server Naming
    12|
    13|- **Python**: `{service}_mcp` (e.g., `slack_mcp`)
    14|- **Node/TypeScript**: `{service}-mcp-server` (e.g., `slack-mcp-server`)
    15|
    16|### Tool Naming
    17|
    18|- Use snake_case with service prefix
    19|- Format: `{service}_{action}_{resource}`
    20|- Example: `slack_send_message`, `github_create_issue`
    21|
    22|### Response Formats
    23|
    24|- Support both JSON and Markdown formats
    25|- JSON for programmatic processing
    26|- Markdown for human readability
    27|
    28|### Pagination
    29|
    30|- Always respect `limit` parameter
    31|- Return `has_more`, `next_offset`, `total_count`
    32|- Default to 20-50 items
    33|
    34|### Character Limits
    35|
    36|- Set CHARACTER_LIMIT constant (typically 25,000)
    37|- Truncate gracefully with clear messages
    38|- Provide guidance on filtering
    39|
    40|---
    41|
    42|## Table of Contents
    43|
    44|1. Server Naming Conventions
    45|2. Tool Naming and Design
    46|3. Response Format Guidelines
    47|4. Pagination Best Practices
    48|5. Character Limits and Truncation
    49|6. Tool Development Best Practices
    50|7. Transport Best Practices
    51|8. Testing Requirements
    52|9. OAuth and Security Best Practices
    53|10. Resource Management Best Practices
    54|11. Prompt Management Best Practices
    55|12. Error Handling Standards
    56|13. Documentation Requirements
    57|14. Compliance and Monitoring
    58|
    59|---
    60|
    61|## 1. Server Naming Conventions
    62|
    63|Follow these standardized naming patterns for MCP servers:
    64|
    65|**Python**: Use format `{service}_mcp` (lowercase with underscores)
    66|
    67|- Examples: `slack_mcp`, `github_mcp`, `jira_mcp`, `stripe_mcp`
    68|
    69|**Node/TypeScript**: Use format `{service}-mcp-server` (lowercase with hyphens)
    70|
    71|- Examples: `slack-mcp-server`, `github-mcp-server`, `jira-mcp-server`
    72|
    73|The name should be:
    74|
    75|- General (not tied to specific features)
    76|- Descriptive of the service/API being integrated
    77|- Easy to infer from the task description
    78|- Without version numbers or dates
    79|
    80|---
    81|
    82|## 2. Tool Naming and Design
    83|
    84|### Tool Naming Best Practices
    85|
    86|1. **Use snake_case**: `search_users`, `create_project`, `get_channel_info`
    87|2. **Include service prefix**: Anticipate that your MCP server may be used alongside other MCP servers
    88|   - Use `slack_send_message` instead of just `send_message`
    89|   - Use `github_create_issue` instead of just `create_issue`
    90|   - Use `asana_list_tasks` instead of just `list_tasks`
    91|3. **Be action-oriented**: Start with verbs (get, list, search, create, etc.)
    92|4. **Be specific**: Avoid generic names that could conflict with other servers
    93|5. **Maintain consistency**: Use consistent naming patterns within your server
    94|
    95|### Tool Design Guidelines
    96|
    97|- Tool descriptions must narrowly and unambiguously describe functionality
    98|- Descriptions must precisely match actual functionality
    99|- Should not create confusion with other MCP servers
   100|- Should provide tool annotations (readOnlyHint, destructiveHint, idempotentHint, openWorldHint)
   101|- Keep tool operations focused and atomic
   102|
   103|---
   104|
   105|## 3. Response Format Guidelines
   106|
   107|All tools that return data should support multiple formats for flexibility:
   108|
   109|### JSON Format (`response_format="json"`)
   110|
   111|- Machine-readable structured data
   112|- Include all available fields and metadata
   113|- Consistent field names and types
   114|- Suitable for programmatic processing
   115|- Use for when LLMs need to process data further
   116|
   117|### Markdown Format (`response_format="markdown"`, typically default)
   118|
   119|- Human-readable formatted text
   120|- Use headers, lists, and formatting for clarity
   121|- Convert timestamps to human-readable format (e.g., "2024-01-15 10:30:00 UTC" instead of epoch)
   122|- Show display names with IDs in parentheses (e.g., "@john.doe (U123456)")
   123|- Omit verbose metadata (e.g., show only one profile image URL, not all sizes)
   124|- Group related information logically
   125|- Use for when presenting information to users
   126|
   127|---
   128|
   129|## 4. Pagination Best Practices
   130|
   131|For tools that list resources:
   132|
   133|- **Always respect the `limit` parameter**: Never load all results when a limit is specified
   134|- **Implement pagination**: Use `offset` or cursor-based pagination
   135|- **Return pagination metadata**: Include `has_more`, `next_offset`/`next_cursor`, `total_count`
   136|- **Never load all results into memory**: Especially important for large datasets
   137|- **Default to reasonable limits**: 20-50 items is typical
   138|- **Include clear pagination info in responses**: Make it easy for LLMs to request more data
   139|
   140|Example pagination response structure:
   141|
   142|```json
   143|{
   144|  "total": 150,
   145|  "count": 20,
   146|  "offset": 0,
   147|  "items": [...],
   148|  "has_more": true,
   149|  "next_offset": 20
   150|}
   151|```
   152|
   153|---
   154|
   155|## 5. Character Limits and Truncation
   156|
   157|To prevent overwhelming responses with too much data:
   158|
   159|- **Define CHARACTER_LIMIT constant**: Typically 25,000 characters at module level
   160|- **Check response size before returning**: Measure the final response length
   161|- **Truncate gracefully with clear indicators**: Let the LLM know data was truncated
   162|- **Provide guidance on filtering**: Suggest how to use parameters to reduce results
   163|- **Include truncation metadata**: Show what was truncated and how to get more
   164|
   165|Example truncation handling:
   166|
   167|```python
   168|CHARACTER_LIMIT = 25000
   169|
   170|if len(result) > CHARACTER_LIMIT:
   171|    truncated_data = data[:max(1, len(data) // 2)]
   172|    response["truncated"] = True
   173|    response["truncation_message"] = (
   174|        f"Response truncated from {len(data)} to {len(truncated_data)} items. "
   175|        f"Use 'offset' parameter or add filters to see more results."
   176|    )
   177|```
   178|
   179|---
   180|
   181|## 6. Transport Options
   182|
   183|MCP servers support multiple transport mechanisms for different deployment scenarios:
   184|
   185|### Stdio Transport
   186|
   187|**Best for**: Command-line tools, local integrations, subprocess execution
   188|
   189|**Characteristics**:
   190|
   191|- Standard input/output stream communication
   192|- Simple setup, no network configuration needed
   193|- Runs as a subprocess of the client
   194|- Ideal for desktop applications and CLI tools
   195|
   196|**Use when**:
   197|
   198|- Building tools for local development environments
   199|- Integrating with desktop applications (e.g., Claude Desktop)
   200|- Creating command-line utilities
   201|- Single-user, single-session scenarios
   202|
   203|### HTTP Transport
   204|
   205|**Best for**: Web services, remote access, multi-client scenarios
   206|
   207|**Characteristics**:
   208|
   209|- Request-response pattern over HTTP
   210|- Supports multiple simultaneous clients
   211|- Can be deployed as a web service
   212|- Requires network configuration and security considerations
   213|
   214|**Use when**:
   215|
   216|- Serving multiple clients simultaneously
   217|- Deploying as a cloud service
   218|- Integration with web applications
   219|- Need for load balancing or scaling
   220|
   221|### Server-Sent Events (SSE) Transport
   222|
   223|**Best for**: Real-time updates, push notifications, streaming data
   224|
   225|**Characteristics**:
   226|
   227|- One-way server-to-client streaming over HTTP
   228|- Enables real-time updates without polling
   229|- Long-lived connections for continuous data flow
   230|- Built on standard HTTP infrastructure
   231|
   232|**Use when**:
   233|
   234|- Clients need real-time data updates
   235|- Implementing push notifications
   236|- Streaming logs or monitoring data
   237|- Progressive result delivery for long operations
   238|
   239|### Transport Selection Criteria
   240|
   241|| Criterion         | Stdio         | HTTP             | SSE         |
   242|| ----------------- | ------------- | ---------------- | ----------- |
   243|| **Deployment**    | Local         | Remote           | Remote      |
   244|| **Clients**       | Single        | Multiple         | Multiple    |
   245|| **Communication** | Bidirectional | Request-Response | Server-Push |
   246|| **Complexity**    | Low           | Medium           | Medium-High |
   247|| **Real-time**     | No            | No               | Yes         |
   248|
   249|---
   250|
   251|## 7. Tool Development Best Practices
   252|
   253|### General Guidelines
   254|
   255|1. Tool names should be descriptive and action-oriented
   256|2. Use parameter validation with detailed JSON schemas
   257|3. Include examples in tool descriptions
   258|4. Implement proper error handling and validation
   259|5. Use progress reporting for long operations
   260|6. Keep tool operations focused and atomic
   261|7. Document expected return value structures
   262|8. Implement proper timeouts
   263|9. Consider rate limiting for resource-intensive operations
   264|10. Log tool usage for debugging and monitoring
   265|
   266|### Security Considerations for Tools
   267|
   268|#### Input Validation
   269|
   270|- Validate all parameters against schema
   271|- Sanitize file paths and system commands
   272|- Validate URLs and external identifiers
   273|- Check parameter sizes and ranges
   274|- Prevent command injection
   275|
   276|#### Access Control
   277|
   278|- Implement authentication where needed
   279|- Use appropriate authorization checks
   280|- Audit tool usage
   281|- Rate limit requests
   282|- Monitor for abuse
   283|
   284|#### Error Handling
   285|
   286|- Don't expose internal errors to clients
   287|- Log security-relevant errors
   288|- Handle timeouts appropriately
   289|- Clean up resources after errors
   290|- Validate return values
   291|
   292|### Tool Annotations
   293|
   294|- Provide readOnlyHint and destructiveHint annotations
   295|- Remember annotations are hints, not security guarantees
   296|- Clients should not make security-critical decisions based solely on annotations
   297|
   298|---
   299|
   300|## 8. Transport Best Practices
   301|
   302|### General Transport Guidelines
   303|
   304|1. Handle connection lifecycle properly
   305|2. Implement proper error handling
   306|3. Use appropriate timeout values
   307|4. Implement connection state management
   308|5. Clean up resources on disconnection
   309|
   310|### Security Best Practices for Transport
   311|
   312|- Follow security considerations for DNS rebinding attacks
   313|- Implement proper authentication mechanisms
   314|- Validate message formats
   315|- Handle malformed messages gracefully
   316|
   317|### Stdio Transport Specific
   318|
   319|- Local MCP servers should NOT log to stdout (interferes with protocol)
   320|- Use stderr for logging messages
   321|- Handle standard I/O streams properly
   322|
   323|---
   324|
   325|## 9. Testing Requirements
   326|
   327|A comprehensive testing strategy should cover:
   328|
   329|### Functional Testing
   330|
   331|- Verify correct execution with valid/invalid inputs
   332|
   333|### Integration Testing
   334|
   335|- Test interaction with external systems
   336|
   337|### Security Testing
   338|
   339|- Validate auth, input sanitization, rate limiting
   340|
   341|### Performance Testing
   342|
   343|- Check behavior under load, timeouts
   344|
   345|### Error Handling
   346|
   347|- Ensure proper error reporting and cleanup
   348|
   349|---
   350|
   351|## 10. OAuth and Security Best Practices
   352|
   353|### Authentication and Authorization
   354|
   355|MCP servers that connect to external services should implement proper authentication:
   356|
   357|**OAuth 2.1 Implementation:**
   358|
   359|- Use secure OAuth 2.1 with certificates from recognized authorities
   360|- Validate access tokens before processing requests
   361|- Only accept tokens specifically intended for your server
   362|- Reject tokens without proper audience claims
   363|- Never pass through tokens received from MCP clients
   364|
   365|**API Key Management:**
   366|
   367|- Store API keys in environment variables, never in code
   368|- Validate keys on server startup
   369|- Provide clear error messages when authentication fails
   370|- Use secure transmission for sensitive credentials
   371|
   372|### Input Validation and Security
   373|
   374|**Always validate inputs:**
   375|
   376|- Sanitize file paths to prevent directory traversal
   377|- Validate URLs and external identifiers
   378|- Check parameter sizes and ranges
   379|- Prevent command injection in system calls
   380|- Use schema validation (Pydantic/Zod) for all inputs
   381|
   382|**Error handling security:**
   383|
   384|- Don't expose internal errors to clients
   385|- Log security-relevant errors server-side
   386|- Provide helpful but not revealing error messages
   387|- Clean up resources after errors
   388|
   389|### Privacy and Data Protection
   390|
   391|**Data collection principles:**
   392|
   393|- Only collect data strictly necessary for functionality
   394|- Don't collect extraneous conversation data
   395|- Don't collect PII unless explicitly required for the tool's purpose
   396|- Provide clear information about what data is accessed
   397|
   398|**Data transmission:**
   399|
   400|- Don't send data to servers outside your organization without disclosure
   401|- Use secure transmission (HTTPS) for all network communication
   402|- Validate certificates for external services
   403|
   404|---
   405|
   406|## 11. Resource Management Best Practices
   407|
   408|1. Only suggest necessary resources
   409|2. Use clear, descriptive names for roots
   410|3. Handle resource boundaries properly
   411|4. Respect client control over resources
   412|5. Use model-controlled primitives (tools) for automatic data exposure
   413|
   414|---
   415|
   416|## 12. Prompt Management Best Practices
   417|
   418|- Clients should show users proposed prompts
   419|- Users should be able to modify or reject prompts
   420|- Clients should show users completions
   421|- Users should be able to modify or reject completions
   422|- Consider costs when using sampling
   423|
   424|---
   425|
   426|## 13. Error Handling Standards
   427|
   428|- Use standard JSON-RPC error codes
   429|- Report tool errors within result objects (not protocol-level)
   430|- Provide helpful, specific error messages
   431|- Don't expose internal implementation details
   432|- Clean up resources properly on errors
   433|
   434|---
   435|
   436|## 14. Documentation Requirements
   437|
   438|- Provide clear documentation of all tools and capabilities
   439|- Include working examples (at least 3 per major feature)
   440|- Document security considerations
   441|- Specify required permissions and access levels
   442|- Document rate limits and performance characteristics
   443|
   444|---
   445|
   446|## 15. Compliance and Monitoring
   447|
   448|- Implement logging for debugging and monitoring
   449|- Track tool usage patterns
   450|- Monitor for potential abuse
   451|- Maintain audit trails for security-relevant operations
   452|- Be prepared for ongoing compliance reviews
   453|
   454|---
   455|
   456|## Summary
   457|
   458|These best practices represent the comprehensive guidelines for building secure, efficient, and compliant MCP servers that work well within the ecosystem. Developers should follow these guidelines to ensure their MCP servers meet the standards for inclusion in the MCP directory and provide a safe, reliable experience for users.
   459|
   460|---
   461|
   462|# Tools
   463|
   464|> Enable LLMs to perform actions through your server
   465|
   466|Tools are a powerful primitive in the Model Context Protocol (MCP) that enable servers to expose executable functionality to clients. Through tools, LLMs can interact with external systems, perform computations, and take actions in the real world.
   467|
   468|<Note>
   469|  Tools are designed to be **model-controlled**, meaning that tools are exposed from servers to clients with the intention of the AI model being able to automatically invoke them (with a human in the loop to grant approval).
   470|</Note>
   471|
   472|## Overview
   473|
   474|Tools in MCP allow servers to expose executable functions that can be invoked by clients and used by LLMs to perform actions. Key aspects of tools include:
   475|
   476|- **Discovery**: Clients can obtain a list of available tools by sending a `tools/list` request
   477|- **Invocation**: Tools are called using the `tools/call` request, where servers perform the requested operation and return results
   478|- **Flexibility**: Tools can range from simple calculations to complex API interactions
   479|
   480|Like [resources](/docs/concepts/resources), tools are identified by unique names and can include descriptions to guide their usage. However, unlike resources, tools represent dynamic operations that can modify state or interact with external systems.
   481|
   482|## Tool definition structure
   483|
   484|Each tool is defined with the following structure:
   485|
   486|```typescript
   487|{
   488|  name: string;          // Unique identifier for the tool
   489|  description?: string;  // Human-readable description
   490|  inputSchema: {         // JSON Schema for the tool's parameters
   491|    type: "object",
   492|    properties: { ... }  // Tool-specific parameters
   493|  },
   494|  annotations?: {        // Optional hints about tool behavior
   495|    title?: string;      // Human-readable title for the tool
   496|    readOnlyHint?: boolean;    // If true, the tool does not modify its environment
   497|    destructiveHint?: boolean; // If true, the tool may perform destructive updates
   498|    idempotentHint?: boolean;  // If true, repeated calls with same args have no additional effect
   499|    openWorldHint?: boolean;   // If true, tool interacts with external entities
   500|  }
   501|