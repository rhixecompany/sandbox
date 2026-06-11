**Prompt: Batch Fix All Errors, Warnings, and Deprecations**

You are tasked with systematically eliminating all errors, warnings, and deprecations in this codebase. Follow these steps strictly:

1. **Run Validation Scripts**
   - Execute `pnpm lint:fix` and `pnpm build`.
   - Collect all errors, warnings, and deprecations from the output.

2. **Document Issues**
   - For each surfaced issue:
     - Identify the file(s) and line(s) involved.
     - Analyze the root cause (e.g., import error, type error, deprecated API).
     - Research third-party package issues if needed.
     - Document each issue, its cause, and the proposed fix in `docs/proposedFixes.MD`.

3. **Apply Fixes**
   - Fix all documented issues:
     - Correct import paths, restore/create missing files, update deprecated APIs, fix type/lint/build errors.
     - Only modify code related to surfaced issues.
     - Ensure all changes follow project standards.

4. **Auto-format**
   - Run `pnpm lint:fix` again to auto-format and resolve any remaining style issues.

5. **Verification**
   - Rerun `pnpm build` and `pnpm lint:fix` to confirm all issues are resolved.
   - Repeat steps 2–5 if any issues remain.

6. **Documentation**
   - For each significant fix, document before/after code, rationale, and references in `docs/proposedFixes.MD`.
   - Add inline comments for non-obvious changes.

7. **Commit & Final Check**
   - Commit all changes with a comprehensive summary.
   - Ensure all scripts pass with zero errors/warnings.

**Constraints:**

- No unrelated refactoring or new features.
- Only address issues surfaced by lint/build output.
- Zero warnings allowed.

## **Goal:** All scripts (`pnpm lint:fix`, `pnpm build`) pass with zero errors/warnings. All fixes are documented and traceable.

**Next:** Begin by running all validation scripts, collecting the current errors/warnings, and then proceed stepwise through the plan above. You will receive a detailed report and all code changes as the process completes.
