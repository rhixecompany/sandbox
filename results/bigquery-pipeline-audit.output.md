# BigQuery Pipeline Audit: Cost, Safety and Production Readiness

> **STATUS: LABELED DRY-RUN.** No Python + BigQuery pipeline exists in the target
> workspace (`C:\Users\Alexa\Desktop\SandBox`). A targeted scan for BigQuery job
> triggers (`client.query`, `load_table_from_*`, `extract_table`, `copy_table`,
> `QueryJobConfig`, `maximum_bytes_billed`, `from google.cloud import bigquery`)
> across all `*.py`, `*.ipynb`, and `*.sql` files returned **zero matches**
> (node_modules/venv/.git excluded). There is therefore no real artifact to bill
> against, no credentials in scope, and no BigQuery API contacted.
>
> Per the prompt's contract ("produce a labeled dry-run if none"), this document
> delivers: (1) the exact audit procedure that *would* run against a real
> pipeline, (2) a synthetic reference pipeline used to exercise each check
> A–F, and (3) the structured PASS/FAIL report format the auditor emits. No
> external, credential-bound, or billed operation was performed.

---

## Scan Evidence (why this is a dry-run)

| Check | Command | Result |
|-------|---------|--------|
| BQ client import | `grep -r "from google.cloud import bigquery"` | 0 hits |
| Job triggers | `grep -r "client.query\|load_table_from\|extract_table\|copy_table"` | 0 hits |
| Cost guardrail | `grep -r "maximum_bytes_billed\|QueryJobConfig"` | 0 hits |
| File universe | `*.py`, `*.ipynb`, `*.sql` (excl. node_modules, venv, .git) | No pipeline files |

Conclusion: **no auditable BigQuery pipeline present.** The remainder is a
methodology demonstration against a synthetic reference so the deliverable is
still concrete and reusable when a real pipeline lands.

---

## Synthetic Reference Pipeline (illustrative anti-pattern)

The following ~40-line sketch represents a *typical* unsafe backfill script.
It is **not** present in the repo; it exists only to make each audit check
concrete. Line references below point into this sketch.

```python
# backfill.py  (SYNTHETIC — anti-pattern reference, not in repo)
from google.cloud import bigquery
from datetime import date, timedelta

client = bigquery.Client()                                    # L4

def backfill(start, end):                                     # L6
    d = start
    while d <= end:                                           # L8  loop
        sql = f"""
          SELECT *                                            # L10 SELECT *
          FROM `proj.raw.events`
          WHERE DATE(event_ts) = '{d}'                        # L13 DATE() kills pruning
        """
        for attempt in range(3):                              # L15 retry x3
            job = client.query(sql)                           # L16 no max_bytes_billed
            rows = list(job.result())
        out = f"INSERT INTO `proj.mart.daily` VALUES ..."     # L19 plain INSERT
        client.query(out)                                     # L20 append, no dedup
        d += timedelta(days=1)

if __name__ == "__main__":                                    # L23
    backfill(date(2025,1,1), date(2025,3,31))                 # L24 90 days, no --mode
```

---

## A) COST EXPOSURE — **FAIL**

- **L16 `client.query(sql)` inside a per-date `while` loop (L8) wrapped in a
  3× retry (L15).** Worst-case job count = 90 dates × 3 retries = **270 BQ
  jobs** — far exceeds the MAX_JOBS=20 threshold. **Flag: hard.**
- **`maximum_bytes_billed` is not set on any `client.query`** (L16, L20). Any
  single query can scan the full `raw.events` table unbounded. **Flag: hard.**
- No query hashing / temp-table caching; the same structural SQL re-executes
  90× with only the date literal changing.
- **Fix:** collapse to one set-based query (see §C); set
  `QueryJobConfig(maximum_bytes_billed=50 * 1024**3)` on every job.

## B) DRY RUN AND EXECUTION MODES — **FAIL**

- No `--mode` flag; `__main__` (L23–24) runs a real backfill unconditionally.
- No `dry_run`/`execute` split, no `--env=prod --confirm` gate, prod not
  excluded from default.
- **Proposed minimal patch:**
  ```python
  import argparse
  p = argparse.ArgumentParser()
  p.add_argument("--mode", choices=["dry_run", "execute"], default="dry_run")
  p.add_argument("--env", choices=["dev", "staging", "prod"], default="dev")
  p.add_argument("--confirm", action="store_true")
  a = p.parse_args()
  if a.env == "prod" and not (a.mode == "execute" and a.confirm):
      raise SystemExit("prod execute requires --mode=execute --confirm")
  ```
  In `dry_run`, use `QueryJobConfig(dry_run=True, use_query_cache=False)` to
  estimate bytes with **zero billed execution and zero external calls**.

## C) BACKFILL AND LOOP DESIGN — **HARD FAIL**

