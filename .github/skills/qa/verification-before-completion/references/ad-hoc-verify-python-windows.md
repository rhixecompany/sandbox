# Ad-hoc verification recipe (Python, Windows/MSYS)

Use when a code edit has no canonical test/lint/build command and the system
asks for "fresh passing verification evidence" via a temp `hermes-verify-*.py`
script. This is targeted ad-hoc verification, NOT a green suite.

## Recipe

1. Write a throwaway script to `os.path.join(tempfile.gettempdir(),
   "hermes-verify-<topic>.py")` (or hardcode the temp path). Use
   `importlib.util.spec_from_file_location` to load the changed module by path
   so you don't depend on the working dir / package layout.
2. Assert the changed behavior with property checks, edge cases, and the
   exact before/after the edit promised.
3. Run it: `python3 "<native-path>"`.
4. Clean up immediately after: `rm -f "<native-path>"` (or `os.remove`).
5. Summarize explicitly as **ad-hoc verification**, never "suite green".

## Pitfall: MSYS path doubling (real, bit this session)

On the Hermes Windows host, `terminal` runs bash via MSYS. A path passed like
`/c/Users/Alexa/AppData/Local/Temp/hermes-verify-lcs.py` gets rewritten by the
MSYS mount layer into `\\c\\Users\\...` (note the doubled leading backslash +
backslashes), which `python3` cannot open -> `[Errno 2] No such file`.

**Fix:** pass a NATIVE Windows path with forward slashes, NOT an MSYS `/c/...`
path:
```
python3 "C:/Users/Alexa/AppData/Local/Temp/hermes-verify-lcs.py"
```
Also: the MSYS `rm` deletes the file, so a `rm` in a failed earlier command
removes the script before you re-run. Write + run in ONE terminal statement,
or recreate the file before retrying.

## Pitfall: bad test assertion / false failure

A failing assert may be the TEST's fault, not the code's. In this session the
code returned a valid LCS `(2,3)` for `(1,2,3)` vs `(2,1,3)`, but the test
hard-coded `== [2,3]`; the equally-valid `[1,3]` made the assert fail. Fix the
assertion (accept any valid result) and re-run — don't "fix" correct code to
match a wrong test.

## Why ad-hoc, not permanent

No canonical test command exists in many small workspaces. The temp script is
the system's prescribed pattern: prove the change, then delete the proof so it
never rots into a stale committed test. Keep the real, durable artifact (the
refactored module + tutorial/markdown) separate from the temp verifier.
