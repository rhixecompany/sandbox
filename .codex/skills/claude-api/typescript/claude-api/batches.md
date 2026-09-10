---
name: typescript-batches
description: "Message Batches API — TypeScript"
version: 1.0.0
author: Alexa
---
     1|# Message Batches API — TypeScript
     2|
     3|The Batches API (`POST /v1/messages/batches`) processes Messages API requests asynchronously at 50% of standard prices.
     4|
     5|## Key Facts
     6|
     7|- Up to 100,000 requests or 256 MB per batch
     8|- Most batches complete within 1 hour; maximum 24 hours
     9|- Results available for 29 days after creation
    10|- 50% cost reduction on all token usage
    11|- All Messages API features supported (vision, tools, caching, etc.)
    12|
    13|---
    14|
    15|## Create a Batch
    16|
    17|```typescript
    18|import Anthropic from "@anthropic-ai/sdk";
    19|
    20|const client = new Anthropic();
    21|
    22|const messageBatch = await client.messages.batches.create({
    23|  requests: [
    24|    {
    25|      custom_id: "request-1",
    26|      params: {
    27|        model: "claude-opus-4-7",
    28|        max_tokens: 16000,
    29|        messages: [
    30|          {
    31|            role: "user",
    32|            content: "Summarize climate change impacts"
    33|          }
    34|        ]
    35|      }
    36|    },
    37|    {
    38|      custom_id: "request-2",
    39|      params: {
    40|        model: "claude-opus-4-7",
    41|        max_tokens: 16000,
    42|        messages: [
    43|          {
    44|            role: "user",
    45|            content: "Explain quantum computing basics"
    46|          }
    47|        ]
    48|      }
    49|    }
    50|  ]
    51|});
    52|
    53|console.log(`Batch ID: ${messageBatch.id}`);
    54|console.log(`Status: ${messageBatch.processing_status}`);
    55|```
    56|
    57|---
    58|
    59|## Poll for Completion
    60|
    61|```typescript
    62|let batch;
    63|while (true) {
    64|  batch = await client.messages.batches.retrieve(messageBatch.id);
    65|  if (batch.processing_status === "ended") break;
    66|  console.log(
    67|    `Status: ${batch.processing_status}, processing: ${batch.request_counts.processing}`
    68|  );
    69|  await new Promise(resolve => setTimeout(resolve, 60_000));
    70|}
    71|
    72|console.log("Batch complete!");
    73|console.log(`Succeeded: ${batch.request_counts.succeeded}`);
    74|console.log(`Errored: ${batch.request_counts.errored}`);
    75|```
    76|
    77|---
    78|
    79|## Retrieve Results
    80|
    81|```typescript
    82|for await (const result of await client.messages.batches.results(
    83|  messageBatch.id
    84|)) {
    85|  switch (result.result.type) {
    86|    case "succeeded":
    87|      console.log(
    88|        `[${result.custom_id}] ${result.result.message.content[0].text.slice(0, 100)}`
    89|      );
    90|      break;
    91|    case "errored":
    92|      if (result.result.error.type === "invalid_request") {
    93|        console.log(
    94|          `[${result.custom_id}] Validation error - fix and retry`
    95|        );
    96|      } else {
    97|        console.log(
    98|          `[${result.custom_id}] Server error - safe to retry`
    99|        );
   100|      }
   101|      break;
   102|    case "expired":
   103|      console.log(`[${result.custom_id}] Expired - resubmit`);
   104|      break;
   105|  }
   106|}
   107|```
   108|
   109|---
   110|
   111|## Cancel a Batch
   112|
   113|```typescript
   114|const cancelled = await client.messages.batches.cancel(
   115|  messageBatch.id
   116|);
   117|console.log(`Status: ${cancelled.processing_status}`); // "canceling"
   118|```
   119|