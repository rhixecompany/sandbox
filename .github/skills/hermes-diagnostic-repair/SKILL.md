---
name: hermes-diagnostic-repair
description: "Diagnose and repair Hermes platform health and fix its bugs."
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: [hermes, diagnostics, debugging, skills-hub, windows]
    related_skills: [hermes-platform-debugging, systematic-debugging, hermes-setup]
---

# Hermes Diagnostic & Repair Workflow

Full-platform health pass for the Hermes install. Proven on the 2026-08-11
battery: `hermes doctor && doctor --fix && security audit && status &&
insights && skills audit/check/update && logs list/errors/desktop/gateway/
gui/agent`, ending with a real code bug fixed (skills-hub perpetual-update
loop), targeted tests passing, and a clean report.

## When to use
- User invokes any `hermes *` diagnostic chain or asks to "fix all bugs,
  issues, warnings, errors" on the Hermes platform itself.
- Skills-hub "update available" loop that survives `hermes skills update`.
- Log triage across `errors.log` / `gateway.log` / `mcp-stderr.log`.

## Environment facts (Windows/MSYS)
- Install root: `$LOCALAPPDATA/hermes/hermes-agent` (git repo, branch `main`).
- Skills hub data: `$LOCALAPPDATA/hermes/skills/.hub/` (lock.json + quarantine/).
- Logs: `$LOCALAPPDATA/hermes/logs/`.
- Gateway state: `$LOCALAPPDATA/hermes/gateway_state.json`.
- `search_files` tool is UNRELIABLE for the install dir (returns 0 matches
  for real patterns) — use `terminal` grep/sed from the repo root instead.
- Invoking Python scripts with MSYS paths: prefix `MSYS_NO_PATHCONV=1` or
  `cd` into the repo first.
- Node MCP servers (github-mcp-server via docker `--memory 2Gb`) can OOM —
  Node "FATAL ERROR: AlignedAlloc/Zone Allocation failed" = V8 OOM, usually
  the constrained docker container, not current-session impact.

## Step 1 — Run the diagnostic battery (in order)
Execute exactly:
```bash
cd "$LOCALAPPDATA/hermes/hermes-agent"
hermes doctor; hermes doctor --fix; hermes security audit
hermes status; hermes insights
hermes skills audit; hermes skills check; hermes skills update
hermes logs list; hermes logs errors; hermes logs desktop
hermes logs gateway; hermes logs gui; hermes logs agent
```
Capture exit codes + key findings. Categorize every finding as one of:
1. **Real code bug** (fix it) — e.g. update/check hash loop, wrong output.
2. **Intentional guard** (do NOT "fix") — security-scan DANGEROUS/BLOCKED
   verdicts on community skills are policy, not errors.
3. **Transient external** (document, verify self-heal) — Telegram/Gemini
   network retry loops, DNS `getaddrinfo` failures, OOM'd MCP server.
4. **Config advisory** (report only) — unused platform integrations, OAuth
   not logged in, provider 403s.

## Step 2 — Root-cause before patching (probe-first)
Never guess. Write a small throwaway probe script under `tools/` comparing
the layers involved:
- A = lock.json `content_hash`, B = on-disk hash, C = fresh-fetch digest.
- Evidence pattern that pins the bug: A==B but A≠C means installed content
  matches lock; the *upstream/bundle digest computation* diverges.
- Isolate further: byte-diff fresh fetch vs installed files; feed both
  layers identical ordering to prove the divergence is sort order, not
  content.
Delete probe scripts after verification (prove cleanup with the file
search tool before claiming it).

## Step 3 — Skills-hub perpetual-update bug (known root causes)
Symptom: `hermes skills check` flags N skills, `hermes skills update`
reports success, but check still flags the same N.

Fix is in `tools/skills_hub.py`. Two distinct defects (fix BOTH):
1. **Sort-order asymmetry.** `bundle_content_hash` sorted by full-string
   normcase; the disk walker (`tools/skills_guard._content_digest`) sorts
   `Path` objects, which compare by *parts*. Diverges whenever a dir and a
   file share a prefix (e.g. a `references/styles` directory containing
   `blueprint.md` vs a sibling file `styles.md`). Correct key:
   ```python
   def _sort_key(path):
       return tuple(os.path.normcase(p) for p in path.replace("\\", "/").split("/"))
   ```
   `Path.relative_to()` yields backslashes on Windows — always
   `.as_posix()` identifiers too.
2. **CRLF write translation.** `quarantine_bundle` wrote `str`-typed bundle
   content with `write_text()` — default `newline=None` translates `\n`→`\r\n`
   on Windows. skills.sh/browse-sh bundles are `str` (LF); official bundles
   arrive as `bytes`. Installed file → CRLF, lock hash from disk, fresh fetch
   → LF → digest never matches → loop. Fix: encode to bytes and
   `write_bytes()` verbatim (or `write_text(..., newline="")`).

After patching: reinstall the skewed skills with `hermes skills update`,
verify A==B==C with the probe, then `hermes skills check` → expect
"0 update(s) available".

## Step 4 — Verify with the canonical runner
```bash
scripts/run_tests.sh tests/hermes_cli/test_skills_hub.py \
  tests/hermes_cli/test_skills_install_flags.py \
  tests/hermes_cli/test_skills_skip_confirm.py -q
# plus quarantine/install-path tests:
scripts/run_tests.sh tests/hermes_cli/test_managed_installs.py -q
```
Then full suite in background: `scripts/run_tests.sh -j 8` with
`notify_on_complete=true`. Also `python -m py_compile` the patched file.
Report test evidence (file → pass counts), not just "tests pass".

## Step 5 — Log triage methodology
- `hermes logs errors`: count ERROR lines, build an hourly histogram to find
  clusters; sample the actual lines. Most WILL be repeated network retry
  loops — classify before treating as bugs.
- Gateway reconnects: `gateway.log` shows escalation ladder
  (attempts + backoffs, fallback IPs, DoH fallback path). Verify current
  state in `gateway_state.json` (`telegram -> connected`).
- `tui_gateway_crash.log` + `mcp-stderr.log`: grep for
  `ERROR|Traceback|Exception|FATAL ERROR`.
- GUI event-loop stalls that coincide with CPU spikes (skills scan/update)
  are GIL pressure, not errors.

## Step 6 — Report classification
Lead with: what was a real bug (fixed + verified), what was intentional,
what was transient/external, what's advisory. Do not pad. Always attach
verification evidence (exit codes, test counts, CLI output).

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Hermes Diagnostic & Repair Workflow operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for Hermes Diagnostic & Repair Workflow.

### Phase 2: Execution

Run the primary Hermes Diagnostic & Repair Workflow operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
