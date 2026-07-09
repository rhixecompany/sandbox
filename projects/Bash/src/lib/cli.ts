/**
 * CLI argument parsing utilities
 */

export interface CliArgs {
  flags: Set<string>;
  named: Record<string, string>;
  positional: string[];
}

export function parseArgs(argv: string[]): CliArgs {
  const flags = new Set<string>();
  const named: Record<string, string> = {};
  const positional: string[] = [];

  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (!arg) continue;

    if (arg.startsWith("--")) {
      const eqIdx = arg.indexOf("=");
      if (eqIdx !== -1) {
        named[arg.slice(2, eqIdx)] = arg.slice(eqIdx + 1);
      } else if (i + 1 < argv.length && !argv[i + 1]!.startsWith("-")) {
        named[arg.slice(2)] = argv[++i]!;
      } else {
        flags.add(arg.slice(2));
      }
    } else if (arg.startsWith("-")) {
      flags.add(arg.slice(1));
    } else {
      positional.push(arg);
    }
  }

  return { flags, named, positional };
}

export function showHelp(usage: string, description?: string): never {
  console.log(usage);
  if (description) console.log(`\n${description}`);
  process.exit(0);
}
