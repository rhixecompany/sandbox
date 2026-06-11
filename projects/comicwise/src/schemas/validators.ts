import type { z } from "zod";

/**
 * Safe validation helper with error handling
 * Returns a standardized result object instead of throwing
 */
export function safeParse<T>(
  schema: z.ZodType<T>,
  data: unknown
): { data: T; success: true } | { error: string; success: false } {
  const result = schema.safeParse(data);
  if (result.success) {
    return { success: true, data: result.data };
  }
  const errorMessages = result.error.issues.map((e: { message: string }) => e.message);
  return { success: false, error: errorMessages.join(", ") };
}

/**
 * Validate data against a schema with custom error handling
 */
export function validate<T>(schema: z.ZodType<T>, data: unknown): T {
  const result = safeParse(schema, data);
  if (!result.success) {
    throw new Error(`Validation failed: ${result.error}`);
  }
  return result.data;
}

/**
 * Check if data is valid without throwing
 */
export function isValid<T>(schema: z.ZodType<T>, data: unknown): data is T {
  return schema.safeParse(data).success;
}
