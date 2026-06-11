/**
 * Author-related Zod schemas
 * Validates author queries, filters, and mutations
 */

import { z } from "zod";

/**
 * Schema for creating a new author (admin only)
 */
export const createAuthorSchema = z.object({
  name: z.string().min(1, "Name is required").max(255),
  bio: z.string().max(2000).optional(),
  image: z.string().url().optional().nullable(),
  isActive: z.boolean().optional().default(true),
});

export type CreateAuthorInput = z.infer<typeof createAuthorSchema>;

/**
 * Schema for updating an author
 */
export const updateAuthorSchema = createAuthorSchema.partial().extend({
  id: z.number().int().positive(),
});

export type UpdateAuthorInput = z.infer<typeof updateAuthorSchema>;

/**
 * Schema for filtering authors
 */
export const authorFilterSchema = z.object({
  search: z.string().optional().default(""),
  isActive: z.boolean().optional(),
  page: z.number().int().min(1).optional().default(1),
  limit: z.number().int().min(1).max(50).optional().default(20),
});

export type AuthorFilter = z.infer<typeof authorFilterSchema>;
