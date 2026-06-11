export type RunOptions = { dryRun?: boolean; verbose?: boolean };

export async function performTask(input: string, opts: RunOptions = { dryRun: true }) {
  const { dryRun = true } = opts;
  if (dryRun) return { input, processed: input.trim(), note: 'dry-run' };
  // real side-effects go here
  return { input, processed: input.trim(), note: 'executed' };
}
