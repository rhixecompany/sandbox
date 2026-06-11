/**
 * Chapter number extraction utilities
 * Extracts chapter numbers from text like "Chapter 273"
 */

/**
 * Extract chapter number from chapter name/title
 *
 * Matches "Chapter 273", "Ch 273", "CHAPTER 5", etc.
 * Requires "Chapter" or "Ch" prefix (case-insensitive)
 * Returns null if no match found
 *
 * @param name - Chapter name like "Chapter 273"
 * @returns Extracted chapter number or null
 */
export function extractChapterNumber(name: string): null | number {
  if (!name || typeof name !== "string") {
    return null;
  }

  // Match "Chapter 273", "Ch 273", "CHAPTER 5", etc.
  // Capture group: (\d+(?:\.\d+)?) allows decimals like "1.5"
  const match = name.match(/chapter\s+(\d+(?:\.\d+)?)/i);

  if (!match) {
    return null;
  }

  const number = parseFloat(match[1]);

  // Validate it's a reasonable chapter number
  if (isNaN(number) || number < 0) {
    return null;
  }

  // Return as integer (round down decimals)
  return Math.floor(number);
}

/**
 * Check if string contains a valid chapter number
 */
export function hasChapterNumber(name: string): boolean {
  return extractChapterNumber(name) !== null;
}

/**
 * Format chapter number for display
 */
export function formatChapterNumber(number: number): string {
  return `Chapter ${number}`;
}
