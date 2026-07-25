---
name: jira-mcp
description: "MCP Reference"
version: 1.0.0
author: Alexa
---
     1|# MCP Reference
     2|
     3|Complete reference for Atlassian Jira operations via MCP.
     4|
     5|## MCP Tool Reference
     6|
     7|### Search Operations
     8|
     9|#### `mcp__atlassian__searchJiraIssuesUsingJql`
    10|
    11|Search Jira using JQL (Jira Query Language).
    12|
    13|**Parameters:**
    14|
    15|- `jql` (required): JQL query string
    16|- `maxResults`: Maximum results (default: 50)
    17|- `startAt`: Pagination offset
    18|- `fields`: Comma-separated fields to return
    19|
    20|**Example:**
    21|
    22|```
    23|mcp__atlassian__searchJiraIssuesUsingJql(jql: "project = PROJ AND status = 'In Progress'")
    24|```
    25|
    26|### Issue Operations
    27|
    28|#### `mcp__atlassian__getJiraIssue`
    29|
    30|Retrieve full issue details by key.
    31|
    32|**Parameters:**
    33|
    34|- `issueKey` (required): Issue key (e.g., "PROJ-123")
    35|- `expand`: Additional data (changelog, transitions, renderedFields)
    36|
    37|**Example:**
    38|
    39|```
    40|mcp__atlassian__getJiraIssue(issueKey: "PROJ-123")
    41|```
    42|
    43|#### `mcp__atlassian__createJiraIssue`
    44|
    45|Create a new issue.
    46|
    47|**Parameters:**
    48|
    49|- `projectKey` (required): Target project
    50|- `issueType` (required): Issue type (Story, Bug, Task, Epic, etc.)
    51|- `summary` (required): Issue title
    52|- `description`: Detailed description
    53|- `assignee`: Account ID (use lookupJiraAccountId first)
    54|- `priority`: Priority name (Highest, High, Medium, Low, Lowest)
    55|- `labels`: Array of labels
    56|- `components`: Array of component names
    57|- Custom fields as needed
    58|
    59|**Example:**
    60|
    61|```
    62|mcp__atlassian__createJiraIssue(
    63|  projectKey: "PROJ",
    64|  issueType: "Story",
    65|  summary: "Implement user authentication",
    66|  description: "Add OAuth2 authentication flow...",
    67|  labels: ["backend", "security"]
    68|)
    69|```
    70|
    71|#### `mcp__atlassian__editJiraIssue`
    72|
    73|Update an existing issue.
    74|
    75|**Parameters:**
    76|
    77|- `issueKey` (required): Issue to update
    78|- Any field to update (summary, description, assignee, etc.)
    79|
    80|**Example:**
    81|
    82|```
    83|mcp__atlassian__editJiraIssue(
    84|  issueKey: "PROJ-123",
    85|  description: "Updated description with more details..."
    86|)
    87|```
    88|
    89|### Transition Operations
    90|
    91|#### `mcp__atlassian__getTransitionsForJiraIssue`
    92|
    93|Get available status transitions for an issue.
    94|
    95|**Parameters:**
    96|
    97|- `issueKey` (required): Issue key
    98|
    99|**Returns:** List of available transitions with IDs and names.
   100|
   101|#### `mcp__atlassian__transitionJiraIssue`
   102|
   103|Change issue status.
   104|
   105|**Parameters:**
   106|
   107|- `issueKey` (required): Issue key
   108|- `transitionId` (required): Transition ID from getTransitions
   109|- `comment`: Optional comment for the transition
   110|
   111|**Workflow:**
   112|
   113|1. Get transitions: `getTransitionsForJiraIssue("PROJ-123")`
   114|2. Find desired transition ID from results
   115|3. Execute: `transitionJiraIssue(issueKey: "PROJ-123", transitionId: "31")`
   116|
   117|### Comment Operations
   118|
   119|#### `mcp__atlassian__addCommentToJiraIssue`
   120|
   121|Add a comment to an issue.
   122|
   123|**Parameters:**
   124|
   125|- `issueKey` (required): Issue key
   126|- `body` (required): Comment text (supports Jira markdown)
   127|
   128|### User Operations
   129|
   130|#### `mcp__atlassian__lookupJiraAccountId`
   131|
   132|Find user account ID for assignments.
   133|
   134|**Parameters:**
   135|
   136|- `query` (required): Search by display name, email, or username
   137|
   138|**Example:**
   139|
   140|```
   141|mcp__atlassian__lookupJiraAccountId(query: "user@example.com")
   142|```
   143|
   144|**Usage:** Always look up account IDs before assigning issues.
   145|
   146|### Project Operations
   147|
   148|#### `mcp__atlassian__getVisibleJiraProjects`
   149|
   150|List available Jira projects.
   151|
   152|**Parameters:**
   153|
   154|- `maxResults`: Maximum results
   155|
   156|#### `mcp__atlassian__getJiraProjectIssueTypesMetadata`
   157|
   158|Get issue types and required fields for a project.
   159|
   160|**Parameters:**
   161|
   162|- `projectKey` (required): Project key
   163|
   164|**Usage:** Call before creating issues to understand required fields.
   165|
   166|#### `mcp__atlassian__getJiraIssueTypeMetaWithFields`
   167|
   168|Get detailed field metadata for an issue type.
   169|
   170|**Parameters:**
   171|
   172|- `projectKey` (required): Project key
   173|- `issueTypeId` (required): Issue type ID
   174|
   175|---
   176|
   177|## JQL (Jira Query Language) Reference
   178|
   179|### Basic Syntax
   180|
   181|```
   182|field operator value [AND|OR field operator value]
   183|```
   184|
   185|### Common Fields
   186|
   187|| Field         | Description        | Example                      |
   188|| ------------- | ------------------ | ---------------------------- |
   189|| `project`     | Project key        | `project = "PROJ"`           |
   190|| `issuetype`   | Issue type         | `issuetype = Bug`            |
   191|| `status`      | Issue status       | `status = "In Progress"`     |
   192|| `assignee`    | Assigned user      | `assignee = currentUser()`   |
   193|| `reporter`    | Issue creator      | `reporter = "jobarksdale"`   |
   194|| `priority`    | Priority level     | `priority = High`            |
   195|| `labels`      | Issue labels       | `labels = "backend"`         |
   196|| `component`   | Components         | `component = "API"`          |
   197|| `created`     | Creation date      | `created >= -30d`            |
   198|| `updated`     | Last update        | `updated >= -7d`             |
   199|| `resolved`    | Resolution date    | `resolved >= startOfMonth()` |
   200|| `sprint`      | Sprint name/ID     | `sprint in openSprints()`    |
   201|| `epic`        | Parent epic        | `"Epic Link" = PROJ-100`     |
   202|| `parent`      | Parent issue       | `parent = PROJ-50`           |
   203|| `text`        | Full-text search   | `text ~ "authentication"`    |
   204|| `summary`     | Title search       | `summary ~ "login"`          |
   205|| `description` | Description search | `description ~ "OAuth"`      |
   206|
   207|### Operators
   208|
   209|| Operator | Meaning | Example |
   210|| --- | --- | --- |
   211|| `=` | Exact match | `status = Done` |
   212|| `!=` | Not equal | `status != Closed` |
   213|| `~` | Contains (text) | `summary ~ "auth*"` |
   214|| `!~` | Does not contain | `summary !~ "test"` |
   215|| `>` `>=` `<` `<=` | Comparisons | `priority >= High` |
   216|| `IN` | Multiple values | `status IN (Open, "In Progress")` |
   217|| `NOT IN` | Exclude values | `status NOT IN (Done, Closed)` |
   218|| `IS` | Null check | `assignee IS EMPTY` |
   219|| `IS NOT` | Not null | `assignee IS NOT EMPTY` |
   220|| `WAS` | Historical value | `status WAS "In Progress"` |
   221|| `CHANGED` | Field changed | `status CHANGED` |
   222|
   223|### Functions
   224|
   225|| Function | Description | Example |
   226|| --- | --- | --- |
   227|| `currentUser()` | Logged-in user | `assignee = currentUser()` |
   228|| `now()` | Current timestamp | `created <= now()` |
   229|| `startOfDay()` | Midnight today | `updated >= startOfDay()` |
   230|| `startOfWeek()` | Start of week | `created >= startOfWeek()` |
   231|| `startOfMonth()` | Start of month | `created >= startOfMonth()` |
   232|| `endOfDay()` | End of today | `due <= endOfDay()` |
   233|| `openSprints()` | Active sprints | `sprint in openSprints()` |
   234|| `closedSprints()` | Completed sprints | `sprint in closedSprints()` |
   235|| `linkedIssues()` | Linked issues | `issue in linkedIssues("PROJ-123")` |
   236|
   237|### Relative Dates
   238|
   239|```jql
   240|# Days
   241|created >= -7d    # Last 7 days
   242|updated >= -30d   # Last 30 days
   243|
   244|# Weeks
   245|created >= -2w    # Last 2 weeks
   246|
   247|# Months
   248|created >= -1M    # Last month
   249|
   250|# Specific date
   251|created >= "2024-01-01"
   252|```
   253|
   254|### Ordering
   255|
   256|```jql
   257|# Order by priority, highest first
   258|project = PROJ ORDER BY priority DESC
   259|
   260|# Multiple sort fields
   261|project = PROJ ORDER BY status ASC, created DESC
   262|```
   263|
   264|### Complex Query Examples
   265|
   266|```jql
   267|# My open issues, high priority
   268|assignee = currentUser() AND status NOT IN (Done, Closed) AND priority >= High
   269|
   270|# Bugs created this week
   271|issuetype = Bug AND created >= startOfWeek() ORDER BY priority DESC
   272|
   273|# Epics in progress with stories
   274|issuetype = Epic AND status = "In Progress" AND issueFunction in hasLinks("is parent of")
   275|
   276|# Issues updated by me recently
   277|updatedBy = currentUser() AND updated >= -7d ORDER BY updated DESC
   278|
   279|# Blocked issues
   280|status = Blocked OR "Flagged" = "Impediment"
   281|
   282|# Issues linked to specific epic
   283|"Epic Link" = PROJ-100 AND status != Done
   284|
   285|# Sprint backlog items
   286|sprint in openSprints() AND status = "To Do" ORDER BY rank ASC
   287|
   288|# Unassigned high-priority bugs
   289|issuetype = Bug AND assignee IS EMPTY AND priority >= High
   290|
   291|# Issues I'm watching
   292|watcher = currentUser()
   293|
   294|# Recently resolved by team
   295|resolved >= -7d AND project = PROJ ORDER BY resolved DESC
   296|```
   297|
   298|---
   299|
   300|## Issue Linking
   301|
   302|### Limitation
   303|
   304|The Atlassian MCP does not currently support creating issue links. Use the bundled `jira-link-issues` script instead.
   305|
   306|### Link Types
   307|
   308|| Link Type | Inward | Outward | Use Case |
   309|| --- | --- | --- | --- |
   310|| Depends On | is dependency of | depends on | Task dependencies |
   311|| Blocks | is blocked by | blocks | Blocking relationships |
   312|| Relates To | relates to | relates to | General relationships |
   313|| Clones | is cloned by | clones | Cloned issues |
   314|| Duplicates | is duplicated by | duplicates | Duplicate issues |
   315|
   316|### Script Usage
   317|
   318|```bash
   319|# Link PROJ-123 depends on PROJ-456
   320|~/.claude/skills/jira/jira-link-issues PROJ-123 PROJ-456 "Depends On"
   321|
   322|# PROJ-100 blocks PROJ-200
   323|~/.claude/skills/jira/jira-link-issues PROJ-100 PROJ-200 "Blocks"
   324|
   325|# General relationship
   326|~/.claude/skills/jira/jira-link-issues PROJ-50 PROJ-75 "Relates To"
   327|```
   328|
   329|### Finding Link Types
   330|
   331|Query the Jira API to get available link types:
   332|
   333|```bash
   334|curl -s -u "$JIRA_USER:$JIRA_API_TOKEN" \
   335|  "$JIRA_BASE_URL/rest/api/3/issueLinkType" | jq '.issueLinkTypes[].name'
   336|```
   337|
   338|Required environment variables:
   339|
   340|- `JIRA_BASE_URL`: Your Atlassian instance (e.g., `https://yourcompany.atlassian.net`)
   341|- `JIRA_USER`: Your email address
   342|- `JIRA_API_TOKEN`: API token from Atlassian account settings
   343|
   344|---
   345|
   346|## Description Formatting
   347|
   348|### Jira Markup (Wiki Style)
   349|
   350|```
   351|h1. Heading 1
   352|h2. Heading 2
   353|h3. Heading 3
   354|
   355|*bold text*
   356|_italic text_
   357|-strikethrough-
   358|+underline+
   359|
   360|{code:java}
   361|public class Example {
   362|    // code here
   363|}
   364|{code}
   365|
   366|{quote}
   367|Quoted text here
   368|{quote}
   369|
   370|* Bullet list
   371|** Nested bullet
   372|# Numbered list
   373|## Nested number
   374|
   375|[Link text|https://example.com]
   376|[Issue link|PROJ-123]
   377|
   378|||Header 1||Header 2||
   379||Cell 1|Cell 2|
   380|
   381|{panel:title=Panel Title}
   382|Panel content here
   383|{panel}
   384|```
   385|
   386|### Atlassian Document Format (ADF)
   387|
   388|For createJiraIssue, descriptions may use ADF format:
   389|
   390|```json
   391|{
   392|  "content": [
   393|    {
   394|      "type": "paragraph",
   395|      "content": [{ "type": "text", "text": "Description text" }]
   396|    }
   397|  ],
   398|  "type": "doc",
   399|  "version": 1
   400|}
   401|```
   402|
   403|---
   404|
   405|## Error Handling
   406|
   407|### Common Errors
   408|
   409|| HTTP Code | Error | Cause | Resolution |
   410|| --- | --- | --- | --- |
   411|| 400 | Bad Request | Invalid field values | Check required fields for issue type |
   412|| 401 | Unauthorized | Invalid credentials | Run `/mcp` to reconnect |
   413|| 403 | Forbidden | Insufficient permissions | Check project permissions |
   414|| 404 | Not Found | Issue/project doesn't exist | Verify key is correct |
   415|| 422 | Unprocessable | Validation failed | Check field constraints |
   416|
   417|### Authentication Issues
   418|
   419|If MCP tools return authentication errors:
   420|
   421|1. Run `/mcp` to check connection status
   422|2. Reconnect the Atlassian MCP service if disconnected
   423|3. Verify API token permissions in Atlassian settings
   424|
   425|### Field Validation
   426|
   427|Before creating issues:
   428|
   429|1. Get project metadata: `getJiraProjectIssueTypesMetadata`
   430|2. Check required fields for the issue type
   431|3. Look up user account IDs for assignee fields
   432|4. Verify custom field IDs and valid values
   433|
   434|---
   435|
   436|## Common Workflows
   437|
   438|### Move Ticket to Done
   439|
   440|```
   441|1. Get available transitions:
   442|   mcp__atlassian__getTransitionsForJiraIssue(issueKey: "PROJ-123")
   443|   → Returns list with transition IDs
   444|
   445|2. Find "Done" transition ID from response
   446|
   447|3. Execute transition:
   448|   mcp__atlassian__transitionJiraIssue(
   449|     issueKey: "PROJ-123",
   450|     transitionId: "done_id"
   451|   )
   452|
   453|4. Add comment:
   454|   mcp__atlassian__addCommentToJiraIssue(
   455|     issueKey: "PROJ-123",
   456|     body: "Completed and deployed"
   457|   )
   458|```
   459|
   460|### Create and Assign Issue
   461|
   462|```
   463|1. Look up user account ID:
   464|   mcp__atlassian__lookupJiraAccountId(query: "john@example.com")
   465|   → Returns account ID
   466|
   467|2. Create issue with assignment:
   468|   mcp__atlassian__createJiraIssue(
   469|     projectKey: "PROJ",
   470|     issueType: "Task",
   471|     summary: "Implement feature X",
   472|     description: "Details here...",
   473|     assignee: "account_id_from_step_1"
   474|   )
   475|```
   476|
   477|### List My In-Progress Issues
   478|
   479|```
   480|mcp__atlassian__searchJiraIssuesUsingJql(
   481|  jql: "assignee = currentUser() AND status = 'In Progress' ORDER BY updated DESC"
   482|)
   483|```
   484|
   485|### Get Project Info Before Creating
   486|
   487|```
   488|1. List available projects:
   489|   mcp__atlassian__getVisibleJiraProjects()
   490|
   491|2. Get issue types for project:
   492|   mcp__atlassian__getJiraProjectIssueTypesMetadata(projectKey: "PROJ")
   493|
   494|3. Create issue with correct type:
   495|   mcp__atlassian__createJiraIssue(
   496|     projectKey: "PROJ",
   497|     issueType: "Story",
   498|     summary: "...",
   499|     description: "..."
   500|   )
   501|