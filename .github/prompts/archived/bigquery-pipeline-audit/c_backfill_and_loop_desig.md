# C) BACKFILL AND LOOP DESIGN

> Extracted from `bigquery-pipeline-audit.prompt.md`.

## C) BACKFILL AND LOOP DESIGN

**Hard fail if:** the script runs one BQ query per date or per entity in a loop.

Check that date-range backfills use one of:

1. A single set-based query with `GENERATE_DATE_ARRAY`
2. A staging table loaded with all dates then one join query
3. Explicit chunks with a hard `MAX_CHUNKS` cap

Also check:

- Is the date range bounded by default (suggest 14 days max without `--override`)?
- If the script crashes mid-run, is it safe to re-run without double-writing?
- For backdated simulations, verify data is read from time-consistent snapshots (`FOR SYSTEM_TIME AS OF`, partitioned as-of tables, or dated snapshot tables). Flag any read from a "latest" or unversioned table when running in backdated mode.

Suggest a concrete rewrite if the current approach is row-by-row.

---
