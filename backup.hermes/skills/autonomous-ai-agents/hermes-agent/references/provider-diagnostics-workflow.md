# Provider Configuration Diagnostics Workflow

## When to Use This Pattern

- Provider endpoint is broken or returning 404/500 errors
- Free model tier has expired and no replacement is obvious
- Need to identify all available free models across a provider's catalog
- Configuration change should be validated before committing

## Workflow Steps

### 1. Web Research (5 min)

Start with web search for the provider's endpoint documentation:

```
Search: "[Provider Name] API endpoint URL base_url"
Extract: Official docs links (usually docs.provider.com or provider.io/docs)
```

### 2. Extract Official Docs (10 min)

Use `web_extract` on the provider's docs pages:

```
Look for:
  - Correct base URL pattern
  - Required path segments (/chat/completions, /v1/messages, etc.)
  - Model listing endpoint
  - Authentication requirements
```

**Common locations:**
- Quickstart guide
- API reference or "Getting Started"
- Provider pricing or model catalog page

### 3. Live Endpoint Tests with curl (5 min per test)

Test endpoints progressively to identify which one works:

```bash
# Test 1: Root endpoint
curl -s -I https://provider.ai/v1

# Test 2: Chat completions endpoint
curl -s -I https://provider.ai/v1/chat/completions

# Test 3: Models listing endpoint
curl -s https://provider.ai/v1/models

# Test 4: Full request with valid model
curl -X POST https://provider.ai/v1/chat/completions \
  -H "Authorization: Bearer *** \
  -H "Content-Type: application/json" \
  -d '{"model": "candidate-model", "messages": [...]}'
```

**Document results:**
- Which endpoints return 200 vs 404
- Which return JSON vs HTML
- Any error messages that indicate what's wrong

### 4. Identify Available Free Models

If the provider has a `/models` endpoint:

```bash
curl -s https://provider.ai/v1/models -H "Authorization: Bearer ***" | jq '.data[] | {id, pricing}'
```

Filter by `free: true` or `$0` pricing.

If no models endpoint exists, check the provider's website or pricing page directly.

### 5. Document Findings

Create a comprehensive report with:
- Current (broken) vs. correct configuration
- Endpoint verification results (curl output)
- Free model options with availability dates
- Configuration examples
- Verification commands for users

### 6. Update Configuration

```bash
hermes config set model.base_url "https://provider.ai/v1/chat/completions"
hermes config set model.default_model "best-free-model"
```

Verify with:
```bash
hermes chat -q "Test message"
hermes status
```

## Example Outputs

### Good: Working Endpoint
```
HTTP/1.1 200 OK
Content-Type: application/json

{"choices":[{"message":{"content":"..."},...}],...}
```

### Bad: Broken Endpoint
```
HTTP/1.1 404 Not Found
Content-Type: text/html

<!DOCTYPE html><html>404 Not Found</html>
```

### Models Listing
```json
{
  "data": [
    {"id": "model-free-v1", "pricing": {"input": 0, "output": 0}, "available": true},
    {"id": "model-paid-v1", "pricing": {"input": 0.05, "output": 0.15}, "available": true},
    ...
  ]
}
```

## Pitfalls to Avoid

1. **Incomplete paths:** Always test the full path including `/chat/completions`, `/messages`, etc. — bare domain won't work.
2. **Expired free tiers:** Document expiration dates if mentioned. Free models rotate; save current list with dates.
3. **API key errors masking endpoint errors:** Get a 401 is better than a 404 — it proves the endpoint exists. Test without auth first to see endpoint availability.
4. **Assuming docs are up-to-date:** Live curl tests catch outdated docs. If docs say `/v1` but curl on `/v1/chat/completions` works, prefer the working endpoint.
5. **Forgetting fallback models:** Identify at least 2-3 free models from the same provider for resilience.

## Time Estimates

| Step | Time | Effort |
|------|------|--------|
| Web research | 5 min | Low |
| Extract docs | 10 min | Low |
| Live tests (4 curl calls) | 5 min | Low |
| Identify free models | 5 min | Low |
| Document findings | 10 min | Medium |
| Update config + verify | 5 min | Low |
| **Total** | **40 min** | **Medium** |

## When to Escalate

If after step 4 you still don't have a working endpoint:
1. Check for IP/geo restrictions (use VPN if available)
2. Look for beta/legacy API versions in docs
3. Check provider's status page for outages
4. Ask in provider's community Discord or GitHub issues
5. File a bug with the provider including your curl commands

## Reference Template

Save this as `PROVIDER_DIAGNOSTICS.md` for each provider you troubleshoot:

```markdown
# [Provider Name] Configuration Diagnostics

**Date:** YYYY-MM-DD
**Issue:** [Brief description]

## Endpoints Tested

- [Endpoint 1]: [Result]
- [Endpoint 2]: [Result]
...

## Free Models Available

| Model ID | Cost | Tested | Notes |
|----------|------|--------|-------|
| model-1  | $0   | ✓      | Recommended |
| model-2  | $0   | ✗      | Deprecated |

## Configuration

FROM:
```yaml
...
```

TO:
```yaml
...
```

## Verification

```bash
[Commands to test fix]
```

## References

- [Link to provider docs]
- [Link to GitHub issue / discussion]
```
