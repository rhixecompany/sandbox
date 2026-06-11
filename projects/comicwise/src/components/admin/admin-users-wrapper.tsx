"use client";

import { DataTable } from "@/components/ui/data-table";

interface UserData {
  createdAt: Date | null;
  email: null | string;
  id: string;
  name: null | string;
  role: string;
}

interface AdminUsersWrapperProps {
  users: UserData[];
}

export function AdminUsersWrapper({ users }: AdminUsersWrapperProps) {
  const columns = [
    { key: "id" as const, header: "ID", render: (u: UserData) => u.id.slice(0, 8) + "…" },
    { key: "name" as const, header: "Name" },
    { key: "email" as const, header: "Email" },
    { key: "role" as const, header: "Role" },
    { key: "createdAt" as const, header: "Joined", render: (u: UserData) => u.createdAt?.toLocaleDateString() ?? "" },
  ];

  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Users</h1>
      <DataTable columns={columns} data={users} keyExtractor={(u) => u.id} />
    </div>
  );
}
