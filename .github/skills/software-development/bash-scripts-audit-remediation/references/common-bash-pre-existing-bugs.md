# Common Pre-Existing Bash Bugs Found During Migration

> Bug patterns discovered during a 54-script migration from project roots to `Bash/`. All three bugs were pre-existing (present in originals before copy), found by `bash -n` syntax check, and required structural fixes — not just formatting changes.

## Bug 1: Case Statement `''|#*)` Parse Failure

**Symptoms:** `bash -n` reports `syntax error near unexpected token 'newline'` on a case pattern like `''|#*) continue;;`.

**Root cause:** Some bash versions (or contexts with embedded newlines) fail to parse combined empty-string + comment patterns in case statements. The `''` (empty string) combined with `|` and inline `;;` creates a parsing ambiguity.

**Fix:** Restructure into separate case branches:

```bash
# ❌ BROKEN — fails to parse on some bash versions
case "$line" in
  ''|#*) continue;;
esac

# ✅ FIXED — separate branches, each with its own ;;
case "$line" in
  '')
    continue
    ;;
  \#*)
    continue
    ;;
esac
```

**Detection:** Run `bash -n script.sh` and look for errors on case statement lines. The error is often reported on a different line than the actual cause.

## Bug 2: Missing `fi` Closing an `if` Block

**Symptoms:** `bash -n` reports `syntax error: unexpected end of file`. No obvious nested-block mismatch.

**Root cause:** An `if` block has no matching `fi`. Common when:
- Adding new code before closing an existing `if`
- The `then` branch ends but the next line starts a new `if` before the first one is closed

**Fix strategy:** Read the entire file top to bottom matching `if`/`then` with `fi`:

```bash
# ❌ BROKEN — first if never closed with fi
if [ -f ./ecom.socket ]
then
    mv ./ecom.socket /etc/systemd/system   # ← this if needs fi BEFORE next if

if [ -f /etc/systemd/system/ecom.socket ]
then
    mv ./ecom.service /etc/systemd/system
else
    echo "Not present"
fi

# ✅ FIXED — added missing fi
if [ -f ./ecom.socket ]
then
    mv ./ecom.socket /etc/systemd/system
fi                                 # ← added this

if [ -f /etc/systemd/system/ecom.socket ]
then
    mv ./ecom.service /etc/systemd/system
else
    echo "Not present"
fi
```

**Detection:** Count `if` vs `fi` occurrences. If they don't match, find the missing one by scanning for `if ... then` blocks without closing `fi`.

## Bug 3: Double-Quote Escaping Conflicts in `grep -E` with Embedded Single Quotes

**Symptoms:** `bash -n` reports `syntax error near unexpected token '('` but the offending line is a `grep -E` with a regex pattern containing character classes with embedded single quotes.

**Root cause:** A regex pattern like `['\"]?[^'\"[:space:]]+` is inside double quotes. The `'` is a literal single quote which is fine inside double quotes, but `\"` escapes the double-quote delimiter. The result is that the string appears to end, and the remaining characters (including `(` from the pattern) are interpreted as bash syntax:

```bash
# ❌ BROKEN — \" inside double-quoted string kills the quoting
grep -oE "(source|require|import) +['\"]?[^'\"[:space:]]+" "$file"

# ^ The \" is interpreted as escaping the outer ", ending the string
#   Then ']?[^' starts a bare single-quoted string, and everything breaks
```

**Fix:** Extract the regex pattern into a variable first, then use `"$var"`:

```bash
# ✅ FIXED — pattern stored in variable, variable expansion is safe
local pattern="(source|require|import|from|using) +['\"]?[^'\"[:space:]]+"
grep -oE "$pattern" "$file" 2>/dev/null

# This also works for grep -qE with parenthesized patterns:
local critical_pattern="(password|secret|token|api_key|credential).*="
if grep -qE "$critical_pattern" "$file" 2>/dev/null; then
    ...
fi
```

**Rule of thumb:** If a `grep -E` or `grep -oE` pattern contains both `"` and `'` in character classes, extract the pattern to a variable. Three levels of quoting (shell → grep → regex) is too brittle for inline patterns.

## General Detection Strategy

```bash
# Phase 1: Syntax check ALL .sh files before any migration
for f in $(find . -name "*.sh" -not -path "*/.git/*" -not -path "*/node_modules/*"); do
  bash -n "$f" 2>&1 && echo "✅ $f" || echo "❌ $f"
done

# Phase 2: Fix originals FIRST, then copy to target
# DO NOT: copy → fix copies → delete originals (copies lag behind)
# DO:    fix originals → re-copy to target → verify → delete originals

# Phase 3: Re-verify after copy
for f in $(find Bash/ -name "*.sh" -type f); do
  bash -n "$f" 2>&1 || echo "STILL BROKEN: $f"
done
```

## Pre-Existing vs Migration-Introduced

When you find a syntax bug in a migrated copy, always check the original:

```bash
if [ -f "$original" ]; then
  bash -n "$original" 2>&1 && echo "Migration-introduced" || echo "Pre-existing"
fi
```

If pre-existing, fix both the original (if it still exists) and the copy. If the original was already deleted, fix only the copy — the bug was latent and surfaced by the safety check.
