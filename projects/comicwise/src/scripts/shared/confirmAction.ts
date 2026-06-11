#!/usr/bin/env tsx

import { createInterface } from "node:readline";

/**
 * Confirmation Utility for Destructive Operations
 *
 * Provides interactive confirmation prompts for destructive scripts.
 * Supports --yes flag to proceed without user interaction (CI/CD safe).
 *
 * @example
 * import { confirmAction } from "./shared/confirmAction";
 *
 * const confirmed = await confirmAction({
 *   title: "Clear Cache",
 *   message: "This will delete all cache entries",
 *   yesFlag: options.yes,
 *   cautionLevel: "high"
 * });
 *
 * if (!confirmed) process.exit(0);
 */

// ANSI color codes (simple, no external dependency)
const ANSI = {
  RESET: "\x1b[0m",
  BOLD: "\x1b[1m",
  RED: "\x1b[31m",
  GREEN: "\x1b[32m",
  YELLOW: "\x1b[33m",
  BLUE: "\x1b[36m", // cyan
  GRAY: "\x1b[90m",
  ORANGE: "\x1b[38;5;208m",
};

interface ConfirmActionOptions {
  /** Affected items count (optional, for context) */
  affectedCount?: number;
  /** What will be affected (optional) */
  affectedType?: string;
  /** Caution level: low, medium, high (determines UI emphasis) */
  cautionLevel?: "high" | "low" | "medium";
  /** Details to show (optional) */
  details?: string[];
  /** Description of what will happen */
  message: string;
  /** Title of the action being confirmed */
  title: string;
  /** Whether --yes flag was passed (skip confirmation) */
  yesFlag?: boolean;
}

/**
 * Prompt user for confirmation before destructive operation
 *
 * Returns true if user confirms or --yes flag is set
 * Returns false if user declines
 */
export async function confirmAction(options: ConfirmActionOptions): Promise<boolean> {
  const {
    title,
    message,
    yesFlag = false,
    cautionLevel = "medium",
    affectedCount,
    affectedType,
    details = [],
  } = options;

  // Skip confirmation if --yes flag provided
  if (yesFlag) {
    return true;
  }

  // Display header
  console.log("\n" + formatHeader(title, cautionLevel));

  // Display message
  console.log(`${ANSI.BOLD}${message}${ANSI.RESET}\n`);

  // Display affected count if provided
  if (affectedCount !== undefined && affectedCount > 0) {
    const countColor = cautionLevel === "high" ? ANSI.RED : ANSI.YELLOW;
    console.log(`${countColor}⚠️  Affected: ${affectedCount} ${affectedType || "items"}${ANSI.RESET}\n`);
  }

  // Display details if provided
  if (details.length > 0) {
    console.log(`${ANSI.GRAY}Details:${ANSI.RESET}`);
    for (const detail of details) {
      console.log(`  ${ANSI.GRAY}• ${detail}${ANSI.RESET}`);
    }
    console.log();
  }

  // Prompt for confirmation
  return await promptYesNo(`${ANSI.BOLD}${ANSI.ORANGE}Proceed? (yes/no)${ANSI.RESET}`);
}

/**
 * Simple yes/no prompt (uses Node.js readline module)
 */
async function promptYesNo(promptText: string): Promise<boolean> {
  return new Promise((resolve) => {
    const readline = createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    readline.question(`${promptText} `, (answer: string) => {
      readline.close();
      const normalized = answer.toLowerCase().trim();
      resolve(normalized === "yes" || normalized === "y");
    });
  });
}

/**
 * Format header with appropriate styling based on caution level
 */
function formatHeader(title: string, cautionLevel: string): string {
  const divider = "═".repeat(60);
  let color = ANSI.BLUE;
  let icon = "⚙️ ";

  if (cautionLevel === "high") {
    color = ANSI.RED;
    icon = "🚨";
  } else if (cautionLevel === "medium") {
    color = ANSI.YELLOW;
    icon = "⚠️ ";
  }

  return (
    `${color}${divider}${ANSI.RESET}\n` +
    `${ANSI.BOLD}${color}${icon}  ${title}${ANSI.RESET}\n` +
    `${color}${divider}${ANSI.RESET}`
  );
}

/**
 * Format a list of affected items for display
 */
export function formatAffectedItems(items: string[]): string[] {
  if (items.length === 0) return [];
  if (items.length <= 5) return items; // Show all if few

  // Show first 3 and count of remaining
  return [...items.slice(0, 3), `... and ${items.length - 3} more`];
}

/**
 * Convenience wrapper for common destructive operations
 */
export async function shouldProceed(options: ConfirmActionOptions): Promise<boolean> {
  return confirmAction(options);
}
