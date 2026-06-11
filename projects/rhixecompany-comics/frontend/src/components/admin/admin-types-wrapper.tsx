"use client";

import { DataTable } from "@/components/ui/data-table";

interface TypeData {
  id: number;
  name: string;
}

interface AdminTypesWrapperProps {
  types: TypeData[];
}

export function AdminTypesWrapper({ types }: AdminTypesWrapperProps) {
  const columns = [
    { key: "id" as const, header: "ID" },
    { key: "name" as const, header: "Name" },
  ];

  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Comic Types</h1>
      <DataTable columns={columns} data={types} keyExtractor={(t) => t.id} />
    </div>
  );
}
