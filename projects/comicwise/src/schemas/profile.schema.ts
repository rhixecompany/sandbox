/**
 * User Profile Type Definitions
 */

import { z } from "zod";

export const ProfileUpdateSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters").max(100),
  email: z.string().email("Invalid email address").optional(),
  bio: z.string().max(500, "Bio must be less than 500 characters").optional(),
  image: z.string().url("Invalid image URL").optional(),
});

export type ProfileUpdateInput = z.infer<typeof ProfileUpdateSchema>;

export const ChangePasswordSchema = z
  .object({
    currentPassword: z.string().min(8, "Password must be at least 8 characters"),
    newPassword: z
      .string()
      .min(8, "Password must be at least 8 characters")
      .regex(/[A-Z]/, "Password must contain an uppercase letter")
      .regex(/[0-9]/, "Password must contain a number")
      .regex(/[^A-Za-z0-9]/, "Password must contain a special character"),
    confirmPassword: z.string(),
  })
  .refine((data) => data.newPassword === data.confirmPassword, {
    message: "Passwords don't match",
    path: ["confirmPassword"],
  })
  .refine((data) => data.currentPassword !== data.newPassword, {
    message: "New password must be different from current password",
    path: ["newPassword"],
  });

export type ChangePasswordInput = z.infer<typeof ChangePasswordSchema>;
