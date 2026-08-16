# API Validation Recipes

## Curl

```bash
# Models list
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer $API_KEY" \
  "$BASE_URL/v1/models"

# Chat completion
curl -s "$BASE_URL/v1/chat/completions" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"grok-3-latest","messages":[{"role":"user","content":"TEST_OK"}],"max_tokens":10}'
```

## Python

```python
import requests

def validate_key(base_url, api_key):
    try:
        r = requests.get(
            f"{base_url}/v1/models",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=20,
        )
        return r.status_code, r.json().get("data", [])[:5]
    except Exception as e:
        return None, str(e)
```

## Endpoints

| Provider | Base URL |
|----------|----------|
| Groq | https://api.groq.com/openai/v1 |
| xAI | https://api.x.ai/v1 |
| OpenRouter | https://openrouter.ai/api/v1 |
| DeepSeek | https://api.deepseek.com/v1 |
| OpenAI | https://api.openai.com/v1 |
| Anthropic | https://api.anthropic.com/v1 |
| Google | https://generativelanguage.googleapis.com/v1beta |
| Ollama Cloud | https://ollama.com/api |
