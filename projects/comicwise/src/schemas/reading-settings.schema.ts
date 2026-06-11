import { z } from "zod";

/**
 * Reader Settings Validation Schema
 * Validates user preferences for the chapter reader UI
 */

export const ReaderSettingsSchema = z.object({
  brightness: z
    .number()
    .min(50, "Brightness must be at least 50%")
    .max(150, "Brightness cannot exceed 150%")
    .default(100),
  contrast: z.number().min(80, "Contrast must be at least 80%").max(120, "Contrast cannot exceed 120%").default(100),
  viewMode: z.enum(["single", "double"]).default("single").describe("Single or double page view mode"),
  autoScroll: z.boolean().default(false),
});

/**
 * Type inference for ReaderSettings
 * Use this to type-check settings objects from the Zustand store
 */
export type ReaderSettings = z.infer<typeof ReaderSettingsSchema>;

/**
 * Partial settings update schema
 * Used when updating only specific settings without resetting others
 */
export const UpdateReaderSettingsSchema = ReaderSettingsSchema.partial();

export type UpdateReaderSettings = z.infer<typeof UpdateReaderSettingsSchema>;

/**
 * Safe validation function with defaults
 * Returns valid settings or throws validation error
 */
export function validateReaderSettings(data: unknown): ReaderSettings {
  const result = ReaderSettingsSchema.safeParse(data);
  if (!result.success) {
    throw new Error(`Validation failed: ${result.error}`);
  }
  return result.data;
}

/**
 * Safe partial validation function
 * Validates and returns only the provided fields
 */
export function validateUpdateReaderSettings(data: unknown): UpdateReaderSettings {
  const result = UpdateReaderSettingsSchema.safeParse(data);
  if (!result.success) {
    throw new Error(`Validation failed: ${result.error}`);
  }
  return result.data;
}
