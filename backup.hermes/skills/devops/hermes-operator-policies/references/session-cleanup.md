# Session Cleanup & DB Reclamation

## Quick Reference

```bash
# Delete all sessions older than N days (0 = all inactive)
hermes sessions prune --older-than 0 --yes

# Delete specific session by ID
hermes sessions delete <session_id> --yes

# Delete all sessions except the current one (paginated list loop)
hermes sessions list | grep -oP '\d{8}_\d{6}_[a-f0-9]+' | while read sid; do
  [ "$sid" != "$CURRENT_SESSION_ID" ] && hermes sessions delete "$sid" --yes
done

# Check stats before/after
hermes sessions stats
```

## Disk Space Reclamation

Deleting sessions via `hermes sessions` removes records from SQLite but does **not** reclaim disk space. The WAL (Write-Ahead Log) file and the main DB file both retain freed pages.

### Full cleanup procedure

1. **Stop the gateway** (it holds an open DB connection):
   ```bash
   hermes gateway stop
   # Or kill the background process via process(action='kill', session_id='...')
   ```

2. **Vacuum the database** to compact the main file:
   ```python
   import sqlite3, os
   db = 'C:/Users/Alexa/AppData/Local/hermes/state.db'
   con = sqlite3.connect(db)
   con.execute('VACUUM;')
   con.close()
   ```

3. **Checkpoint and truncate the WAL** (can be done while DB is in use):
   ```python
   import sqlite3, os
   db = 'C:/Users/Alexa/AppData/Local/hermes/state.db'
   con = sqlite3.connect(db)
   # Truncate checkpoint flushes WAL into DB and truncates it
   con.execute('PRAGMA wal_checkpoint(TRUNCATE);')
   con.close()
   ```

4. **Restart the gateway**:
   ```bash
   hermes gateway run
   ```

### Expected space savings

| Scenario | Before | After | Savings |
|----------|--------|-------|---------|
| 170 sessions → 1 session (no VACUUM) | 139.6 MB | 139.6 MB | 0% |
| After VACUUM | 139.6 MB | 69.7 MB | ~50% |
| After WAL truncation | 71 MB WAL | 0 KB WAL | +50% of freed pages |

## Pitfalls

- **`hermes sessions list` paginates at 20 results.** Multiple passes may be needed when deleting all sessions except the current one — deleted sessions shift the page boundary.
- **VACUUM requires exclusive access.** Fails with `database is locked` if any Hermes session or gateway currently has the DB open. Stop the gateway first.
- **WAL truncation with `PRAGMA wal_checkpoint(TRUNCATE)`** can run while the session is active (passive checkpoint mode). Use `TRUNCATE` (mode 1) over `PASSIVE` (mode 0) for full reclamation.
- **DB size may still be >50 MB with 1 session** because FTS5 indexes and conversation history (including tool output) grow with each session. This is normal.
