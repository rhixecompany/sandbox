---
name: batches-python
description: "Message Batches API — Python"
version: 1.0.0
author: Alexa
---
     1|# Message Batches API — Python
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
    17|```python
    18|import anthropic
    19|from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    20|from anthropic.types.messages.batch_create_params import Request
    21|
    22|client = anthropic.Anthropic()
    23|
    24|message_batch = client.messages.batches.create(
    25|    requests=[
    26|        Request(
    27|            custom_id="request-1",
    28|            params=MessageCreateParamsNonStreaming(
    29|                model="claude-opus-4-7",
    30|                max_tokens=16000,
    31|                messages=[{"role": "user", "content": "Summarize climate change impacts"}]
    32|            )
    33|        ),
    34|        Request(
    35|            custom_id="request-2",
    36|            params=MessageCreateParamsNonStreaming(
    37|                model="claude-opus-4-7",
    38|                max_tokens=16000,
    39|                messages=[{"role": "user", "content": "Explain quantum computing basics"}]
    40|            )
    41|        ),
    42|    ]
    43|)
    44|
    45|print(f"Batch ID: {message_batch.id}")
    46|print(f"Status: {message_batch.processing_status}")
    47|```
    48|
    49|---
    50|
    51|## Poll for Completion
    52|
    53|```python
    54|import time
    55|
    56|while True:
    57|    batch = client.messages.batches.retrieve(message_batch.id)
    58|    if batch.processing_status == "ended":
    59|        break
    60|    print(f"Status: {batch.processing_status}, processing: {batch.request_counts.processing}")
    61|    time.sleep(60)
    62|
    63|print("Batch complete!")
    64|print(f"Succeeded: {batch.request_counts.succeeded}")
    65|print(f"Errored: {batch.request_counts.errored}")
    66|```
    67|
    68|---
    69|
    70|## Retrieve Results
    71|
    72|> **Note:** Examples below use `match/case` syntax, requiring Python 3.10+. For earlier versions, use `if/elif` chains instead.
    73|
    74|```python
    75|for result in client.messages.batches.results(message_batch.id):
    76|    match result.result.type:
    77|        case "succeeded":
    78|            msg = result.result.message
    79|            text = next((b.text for b in msg.content if b.type == "text"), "")
    80|            print(f"[{result.custom_id}] {text[:100]}")
    81|        case "errored":
    82|            if result.result.error.type == "invalid_request":
    83|                print(f"[{result.custom_id}] Validation error - fix request and retry")
    84|            else:
    85|                print(f"[{result.custom_id}] Server error - safe to retry")
    86|        case "canceled":
    87|            print(f"[{result.custom_id}] Canceled")
    88|        case "expired":
    89|            print(f"[{result.custom_id}] Expired - resubmit")
    90|```
    91|
    92|---
    93|
    94|## Cancel a Batch
    95|
    96|```python
    97|cancelled = client.messages.batches.cancel(message_batch.id)
    98|print(f"Status: {cancelled.processing_status}")  # "canceling"
    99|```
   100|
   101|---
   102|
   103|## Batch with Prompt Caching
   104|
   105|```python
   106|shared_system = [
   107|    {"type": "text", "text": "You are a literary analyst."},
   108|    {
   109|        "type": "text",
   110|        "text": large_document_text,  # Shared across all requests
   111|        "cache_control": {"type": "ephemeral"}
   112|    }
   113|]
   114|
   115|message_batch = client.messages.batches.create(
   116|    requests=[
   117|        Request(
   118|            custom_id=f"analysis-{i}",
   119|            params=MessageCreateParamsNonStreaming(
   120|                model="claude-opus-4-7",
   121|                max_tokens=16000,
   122|                system=shared_system,
   123|                messages=[{"role": "user", "content": question}]
   124|            )
   125|        )
   126|        for i, question in enumerate(questions)
   127|    ]
   128|)
   129|```
   130|
   131|---
   132|
   133|## Full End-to-End Example
   134|
   135|```python
   136|import anthropic
   137|import time
   138|from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
   139|from anthropic.types.messages.batch_create_params import Request
   140|
   141|client = anthropic.Anthropic()
   142|
   143|# 1. Prepare requests
   144|items_to_classify = [
   145|    "The product quality is excellent!",
   146|    "Terrible customer service, never again.",
   147|    "It's okay, nothing special.",
   148|]
   149|
   150|requests = [
   151|    Request(
   152|        custom_id=f"classify-{i}",
   153|        params=MessageCreateParamsNonStreaming(
   154|            model="claude-haiku-4-5",
   155|            max_tokens=50,
   156|            messages=[{
   157|                "role": "user",
   158|                "content": f"Classify as positive/negative/neutral (one word): {text}"
   159|            }]
   160|        )
   161|    )
   162|    for i, text in enumerate(items_to_classify)
   163|]
   164|
   165|# 2. Create batch
   166|batch = client.messages.batches.create(requests=requests)
   167|print(f"Created batch: {batch.id}")
   168|
   169|# 3. Wait for completion
   170|while True:
   171|    batch = client.messages.batches.retrieve(batch.id)
   172|    if batch.processing_status == "ended":
   173|        break
   174|    time.sleep(10)
   175|
   176|# 4. Collect results
   177|results = {}
   178|for result in client.messages.batches.results(batch.id):
   179|    if result.result.type == "succeeded":
   180|        msg = result.result.message
   181|        results[result.custom_id] = next((b.text for b in msg.content if b.type == "text"), "")
   182|
   183|for custom_id, classification in sorted(results.items()):
   184|    print(f"{custom_id}: {classification}")
   185|```
   186|