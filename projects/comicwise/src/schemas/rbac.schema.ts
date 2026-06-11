/**
 * RBAC-related Zod schemas
 * Validates role and permission operations
 */

import { z } from "zod";

/**
 * Schema for creating a role
 */
export const createRoleSchema = z.object({
  name: z.string().min(1, "Name is required").max(100),
  description: z.string().max(500).optional(),
  isSystem: z.boolean().optional().default(false),
});

export type CreateRoleInput = z.infer<typeof createRoleSchema>;

/**
 * Schema for updating a role
 */
export const updateRoleSchema = createRoleSchema.partial().extend({
  id: z.number().int().positive(),
});

export type UpdateRoleInput = z.infer<typeof updateRoleSchema>;

/**
 * Schema for creating a permission
 */
export const createPermissionSchema = z.object({
  name: z.string().min(1, "Name is required").max(100),
  description: z.string().max(500).optional(),
  resource: z.enum([
    "comic",
    "chapter",
    "user",
    "comment",
    "rating",
    "bookmark",
    "notification",
    "author",
    "artist",
    "genre",
    "type",
    "system",
  ]),
  action: z.enum(["create", "read", "update", "delete", "manage"]),
});

export type CreatePermissionInput = z.infer<typeof createPermissionSchema>;

/**
 * Schema for updating a permission
 */
export const updatePermissionSchema = createPermissionSchema.partial().extend({
  id: z.number().int().positive(),
});

export type UpdatePermissionInput = z.infer<typeof updatePermissionSchema>;

/**
 * Schema for assigning a role to a user
 */
export const assignRoleSchema = z.object({
  userId: z.string().min(1, "User ID is required"),
  roleId: z.number().int().positive(),
});

export type AssignRoleInput = z.infer<typeof assignRoleSchema>;

/**
 * Schema for removing a role from a user
 */
export const removeRoleSchema = z.object({
  userId: z.string().min(1, "User ID is required"),
  roleId: z.number().int().positive(),
});

export type RemoveRoleInput = z.infer<typeof removeRoleSchema>;
