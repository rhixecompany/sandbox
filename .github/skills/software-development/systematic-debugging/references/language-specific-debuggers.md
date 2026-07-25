# Debugger Tooling

Companion class-level skill for language-specific debuggers that complement the generic root-cause
methodology in `systematic-debugging`. Use the Python section when debugging Python code (Hermes
gateway, TUI workers, tests), and the Node.js section when debugging Ink/TypeScript UI, tui_gateway
child processes, or Node scripts. Quick-reference cheat-sheets live under `references/`.

## When to Use

- A Python test fails and `pytest -vv --tb=long` doesn't reveal why
- A long-lived Python process (gateway, tui_gateway, daemon) misbehaves
- You need to inspect a value in a closure, generator, or async coroutine
- A Node/Ink component crashes or renders incorrectly
- You want CPU/heap profiles from a running Node process
- Remote attach to a containerized or SSH-host process

**Don't use for:** things `print()` / `logging.debug()` solve in under a minute, or things `pytest -vv --tb=long --showlocals` already reveals. For generic root-cause methodology, use `systematic-debugging`.

---

## 1. Python Debugging (pdb + debugpy)

Three tools, picked by situation:

| Tool | When |
|---|---|
| `breakpoint()` + pdb | Local, interactive, simplest. |
| `python -m pdb` | Launch under pdb with no source edits. |
| `debugpy` | Remote / headless / attach to already-running process. |

**Start with `breakpoint()`.** It's the cheapest thing that works.

### pdb Quick Reference

Inside any pdb prompt (`(Pdb)`):

| Command | Action |
|---|---|
| `n` / `next` | next line (step over) |
| `s` / `step` | step into |
| `r` / `return` | return from current function |
| `c` / `cont` | continue |
| `unt N` | continue until line N |
| `j N` | jump to line N (same function only) |
| `b file:line` | set breakpoint |
| `cl N` | clear breakpoint N |
| `!stmt` | execute arbitrary Python |
| `interact` | full Python REPL (Ctrl+D to exit) |

Common patterns:
```python
def compute(x, y):
    result = some_helper(x)
    breakpoint()           # drops into pdb here
    return result + y
```

```bash
python -m pdb path/to/script.py arg1
# or:
python -m pdb -c continue script.py   # post-mortem on crash
```

### Recipe: Post-mortem on any exception
```python
import pdb, sys
try:
    run_the_thing()
except Exception:
    pdb.post_mortem(sys.exc_info()[2])
```

### Remote Debugging with debugpy

**Pattern A: Source-edit — process waits for debugger**
```python
import debugpy
debugpy.listen(("127.0.0.1", 5678))
debugpy.wait_for_client()
debugpy.breakpoint()       # optional: pause immediately
```

**Pattern B: No source edit — launch with `-m debugpy`**
```bash
python -m debugpy --listen 127.0.0.1:5678 --wait-for-client your_script.py
```

**Pattern C: Attach to an already-running process**
```bash
python -m debugpy --listen 127.0.0.1:5678 --pid <pid>
```

### Connecting a Client

**Option 1: VS Code / Cursor — add a `launch.json`:**
```json
{"name": "Attach", "type": "debugpy", "request": "attach",
 "connect": {"host": "127.0.0.1", "port": 5678}, "justMyCode": false}
```

**Option 2: `remote-pdb` — terminal-only, agent-friendly:**
```python
from remote_pdb import set_trace
set_trace(host="127.0.0.1", port=4444)
# Then: nc 127.0.0.1 4444
```

### Debugging Hermes-Specific Processes

| Target | Easiest Approach |
|---|---|
| Tests | `pytest tests/foo.py --pdb -p no:xdist` |
| `run_agent.py` / CLI | Add `breakpoint()` near suspect line, run normally |
| `tui_gateway` | `remote-pdb` at a handler entry |
| `_SlashWorker` | `remote-pdb` inside worker's `exec` path |

### Common Python Debugging Pitfalls

