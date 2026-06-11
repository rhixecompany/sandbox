/**
 * Common types for server actions
 */

/**
 * Standard server action result pattern
 * All server actions should return this type for consistency
 */
export type ActionResult<T> = { data: T; ok: true } | { error: string; ok: false };
