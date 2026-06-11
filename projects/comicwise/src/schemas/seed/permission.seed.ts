import { z } from "zod";

export const permissionSeedItemSchema = z.object({
  name: z.string().min(1),
  description: z.string().optional(),
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
  createdAt: z.date().optional(),
});

export const permissionSeedSchema = z.array(permissionSeedItemSchema);

export type PermissionSeedItem = z.infer<typeof permissionSeedItemSchema>;
export type PermissionSeed = z.infer<typeof permissionSeedSchema>;
