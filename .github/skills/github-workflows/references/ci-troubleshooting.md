# CI Troubleshooting Quick Reference

Common CI failure patterns and how to diagnose them from the logs.

## Reading CI Logs

```bash
# With gh
gh run view <RUN_ID> --log-failed

# With curl — download and extract
curl -sL -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$GH_OWNER/$GH_REPO/actions/runs/<RUN_ID>/logs \
  -o /tmp/ci-logs.zip && unzip -o /tmp/ci-logs.zip -d /tmp/ci-logs
```

## Common Failure Patterns

### Test Failures

**Signatures in logs:**
```
FAILED tests/test_foo.py::test_bar - AssertionError
E       assert 42 == 43
ERROR tests/test_foo.py - ModuleNotFoundError
```

**Diagnosis:** find the test file/line from the traceback; `read_file` the
failing test; check logic error vs stale assertion; `ModuleNotFoundError` is
usually a missing CI dependency.

**Fixes:** update assertion; add missing dependency to requirements/pyproject;
fix flaky test (retry, mock external service, fix race).

### Lint / Formatting Failures

**Signatures:** `src/auth.py:45:1: E302 expected 2 blank lines`, `E501 line too long`.

**Diagnosis:** read the file:line; check which linter (flake8, ruff, black, isort, mypy).

**Fixes:** run formatter locally (`black .`, `isort .`, `ruff check --fix .`); fix the violation.

### Type Check Failures (mypy / pyright)

**Signatures:** `src/api.py:23: error: Argument 1 to "process" has incompatible type "str"; expected "int"`.

**Fixes:** add cast/conversion; fix signature; `# type: ignore` as last resort (with explanation).

### Build / Compilation Failures

**Signatures:** `ModuleNotFoundError: No module named 'some_package'`, `npm ERR! Could not resolve dependency`.

**Fixes:** add missing dependency; pin compatible version; update lockfile.

### Permission / Auth Failures

**Signatures:** `fatal: could not read Username for 'https://github.com'`, `Error: Resource not accessible by integration`, `403 Forbidden`.

**Fixes:** add `permissions:` block to workflow YAML; verify secrets exist
(`gh secret list`); fork PRs don't get some secrets by design.

### Timeout Failures

**Signatures:** `Error: The operation was canceled.`, `exceeded the maximum execution time`.

**Fixes:** add `timeout-minutes: 10` to the step; fix the perf issue; split into parallel jobs.

### Docker / Container Failures

**Signatures:** `docker: Error response from daemon`, `COPY failed: file not found in build context`.

**Fixes:** fix path in COPY/ADD; update base image tag; fix `.dockerignore`.

## Auto-Fix Decision Tree

```
CI Failed
├── Test failure → update test or fix logic / add dependency
├── Lint failure → run formatter, fix style
├── Type error → fix types
├── Build failure → add dep / update pins
├── Permission error → update workflow permissions (needs user)
└── Timeout → investigate perf (may need user input)
```

## Re-running After Fix

```bash
git add <fixed_files> && git commit -m "fix: resolve CI failure" && git push
gh pr checks --watch
```
