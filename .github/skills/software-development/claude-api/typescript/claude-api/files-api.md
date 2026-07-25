---
name: typescript-files-api
description: "Files API — TypeScript"
version: 1.0.0
author: Alexa
---
     1|# Files API — TypeScript
     2|
     3|The Files API uploads files for use in Messages API requests. Reference files via `file_id` in content blocks, avoiding re-uploads across multiple API calls.
     4|
     5|**Beta:** Pass `betas: ["files-api-2025-04-14"]` in your API calls (the SDK sets the required header automatically).
     6|
     7|## Key Facts
     8|
     9|- Maximum file size: 500 MB
    10|- Total storage: 100 GB per organization
    11|- Files persist until deleted
    12|- File operations (upload, list, delete) are free; content used in messages is billed as input tokens
    13|- Not available on Amazon Bedrock or Google Vertex AI
    14|
    15|---
    16|
    17|## Upload a File
    18|
    19|```typescript
    20|import Anthropic, { toFile } from "@anthropic-ai/sdk";
    21|import fs from "fs";
    22|
    23|const client = new Anthropic();
    24|
    25|const uploaded = await client.beta.files.upload({
    26|  file: await toFile(fs.createReadStream("report.pdf"), undefined, {
    27|    type: "application/pdf"
    28|  }),
    29|  betas: ["files-api-2025-04-14"]
    30|});
    31|
    32|console.log(`File ID: ${uploaded.id}`);
    33|console.log(`Size: ${uploaded.size_bytes} bytes`);
    34|```
    35|
    36|---
    37|
    38|## Use a File in Messages
    39|
    40|### PDF / Text Document
    41|
    42|```typescript
    43|const response = await client.beta.messages.create({
    44|  model: "claude-opus-4-7",
    45|  max_tokens: 16000,
    46|  messages: [
    47|    {
    48|      role: "user",
    49|      content: [
    50|        {
    51|          type: "text",
    52|          text: "Summarize the key findings in this report."
    53|        },
    54|        {
    55|          type: "document",
    56|          source: { type: "file", file_id: uploaded.id },
    57|          title: "Q4 Report",
    58|          citations: { enabled: true }
    59|        }
    60|      ]
    61|    }
    62|  ],
    63|  betas: ["files-api-2025-04-14"]
    64|});
    65|
    66|console.log(response.content[0].text);
    67|```
    68|
    69|---
    70|
    71|## Manage Files
    72|
    73|### List Files
    74|
    75|```typescript
    76|const files = await client.beta.files.list({
    77|  betas: ["files-api-2025-04-14"]
    78|});
    79|for (const f of files.data) {
    80|  console.log(`${f.id}: ${f.filename} (${f.size_bytes} bytes)`);
    81|}
    82|```
    83|
    84|### Delete a File
    85|
    86|```typescript
    87|await client.beta.files.delete("file_011CNha8iCJcU1wXNR6q4V8w", {
    88|  betas: ["files-api-2025-04-14"]
    89|});
    90|```
    91|
    92|### Download a File
    93|
    94|```typescript
    95|const response = await client.beta.files.download(
    96|  "file_011CNha8iCJcU1wXNR6q4V8w",
    97|  { betas: ["files-api-2025-04-14"] }
    98|);
    99|const content = Buffer.from(await response.arrayBuffer());
   100|await fs.promises.writeFile("output.txt", content);
   101|```
   102|