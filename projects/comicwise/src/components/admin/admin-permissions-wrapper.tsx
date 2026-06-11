"use client";

interface PermissionData {
  action: string;
  description?: null | string;
  id: number | string;
  name: string;
  resource: string;
}

interface AdminPermissionsWrapperProps {
  permissions: Array<{
    action: string;
    description?: null | string;
    id: number | string;
    name: string;
    resource: string;
  }>;
}

export function AdminPermissionsWrapper({ permissions }: AdminPermissionsWrapperProps) {
  return (
    <div className="container mx-auto py-8">
      <h1 className="mb-6 text-2xl font-bold">Permissions Management</h1>
      <div className="rounded-lg border">
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th className="p-4 text-left">ID</th>
              <th className="p-4 text-left">Name</th>
              <th className="p-4 text-left">Resource</th>
              <th className="p-4 text-left">Action</th>
              <th className="p-4 text-left">Description</th>
            </tr>
          </thead>
          <tbody>
            {permissions.length === 0 ? (
              <tr>
                <td className="p-4 text-center text-muted-foreground" colSpan={5}>
                  No permissions found
                </td>
              </tr>
            ) : (
              permissions.map((permission: PermissionData) => (
                <tr className="border-b" key={permission.id}>
                  <td className="p-4">{permission.id}</td>
                  <td className="p-4 font-medium">{permission.name}</td>
                  <td className="p-4">{permission.resource}</td>
                  <td className="p-4">{permission.action}</td>
                  <td className="p-4">{permission.description ?? "-"}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
