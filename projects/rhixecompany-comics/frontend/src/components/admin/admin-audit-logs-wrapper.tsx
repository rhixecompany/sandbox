"use client";

interface AuditLogData {
  action: string;
  createdAt: Date;
  details?: null | string;
  id: string;
  resource: string;
  userId: null | string;
}

interface AdminAuditLogsWrapperProps {
  logs: AuditLogData[];
}

export function AdminAuditLogsWrapper({ logs }: AdminAuditLogsWrapperProps) {
  return (
    <div className="container mx-auto py-8">
      <h1 className="mb-6 text-2xl font-bold">Audit Logs</h1>
      <div className="rounded-lg border">
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th className="p-4 text-left">ID</th>
              <th className="p-4 text-left">User</th>
              <th className="p-4 text-left">Action</th>
              <th className="p-4 text-left">Resource</th>
              <th className="p-4 text-left">Details</th>
              <th className="p-4 text-left">Date</th>
            </tr>
          </thead>
          <tbody>
            {logs.length === 0 ? (
              <tr>
                <td className="p-4 text-center text-muted-foreground" colSpan={6}>
                  No audit logs found
                </td>
              </tr>
            ) : (
              logs.map((log: AuditLogData) => (
                <tr className="border-b" key={log.id}>
                  <td className="p-4 text-sm">{log.id.slice(0, 8)}...</td>
                  <td className="p-4">{log.userId ?? "-"}</td>
                  <td className="p-4">
                    <span className="rounded bg-secondary px-2 py-1 text-xs">{log.action}</span>
                  </td>
                  <td className="p-4">{log.resource}</td>
                  <td className="p-4 text-sm text-muted-foreground">
                    {log.details ? JSON.stringify(log.details).slice(0, 50) : "-"}
                  </td>
                  <td className="p-4 text-sm">{new Date(log.createdAt).toLocaleString()}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
