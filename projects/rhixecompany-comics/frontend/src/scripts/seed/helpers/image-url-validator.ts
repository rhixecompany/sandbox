/**
 * Image URL validation utilities
 * @module image-url-validator
 */

import { extractExtension } from "@/storages/image-downloader";

const IMAGE_EXTENSIONS = /\.(jpg|jpeg|png|webp|avif|gif|svg)(\?.*)?$/i;
const KNOWN_CDN_PATTERNS = /placehold|dicebear|imagekit|cloudinary|imgur|unsplash/;

/**
 * Validate that a string is a valid image URL or known CDN pattern
 *
 * @param url - URL to validate
 * @returns true if valid image URL
 */
export function isValidImageUrl(url: string): boolean {
  try {
    const parsed = new URL(url);
    if (parsed.protocol !== "http:" && parsed.protocol !== "https:") return false;
    if (IMAGE_EXTENSIONS.test(parsed.pathname)) return true;
    if (KNOWN_CDN_PATTERNS.test(parsed.hostname)) return true;
    return true;
  } catch {
    return false;
  }
}

export { extractExtension };
