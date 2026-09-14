---
name: shared-error-codes
description: "HTTP Error Codes Reference"
version: 1.0.0
author: Alexa
---
     1|# HTTP Error Codes Reference
     2|
     3|This file documents HTTP error codes returned by the Claude API, their common causes, and how to handle them. For language-specific error handling examples, see the `python/` or `typescript/` folders.
     4|
     5|## Error Code Summary
     6|
     7|| Code | Error Type | Retryable | Common Cause |
     8|| --- | --- | --- | --- |
     9|| 400 | `invalid_request_error` | No | Invalid request format or parameters |
    10|| 401 | `authentication_error` | No | Invalid or missing API key |
    11|| 403 | `permission_error` | No | API key lacks permission |
    12|| 404 | `not_found_error` | No | Invalid endpoint or model ID |
    13|| 413 | `request_too_large` | No | Request exceeds size limits |
    14|| 429 | `rate_limit_error` | Yes | Too many requests |
    15|| 500 | `api_error` | Yes | Anthropic service issue |
    16|| 529 | `overloaded_error` | Yes | API is temporarily overloaded |
    17|
    18|## Detailed Error Information
    19|
    20|### 400 Bad Request
    21|
    22|**Causes:**
    23|
    24|- Malformed JSON in request body
    25|- Missing required parameters (`model`, `max_tokens`, `messages`)
    26|- Invalid parameter types (e.g., string where integer expected)
    27|- Empty messages array
    28|- Messages not alternating user/assistant
    29|
    30|**Example error:**
    31|
    32|```json
    33|{
    34|  "error": {
    35|    "type": "invalid_request_error",
    36|    "message": "messages: roles must alternate between \"user\" and \"assistant\""
    37|  },
    38|  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy",
    39|  "type": "error"
    40|}
    41|```
    42|
    43|**Fix:** Validate request structure before sending. Check that:
    44|
    45|- `model` is a valid model ID
    46|- `max_tokens` is a positive integer
    47|- `messages` array is non-empty and alternates correctly
    48|
    49|---
    50|
    51|### 401 Unauthorized
    52|
    53|**Causes:**
    54|
    55|- Missing `x-api-key` header or `Authorization` header
    56|- Invalid API key format
    57|- Revoked or deleted API key
    58|
    59|**Fix:** Ensure `ANTHROPIC_API_KEY` environment variable is set correctly.
    60|
    61|---
    62|
    63|### 403 Forbidden
    64|
    65|**Causes:**
    66|
    67|- API key doesn't have access to the requested model
    68|- Organization-level restrictions
    69|- Attempting to access beta features without beta access
    70|
    71|**Fix:** Check your API key permissions in the Console. You may need a different API key or to request access to specific features.
    72|
    73|---
    74|
    75|### 404 Not Found
    76|
    77|**Causes:**
    78|
    79|- Typo in model ID (e.g., `claude-sonnet-4.6` instead of `claude-sonnet-4-6`)
    80|- Using deprecated model ID
    81|- Invalid API endpoint
    82|
    83|**Fix:** Use exact model IDs from the models documentation. You can use aliases (e.g., `claude-opus-4-7`).
    84|
    85|---
    86|
    87|### 413 Request Too Large
    88|
    89|**Causes:**
    90|
    91|- Request body exceeds maximum size
    92|- Too many tokens in input
    93|- Image data too large
    94|
    95|**Fix:** Reduce input size — truncate conversation history, compress/resize images, or split large documents into chunks.
    96|
    97|---
    98|
    99|### 400 Validation Errors
   100|
   101|Some 400 errors are specifically related to parameter validation:
   102|
   103|- `max_tokens` exceeds model's limit
   104|- Invalid `temperature` value (must be 0.0-1.0)
   105|- `budget_tokens` >= `max_tokens` in extended thinking
   106|- Invalid tool definition schema
   107|
   108|**Model-specific 400s on Opus 4.7:**
   109|
   110|- `temperature`, `top_p`, `top_k` are removed — sending any of them returns 400. Delete the parameter; see `shared/model-migration.md` → Per-SDK Syntax Reference.
   111|- `thinking: {type: "enabled", budget_tokens: N}` is removed — sending it returns 400. Use `thinking: {type: "adaptive"}` instead.
   112|
   113|**Common mistake with extended thinking on older models (Opus 4.6 and earlier):**
   114|
   115|```
   116|# Wrong: budget_tokens must be < max_tokens
   117|thinking: budget_tokens=10000, max_tokens=1000  → Error!
   118|
   119|# Correct
   120|thinking: budget_tokens=10000, max_tokens=16000
   121|```
   122|
   123|---
   124|
   125|### 429 Rate Limited
   126|
   127|**Causes:**
   128|
   129|- Exceeded requests per minute (RPM)
   130|- Exceeded tokens per minute (TPM)
   131|- Exceeded tokens per day (TPD)
   132|
   133|**Headers to check:**
   134|
   135|- `retry-after`: Seconds to wait before retrying
   136|- `x-ratelimit-limit-*`: Your limits
   137|- `x-ratelimit-remaining-*`: Remaining quota
   138|
   139|**Fix:** The Anthropic SDKs automatically retry 429 and 5xx errors with exponential backoff (default: `max_retries=2`). For custom retry behavior, see the language-specific error handling examples.
   140|
   141|---
   142|
   143|### 500 Internal Server Error
   144|
   145|**Causes:**
   146|
   147|- Temporary Anthropic service issue
   148|- Bug in API processing
   149|
   150|**Fix:** Retry with exponential backoff. If persistent, check [status.anthropic.com](https://status.anthropic.com).
   151|
   152|---
   153|
   154|### 529 Overloaded
   155|
   156|**Causes:**
   157|
   158|- High API demand
   159|- Service capacity reached
   160|
   161|**Fix:** Retry with exponential backoff. Consider using a different model (Haiku is often less loaded), spreading requests over time, or implementing request queuing.
   162|
   163|---
   164|
   165|## Common Mistakes and Fixes
   166|
   167|| Mistake | Error | Fix |
   168|| --- | --- | --- |
   169|| `temperature`/`top_p`/`top_k` on Opus 4.7 | 400 | Remove the parameter (see `shared/model-migration.md`) |
   170|| `budget_tokens` on Opus 4.7 | 400 | Use `thinking: {type: "adaptive"}` |
   171|| `budget_tokens` >= `max_tokens` (older models) | 400 | Ensure `budget_tokens` < `max_tokens` |
   172|| Typo in model ID | 404 | Use valid model ID like `claude-opus-4-7` |
   173|| First message is `assistant` | 400 | First message must be `user` |
   174|| Consecutive same-role messages | 400 | Alternate `user` and `assistant` |
   175|| API key in code | 401 (leaked key) | Use environment variable |
   176|| Custom retry needs | 429/5xx | SDK retries automatically; customize with `max_retries` |
   177|
   178|## Typed Exceptions in SDKs
   179|
   180|**Always use the SDK's typed exception classes** instead of checking error messages with string matching. Each HTTP error code maps to a specific exception class:
   181|
   182|| HTTP Code | TypeScript Class | Python Class |
   183|| --- | --- | --- |
   184|| 400 | `Anthropic.BadRequestError` | `anthropic.BadRequestError` |
   185|| 401 | `Anthropic.AuthenticationError` | `anthropic.AuthenticationError` |
   186|| 403 | `Anthropic.PermissionDeniedError` | `anthropic.PermissionDeniedError` |
   187|| 404 | `Anthropic.NotFoundError` | `anthropic.NotFoundError` |
   188|| 429 | `Anthropic.RateLimitError` | `anthropic.RateLimitError` |
   189|| 500+ | `Anthropic.InternalServerError` | `anthropic.InternalServerError` |
   190|| Any | `Anthropic.APIError` | `anthropic.APIError` |
   191|
   192|```typescript
   193|// ✅ Correct: use typed exceptions
   194|try {
   195|  const response = await client.messages.create({...});
   196|} catch (error) {
   197|  if (error instanceof Anthropic.RateLimitError) {
   198|    // Handle rate limiting
   199|  } else if (error instanceof Anthropic.APIError) {
   200|    console.error(`API error ${error.status}:`, error.message);
   201|  }
   202|}
   203|
   204|// ❌ Wrong: don't check error messages with string matching
   205|try {
   206|  const response = await client.messages.create({...});
   207|} catch (error) {
   208|  const msg = error instanceof Error ? error.message : String(error);
   209|  if (msg.includes("429") || msg.includes("rate_limit")) { ... }
   210|}
   211|```
   212|
   213|All exception classes extend `Anthropic.APIError`, which has a `status` property. Use `instanceof` checks from most specific to least specific (e.g., check `RateLimitError` before `APIError`).
   214|