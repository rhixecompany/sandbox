/**
 * Color utilities for terminal output
 */

const isColorSupported = process.stdout.isTTY && !process.env["NO_COLOR"];

const esc = (code: number) => (s: string) =>
  isColorSupported ? `\x1b[${code}m${s}\x1b[0m` : s;

export const red = esc(31);
export const green = esc(32);
export const yellow = esc(33);
export const blue = esc(34);
export const magenta = esc(35);
export const cyan = esc(36);
export const bold = esc(1);
export const dim = esc(2);

export const ok = (s: string) => green(`✓ ${s}`);
export const fail = (s: string) => red(`✗ ${s}`);
export const warn = (s: string) => yellow(`⚠ ${s}`);
export const info = (s: string) => blue(`ℹ ${s}`);