1. **pdb under pytest-xdist silently does nothing.** Always use `-p no:xdist` or `-n 0`.
2. **`breakpoint()` in CI / non-TTY contexts hangs.** Safe locally; never commit it.
3. **`PYTHONBREAKPOINT=0` disables `breakpoint()`.** Check `echo $PYTHONBREAKPOINT`.
4. **`debugpy.listen` blocks only if you also call `wait_for_client()`.** Without it, execution continues.
5. **Attach to PID fails on hardened kernels.** `ptrace_scope=1` (Ubuntu default) blocks non-child injection.
6. **Threads.** pdb only debugs the current thread; use debugpy for thread-aware DAP.
7. **asyncio.** pdb works in coroutines but `await` inside pdb requires Python 3.13+ on `await` from `interact` mode on older versions. For 3.11/3.12, use `asyncio.ensure_future` tricks or `!stmt`-based awaits.
8. **Forking / multiprocessing.** pdb does not follow forks. Each child needs its own `breakpoint()`.
9. **`scripts/run_tests.sh` strips credentials.** Bugs depending on real API keys won't reproduce under the wrapper — debug with raw `pytest` first.

---

## 2. Node.js Debugging (node inspect + Chrome DevTools Protocol)

Two tools, pick one:

- **`node inspect`** — built-in, zero-install, CLI REPL. Best for quick poking.
- **CDP via `chrome-remote-interface`** — scriptable from Node/Python; best when you want automation, many breakpoints, or non-interactive debugging from an agent loop.

**Prefer `node inspect` first.** It's always available and the REPL is fast.

### Quick Reference: `node inspect` REPL

Launch paused on first line:
```bash
node inspect path/to/script.js
# or with tsx:
node --inspect-brk $(which tsx) path/to/script.ts
```

The `debug>` prompt accepts:

| Command | Action |
|---|---|
| `c` / `cont` | continue |
| `n` / `next` | step over |
| `s` / `step` | step into |
| `o` / `out` | step out |
| `sb('file.js', 42)` | set breakpoint |
| `bt` | backtrace (call stack) |
| `repl` | REPL in current scope (Ctrl+C to exit) |
| `kill` | kill the script |

### Attaching to a Running Process

```bash
# 1. Enable inspector on existing process
kill -SIGUSR1 <pid>

# 2. Attach the debugger CLI
node inspect -p <pid>
# or by URL
node inspect ws://127.0.0.1:9229/<uuid>
```

To start a process with the inspector from the beginning:
```bash
node --inspect script.js           # listen on 127.0.0.1:9229, keep running
node --inspect-brk script.js       # listen AND pause on first line
node --inspect=0.0.0.0:9230 script.js   # custom host:port
```

### Programmatic CDP (scripting from terminal)

When you want to automate — set many breakpoints, capture scope state, script a repro:
```bash
npm i -g chrome-remote-interface
node --inspect-brk=9229 target.js &
```

Driver pattern (save as `/tmp/cdp-debug.js`):
```javascript
const CDP = require('chrome-remote-interface');
const client = await CDP({ port: 9229 });
const { Debugger, Runtime } = client;
// set breakpoints, inspect scopes, evaluate expressions, resume
```

### Debugging Hermes ui-tui

- **Single Ink component:** `node inspect` with built dist, set breakpoints in `dist/app.js`.
- **Running `hermes --tui`:** find TUI PID, `kill -SIGUSR1`, attach via `node inspect -p <pid>`.
- **`_SlashWorker` / PTY child processes:** these are Python, not Node — use the Python section instead.

### Node.js Debugging Pitfalls

1. **Wrong line numbers in TS source.** Breakpoints hit the emitted JS, not the `.ts`. Either break in `dist/*.js`, or enable sourcemaps.
2. **`--inspect` vs `--inspect-brk`.** `--inspect` starts but doesn't pause — the script may race past your first breakpoint. Use `--inspect-brk` when you need to set breakpoints before any code runs.
3. **Port collisions.** Default `9229`. If multiple Node processes inspect, pass `--inspect=0` (random port) and read the actual URL from `/json/list`.
4. **Child processes.** `--inspect` on a parent does NOT inspect children. Use `NODE_OPTIONS='--inspect-brk'` to propagate.
5. **Running `node inspect` through an agent terminal.** It's a PTY-friendly REPL. Launch with `terminal(pty=true)` or `background=true` + `process(action='submit', ...)`.
6. **Security.** `--inspect=0.0.0.0:9229` exposes arbitrary code execution. Always bind to `127.0.0.1`.

---

## See Also

- `systematic-debugging` — 4-phase root-cause methodology that governs when to reach for these tools
