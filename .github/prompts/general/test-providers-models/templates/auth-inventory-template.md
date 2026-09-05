---
name: auth-inventory-template
description: Captures `hermes auth list` + `.env` state per provider.
variables:
  provider: "name (e.g., opencode-zen)"
  key_env_var: "env variable holding key"
  status: "valid / exhausted / rate-limited / auth-failed / missing"
  rate_details: "e.g., 429 42m; 402 ready; 401 auth-failed"
  docs_url: "provider docs link"
  auth_file: "path to auth.json / .env"
---

# Auth inventory — {{ provider }}

- **Provider:** {{ provider }}
- **Key env:** `{{ key_env_var }}`
- **Status:** {{ status }}
- **Rate / auth notes:** {{ rate_details }}
- **Docs:** {{ docs_url }}
- **Auth file verified:** {{ auth_file }}
