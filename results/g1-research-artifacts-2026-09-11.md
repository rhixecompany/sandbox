# G1 Evidence — Research Artifacts (2026-09-11)

**Status: PASS** · Gate: 11/11 scripts tested green, hook OK, requirements.txt valid.

## Delivered

| Artifact         | Count                                   | Path                               |
| ---------------- | --------------------------------------- | ---------------------------------- |
| Topic skills     | 11                                      | `skills/research-{topic}/SKILL.md` |
| Digest scripts   | 12 (11 topics + update_requirements.py) | `scripts/research_*.py`            |
| Tests            | 55 assertions (11 classes × 5)          | `scripts/tests/test_research_*.py` |
| Hook             | 1                                       | `hooks/research-check.sh`          |
| requirements.txt | 275 packages (was 210)                  | `requirements.txt`                 |

## Verification Evidence

- `python -m unittest discover -s scripts/tests` → **Ran 55 tests OK** (10.7s)
- `bash hooks/research-check.sh` → exit 0, "OK: all research topics have md + skill + script + test"
- `uv pip check --python .venv/Scripts/python.exe` → "All installed packages are compatible" (exit 0)
- requirements.txt union: installed (1 editable root via uv freeze) + Unique Package Index (274)

## Debugging Log (trace before fix)

1. `research_common.py` SyntaxError (missing paren in `list_root_files`) → fixed line 39.
2. Test suite 22/110 failures: base `ResearchScriptTestCase` was collected by unittest itself and ran with empty `script_name` → subprocess invoked the `scripts/` _directory_ ("can't find '**main**' module"). Fixed at the class level: shared base became a `make_research_tests()` factory — no collectable TestCase at module level → 55 tests, 0 failures.
3. Hook slug bug: derived script names without `research_` prefix → prefixed in hook loop.

## Open Item (documented, not fabricated)

`python-packages.md` Unique Package Index references **274 cheat-sheets** under `research/packages/python/*.md` — directory does not exist yet. Generating 274 web-researched cheat-sheets is a follow-up batch (web-research-pipeline per package), not part of the approved 11-topic scope. Script `scripts/update_requirements.py` reports the missing paths at each run.

## Files Touched

- scripts/: research_common.py, research_{10 topics}.py, research_uk_earning_sites.py, update_requirements.py, tests/{research_test_common.py, test_research_*.py ×11}
- skills/: research-{11 topics}/SKILL.md
- hooks/: research-check.sh
- requirements.txt (regenerated)
