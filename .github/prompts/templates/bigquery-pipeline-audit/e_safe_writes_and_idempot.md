# E) SAFE WRITES AND IDEMPOTENCY

> Extracted from `bigquery-pipeline-audit.prompt.md`.

## E) SAFE WRITES AND IDEMPOTENCY

Identify every write operation. Flag plain `INSERT`/append with no dedup logic.

Each write should use one of:

1. `MERGE` on a deterministic key (e.g., `entity_id + date + model_version`)
2. Write to a staging table scoped to the run, then swap or merge into final
3. Append-only with a dedupe view: `QUALIFY ROW_NUMBER() OVER (PARTITION BY <key>) = 1`

Also check:

- Will a re-run create duplicate rows?
- Is the write disposition (`WRITE_TRUNCATE` vs `WRITE_APPEND`) intentional and documented?
- Is `run_id` being used as part of the merge or dedupe key? If so, flag it. `run_id` should be stored as a metadata column, not as part of the uniqueness key, unless you explicitly want multi-run history.

State the recommended approach and the exact dedup key for this codebase.

---
