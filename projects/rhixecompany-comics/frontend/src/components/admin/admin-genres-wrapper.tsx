"use client";

import { DataTable } from "@/components/ui/data-table";

interface GenreData {
  id: number;
  name: string;
  slug: string;
}

interface AdminGenresWrapperProps {
  genres: GenreData[];
}

export function AdminGenresWrapper({ genres }: AdminGenresWrapperProps) {
  const columns = [
    { key: "id" as const, header: "ID" },
    { key: "name" as const, header: "Name" },
    { key: "slug" as const, header: "Slug" },
  ];

  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Genres</h1>
      <DataTable columns={columns} data={genres} keyExtractor={(g) => g.id} />
    </div>
  );
}
