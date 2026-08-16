# Pending Store — Schema & Limits

## Location
- `C:\Users\Alexa\AppData\Local\hermes\pending\memory\*.json`
- `C:\Users\Alexa\AppData\Local\hermes\pending\skills\*.json`
- `_pruned/` subdir = non-destructive holding area for dropped entries.

## Entry shape (common fields)
```
{
  "id": "<short-hex>",
  "action": "add|replace|batch|remove",   # memory
  "action": "create|patch|write_file|edit|delete",  # skills
  "created_at": <epoch-float>,
  "payload": { ... }
}
```

### memory payload
- add: `{action:"add", target:"memory|user", content:"..."}`
- replace: `{action:"replace", target, content, old_text}`
- batch: `{action:"batch", target, operations:[ {action,content,old_text} ]}`

### skills payload
- create: `{action:"create", name:"<cat\\>skill"|skill, category, content}`
- patch: `{action:"patch", name, old_string, new_string, file_path?}`
- write_file: `{action:"write_file", name, file_path:"references/x.md", content}`
- edit: full rewrite (treated as patch)
- delete: `{action:"delete", name}`

## Size caps (hard — validated by validate-memories)
| File | Cap |
|------|-----|
| `MEMORY.md` | < 2200 bytes |
| `USER.md` | < 1375 bytes |

## Safety-copy recipe (no git on ~/.hermes)
```bash
cp ~/.hermes/memories/MEMORY.md ~/Desktop/SandBox/scripts/MEMORY_precompact.md
cp ~/.hermes/memories/USER.md   ~/Desktop/SandBox/scripts/USER_precompact.md
```

## Path resolution
- `name` with `\` or `/` → literal subpath under `skills/`.
- bare `name` → located by basename glob; if absent, create under `skills/<category>/<name>` (or `skills/<name>` when category=development).
