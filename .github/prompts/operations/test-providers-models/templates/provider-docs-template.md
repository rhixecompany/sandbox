---
name: provider-docs-template
description: Link each auth provider's docs URL, inference endpoint, auth mechanism (api_key / oauth / device_code), and known rate limits.
variables:
  docs_url: "provider documentation URL"
  docs_content_path: "local markdown file of extracted docs"
---

# Provider docs — verified

- **Provider:** (fill from `hermes auth list`)
- **Docs URL:** {{ docs_url }}
- **Docs extracted to:** `{{ docs_content_path }}`
- **Auth mechanism:** api_key / oauth / device_code (verified from `.env` / `auth.json`)
- **Inference endpoint:** (from `hermes config show` or provider site)
