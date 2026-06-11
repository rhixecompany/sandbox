"use server";

import { auth } from "@/auth";
import { auditLogDal } from "@/dal/audit-log-dal";
import type { ActionResult } from "@/types/actions-types";

type AuditLogType = Awaited<ReturnType<typeof auditLogDal.list>>[number];

export async function getAuditLogsAction(): Promise<ActionResult<AuditLogType[]>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    return { ok: false, error: "Forbidden" };
  }
  try {
    const auditLogs = await auditLogDal.list({ limit: 100 });
    return { ok: true, data: auditLogs };
  } catch (error) {
    console.error("[getAuditLogsAction]", error);
    return { ok: false, error: "Failed to fetch audit logs" };
  }
}