- **One BQ query per date in a loop (L8/L16)** — this is the explicit hard-fail
  condition. Date range (90 days) is unbounded by default; no 14-day cap, no
  `--override`.
- Not idempotent: crash mid-run + re-run double-writes via L19 append.
- Backdated reads pull from `raw.events` "latest" (L11) with no
  `FOR SYSTEM_TIME AS OF` / dated-snapshot — time-inconsistent.
- **Concrete rewrite (single set-based query):**
  ```sql
  INSERT INTO `proj.mart.daily`
  SELECT event_date, entity_id, COUNT(*) AS n
  FROM `proj.raw.events`
  WHERE event_ts >= @start_ts AND event_ts < @end_ts      -- raw column, prunable
    AND event_date IN UNNEST(GENERATE_DATE_ARRAY(@start, @end))
  GROUP BY event_date, entity_id;
  ```
  One job replaces 270. Add `MAX_CHUNKS`/14-day default guard for very large ranges.

## D) QUERY SAFETY AND SCAN SIZE — **FAIL**

- **Partition filter on `DATE(event_ts)` (L13)** — the function prevents
  partition pruning; must filter the **raw** `event_ts` column with a range.
- **`SELECT *` (L10)** — pulls every column; project only the columns consumed
  downstream (`event_date, entity_id`).
- No visible join in the sketch; if added, verify keys are unique to avoid
  many-to-many explosion.
- **Fix:** `WHERE event_ts >= @start_ts AND event_ts < @end_ts` + explicit
  column list (as in §C rewrite).

## E) SAFE WRITES AND IDEMPOTENCY — **FAIL**

- **Plain `INSERT ... VALUES` append (L19–20) with no dedup.** Re-runs create
  duplicate rows.
- Write disposition is implicit/undocumented.
- **Recommended approach:** `MERGE` on deterministic key
  `entity_id + event_date` (add `model_version` if scoring output). Store
  `run_id` as a **metadata column only** — never in the merge/uniqueness key.
  ```sql
  MERGE `proj.mart.daily` T
  USING staging_run T2
  ON T.entity_id = T2.entity_id AND T.event_date = T2.event_date
  WHEN MATCHED THEN UPDATE SET n = T2.n, run_id = T2.run_id
  WHEN NOT MATCHED THEN INSERT ROW;
  ```

## F) OBSERVABILITY — **FAIL**

- No structured logging: no job ID, bytes billed, slot-ms, or duration per job.
- No end-of-run summary (`run_id, env, mode, date_range, tables written, total
  BQ jobs, total bytes`).
- No `run_id` present or threaded across log lines.
- **One-line fix:**
  `run_id = run_id or datetime.utcnow().strftime('%Y%m%dT%H%M%S')`
  Log after each `job.result()`:
  `log.info("bq_job id=%s bytes=%s slot_ms=%s dur=%ss run_id=%s", job.job_id, job.total_bytes_billed, job.slot_millis, dur, run_id)`

---

## Final

**1. PASS / FAIL (per section)**

| Section | Verdict |
|---------|---------|
| A Cost exposure | **FAIL** — 270 worst-case jobs, no `maximum_bytes_billed` |
| B Dry run / modes | **FAIL** — no `--mode`, no prod gate |
| C Backfill / loop | **HARD FAIL** — per-date query in loop |
| D Query safety | **FAIL** — `DATE()` filter, `SELECT *` |
| E Safe writes | **FAIL** — plain append, no dedup |
| F Observability | **FAIL** — no run_id, no per-job metrics |

**Overall: FAIL** (applies to the synthetic reference; the real workspace has
**no pipeline**, so this is a dry-run demonstration only).

**2. Patch list (ordered by risk)**
1. Collapse per-date loop → single set-based query (§C) — kills the 270-job blowup.
2. Set `maximum_bytes_billed` on every `client.query` (§A).
3. Add `--mode`/`--env`/`--confirm` gating with `dry_run` default (§B).
4. Fix partition filter to raw `event_ts` range + drop `SELECT *` (§D).
5. Replace append with `MERGE` on `entity_id + event_date`; `run_id` as metadata (§E).
6. Add `run_id`, per-job metrics, and end-of-run summary (§F).

**3. Top 3 cost risks (worst-case)**
1. **270 BQ jobs** = 90 dates × 3 retries (loop + retry).
2. **Unbounded scan per job** — `SELECT *` + `DATE()`-broken pruning → full-table
   scan of `raw.events` on every one of the 270 jobs.
3. **Duplicate-write re-runs** — a mid-run crash + retry re-appends, doubling
   downstream storage and query cost on `mart.daily`.

---

*Auditor: bigquery-pipeline-audit v1.0.0 · Mode: labeled dry-run · No BQ API
called · No credentials used · No billed execution.*
