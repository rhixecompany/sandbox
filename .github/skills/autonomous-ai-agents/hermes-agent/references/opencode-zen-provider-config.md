# OpenCode Zen Provider Configuration

## Critical Issue: Endpoint Path Required

**Problem:** OpenCode Zen configuration often omits the required `/chat/completions` path, resulting in 404 errors.

**Incorrect Configuration:**
```yaml
providers:
  opencode-zen:
    api_key: "your-key"
    base_url: "https://opencode.ai/zen/v1"   # ❌ WRONG — returns 404
```

**Correct Configuration:**
```yaml
providers:
  opencode-zen:
    api_key: "your-key"
    base_url: "https://opencode.ai/zen/v1/chat/completions"  # ✓ CORRECT
```

## Why This Matters

The bare `/v1` endpoint returns the OpenCode Zen website (HTML 404) when queried as an API endpoint. The actual API endpoints are:

| Endpoint | Purpose | Returns |
|----------|---------|---------|
| `/v1/chat/completions` | OpenAI-compatible chat API | Chat completion responses ✓ |
| `/v1/messages` | Anthropic-compatible messages API | Message responses ✓ |
| `/v1/models` | List available models | JSON array of models ✓ |
| `/v1` | Website root | HTML 404 page ❌ |

## Provider Setup Example

```bash
hermes config set model.provider opencode-zen
hermes config set model.base_url "https://opencode.ai/zen/v1/chat/completions"
```

## Free Models (May 2026)

OpenCode Zen free models available:

| Model ID | Cost | Notes |
|----------|------|-------|
| `big-pickle` | $0 | Recommended for DevOps tasks |
| `deepseek-v4-flash-free` | $0 | Better reasoning; alternative |
| `nemotron-3-super-free` | $0 | NVIDIA trial, data logging — testing only |

⚠️ **Deprecated:** `qwen3.6-plus-free` free tier ended May 2026 — migrate to `big-pickle` or subscribe to OpenCode Go.

## Verification Command

```bash
# Test the corrected endpoint
curl -X POST https://opencode.ai/zen/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "big-pickle",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 10
  }'

# Expected: JSON chat completion response
# Actual error: {"error": {...}} if model is invalid, but endpoint is reachable
```

## Pitfall: Forgetting the `/chat/completions` Path

This is a common mistake because:
1. Some provider docs show the base URL without the full path
2. The domain is `opencode.ai/zen`, which looks complete
3. The docs mention `/v1` but don't always emphasize `/chat/completions` as required

**Always test with curl** before deploying configuration changes to catch 404 errors early.

## List All Models

```bash
curl https://opencode.ai/zen/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Accept: application/json"
```

Returns JSON array of 40+ available models (OpenAI, Anthropic, Google, Qwen, etc.).
