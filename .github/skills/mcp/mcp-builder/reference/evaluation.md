---
name: mcp-builder-evaluation
description: "MCP Server Evaluation Guide"
version: 1.0.0
author: Alexa
---
     1|# MCP Server Evaluation Guide
     2|
     3|## Overview
     4|
     5|This document provides guidance on creating comprehensive evaluations for MCP servers. Evaluations test whether LLMs can effectively use your MCP server to answer realistic, complex questions using only the tools provided.
     6|
     7|---
     8|
     9|## Quick Reference
    10|
    11|### Evaluation Requirements
    12|
    13|- Create 10 human-readable questions
    14|- Questions must be READ-ONLY, INDEPENDENT, NON-DESTRUCTIVE
    15|- Each question requires multiple tool calls (potentially dozens)
    16|- Answers must be single, verifiable values
    17|- Answers must be STABLE (won't change over time)
    18|
    19|### Output Format
    20|
    21|```xml
    22|<evaluation>
    23|   <qa_pair>
    24|      <question>Your question here</question>
    25|      <answer>Single verifiable answer</answer>
    26|   </qa_pair>
    27|</evaluation>
    28|```
    29|
    30|---
    31|
    32|## Purpose of Evaluations
    33|
    34|The measure of quality of an MCP server is NOT how well or comprehensively the server implements tools, but how well these implementations (input/output schemas, docstrings/descriptions, functionality) enable LLMs with no other context and access ONLY to the MCP servers to answer realistic and difficult questions.
    35|
    36|## Evaluation Overview
    37|
    38|Create 10 human-readable questions requiring ONLY READ-ONLY, INDEPENDENT, NON-DESTRUCTIVE, and IDEMPOTENT operations to answer. Each question should be:
    39|
    40|- Realistic
    41|- Clear and concise
    42|- Unambiguous
    43|- Complex, requiring potentially dozens of tool calls or steps
    44|- Answerable with a single, verifiable value that you identify in advance
    45|
    46|## Question Guidelines
    47|
    48|### Core Requirements
    49|
    50|1. **Questions MUST be independent**
    51|   - Each question should NOT depend on the answer to any other question
    52|   - Should not assume prior write operations from processing another question
    53|
    54|2. **Questions MUST require ONLY NON-DESTRUCTIVE AND IDEMPOTENT tool use**
    55|   - Should not instruct or require modifying state to arrive at the correct answer
    56|
    57|3. **Questions must be REALISTIC, CLEAR, CONCISE, and COMPLEX**
    58|   - Must require another LLM to use multiple (potentially dozens of) tools or steps to answer
    59|
    60|### Complexity and Depth
    61|
    62|4. **Questions must require deep exploration**
    63|   - Consider multi-hop questions requiring multiple sub-questions and sequential tool calls
    64|   - Each step should benefit from information found in previous questions
    65|
    66|5. **Questions may require extensive paging**
    67|   - May need paging through multiple pages of results
    68|   - May require querying old data (1-2 years out-of-date) to find niche information
    69|   - The questions must be DIFFICULT
    70|
    71|6. **Questions must require deep understanding**
    72|   - Rather than surface-level knowledge
    73|   - May pose complex ideas as True/False questions requiring evidence
    74|   - May use multiple-choice format where LLM must search different hypotheses
    75|
    76|7. **Questions must not be solvable with straightforward keyword search**
    77|   - Do not include specific keywords from the target content
    78|   - Use synonyms, related concepts, or paraphrases
    79|   - Require multiple searches, analyzing multiple related items, extracting context, then deriving the answer
    80|
    81|### Tool Testing
    82|
    83|8. **Questions should stress-test tool return values**
    84|   - May elicit tools returning large JSON objects or lists, overwhelming the LLM
    85|   - Should require understanding multiple modalities of data:
    86|     - IDs and names
    87|     - Timestamps and datetimes (months, days, years, seconds)
    88|     - File IDs, names, extensions, and mimetypes
    89|     - URLs, GIDs, etc.
    90|   - Should probe the tool's ability to return all useful forms of data
    91|
    92|9. **Questions should MOSTLY reflect real human use cases**
    93|   - The kinds of information retrieval tasks that HUMANS assisted by an LLM would care about
    94|
    95|10. **Questions may require dozens of tool calls**
    96|    - This challenges LLMs with limited context
    97|    - Encourages MCP server tools to reduce information returned
    98|
    99|11. **Include ambiguous questions**
   100|    - May be ambiguous OR require difficult decisions on which tools to call
   101|    - Force the LLM to potentially make mistakes or misinterpret
   102|    - Ensure that despite AMBIGUITY, there is STILL A SINGLE VERIFIABLE ANSWER
   103|
   104|### Stability
   105|
   106|12. **Questions must be designed so the answer DOES NOT CHANGE**
   107|    - Do not ask questions that rely on "current state" which is dynamic
   108|    - For example, do not count:
   109|      - Number of reactions to a post
   110|      - Number of replies to a thread
   111|      - Number of members in a channel
   112|
   113|13. **DO NOT let the MCP server RESTRICT the kinds of questions you create**
   114|    - Create challenging and complex questions
   115|    - Some may not be solvable with the available MCP server tools
   116|    - Questions may require specific output formats (datetime vs. epoch time, JSON vs. MARKDOWN)
   117|    - Questions may require dozens of tool calls to complete
   118|
   119|## Answer Guidelines
   120|
   121|### Verification
   122|
   123|1. **Answers must be VERIFIABLE via direct string comparison**
   124|   - If the answer can be re-written in many formats, clearly specify the output format in the QUESTION
   125|   - Examples: "Use YYYY/MM/DD.", "Respond True or False.", "Answer A, B, C, or D and nothing else."
   126|   - Answer should be a single VERIFIABLE value such as:
   127|     - User ID, user name, display name, first name, last name
   128|     - Channel ID, channel name
   129|     - Message ID, string
   130|     - URL, title
   131|     - Numerical quantity
   132|     - Timestamp, datetime
   133|     - Boolean (for True/False questions)
   134|     - Email address, phone number
   135|     - File ID, file name, file extension
   136|     - Multiple choice answer
   137|   - Answers must not require special formatting or complex, structured output
   138|   - Answer will be verified using DIRECT STRING COMPARISON
   139|
   140|### Readability
   141|
   142|2. **Answers should generally prefer HUMAN-READABLE formats**
   143|   - Examples: names, first name, last name, datetime, file name, message string, URL, yes/no, true/false, a/b/c/d
   144|   - Rather than opaque IDs (though IDs are acceptable)
   145|   - The VAST MAJORITY of answers should be human-readable
   146|
   147|### Stability
   148|
   149|3. **Answers must be STABLE/STATIONARY**
   150|   - Look at old content (e.g., conversations that have ended, projects that have launched, questions answered)
   151|   - Create QUESTIONS based on "closed" concepts that will always return the same answer
   152|   - Questions may ask to consider a fixed time window to insulate from non-stationary answers
   153|   - Rely on context UNLIKELY to change
   154|   - Example: if finding a paper name, be SPECIFIC enough so answer is not confused with papers published later
   155|
   156|4. **Answers must be CLEAR and UNAMBIGUOUS**
   157|   - Questions must be designed so there is a single, clear answer
   158|   - Answer can be derived from using the MCP server tools
   159|
   160|### Diversity
   161|
   162|5. **Answers must be DIVERSE**
   163|   - Answer should be a single VERIFIABLE value in diverse modalities and formats
   164|   - User concept: user ID, user name, display name, first name, last name, email address, phone number
   165|   - Channel concept: channel ID, channel name, channel topic
   166|   - Message concept: message ID, message string, timestamp, month, day, year
   167|
   168|6. **Answers must NOT be complex structures**
   169|   - Not a list of values
   170|   - Not a complex object
   171|   - Not a list of IDs or strings
   172|   - Not natural language text
   173|   - UNLESS the answer can be straightforwardly verified using DIRECT STRING COMPARISON
   174|   - And can be realistically reproduced
   175|   - It should be unlikely that an LLM would return the same list in any other order or format
   176|
   177|## Evaluation Process
   178|
   179|### Step 1: Documentation Inspection
   180|
   181|Read the documentation of the target API to understand:
   182|
   183|- Available endpoints and functionality
   184|- If ambiguity exists, fetch additional information from the web
   185|- Parallelize this step AS MUCH AS POSSIBLE
   186|- Ensure each subagent is ONLY examining documentation from the file system or on the web
   187|
   188|### Step 2: Tool Inspection
   189|
   190|List the tools available in the MCP server:
   191|
   192|- Inspect the MCP server directly
   193|- Understand input/output schemas, docstrings, and descriptions
   194|- WITHOUT calling the tools themselves at this stage
   195|
   196|### Step 3: Developing Understanding
   197|
   198|Repeat steps 1 & 2 until you have a good understanding:
   199|
   200|- Iterate multiple times
   201|- Think about the kinds of tasks you want to create
   202|- Refine your understanding
   203|- At NO stage should you READ the code of the MCP server implementation itself
   204|- Use your intuition and understanding to create reasonable, realistic, but VERY challenging tasks
   205|
   206|### Step 4: Read-Only Content Inspection
   207|
   208|After understanding the API and tools, USE the MCP server tools:
   209|
   210|- Inspect content using READ-ONLY and NON-DESTRUCTIVE operations ONLY
   211|- Goal: identify specific content (e.g., users, channels, messages, projects, tasks) for creating realistic questions
   212|- Should NOT call any tools that modify state
   213|- Will NOT read the code of the MCP server implementation itself
   214|- Parallelize this step with individual sub-agents pursuing independent explorations
   215|- Ensure each subagent is only performing READ-ONLY, NON-DESTRUCTIVE, and IDEMPOTENT operations
   216|- BE CAREFUL: SOME TOOLS may return LOTS OF DATA which would cause you to run out of CONTEXT
   217|- Make INCREMENTAL, SMALL, AND TARGETED tool calls for exploration
   218|- In all tool call requests, use the `limit` parameter to limit results (<10)
   219|- Use pagination
   220|
   221|### Step 5: Task Generation
   222|
   223|After inspecting the content, create 10 human-readable questions:
   224|
   225|- An LLM should be able to answer these with the MCP server
   226|- Follow all question and answer guidelines above
   227|
   228|## Output Format
   229|
   230|Each QA pair consists of a question and an answer. The output should be an XML file with this structure:
   231|
   232|```xml
   233|<evaluation>
   234|   <qa_pair>
   235|      <question>Find the project created in Q2 2024 with the highest number of completed tasks. What is the project name?</question>
   236|      <answer>Website Redesign</answer>
   237|   </qa_pair>
   238|   <qa_pair>
   239|      <question>Search for issues labeled as "bug" that were closed in March 2024. Which user closed the most issues? Provide their username.</question>
   240|      <answer>sarah_dev</answer>
   241|   </qa_pair>
   242|   <qa_pair>
   243|      <question>Look for pull requests that modified files in the /api directory and were merged between January 1 and January 31, 2024. How many different contributors worked on these PRs?</question>
   244|      <answer>7</answer>
   245|   </qa_pair>
   246|   <qa_pair>
   247|      <question>Find the repository with the most stars that was created before 2023. What is the repository name?</question>
   248|      <answer>data-pipeline</answer>
   249|   </qa_pair>
   250|</evaluation>
   251|```
   252|
   253|## Evaluation Examples
   254|
   255|### Good Questions
   256|
   257|**Example 1: Multi-hop question requiring deep exploration (GitHub MCP)**
   258|
   259|```xml
   260|<qa_pair>
   261|   <question>Find the repository that was archived in Q3 2023 and had previously been the most forked project in the organization. What was the primary programming language used in that repository?</question>
   262|   <answer>Python</answer>
   263|</qa_pair>
   264|```
   265|
   266|This question is good because:
   267|
   268|- Requires multiple searches to find archived repositories
   269|- Needs to identify which had the most forks before archival
   270|- Requires examining repository details for the language
   271|- Answer is a simple, verifiable value
   272|- Based on historical (closed) data that won't change
   273|
   274|**Example 2: Requires understanding context without keyword matching (Project Management MCP)**
   275|
   276|```xml
   277|<qa_pair>
   278|   <question>Locate the initiative focused on improving customer onboarding that was completed in late 2023. The project lead created a retrospective document after completion. What was the lead's role title at that time?</question>
   279|   <answer>Product Manager</answer>
   280|</qa_pair>
   281|```
   282|
   283|This question is good because:
   284|
   285|- Doesn't use specific project name ("initiative focused on improving customer onboarding")
   286|- Requires finding completed projects from specific timeframe
   287|- Needs to identify the project lead and their role
   288|- Requires understanding context from retrospective documents
   289|- Answer is human-readable and stable
   290|- Based on completed work (won't change)
   291|
   292|**Example 3: Complex aggregation requiring multiple steps (Issue Tracker MCP)**
   293|
   294|```xml
   295|<qa_pair>
   296|   <question>Among all bugs reported in January 2024 that were marked as critical priority, which assignee resolved the highest percentage of their assigned bugs within 48 hours? Provide the assignee's username.</question>
   297|   <answer>alex_eng</answer>
   298|</qa_pair>
   299|```
   300|
   301|This question is good because:
   302|
   303|- Requires filtering bugs by date, priority, and status
   304|- Needs to group by assignee and calculate resolution rates
   305|- Requires understanding timestamps to determine 48-hour windows
   306|- Tests pagination (potentially many bugs to process)
   307|- Answer is a single username
   308|- Based on historical data from specific time period
   309|
   310|**Example 4: Requires synthesis across multiple data types (CRM MCP)**
   311|
   312|```xml
   313|<qa_pair>
   314|   <question>Find the account that upgraded from the Starter to Enterprise plan in Q4 2023 and had the highest annual contract value. What industry does this account operate in?</question>
   315|   <answer>Healthcare</answer>
   316|</qa_pair>
   317|```
   318|
   319|This question is good because:
   320|
   321|- Requires understanding subscription tier changes
   322|- Needs to identify upgrade events in specific timeframe
   323|- Requires comparing contract values
   324|- Must access account industry information
   325|- Answer is simple and verifiable
   326|- Based on completed historical transactions
   327|
   328|### Poor Questions
   329|
   330|**Example 1: Answer changes over time**
   331|
   332|```xml
   333|<qa_pair>
   334|   <question>How many open issues are currently assigned to the engineering team?</question>
   335|   <answer>47</answer>
   336|</qa_pair>
   337|```
   338|
   339|This question is poor because:
   340|
   341|- The answer will change as issues are created, closed, or reassigned
   342|- Not based on stable/stationary data
   343|- Relies on "current state" which is dynamic
   344|
   345|**Example 2: Too easy with keyword search**
   346|
   347|```xml
   348|<qa_pair>
   349|   <question>Find the pull request with title "Add authentication feature" and tell me who created it.</question>
   350|   <answer>developer123</answer>
   351|</qa_pair>
   352|```
   353|
   354|This question is poor because:
   355|
   356|- Can be solved with a straightforward keyword search for exact title
   357|- Doesn't require deep exploration or understanding
   358|- No synthesis or analysis needed
   359|
   360|**Example 3: Ambiguous answer format**
   361|
   362|```xml
   363|<qa_pair>
   364|   <question>List all the repositories that have Python as their primary language.</question>
   365|   <answer>repo1, repo2, repo3, data-pipeline, ml-tools</answer>
   366|</qa_pair>
   367|```
   368|
   369|This question is poor because:
   370|
   371|- Answer is a list that could be returned in any order
   372|- Difficult to verify with direct string comparison
   373|- LLM might format differently (JSON array, comma-separated, newline-separated)
   374|- Better to ask for a specific aggregate (count) or superlative (most stars)
   375|
   376|## Verification Process
   377|
   378|After creating evaluations:
   379|
   380|1. **Examine the XML file** to understand the schema
   381|2. **Load each task instruction** and in parallel using the MCP server and tools, identify the correct answer by attempting to solve the task YOURSELF
   382|3. **Flag any operations** that require WRITE or DESTRUCTIVE operations
   383|4. **Accumulate all CORRECT answers** and replace any incorrect answers in the document
   384|5. **Remove any `<qa_pair>`** that require WRITE or DESTRUCTIVE operations
   385|
   386|Remember to parallelize solving tasks to avoid running out of context, then accumulate all answers and make changes to the file at the end.
   387|
   388|## Tips for Creating Quality Evaluations
   389|
   390|1. **Think Hard and Plan Ahead** before generating tasks
   391|2. **Parallelize Where Opportunity Arises** to speed up the process and manage context
   392|3. **Focus on Realistic Use Cases** that humans would actually want to accomplish
   393|4. **Create Challenging Questions** that test the limits of the MCP server's capabilities
   394|5. **Ensure Stability** by using historical data and closed concepts
   395|6. **Verify Answers** by solving the questions yourself using the MCP server tools
   396|7. **Iterate and Refine** based on what you learn during the process
   397|
   398|---
   399|
   400|# Running Evaluations
   401|
   402|After creating your evaluation file, you can use the provided evaluation harness to test your MCP server.
   403|
   404|## Setup
   405|
   406|1. **Install Dependencies**
   407|
   408|   ```bash
   409|   pip install -r scripts/requirements.txt
   410|   ```
   411|
   412|   Or install manually:
   413|
   414|   ```bash
   415|   pip install anthropic mcp
   416|   ```
   417|
   418|2. **Set API Key**
   419|
   420|   ```bash
   421|   export ANTHROPIC_API_KEY=your_api_key_here
   422|   ```
   423|
   424|## Evaluation File Format
   425|
   426|Evaluation files use XML format with `<qa_pair>` elements:
   427|
   428|```xml
   429|<evaluation>
   430|   <qa_pair>
   431|      <question>Find the project created in Q2 2024 with the highest number of completed tasks. What is the project name?</question>
   432|      <answer>Website Redesign</answer>
   433|   </qa_pair>
   434|   <qa_pair>
   435|      <question>Search for issues labeled as "bug" that were closed in March 2024. Which user closed the most issues? Provide their username.</question>
   436|      <answer>sarah_dev</answer>
   437|   </qa_pair>
   438|</evaluation>
   439|```
   440|
   441|## Running Evaluations
   442|
   443|The evaluation script (`scripts/evaluation.py`) supports three transport types:
   444|
   445|**Important:**
   446|
   447|- **stdio transport**: The evaluation script automatically launches and manages the MCP server process for you. Do not run the server manually.
   448|- **sse/http transports**: You must start the MCP server separately before running the evaluation. The script connects to the already-running server at the specified URL.
   449|
   450|### 1. Local STDIO Server
   451|
   452|For locally-run MCP servers (script launches the server automatically):
   453|
   454|```bash
   455|python scripts/evaluation.py \
   456|  -t stdio \
   457|  -c python \
   458|  -a my_mcp_server.py \
   459|  evaluation.xml
   460|```
   461|
   462|With environment variables:
   463|
   464|```bash
   465|python scripts/evaluation.py \
   466|  -t stdio \
   467|  -c python \
   468|  -a my_mcp_server.py \
   469|  -e API_KEY=abc123 \
   470|  -e DEBUG=true \
   471|  evaluation.xml
   472|```
   473|
   474|### 2. Server-Sent Events (SSE)
   475|
   476|For SSE-based MCP servers (you must start the server first):
   477|
   478|```bash
   479|python scripts/evaluation.py \
   480|  -t sse \
   481|  -u https://example.com/mcp \
   482|  -H "Authorization: Bearer *** \
   483|  -H "X-Custom-Header: value" \
   484|  evaluation.xml
   485|```
   486|
   487|### 3. HTTP (Streamable HTTP)
   488|
   489|For HTTP-based MCP servers (you must start the server first):
   490|
   491|```bash
   492|python scripts/evaluation.py \
   493|  -t http \
   494|  -u https://example.com/mcp \
   495|  -H "Authorization: Bearer *** \
   496|  evaluation.xml
   497|```
   498|
   499|## Command-Line Options
   500|
   501|