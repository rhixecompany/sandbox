/**
 * Interactive Confirmation Utility
 * ================================
 * Safe confirmations for destructive operations without external dependencies
 */

import { createInterface } from "node:readline";

import { ANSI, info, warning } from "./colors.js";

export interface ConfirmOptions {
  cautionLevel?: "high" | "low" | "medium";
  defaultValue?: boolean;
  items?: string[];
  itemsLabel?: string;
  message?: string;
  title: string;
}

export async function confirmAction(options: ConfirmOptions): Promise<boolean> {
  const {
    title,
    message,
    items = [],
    itemsLabel = "Items affected",
    cautionLevel = "medium",
    defaultValue = false,
  } = options;

  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const question = (prompt: string): Promise<string> => {
    return new Promise((resolve) => {
      rl.question(prompt, resolve);
    });
  };

  try {
    // Show confirmation prompt
    console.log();
    if (cautionLevel === "high") {
      console.log(warning(`${ANSI.BOLD}${title}${ANSI.RESET}`));
    } else {
      console.log(info(`${ANSI.BOLD}${title}${ANSI.RESET}`));
    }

    if (message) {
      console.log(message);
    }

    // Show affected items if provided
    if (items.length > 0) {
      console.log(`\n${itemsLabel}:`);
      for (const item of items.slice(0, 10)) {
        console.log(`  • ${item}`);
      }
      if (items.length > 10) {
        console.log(`  ... and ${items.length - 10} more`);
      }
    }

    // Show caution level
    if (cautionLevel === "high") {
      console.log(warning("⚠ This action cannot be easily undone!"));
    } else if (cautionLevel === "medium") {
      console.log(info("This operation will make changes to your files."));
    }

    // Ask for confirmation
    const prompt =
      cautionLevel === "high"
        ? `\n${ANSI.BOLD}Type "yes" to confirm: ${ANSI.RESET}`
        : `\n${ANSI.BOLD}Continue? [y/N]: ${ANSI.RESET}`;

    const answer = await question(prompt);

    console.log();

    // Validate response
    if (cautionLevel === "high") {
      return answer.toLowerCase() === "yes";
    }

    if (answer === "") {
      return defaultValue;
    }

    return answer.toLowerCase().startsWith("y");
  } finally {
    rl.close();
  }
}

export async function formatAffectedItems(items: string[], maxDisplay: number = 10): Promise<string> {
  const displayed = items.slice(0, maxDisplay);
  const extra = items.length - maxDisplay;

  let result = displayed.map((item) => `  • ${item}`).join("\n");

  if (extra > 0) {
    result += `\n  ... and ${extra} more items`;
  }

  return result;
}

export async function shouldProceed(prompt: string, defaultValue: boolean = false): Promise<boolean> {
  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  return new Promise((resolve) => {
    const question = defaultValue ? "[Y/n]" : "[y/N]";
    rl.question(`${prompt} ${question}: `, (answer: string) => {
      rl.close();

      if (answer === "") {
        resolve(defaultValue);
        return;
      }

      resolve(answer.toLowerCase().startsWith("y"));
    });
  });
}
