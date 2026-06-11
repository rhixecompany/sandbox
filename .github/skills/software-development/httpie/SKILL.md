---
category: software-development
title: Httpie
name: httpie
description: "Use when testing REST APIs, debugging HTTP services, making authenticated requests, uploading files via API, or inspecting HTTP responses."
---


## Description


CLI HTTP client for APIs. Use for REST requests, debugging services, testing endpoints, authentication (Bearer/Basic), and file uploads.

## When to Use

- Testing REST APIs
- Debugging HTTP services
- Making authenticated requests
- Uploading files via API
- Testing endpoint behavior
- Inspecting HTTP headers and responses
- Troubleshooting API issues

## When NOT to Use

- Browser-based testing (use browser tools)
- GraphQL APIs (use graphql-cli)
- WebSocket connections
- Real-time streaming

## Workflow

### Phase 1: Identify Endpoint

- Determine API URL and method
- Identify required parameters
- Plan authentication approach

### Phase 2: Construct Request

- Build request with headers
- Add authentication (Bearer/Basic)
- Include request body if needed
- Add query parameters

### Phase 3: Execute Request

- Send HTTP request
- Inspect response status
- Review response headers
- Examine response body

### Phase 4: Debug & Iterate

- Analyze response for errors
- Adjust request as needed
- Test different scenarios
- Document findings

## Tools & References

- **Related Skills**: systematic-debugging
- **HTTPie**: https://httpie.io
- **Authentication**: Bearer tokens, Basic auth
- **Common Issues**: 401, 429, SSL errors, timeouts

## Best Practices

- Use descriptive request names
- Save common requests
- Test with different payloads
- Check response headers
- Handle rate limiting
- Verify SSL certificates
- Document API behavior

