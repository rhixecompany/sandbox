# Validating a committed GitHub Actions YAML (local, no push needed)

When you add or edit a `.github/workflows/*.yml`, validate it locally before pushing so a
malformed workflow doesn't waste an Actions run. There is no build/test "suite" for a YAML
config — local parse + spec-conformance check is the right ad-hoc verification.

## The `on:` gotcha
PyYAML (the usual `python3 -c "import yaml; yaml.safe_load(...)"`) parses the bare YAML key
`on` as the boolean `True`. So `doc["on"]` raises `KeyError` and `doc.get("on")` returns
`None`. GitHub Actions itself is fine with `on:` — this is only a *local validator* quirk.

Read it defensively:
```python
doc = yaml.safe_load(open(".github/workflows/ci.yml"))
on_val = doc.get("on", doc.get(True))   # PyYAML maps bare 'on' -> True key
assert set(on_val) == {"push", "pull_request"}
```

## Minimal verification snippet
```python
import yaml
doc = yaml.safe_load(open(".github/workflows/ci.yml"))
on_val = doc.get("on", doc.get(True))
assert on_val is not None
assert set(on_val) == {"push", "pull_request"}, on_val
assert doc.get("name") == "CI"
jobs = doc["jobs"]; assert "build" in jobs
steps = jobs["build"]["steps"]
runs = [s.get("run") for s in steps if "run" in s]
assert "bun install" in runs
assert any("actions/checkout@v4" in s.get("uses", "") for s in steps)
assert any("oven-sh/setup-bun@v1" in s.get("uses", "") for s in steps)
print("YAML VALID + matches spec")
```
Run with `python3 verify_ci.py`. No PyYAML? `pip install pyyaml` or fall back to a `grep`/`regex`
check for the required `uses:`/`run:` lines.

## Note on real CI runs
A local parse proves syntax + structure only. A true green CI run requires pushing and waiting
for the Actions job — schedule that as part of the push step, not as local verification.
