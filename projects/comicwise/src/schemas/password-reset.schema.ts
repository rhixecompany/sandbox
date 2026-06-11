/**
 * Password reset Zod schemas
 * Validates password reset operations
 */

import { z } from "zod";

/**
 * Schema for requesting a password reset
 */
export const requestPasswordResetSchema = z.object({
  email: z.string().email("Valid email is required"),
});

export type RequestPasswordResetInput = z.infer<typeof requestPasswordResetSchema>;

/**
 * Schema for resetting a password
 */
export const resetPasswordSchema = z.object({
  token: z.string().min(1, "Token is required"),
  password: z
    .string()
    .min(8, "Password must be at least 8 characters")
    .max(100, "Password must be less than 100 characters"),
});

export type ResetPasswordInput = z.infer<typeof resetPasswordSchema>;
