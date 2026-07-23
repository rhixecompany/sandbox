# A) COST EXPOSURE: What will actually get billed?

> Extracted from `bigquery-pipeline-audit.prompt.md`.

## A) COST EXPOSURE: What will actually get billed?

Locate every BigQuery job trigger (`client.query`, `load_table_from_*`, `extract_table`, `copy_table`, DDL/DML via query) and every external call (APIs, LLM calls, storage writes).

For each, answer:

- Is this inside a loop, retry block, or async gather?
- What is the realistic worst-case call count?
- For each `client.query`, is `QueryJobConfig.maximum_bytes_billed` set? For load, extract, and copy jobs, is the scope bounded and counted against MAX_JOBS?
- Is the same SQL and params being executed more than once in a single run? Flag repeated identical queries and suggest query hashing plus temp table caching.

**Flag immediately if:**

- Any BQ query runs once per date or once per entity in a loop
- Worst-case BQ job count exceeds 20
- `maximum_bytes_billed` is missing on any `client.query` call

---
