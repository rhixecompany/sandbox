/**
 * Type-related Zod schemas
 * Validates type queries, filters, and mutations
 */

import { z } from "zod";

/**
 * Schema for creating a new type (admin only)
 */
export const createTypeSchema = z.object({
  name: z.string().min(1, "Name is required").max(100),
  description: z.string().max(500).optional(),
  isActive: z.boolean().optional().default(true),
});

export type CreateTypeInput = z.infer<typeof createTypeSchema>;

/**
 * Schema for updating a type
 */
export const updateTypeSchema = createTypeSchema.partial().extend({
  id: z.number().int().positive(),
});

export type UpdateTypeInput = z.infer<typeof updateTypeSchema>;

/**
 * Schema for filtering types
 */
export const typeFilterSchema = z.object({
  search: z.string().optional().default(""),
  isActive: z.boolean().optional(),
  page: z.number().int().min(1).optional().default(1),
  limit: z.number().int().min(1).max(50).optional().default(20),
});

export type TypeFilter = z.infer<typeof typeFilterSchema>;
