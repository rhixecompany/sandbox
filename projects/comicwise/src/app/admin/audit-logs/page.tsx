/**
 * Audit Logs Admin Page
 * Route: /admin/audit-logs
 */

import { getAuditLogsAction } from "@/actions/admin/audit-log.actions";
import { AdminAuditLogsWrapper } from "@/components/admin/admin-audit-logs-wrapper";

export const metadata = {
  title: "Admin - Audit Logs",
};

export default async function AuditLogsPage() {
  const result = await getAuditLogsAction();
  const logs = result.ok ? result.data : [];

  return <AdminAuditLogsWrapper logs={logs} />;
}
