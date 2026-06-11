/**
 * Zod schema for User seed data with flexible type coercion
 * @module user.seed
 */

import { z } from "zod";

/**
 * Image URL or path validator - accepts URLs, local paths, and query parameters
 */
const imageField = z
  .string()
  .refine((val) => {
    // Accept URLs (http/https)
    if (val.startsWith("http://") || val.startsWith("https://")) {
      try {
        new URL(val);
        return true;
      } catch {
        return false;
      }
    }
    // Accept local paths and relative URLs
    return val.startsWith("/") || val.startsWith("./") || val.startsWith("../");
  }, "Image must be a valid URL or local path (starting with /, ./, ../)")
  .nullable()
  .optional();

/**
 * User seed schema with support for flexible date/UUID formats
 * Handles both string and Date inputs via coercion
 * Password is optional in seed data (can be generated or set separately)
 */
export const userSeedSchema = z.array(
  z.object({
    id: z.string().uuid().optional(),
    email: z.string().email("Invalid email format"),
    name: z.string().min(1, "Name is required"),
    password: z.string().min(6, "Password must be at least 6 characters").optional(),
    role: z.enum(["user", "admin", "moderator"]).default("user"),
    image: imageField,
    emailVerified: z.coerce.date().nullable().optional(),
    status: z.boolean().default(true),
    createdAt: z.coerce.date().default(() => new Date()),
    updatedAt: z.coerce.date().default(() => new Date()),
    lastActivityDate: z.coerce.date().nullable().optional(),
  })
);

/**
 * Inferred TypeScript type from the Zod schema
 */
export type UserSeed = z.infer<typeof userSeedSchema>;

/**
 * Single user seed item (not wrapped in array)
 */
export const userSeedItemSchema = userSeedSchema.element;
export type UserSeedItem = z.infer<typeof userSeedItemSchema>;
