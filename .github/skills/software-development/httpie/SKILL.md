---
author: Hermes Agent
description: Use when testing REST APIs, debugging HTTP services, making authenticated
  requests, uploading files via API, or inspecting HTTP responses.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: httpie
tags:
- http
- api
- debugging
- rest
- httpie
title: HTTPie
version: 1.0.0

---
# HTTPie

## Overview

HTTPie is a user-friendly CLI HTTP client for testing APIs, debugging HTTP services, and making authenticated requests. This skill provides concrete workflows for common HTTPie operations.

## When to Use

- Testing REST APIs during development
- Debugging HTTP service issues
- Making authenticated API requests (Bearer, Basic, Digest)
- Uploading files via multipart API endpoints
- Inspecting HTTP response headers and status codes
- Quick API prototyping without writing code

## When NOT to Use

- Browser-based testing (use browser tools)
- GraphQL APIs (use graphql-cli or curl)
- WebSocket connections
- Real-time streaming APIs
- Performance/load testing (use wrk, ab, or k6)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug HTTP response issues |
| `rest-graphql-debug` | Debug REST/GraphQL API patterns |

## Workflow

### Phase 1: Identify Endpoint

1. Determine the API URL, HTTP method (GET/POST/PUT/DELETE/PATCH)
2. Identify required headers (Content-Type, Authorization, etc.)
3. Plan authentication approach (Bearer token, Basic auth, API key)
4. Determine request body format (JSON, form-data, multipart)

### Phase 2: Construct & Execute Request

**Basic GET:**
```bash
http GET https://api.example.com/users
```

**With query parameters:**
```bash
http GET https://api.example.com/users page==1 limit==20
```

**POST with JSON body:**
```bash
http POST https://api.example.com/users \
  name="John Doe" \
  email="john@example.com" \
  role=admin
```

**With headers:**
```bash
http GET https://api.example.com/users \
  Authorization:"Bearer $API_TOKEN" \
  Accept:application/json
```

**File upload (multipart):**
```bash
http -f POST https://api.example.com/upload \
  file@/path/to/file.pdf \
  description="My document"
```

### Phase 3: Inspect Response

```bash
# Show response headers only
http --headers GET https://api.example.com/users

# Show request and response (verbose)
http --verbose GET https://api.example.com/users

# Show only response body
http --body GET https://api.example.com/users

# Follow redirects
http --follow GET https://api.example.com/redirect

# Save response to file
http --output response.json GET https://api.example.com/data
```

### Phase 4: Debug Issues

```bash
# Check SSL certificate issues
http --verify=no GET https://api.example.com

# Set timeout
http --timeout=30 GET https://api.example.com/slow-endpoint

# Debug 401: Check auth token
http -a username:password GET https://api.example.com/protected
http GET https://api.example.com/protected "Authorization:Bearer $TOKEN"

# Debug 429: Check rate limit headers
http --headers GET https://api.example.com/limited | grep -i "rate\|retry"

# Debug 500: Inspect full response
http --verbose POST https://api.example.com/broken endpoint=value
```

## Common Patterns

### Authentication

```bash
# Bearer token
http GET api.example.com "Authorization:Bearer $TOKEN"

# Basic auth
http -a user:pass api.example.com

# API key in header
http GET api.example.com "X-API-Key:$API_KEY"

# API key in query param
http GET "api.example.com/data?api_key=$API_KEY"
```

### JSON API Interaction

```bash
# Create resource
http POST api.example.com/items name="Widget" price:=29.99 quantity:=100

# Update resource (note := for non-string values)
http PUT api.example.com/items/42 name="Updated Widget" price:=39.99

# Delete resource
http DELETE api.example.com/items/42

# List with filtering
http GET api.example.com/items status==active sort==-created_at
```

### Session Management

```bash
# Create a session (saves auth/cookies)
http --session=./api-session.json GET api.example.com/login user=admin pass=secret

# Reuse session for subsequent requests
http --session=./api-session.json GET api.example.com/protected-resource
```

## Verification Checklist

- [ ] Correct HTTP method used (GET/POST/PUT/DELETE/PATCH)
- [ ] Authentication headers/tokens properly set
- [ ] Content-Type matches request body format
- [ ] Response status code is expected (200, 201, etc.)
- [ ] Response body parsed and validated
- [ ] Error responses handled gracefully
- [ ] Rate limits respected (check Retry-After header)

## Pitfalls

- **String vs. JSON values:** Use `=` for string values, `:=` for JSON (numbers, booleans, null)
- **Shell special characters:** Quote values with special chars: `name="value with spaces"`
- **Token expiration:** Bearer tokens expire — check 401 responses and refresh
- **SSL verification:** Don't disable `--verify=no` in production — fix the cert instead
- **Rate limiting:** Check `X-RateLimit-Remaining` and `Retry-After` headers
- **Large responses:** Use `--output file.json` for large responses instead of terminal
