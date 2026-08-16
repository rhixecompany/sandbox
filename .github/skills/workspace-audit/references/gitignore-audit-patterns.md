# Gitignore Coverage Audit Patterns

## When to Use

When auditing whether a project's `.gitignore` covers a required set of entries across a workspace of N repos. This technique handles the fact that gitignore patterns have multiple equivalent forms.

## Core Technique: Shell grep with Alternative-Pattern Fallbacks

A straight `grep -qF "pattern"` produces false negatives when the equivalent pattern uses a different format. Use this per-project loop:

```bash
# Required entries to check
REQUIRED=("node_modules/" ".env" "*.pyc" "__pycache__/" "dist/"
          "build/" ".next/" "venv/" ".DS_Store")

MISS=""
COV=""

for pat in "${REQUIRED[@]}"; do
  if grep -qF "$pat" .gitignore 2>/dev/null; then
    COV="$COV $pat"
  else
    # Check alternative patterns that functionally cover the same thing
    case "$pat" in
      "*.pyc")
        if grep -qF '*.py[cod]' .gitignore 2>/dev/null; then
          COV="$COV $pat(via *.py[cod])"
        elif grep -q '*pyc' .gitignore 2>/dev/null; then
          COV="$COV $pat(via *pyc)"
        else
          MISS="$MISS $pat"
        fi
        ;;
      "build/")
        if grep -qE '(^|/)build($|/)' .gitignore 2>/dev/null &&
           ! grep -qE 'build/' .gitignore 2>/dev/null; then
          COV="$COV $pat(via /build)"
        else
          MISS="$MISS $pat"
        fi
        ;;
      "dist/")
        if grep -qE '(^|/)dist($|/)' .gitignore 2>/dev/null &&
           ! grep -qF 'dist/' .gitignore 2>/dev/null; then
          COV="$COV $pat(via dist or /dist)"
        else
          MISS="$MISS $pat"
        fi
        ;;
      ".env")
        if grep -qE '\.env\*|\.env\.' .gitignore 2>/dev/null; then
          COV="$COV $pat(via .env* or .env.)"
        else
          MISS="$MISS $pat"
        fi
        ;;
      "node_modules/")
        if grep -qE '(^|/)node_modules($|/)' .gitignore 2>/dev/null; then
          COV="$COV $pat(via node_modules or /node_modules)"
        else
          MISS="$MISS $pat"
        fi
        ;;
      ".DS_Store")
        if grep -qF '*.DS_Store' .gitignore 2>/dev/null; then
          COV="$COV $pat(via *.DS_Store)"
        elif grep -qF '._*' .gitignore 2>/dev/null; then
          COV="$COV $pat(via ._* wildcard)"
        else
          MISS="$MISS $pat"
        fi
        ;;
      "venv/")
        if grep -qE '(^|/)\.?venv($|/)' .gitignore 2>/dev/null; then
          COV="$COV $pat(via .venv/ or venv)"
        else
          MISS="$MISS $pat"
        fi
        ;;
      *)
        MISS="$MISS $pat"
        ;;
    esac
  fi
done

echo "Covered: $COV"
echo "Missing: $MISS"
```

## Gitignore Pattern Equivalence

These patterns are functionally equivalent in git's gitignore matching:

| Required Pattern | Equivalent Forms | Notes |
|---|---|---|
| `node_modules/` | `node_modules`, `/node_modules` | Without trailing slash matches both file and dir |
| `.env` | `.env*`, `.env.local`, `.env.*`, `.envs/` | Glob catches all dotenv variants |
| `*.pyc` | `*.py[cod]`, `*$py.class`, `*pyc` | `*.py[cod]` also covers `.pyo`, `.pyd` |
| `__pycache__/` | `__pycache__` | No trailing slash also valid |
| `dist/` | `dist`, `/dist`, `/dist/` | `/dist` scoped to root only; `dist` matches anywhere |
| `build/` | `build`, `/build`, `/build/`, `**/build/` | `build/Release` is narrower (only matches that subpath) |
| `.next/` | `.next`, `/.next`, `/.next/` | Common in Next.js projects |
| `venv/` | `venv`, `.venv/`, `.venv`, `env/`, `myvenv/` | Many venv naming conventions exist |
| `.DS_Store` | `*.DS_Store`, `._*`, `.DS_*` | `*.DS_Store` matches `.DS_Store` in git gitignore |

## Running Across N Repos

```bash
BASE="/c/Users/username/projects"
for d in "$BASE"/*/; do
  name=$(basename "$d")
  cd "$d" || continue
  echo "=== $name ==="
  [ -f .gitignore ] && echo "GITIGNORE=yes" || echo "GITIGNORE=no"
  # Run the grep loop above on .gitignore
  ...
done
```

## Key Caveats

- **Trailing slash matters for accuracy but not functionality** — `node_modules` (no `/`) matches both a file and directory named `node_modules`. `node_modules/` matches only a directory. Both work for the purpose of ignoring a folder.
- **Root-scoped patterns** (`/build`) match only at project root, while bare `build/` matches anywhere. For audit purposes, root-scoped coverage is usually sufficient since build artifacts are at the repo root.
- **Negative patterns** (`!keep/this`) override ignore rules — check that required entries aren't accidentally un-ignored by a later `!` pattern.
