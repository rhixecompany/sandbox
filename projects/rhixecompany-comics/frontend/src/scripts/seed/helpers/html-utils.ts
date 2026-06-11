/**
 * HTML utility functions for seed data processing
 * @module html-utils
 */

/**
 * Strip HTML tags from a string
 * Used to clean descriptions extracted from web scraping
 */
export function stripHtmlTags(html: string): string {
  return html.replaceAll(/<[^>]*>/g, "");
}
