"use client";

interface RoleType {
  description: null | string;
  id: number;
  isSystem: boolean;
  name: string;
}

interface AdminRolesWrapperProps {
  roles: RoleType[];
}

export function AdminRolesWrapper({ roles }: AdminRolesWrapperProps) {
  return (
    <div className="container mx-auto py-8">
      <h1 className="mb-6 text-2xl font-bold">Roles Management</h1>
      <div className="rounded-lg border">
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th className="p-4 text-left">ID</th>
              <th className="p-4 text-left">Name</th>
              <th className="p-4 text-left">Description</th>
              <th className="p-4 text-left">System</th>
              <th className="p-4 text-left">Actions</th>
            </tr>
          </thead>
          <tbody>
            {roles.length === 0 ? (
              <tr>
                <td className="p-4 text-center text-muted-foreground" colSpan={5}>
                  No roles found
                </td>
              </tr>
            ) : (
              roles.map((role: RoleType) => (
                <tr className="border-b" key={role.id}>
                  <td className="p-4">{role.id}</td>
                  <td className="p-4 font-medium">{role.name}</td>
                  <td className="p-4">{role.description ?? "-"}</td>
                  <td className="p-4">{role.isSystem ? "Yes" : "No"}</td>
                  <td className="p-4">
                    <button className="text-primary hover:underline">Edit</button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
