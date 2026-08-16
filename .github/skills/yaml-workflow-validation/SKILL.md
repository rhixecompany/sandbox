---
name: yaml-workflow-validation
title: "YAML & GitHub Actions Workflow Validation"
description: "Use when auditing, fixing, validating, or enhancing .yml/.yaml files and GitHub Actions workflows. Covers yamllint config, line-ending normalization, CI validation for workflows."
category: devops
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [yaml, github-actions, validation, linting, ci]
---
# YAML & Workflow Validation

## Overview

Automated reasoning and workflow tool for `yaml-workflow-validation`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use
- Auditing/fixing `.yml`/`.yaml` files for issues (CRLF, trailing spaces, missing EOF newline)
- Validating GitHub Actions workflows before PR
- Adding YAML validation to CI pipeline
- Creating `.yamllint.yaml` config or `.gitattributes` for line-ending normalization

## Tools
- `yamllint` — YAML linter (install: `pip install yamllint`)
- `.yamllint.yaml` — workspace-wide config (use from repo root)
- `.gitattributes` — line-ending normalization
- `scripts/validate-yaml.sh` — reusable validation script

## Workflow

### Phase 1: Setup
1. Install yamllint: `pip install yamllint`
2. Create `.yamllint.yaml` workspace config (relaxed rules for GHA)
3. Create/update `.gitattributes` with `*.yml text eol=lf`
4. Create `scripts/validate-yaml.sh` (exists at workspace root)

### Phase 2: Scan
```bash
yamllint -c .yamllint.yaml .github/workflows/*.yml
yamllint -c .yamllint.yaml projects/**/*.yml
yamllint -c .yamllint.yaml projects/**/*.yaml
```
Or use the reusable script:
```bash
bash scripts/validate-yaml.sh
```

### Phase 3: Fix Common Issues

**Preferred (cross-platform with submodule support):** Use the Python unified fix script in `references/bulk-fix-yml-workflows.md` — handles CRLF, trailing spaces, and EOF newlines in one pass, correctly excludes node_modules and .venv on Windows/MSYS.

**Alternative (simple repos, shell only):**
| Issue | Fix Command |
|-------|-------------|
| CRLF → LF | `find . -name "*.yml" -o -name "*.yaml" \| xargs sed -i 's/\\r$//'` |
| Missing EOF newline | `find . -name "*.yml" -o -name "*.yaml" -exec sh -c 'tail -c1 "$1" \| read -r _ \|\| echo >> "$1"' _ {} \;` |
| Trailing spaces | `find . -name "*.yml" -o -name "*.yaml" \| xargs sed -i 's/[[:space:]]*$//'` |

### Phase 4: Validate
```bash
yamllint -c .yamllint.yaml -f parsable .github/workflows/
```

### Phase 5: Add CI
Add `.github/workflows/yaml-validation.yml` to run yamllint on push/PR.

## Pitfalls
- **Always validate the config file first**: Run `yamllint -c .yamllint.yaml .yamllint.yaml` before scanning the full repo. An invalid config (e.g. unsupported options like `allow-non-break-words`) blocks all validation and produces a misleading exit code.
- **CRLF files**: MSYS2/git-bash can create CRLF files even on Linux repos. Always set `*.yml text eol=lf` in `.gitattributes`.
- **CRLF verification on MSYS/Windows**: Do NOT rely on `od -c | grep -q '\\r'` in MSYS git-bash — MSYS translates LF→CRLF at the terminal output level, producing false positives even on LF-only files. Always verify CRLF with Python binary-mode read instead:
  ```python
  with open(path, 'rb') as f:
      data = f.read()
  print('Has CRLF:', b'\r\n' in data)   # reliable
  print('Has lone \\r:', b'\r' in data)  # also check bare CR
  ```
  The `sed -i 's/\r$//'` fix DOES work in MSYS git-bash despite MSYS terminal translation confusing your verification.
