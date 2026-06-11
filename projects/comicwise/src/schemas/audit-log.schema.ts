/**
 * Audit log Zod schemas
 * Validates audit log queries
 */

import { z } from "zod";

/**
 * Schema for filtering audit logs
 */
export const auditLogFilterSchema = z.object({
  userId: z.string().optional(),
  action: z.string().optional(),
  resourceType: z.string().optional(),
  resourceId: z.string().optional(),
  startDate: z.date().optional(),
  endDate: z.date().optional(),
  page: z.number().int().min(1).optional().default(1),
  limit: z.number().int().min(1).max(100).optional().default(50),
});

export type AuditLogFilter = z.infer<typeof auditLogFilterSchema>;
