# Common Bash Pitfall Fixes

## 1. Subshell Variable Propagation (`find | while`)

**Problem**: Variables set inside a `while` loop on the right side of a pipe are lost because each command in a pipeline runs in a subshell.

```bash
# BROKEN — WARNINGS is lost after the loop
find "$path" -type f -print0 | while IFS= read -r -d '' f; do
    rm -f "$f" || WARNINGS=$((WARNINGS + 1))
done
echo "Warnings: $WARNINGS"  # Always 0!

# FIXED — process substitution keeps while in the current shell
while IFS= read -r -d '' f; do
    rm -f "$f" || WARNINGS=$((WARNINGS + 1))
done < <(find "$path" -type f -print0)
echo "Warnings: $WARNINGS"  # Correct value
```

**Affects**: Any variable the loop body writes to (`COUNTER`, `ERRORS`, `FOUND`, arrays via `+=()`).

## 2. `eval` → `bash -c`

**Problem**: `eval "$cmd"` executes arbitrary strings in the current shell context, introducing injection risk and unexpected expansion.

```bash
# BAD — eval
eval "$cmd" 2>&1 | tee -a "$LOG_FILE"

# GOOD — bash -c (safer, same effect)
bash -c "$cmd" 2>&1 | tee -a "$LOG_FILE"
```

## 3. Background `$?` Check

**Problem**: `$?` after `command &` checks whether the background launch succeeded (always true), NOT whether the command itself succeeded.

```bash
# BROKEN — $? checks background launch, not the delete result
rm -rf "$folder" &
if [[ $? -eq 0 ]]; then
    echo "Deleted"  # Always runs!
fi

# FIXED A — handle inline (no background)
if rm -rf "$folder"; then
    echo "Deleted"
fi

# FIXED B — track background PIDs for later wait
rm -rf "$folder" &
PID=$!
# ... later ...
wait $PID
if [[ $? -eq 0 ]]; then
    echo "Deleted"
fi
```

## 4. Unbound Variable References with `set -u`

**Problem**: `set -u` (part of `set -euo pipefail`) causes the script to exit when referencing an unset variable.

```bash
# BROKEN — crashes if SCAN_PATHS is unset
if [[ -n "$SCAN_PATHS" ]]; then ...

# FIXED — safe default expansion
if [[ -n "${SCAN_PATHS:-}" ]]; then ...
```
