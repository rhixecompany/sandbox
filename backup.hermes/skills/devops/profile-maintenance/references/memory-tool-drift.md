# Memory Tool Drift After File Patches

## What happened
- Patching `~/AppData/Local/hermes/memories/MEMORY.md` or `USER.md` can leave the memory tool's internal snapshot out of sync with the on-disk file.
- A subsequent `memory(action='add'|'replace')` may fail with:
  - `Refusing to write MEMORY.md: file on disk has content that wouldn't round-trip`
- The guard may emit a `.bak.<timestamp>` snapshot during failure handling.

## Repro pattern
1. Use `patch()` or another direct file edit on a memory file.
2. Verify the file contents on disk look correct.
3. Call `memory()` in the same session.
4. The tool can still reject the write even though the file reads cleanly.

## Recovery pattern
- Remove generated `.bak.*` artifacts after inspecting them.
- Do not keep retrying `memory()` in the same session.
- If the memory content must be updated immediately, rewrite the file cleanly with `write_file`, then stop using `memory()` until the next session start.
- If the content is already correct on disk, leave it and let the next session resync.

## Why this matters
- Prevents infinite retry loops.
- Prevents accidental `.bak` clutter.
- Keeps the distinction clear between file state and memory-store state.
