# Testing Hermes Hooks End-to-End (verified 2026-08-11)

Realistic-payload harness for the live shell hooks
(`session-logger`, `governance-audit`, `session-auto-commit` under
`%LOCALAPPDATA%/hermes/hooks/`). Proven in the session that implemented
full session-end capture.

## The wire shape (what the runtime ACTUALLY sends)

```json
{"hook_event_name":"on_session_end","session_id":"<SID>","cwd":"C:/Users/Alexa/Desktop/SandBox",
 "extra":{"session_id":"<SID>","model":"deepseek-v4-flash-free","platform":"cli",
          "completed":true,"failed":false,"interrupted":false,
          "turn_exit_reason":"text_response(finish_reason=stop)"}}
```

- `turn_exit_reason` is a STRINGIFIED TurnResponse REPR in production
  (`text_response(finish_reason=stop)`, `agent_error(exception=...)`,
  `interrupted(user_interrupt)`) — NOT the bare token `"completed"` shown in
  older docs/fixtures. Hooks must route it through `lib.normalize_status()`
  (-> `completed`/`failed`/`interrupted`/`truncated`) before storing; never
  persist the raw repr. See
  `hook-end-status-normalization.md` for the full value map.

- `on_session_end` never sends `duration_ms`, `turns`, `tokens_*`, `status`,
  or `exit_code`. Hooks derive them: status from `extra.turn_exit_reason` /
  `extra.completed|failed|interrupted`; duration from the session_start record
  timestamp in the SAME JSONL; turns = count of `pre_llm_call` rows.
- Each hook derives from ITS OWN log store: session-logger reads
  `logs/sessions/<id>.jsonl`; governance-audit reads
  `logs/hermes/governance/<id>.jsonl`. Seed whichever store you are testing.

## Synthetic-id guard (added 2026-08-11)

All three hooks skip payloads whose `session_id` is empty, `unknown`, or
starts with `test`/`e2e-` (guard in each `hook.py` main(), before dispatch;
writes a skip record to the hook's `*-skips.jsonl`). Consequences:

- `hermes hooks doctor` fires hooks with `session_id=test-session` → hooks
  skip and exit 0. This is by design — it prevents junk commits and log
  pollution from verification runs.
- Manual test payloads MUST use a real-looking id (e.g.
  `20260811_183728_b92b2f`) to exercise the write/commit paths.
  `"session_id":"test"` will silently skip and write nothing.

## Junk-commit recovery (why the guards exist)

Before the guards, any fake-id fire made `session-auto-commit` commit a dirty
tree under `chore(session): auto-commit session test-session at <ts>`. If you
hit this:

```bash
git log --oneline -1                                   # find the junk commit
SID=$(python -c "import sqlite3,os; c=sqlite3.connect(os.path.expandvars(r'%LOCALAPPDATA%/hermes/state.db')); print(c.execute('SELECT id FROM sessions ORDER BY started_at DESC LIMIT 1').fetchone()[0])")
git commit --amend -m "chore(session): auto-commit session $SID at <ts>"
```

## End-to-end harness (session end capture)

```bash
HOOKS="$LOCALAPPDATA/hermes/hooks"; LOGS="$LOCALAPPDATA/hermes/logs/sessions"
SID="e2e-end-$(date +%s)"

# 1) Seed the store so derivation has inputs (start 125s ago + 2 turns)
python - "$SID" "$LOGS" <<'EOF'
import json, sys, datetime, pathlib
sid, logs = sys.argv[1], pathlib.Path(sys.argv[2])
now = datetime.datetime.now(datetime.timezone.utc)
recs = [
  {"event":"session_start","session_id":sid,"timestamp":(now-datetime.timedelta(seconds=125)).strftime("%Y-%m-%dT%H:%M:%SZ"),"profile":"default","user":"Alexa","model":"deepseek-v4-flash-free","provider":"opencode-zen","platform":"cli","working_dir":"C:/Users/Alexa/Desktop/SandBox"},
  {"event":"pre_llm_call","session_id":sid,"timestamp":(now-datetime.timedelta(seconds=100)).strftime("%Y-%m-%dT%H:%M:%SZ"),"model":"deepseek-v4-flash-free","prompt_length":25},
  {"event":"pre_llm_call","session_id":sid,"timestamp":(now-datetime.timedelta(seconds=40)).strftime("%Y-%m-%dT%H:%M:%SZ"),"model":"deepseek-v4-flash-free","prompt_length":30},
]
(logs/f"{sid}.jsonl").write_text("".join(json.dumps(r,separators=(",",":"))+"\n" for r in recs), encoding="utf-8")
EOF

# 2) Fire realistic payload through the live wrapper (stdin → hook.sh → hook.py)
cat payload.json | bash "$HOOKS/session-logger/hook.sh"
cat payload.json | bash "$HOOKS/governance-audit/hook.sh"

# 3) Verify derived fields
grep '"event":"session_end"' "$LOGS/$SID.jsonl" | tail -1
# Expect: status=completed, duration≈125s, turns=2, user/model/provider
# resolved, git_branch/git_sha/git_dirty from cwd.
```

### Auto-commit test (prove envelope-cwd resolution)

```bash
SCRATCH="C:/Users/Alexa/AppData/Local/Temp/e2e-ac-test"
git init -q -b development "$SCRATCH" && git -C "$SCRATCH" config user.email t@e.com && git -C "$SCRATCH" config user.name T
echo x > "$SCRATCH/f.txt" && git -C "$SCRATCH" add . && git -C "$SCRATCH" commit -qm init
echo dirty >> "$SCRATCH/f.txt"
# Fire from a DIFFERENT cwd (cd /tmp) with payload cwd=scratch → commit must
# land in scratch, proving the hook used the envelope cwd, not its own.
# Payload cwd MUST be a Windows path (C:/Users/.../Temp/...); Path('/tmp/...')
# does not resolve under Windows Python.
```

## Cleanup + verification

```bash
rm -f "$LOGS"/e2e-*.jsonl "$LOCALAPPDATA/hermes/logs/hermes/governance"/e2e-*.jsonl
rm -rf "$LOCALAPPDATA/Temp/e2e-ac-test" /tmp/e2e-end-*.json
find <mirror> -name __pycache__ -type d -exec rm -rf {} +   # keep mirror pyc-free
python -m py_compile lib.py <hook-dir>/hook.py              # live AND mirror
hermes hooks doctor                                         # must stay healthy
```

## Gotchas

- `ls | grep e2e` false-positives on REAL session ids containing `e2e` as hex
  (e.g. `20260808_140016_85e2e4`). Use anchored `^(test|e2e)` patterns.
- `hermes hooks doctor` fires the hooks during verification → expect skip
  records in `*-skips.jsonl` afterward; that is the guard working, not a bug.
- Mirror-sync rule: copy live hook files to `.github/hooks/` and re-run
  `py_compile` there; the session-auto-commit hook picks the mirror up at
  session end (with the real session id once guards are in place).
