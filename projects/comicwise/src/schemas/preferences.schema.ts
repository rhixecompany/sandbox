import { z } from "zod";

/**
 * User Preferences Validation Schema
 * Defines all user preference settings with validation rules
 */

export const UserPreferencesSchema = z.object({
  // Theme preferences
  theme: z.enum(["light", "dark", "system"]).default("system"),

  // Reading preferences
  defaultLayout: z.enum(["webtoon", "comic", "book"]).default("webtoon"),
  pageNavigationStyle: z.enum(["buttons", "swipe", "click"]).default("buttons"),

  // Display preferences
  fontSize: z.number().int().min(12).max(24).default(16),
  lineHeight: z.enum(["compact", "normal", "relaxed"]).default("normal"),

  // Notification preferences
  notifyNewChapters: z.boolean().default(true),
  notifyComments: z.boolean().default(true),
  notifyBookmarkUpdates: z.boolean().default(false),

  // Privacy preferences
  profilePublic: z.boolean().default(false),
  showReadingHistory: z.boolean().default(false),
});

export type UserPreferences = z.infer<typeof UserPreferencesSchema>;

/**
 * Partial preferences schema for updates
 * Allows updating only specific preference fields
 */
export const UpdateUserPreferencesSchema = UserPreferencesSchema.partial();

export type UpdateUserPreferences = z.infer<typeof UpdateUserPreferencesSchema>;

/**
 * Notification preferences subset
 * For the notify preferences section
 */
export const NotificationPreferencesSchema = z.object({
  notifyNewChapters: z.boolean(),
  notifyComments: z.boolean(),
  notifyBookmarkUpdates: z.boolean(),
});

export type NotificationPreferences = z.infer<typeof NotificationPreferencesSchema>;

/**
 * Privacy preferences subset
 * For the privacy preferences section
 */
export const PrivacyPreferencesSchema = z.object({
  profilePublic: z.boolean(),
  showReadingHistory: z.boolean(),
});

export type PrivacyPreferences = z.infer<typeof PrivacyPreferencesSchema>;

/**
 * Display preferences subset
 * For the display preferences section
 */
export const DisplayPreferencesSchema = z.object({
  theme: z.enum(["light", "dark", "system"]),
  defaultLayout: z.enum(["webtoon", "comic", "book"]),
  pageNavigationStyle: z.enum(["buttons", "swipe", "click"]),
  fontSize: z.number().int().min(12).max(24),
  lineHeight: z.enum(["compact", "normal", "relaxed"]),
});

export type DisplayPreferences = z.infer<typeof DisplayPreferencesSchema>;
