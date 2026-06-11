/**
 * Zod schema for Type seed data
 * @module type.seed
 */

import { z } from "zod";

/**
 * Type seed item schema
 */
export const typeSeedItemSchema = z.object({
  name: z.string().min(1, "Type name is required"),
  description: z.string().optional(),
});

/**
 * Array schema for multiple types
 */
export const typeSeedSchema = z.array(typeSeedItemSchema);

/**
 * Inferred types
 */
export type TypeSeed = z.infer<typeof typeSeedItemSchema>;
export type TypeSeedArray = z.infer<typeof typeSeedSchema>;
