import { z } from "zod";

export const userRoleSeedItemSchema = z.object({
  userId: z.string().min(1),
  roleId: z.number().int().positive(),
  assignedBy: z.string().optional(),
  assignedAt: z.date().optional(),
});

export const userRoleSeedSchema = z.array(userRoleSeedItemSchema);

export type UserRoleSeedItem = z.infer<typeof userRoleSeedItemSchema>;
export type UserRoleSeed = z.infer<typeof userRoleSeedSchema>;
