/*
 * TypeScript module template for migrating shell logic into TypeScript.
 * - Export functions with minimal side effects
 * - Provide a dryRun boolean param to avoid side effects in tests
 * - Add unit tests under Bash/src/migration/__tests__
 */

export type RunOptions = {
  dryRun?: boolean;
  verbose?: boolean;
};

export async function performTask(input: string, opts: RunOptions = {}) {
  const { dryRun = true, verbose = false } = opts;
  if (verbose) console.log(`performTask input=${input} dryRun=${dryRun}`);

  // Place business logic here. Avoid direct fs or network writes unless !dryRun.
  const result = { input, processed: input.trim().toUpperCase() };

  if (dryRun) {
    return { ...result, note: "dry-run: no side effects" };
  }

  // Real side-effect code goes here (example: write file, call API)
  // Keep it small and testable. Use try/catch and bubble errors up.

  return { ...result, note: "executed" };
}
