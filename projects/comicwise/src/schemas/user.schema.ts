import { z } from "zod";

/**
 * User Schema (v1.0.0)
 * Normalized internal format for user data
 */
export const UserSchema = z.object({
  _version: z.literal("1.0.0").default("1.0.0"),
  id: z.string().uuid(),
  email: z.string().email(),
  name: z.string().nullish(),
  image: z.string().url().nullish(),
  role: z.enum(["user", "admin", "moderator"]),
  emailVerified: z.date().nullish(),
  lastActivityDate: z.date().nullish(),
  createdAt: z.date(),
  updatedAt: z.date(),
});

export type User = z.infer<typeof UserSchema>;

/**
 * @deprecated Use UserSchema. This union format was for scraper compatibility.
 */
export const UserSchemaLegacy = z.array(
  z.union([
    z.object({
      image: z.string(),
      email: z.string(),
      name: z.string(),
      id: z.string(),
      role: z.string(),
      status: z.boolean(),
      updatedAt: z.string(),
      createdAt: z.string(),
      lastActivityDate: z.null(),
      emailVerified: z.string(),
    }),
    z.object({
      image: z.string(),
      email: z.string(),
      name: z.string(),
      id: z.string(),
      role: z.string(),
      status: z.boolean(),
      updatedAt: z.string(),
      createdAt: z.string(),
      lastActivityDate: z.string(),
      emailVerified: z.string(),
    }),
  ])
);
