/**
 * Follow-related Zod schemas
 * Validates follow operations
 */

import { z } from "zod";

/**
 * Schema for following a user
 */
export const followUserSchema = z.object({
  targetUserId: z.string().min(1, "Target user ID is required"),
});

export type FollowUserInput = z.infer<typeof followUserSchema>;

/**
 * Schema for unfollowing a user
 */
export const unfollowUserSchema = z.object({
  targetUserId: z.string().min(1, "Target user ID is required"),
});

export type UnfollowUserInput = z.infer<typeof unfollowUserSchema>;
