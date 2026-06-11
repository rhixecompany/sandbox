"use client";

import { DataTable } from "@/components/ui/data-table";

interface AuthorData {
  id: number;
  name: string;
}

interface AdminAuthorsWrapperProps {
  authors: AuthorData[];
}

export function AdminAuthorsWrapper({ authors }: AdminAuthorsWrapperProps) {
  const columns = [
    { key: "id" as const, header: "ID" },
    { key: "name" as const, header: "Name" },
  ];

  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Authors</h1>
      <DataTable columns={columns} data={authors} keyExtractor={(a) => a.id} />
    </div>
  );
}
