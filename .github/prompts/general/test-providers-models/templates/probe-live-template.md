---
name: probe-live-template
description: Run `hermes auth list`, `hermes config show`, `hermes status`, `hermes doctor`, `hermes doctor --fix`, `hermes insights`, `hermes fallback list`, `hermes model`.
---

# Provider probe — live execution

Run commands in order and capture stdout/stderr:

1. `hermes auth list`
2. `hermes config show`
3. `hermes status`
4. `hermes doctor`
5. `hermes doctor --fix`
6. `hermes insights`
7. `hermes fallback list`
8. `hermes model`

Record: exit code, key state per provider, rate-limit flags, model/provider defaults, auth expiration timestamps.
