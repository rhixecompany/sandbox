/**
 * ANSI Color Utilities for Terminal Output
 * =============================================
 * Simple color constants without external dependencies
 * Used by all unified scripts for consistent terminal styling
 */

export const ANSI = {
  // Reset
  RESET: "\x1b[0m",

  // Foreground Colors
  BLACK: "\x1b[30m",
  RED: "\x1b[31m",
  GREEN: "\x1b[32m",
  YELLOW: "\x1b[33m",
  BLUE: "\x1b[34m",
  MAGENTA: "\x1b[35m",
  CYAN: "\x1b[36m",
  WHITE: "\x1b[37m",

  // Bright Foreground Colors
  BRIGHT_BLACK: "\x1b[90m",
  BRIGHT_RED: "\x1b[91m",
  BRIGHT_GREEN: "\x1b[92m",
  BRIGHT_YELLOW: "\x1b[93m",
  BRIGHT_BLUE: "\x1b[94m",
  BRIGHT_MAGENTA: "\x1b[95m",
  BRIGHT_CYAN: "\x1b[96m",
  BRIGHT_WHITE: "\x1b[97m",

  // Text Styles
  BOLD: "\x1b[1m",
  DIM: "\x1b[2m",
  ITALIC: "\x1b[3m",
  UNDERLINE: "\x1b[4m",

  // Background Colors
  BG_RED: "\x1b[41m",
  BG_GREEN: "\x1b[42m",
  BG_YELLOW: "\x1b[43m",
  BG_BLUE: "\x1b[44m",
} as const;

/**
 * Formatting helpers with colors
 */
export function colorize(text: string, color: string): string {
  return `${color}${text}${ANSI.RESET}`;
}

export function success(text: string): string {
  return `${ANSI.GREEN}✓${ANSI.RESET} ${text}`;
}

export function error(text: string): string {
  return `${ANSI.RED}✖${ANSI.RESET} ${text}`;
}

export function warning(text: string): string {
  return `${ANSI.YELLOW}⚠${ANSI.RESET} ${text}`;
}

export function info(text: string): string {
  return `${ANSI.BLUE}ℹ${ANSI.RESET} ${text}`;
}

export function muted(text: string): string {
  return colorize(text, ANSI.BRIGHT_BLACK);
}

export function bold(text: string): string {
  return colorize(text, ANSI.BOLD);
}

export function title(text: string): string {
  return colorize(text, `${ANSI.BOLD}${ANSI.CYAN}`);
}
