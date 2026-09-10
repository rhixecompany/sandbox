---
name: files-api-python
description: "Files API — Python"
version: 1.0.0
author: Alexa
---
     1|# Files API — Python
     2|
     3|The Files API uploads files for use in Messages API requests. Reference files via `file_id` in content blocks, avoiding re-uploads across multiple API calls.
     4|
     5|**Beta:** Pass `betas=["files-api-2025-04-14"]` in your API calls (the SDK sets the required header automatically).
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
    19|```python
    20|import anthropic
    21|
    22|client = anthropic.Anthropic()
    23|
    24|uploaded = client.beta.files.upload(
    25|    file=("report.pdf", open("report.pdf", "rb"), "application/pdf"),
    26|)
    27|print(f"File ID: {uploaded.id}")
    28|print(f"Size: {uploaded.size_bytes} bytes")
    29|```
    30|
    31|---
    32|
    33|## Use a File in Messages
    34|
    35|### PDF / Text Document
    36|
    37|```python
    38|response = client.beta.messages.create(
    39|    model="claude-opus-4-7",
    40|    max_tokens=16000,
    41|    messages=[{
    42|        "role": "user",
    43|        "content": [
    44|            {"type": "text", "text": "Summarize the key findings in this report."},
    45|            {
    46|                "type": "document",
    47|                "source": {"type": "file", "file_id": uploaded.id},
    48|                "title": "Q4 Report",           # optional
    49|                "citations": {"enabled": True}   # optional, enables citations
    50|            }
    51|        ]
    52|    }],
    53|    betas=["files-api-2025-04-14"],
    54|)
    55|for block in response.content:
    56|    if block.type == "text":
    57|        print(block.text)
    58|```
    59|
    60|### Image
    61|
    62|```python
    63|image_file = client.beta.files.upload(
    64|    file=("photo.png", open("photo.png", "rb"), "image/png"),
    65|)
    66|
    67|response = client.beta.messages.create(
    68|    model="claude-opus-4-7",
    69|    max_tokens=16000,
    70|    messages=[{
    71|        "role": "user",
    72|        "content": [
    73|            {"type": "text", "text": "What's in this image?"},
    74|            {
    75|                "type": "image",
    76|                "source": {"type": "file", "file_id": image_file.id}
    77|            }
    78|        ]
    79|    }],
    80|    betas=["files-api-2025-04-14"],
    81|)
    82|```
    83|
    84|---
    85|
    86|## Manage Files
    87|
    88|### List Files
    89|
    90|```python
    91|files = client.beta.files.list()
    92|for f in files.data:
    93|    print(f"{f.id}: {f.filename} ({f.size_bytes} bytes)")
    94|```
    95|
    96|### Get File Metadata
    97|
    98|```python
    99|file_info = client.beta.files.retrieve_metadata("file_011CNha8iCJcU1wXNR6q4V8w")
   100|print(f"Filename: {file_info.filename}")
   101|print(f"MIME type: {file_info.mime_type}")
   102|```
   103|
   104|### Delete a File
   105|
   106|```python
   107|client.beta.files.delete("file_011CNha8iCJcU1wXNR6q4V8w")
   108|```
   109|
   110|### Download a File
   111|
   112|Only files created by the code execution tool or skills can be downloaded (not user-uploaded files).
   113|
   114|```python
   115|file_content = client.beta.files.download("file_011CNha8iCJcU1wXNR6q4V8w")
   116|file_content.write_to_file("output.txt")
   117|```
   118|
   119|---
   120|
   121|## Full End-to-End Example
   122|
   123|Upload a document once, ask multiple questions about it:
   124|
   125|```python
   126|import anthropic
   127|
   128|client = anthropic.Anthropic()
   129|
   130|# 1. Upload once
   131|uploaded = client.beta.files.upload(
   132|    file=("contract.pdf", open("contract.pdf", "rb"), "application/pdf"),
   133|)
   134|print(f"Uploaded: {uploaded.id}")
   135|
   136|# 2. Ask multiple questions using the same file_id
   137|questions = [
   138|    "What are the key terms and conditions?",
   139|    "What is the termination clause?",
   140|    "Summarize the payment schedule.",
   141|]
   142|
   143|for question in questions:
   144|    response = client.beta.messages.create(
   145|        model="claude-opus-4-7",
   146|        max_tokens=16000,
   147|        messages=[{
   148|            "role": "user",
   149|            "content": [
   150|                {"type": "text", "text": question},
   151|                {
   152|                    "type": "document",
   153|                    "source": {"type": "file", "file_id": uploaded.id}
   154|                }
   155|            ]
   156|        }],
   157|        betas=["files-api-2025-04-14"],
   158|    )
   159|    print(f"\nQ: {question}")
   160|    text = next((b.text for b in response.content if b.type == "text"), "")
   161|    print(f"A: {text[:200]}")
   162|
   163|# 3. Clean up when done
   164|client.beta.files.delete(uploaded.id)
   165|```
   166|