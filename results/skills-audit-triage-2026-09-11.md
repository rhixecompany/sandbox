# Skills Audit Triage — 2026-09-11

Command: `hermes skills audit` → 30 skills scanned, 27 ALLOWED, 1 BLOCKED (drawio-skill, community, caution verdict, 40 MEDIUM findings).
Zero HIGH/CRITICAL findings across all skills.

## Triage of the 40 MEDIUM findings (all in drawio-skill scripts)

| Category | Count | Verdict | Evidence |
|---|---|---|---|
| execution (`subprocess.run([...])`) | 33 | ✅ BENIGN — list-arg form, no `shell=True`, no string interpolation into shell | pyimports.py:97, raster2drawio.py:140, svgflow.py:38, timelapse.py:46-108, tfimports.py:184, rustimports.py:150 |
| obfuscation (binary bytes) | 3 | ✅ BENIGN — PNG chunk magic constants (`IEND`, `\xaeB\x82`) | repair_png.py:17,25 |
| supply_chain (`pip install` mentions) | 2 | ✅ BENIGN — documentation of install commands, not executed | ATTRIBUTION.md:31, SKILL.md:202 |
| network (curl localhost / ws://127.0.0.1) | 2 | ✅ BENIGN — tool docs referencing local services | neuroskill-bci references/api.md (separate skill, still ALLOWED) |

## Decision

All 40 findings are heuristic lints on safe patterns. No code changes applied to community skills (would be reverted by updates; not ours to maintain). Verdict: **documented false-positive class, not a security debt**.

## Follow-up

- `hermes skills update` run to refresh the 7 available updates (per plan TASK-017).
- Orphaned lock entries (openhands, youtube-full) handled via `hermes skills uninstall` if present as stale lock entries.
- Re-audit after updates to confirm no new HIGH findings.