/**
 * Flexible date parsing utilities
 * Handles multiple date formats and returns null for unparseable dates
 */

/**
 * Parse date from multiple formats
 *
 * Supports:
 * - "August 14th 2025"
 * - "August 14, 2025"
 * - "2025-08-14" (ISO-8601)
 * - "8/14/2025" (US format)
 * - ISO Date strings
 *
 * @param dateStr - Date string to parse
 * @returns Parsed Date or null if unparseable
 */
export function parseDate(dateStr: null | string | undefined): Date | null {
  if (!dateStr || typeof dateStr !== "string") {
    return null;
  }

  const trimmed = dateStr.trim();

  // Try ISO-8601 format first
  if (isValidISODate(trimmed)) {
    return new Date(trimmed);
  }

  // Try ordinal date format: "August 14th 2025"
  const ordinalMatch = trimmed.match(/^(\w+)\s+(\d{1,2})[a-z]{0,2}\s+(\d{4})$/i);
  if (ordinalMatch) {
    const [, month, day, year] = ordinalMatch;
    const dateObj = new Date(`${month} ${day}, ${year}`);
    if (!isNaN(dateObj.getTime())) {
      return dateObj;
    }
  }

  // Try common US format: "August 14, 2025"
  const usMatch = trimmed.match(/^(\w+)\s+(\d{1,2}),\s+(\d{4})$/);
  if (usMatch) {
    const [, month, day, year] = usMatch;
    const dateObj = new Date(`${month} ${day}, ${year}`);
    if (!isNaN(dateObj.getTime())) {
      return dateObj;
    }
  }

  // Try numeric format: "8/14/2025"
  const numericMatch = trimmed.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/);
  if (numericMatch) {
    const [, month, day, year] = numericMatch;
    const dateObj = new Date(parseInt(year), parseInt(month) - 1, parseInt(day));
    if (!isNaN(dateObj.getTime())) {
      return dateObj;
    }
  }

  // Try native Date parsing as fallback
  const dateObj = new Date(trimmed);
  if (!isNaN(dateObj.getTime())) {
    return dateObj;
  }

  return null;
}

/**
 * Check if string is valid ISO-8601 date format
 */
function isValidISODate(dateStr: string): boolean {
  const isoRegex = /^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d{3})?(Z|[+-]\d{2}:\d{2})?)?$/;
  if (!isoRegex.test(dateStr)) {
    return false;
  }

  const dateObj = new Date(dateStr);
  return !isNaN(dateObj.getTime());
}