- **`find -not -path` on Windows/MSYS is unreliable for deep trees**: The `find` command with `-not -path '*/node_modules/*'` often leaks files from deeply nested node_modules subdirectories, especially under multi-project git-submodule workspaces. Prefer Python `os.walk` with `dirs[:]` filtering instead (run via `execute_code`):
  ```python
  basedir = "projects"
  yml_files = []
  for root, dirs, files in os.walk(basedir):
      dirs[:] = [d for d in dirs if d not in ('node_modules', '.venv', '__pycache__', '.git')]
      if '{{cookiecutter' in root:
          continue
      for f in files:
          if f.endswith('.yml') or f.endswith('.yaml'):
              yml_files.append(os.path.join(root, f))
  ```
  This is the only reliably correct approach on Windows/MSYS — `find` exclusion patterns are unpredictable with submodules.
- **Write-file-overwrite risk**: `write_file()` replaces the entire file. If you read only a partial view (offset/limit pagination) and then write back, you truncate the rest. Always read the full file first, or use `patch()` for targeted edits. If you accidentally truncate a file in a git submodule, recover it with:
  ```bash
  cd <submodule_dir> && git show HEAD:<path> > <path>
  ```
- **cookiecutter Jinja**: Files under `{{cookiecutter.*}}/` contain Jinja placeholders that break yamllint. Exclude with `grep -v '/{{cookiecutter'`.
- **Lock files**: `resource-staleness-report.lock.yml` has very long inline scripts (up to 1178 chars) — set `line-length: max: 1200` repo-wide or skip the file.
- **Trailing spaces**: Most common in docker-compose files with multiline `|` blocks.
- **No trailing newline**: `printf` or `echo >>` not `sed -i '$a\'` (sed adds content on some platforms). Prefer: `tail -c1 file | read -r _ || echo >> file`.
- **yamllint line-length vs GHA**: GitHub Actions `run:` blocks with multi-line shell scripts often exceed 80 chars. Set `max: 200` or higher. The `allow-non-break-words` option does NOT exist in yamllint 1.38 — do not use it.
- **Always re-verify after batch fixes**: Run the full sweep to catch regressions.
- **`level: false` is invalid in yamllint**: Setting `level: false` on a rule produces `invalid config: level should be "error" or "warning"`. To disable a rule, remove it from the `rules:` block entirely — do not set level to false.
- **Scope estimation**: Initial file discovery via `search_files` or `ls` often misses hidden dotfiles (`.readthedocs.yml`, `.pre-commit-config.yaml`) and nested `.github/workflows/` inside sub-projects. Always run a full `os.walk` tree with explicit filtering before committing to file-count estimates. In this session, the initial ~70 estimate was actually ~119 files.
- **Lock file exclusion**: Auto-generated lock files (`.lock.yml`, `.lock.yaml`) embed long JSON strings that always break line-length rules. Exclude them from yamllint with `ignore: | *.lock.yml` in the config rather than bumping line-length to 1200+ for the entire project.
- **Config self-validate first**: Before running any validation sweep, validate the config itself: `yamllint -c .yamllint.yaml .yamllint.yaml`. An invalid config produces silent failures or misleading results across every file.
- **yamllint ignore pattern syntax**: The `ignore:` field in `.yamllint.yaml` supports shell globs (`*.lock.yml`) and directory paths (`.venv/`). These work per-line under the `|` block continuation.

## References
- `references/bulk-fix-yml-workflows.md` — Full batch-fix recipe: CRLF→LF, trailing spaces, missing newline, yamllint config pitfalls, and verification for 30+ file jobs.

## Verification Checklist
- [ ] `yamllint -c .yamllint.yaml` returns 0 on all YAML files
- [ ] All files use LF line endings
- [ ] No trailing whitespace in any YAML file
- [ ] All files end with `\n`
- [ ] `.gitattributes` covers `*.yml` and `*.yaml`
- [ ] CI workflow validates YAML on push/PR
- [ ] Cookiecutter Jinja templates excluded from validation

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
