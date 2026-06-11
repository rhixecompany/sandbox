import { z } from "zod";

export const roleSeedItemSchema = z.object({
  name: z.string().min(1),
  description: z.string().optional(),
  isSystem: z.boolean().default(false),
  createdAt: z.date().optional(),
  updatedAt: z.date().optional(),
});

export const roleSeedSchema = z.array(roleSeedItemSchema);

export type RoleSeedItem = z.infer<typeof roleSeedItemSchema>;
export type RoleSeed = z.infer<typeof roleSeedSchema>;
