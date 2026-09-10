---
name: shared-managed-agents-memory
description: "Managed Agents — Memory Stores"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Memory Stores
     2|
     3|> **Public beta.** Memory stores ship under the `managed-agents-2026-04-01` beta header; the SDK sets it automatically on all `client.beta.memory_stores.*` calls. If `client.beta.memory_stores` is missing, upgrade to the latest SDK release.
     4|
     5|Sessions are ephemeral by default — when one ends, anything the agent learned is gone. A **memory store** is a workspace-scoped collection of small text documents that persists across sessions. When a store is attached to a session (via `resources[]`), it is mounted into the container as a filesystem directory; the agent reads and writes it with the ordinary file tools, and a system-prompt note tells it the mount is there.
     6|
     7|Every mutation to a memory produces an immutable **memory version** (`memver_...`), giving you an audit trail and point-in-time rollback/redact.
     8|
     9|## Object model
    10|
    11|| Object | ID prefix | Scope | Notes |
    12|| --- | --- | --- | --- |
    13|| Memory store | `memstore_...` | Workspace | Attach to sessions via `resources[]` |
    14|| Memory | `mem_...` | Store | One text file, addressed by `path` (≤ 100KB each — prefer many small files) |
    15|| Memory version | `memver_...` | Memory | Immutable snapshot per mutation; `operation` ∈ `created` / `modified` / `deleted` |
    16|
    17|## Create a store
    18|
    19|`description` is passed to the agent so it knows what the store contains — write it for the model, not for humans.
    20|
    21|```python
    22|store = client.beta.memory_stores.create(
    23|    name="User Preferences",
    24|    description="Per-user preferences and project context.",
    25|)
    26|print(store.id)  # memstore_01Hx...
    27|```
    28|
    29|Other SDKs: TypeScript `client.beta.memoryStores.create({...})`; Go `client.Beta.MemoryStores.New(ctx, ...)`. See `shared/managed-agents-api-reference.md` → SDK Method Reference for the full per-language table.
    30|
    31|Stores support `retrieve` / `update` / `list` (with `include_archived`, `created_at_{gte,lte}` filters) / `delete` / **`archive`**. Archive makes the store read-only — existing session attachments continue, new sessions cannot reference it; no unarchive.
    32|
    33|### Seed with content (optional)
    34|
    35|Pre-load reference material before any session runs. `memories.create` creates a memory at the given `path`; if a memory already exists there the call returns `409` (`memory_path_conflict_error`, with the `conflicting_memory_id`). The store ID is the first positional argument.
    36|
    37|```python
    38|client.beta.memory_stores.memories.create(
    39|    store.id,
    40|    path="/formatting_standards.md",
    41|    content="All reports use GAAP formatting. Dates are ISO-8601...",
    42|)
    43|```
    44|
    45|## Attach to a session
    46|
    47|Memory stores go in the session's `resources[]` array alongside `file` and `github_repository` resources (see `shared/managed-agents-environments.md` → Resources). Memory stores attach at **session create time only** — `sessions.resources.add()` does not accept `memory_store`.
    48|
    49|```python
    50|session = client.beta.sessions.create(
    51|    agent=agent.id,
    52|    environment_id=environment.id,
    53|    resources=[
    54|        {
    55|            "type": "memory_store",
    56|            "memory_store_id": store.id,
    57|            "access": "read_write",  # or "read_only"; default is "read_write"
    58|            "instructions": "User preferences and project context. Check before starting any task.",
    59|        }
    60|    ],
    61|)
    62|```
    63|
    64|| Field | Required | Notes |
    65|| --- | --- | --- |
    66|| `type` | ✅ | `"memory_store"` |
    67|| `memory_store_id` | ✅ | `memstore_...` |
    68|| `access` | — | `"read_write"` (default) or `"read_only"` — enforced at the filesystem level on the mount |
    69|| `instructions` | — | Session-specific guidance for this store, in addition to the store's `name`/`description`. ≤ 4,096 chars. |
    70|
    71|**Max 8 memory stores per session.** Attach multiple when different slices of memory have different owners or lifecycles — e.g. one read-only shared-reference store plus one read-write per-user store, or one store per end-user/team/project sharing a single agent config.
    72|
    73|### How the agent sees it (FUSE mount)
    74|
    75|Each attached store is mounted in the session container at `/mnt/memory/<store-name>/`. The agent interacts with it using the standard file tools (`bash`, `read`, `write`, `edit`, `glob`, `grep`) — there are no dedicated memory tools. `access: "read_only"` makes the mount read-only at the filesystem level; `"read_write"` allows the agent to create, edit, and delete files under it. A short description of each mount (name, path, `instructions`, access) is automatically injected into the system prompt so the agent knows the store exists without you having to mention it.
    76|
    77|Writes the agent makes under the mount are persisted back to the store and produce memory versions just like host-side `memories.update` calls.
    78|
    79|## Manage memories directly (host-side)
    80|
    81|Use these for review workflows, correcting bad memories, or seeding stores out-of-band.
    82|
    83|### List
    84|
    85|Returns `Memory | MemoryPrefix` entries — a `MemoryPrefix` (`type: "memory_prefix"`, just a `path`) is a directory-like node when listing hierarchically. Use `path_prefix` to scope (include a trailing slash: `"/notes/"` matches `/notes/a.md` but not `/notes_backup/old.md`) and `depth` to bound the tree walk. `order_by` / `order` sort the result. Pass `view="full"` to include `content` in each item; the default `"basic"` returns metadata only.
    86|
    87|```python
    88|for m in client.beta.memory_stores.memories.list(store.id, path_prefix="/"):
    89|    if m.type == "memory":
    90|        print(f"{m.path}  ({m.content_size_bytes} bytes, sha={m.content_sha256[:8]})")
    91|    else:  # "memory_prefix"
    92|        print(f"{m.path}/")
    93|```
    94|
    95|### Read
    96|
    97|```python
    98|mem = client.beta.memory_stores.memories.retrieve(memory_id, memory_store_id=store.id)
    99|print(mem.content)
   100|```
   101|
   102|`retrieve` defaults to `view="full"` (content included); `view` matters mainly on list endpoints.
   103|
   104|### Create vs. update
   105|
   106|| Operation | Addressed by | Semantics |
   107|| --- | --- | --- |
   108|| `memories.create(store_id, path=..., content=...)` | **Path** | Create at `path`. `409` (`memory_path_conflict_error`, includes `conflicting_memory_id`) if the path is already occupied. |
   109|| `memories.update(mem_id, memory_store_id=..., path=..., content=...)` | **`mem_...` ID** | Mutate existing memory. Change `content`, `path` (rename), or both. Renaming onto an occupied path returns the same `409 memory_path_conflict_error`. |
   110|
   111|```python
   112|mem = client.beta.memory_stores.memories.create(
   113|    store.id,
   114|    path="/preferences/formatting.md",
   115|    content="Always use tabs, not spaces.",
   116|)
   117|
   118|client.beta.memory_stores.memories.update(
   119|    mem.id,
   120|    memory_store_id=store.id,
   121|    path="/archive/2026_q1_formatting.md",  # rename
   122|)
   123|```
   124|
   125|### Optimistic concurrency (precondition on `update`)
   126|
   127|`memories.update` accepts a `precondition` so you can read → modify → write back without clobbering a concurrent writer. The only supported type is `content_sha256`. On mismatch the API returns `409` (`memory_precondition_failed_error`) — re-read and retry against fresh state.
   128|
   129|```python
   130|client.beta.memory_stores.memories.update(
   131|    mem.id,
   132|    memory_store_id=store.id,
   133|    content="CORRECTED: Always use 2-space indentation.",
   134|    precondition={"type": "content_sha256", "content_sha256": mem.content_sha256},
   135|)
   136|```
   137|
   138|### Delete
   139|
   140|```python
   141|client.beta.memory_stores.memories.delete(mem.id, memory_store_id=store.id)
   142|```
   143|
   144|Pass `expected_content_sha256` for a conditional delete.
   145|
   146|## Audit and rollback — memory versions
   147|
   148|Every mutation creates an immutable `memver_...` snapshot. Versions accumulate for the lifetime of the parent memory; `memories.retrieve` always returns the current head, the version endpoints give you history.
   149|
   150|| Operation that triggers it | `operation` field on the version |
   151|| --- | --- |
   152|| `memories.create` at a new path | `"created"` |
   153|| `memories.update` changing `content`, `path`, or both (or an agent-side write to the mount) | `"modified"` |
   154|| `memories.delete` | `"deleted"` |
   155|
   156|Each version also records `created_by` — an actor object with `type` ∈ `session_actor` / `api_actor` / `user_actor` — and, after redaction, `redacted_at` + `redacted_by`.
   157|
   158|### List versions
   159|
   160|Newest-first, paginated. Filter by `memory_id`, `operation`, `session_id`, `api_key_id`, or `created_at_gte` / `created_at_lte`. Pass `view="full"` to include `content`; default is metadata-only.
   161|
   162|```python
   163|for v in client.beta.memory_stores.memory_versions.list(store.id, memory_id=mem.id):
   164|    print(f"{v.id}: {v.operation}")
   165|```
   166|
   167|### Retrieve a version
   168|
   169|```python
   170|version = client.beta.memory_stores.memory_versions.retrieve(
   171|    version_id, memory_store_id=store.id
   172|)
   173|print(version.content)
   174|```
   175|
   176|### Redact a version
   177|
   178|Scrubs content from a historical version while preserving the audit trail (actor + timestamps). Clears `content`, `content_sha256`, `content_size_bytes`, and `path`; everything else stays. Use for leaked secrets, PII, or user-deletion requests.
   179|
   180|```python
   181|client.beta.memory_stores.memory_versions.redact(version_id, memory_store_id=store.id)
   182|```
   183|
   184|## Endpoint reference
   185|
   186|See `shared/managed-agents-api-reference.md` → Memory Stores / Memories / Memory Versions for the full HTTP method/path tables. Raw HTTP base path:
   187|
   188|```
   189|POST   /v1/memory_stores
   190|POST   /v1/memory_stores/{memory_store_id}/archive
   191|GET    /v1/memory_stores/{memory_store_id}/memories
   192|PATCH  /v1/memory_stores/{memory_store_id}/memories/{memory_id}
   193|GET    /v1/memory_stores/{memory_store_id}/memory_versions
   194|POST   /v1/memory_stores/{memory_store_id}/memory_versions/{version_id}/redact
   195|```
   196|
   197|For cURL examples and the CLI (`ant beta:memory-stores ...`), WebFetch the Memory URL in `shared/live-sources.md` → Managed Agents.
   198|