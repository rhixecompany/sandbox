/**
 * Error handling utilities
 */

export class ScriptError extends Error {
  constructor(
    message: string,
    public readonly exitCode: number = 1,
  ) {
    super(message);
    this.name = "ScriptError";
  }
}

export class UsageError extends ScriptError {
  constructor(message: string) {
    super(message, 1);
    this.name = "UsageError";
  }
}

export async function safeExec(
  fn: () => Promise<void>,
  options?: { onError?: (err: Error) => void },
): Promise<number> {
  try {
    await fn();
    return 0;
  } catch (err) {
    if (options?.onError) {
      options.onError(err instanceof Error ? err : new Error(String(err)));
    }
    if (err instanceof ScriptError) {
      return err.exitCode;
    }
    console.error(err instanceof Error ? err.message : String(err));
    return 1;
  }
}
