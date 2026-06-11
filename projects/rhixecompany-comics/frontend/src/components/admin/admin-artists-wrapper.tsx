"use client";

import { DataTable } from "@/components/ui/data-table";

interface ArtistData {
  id: number;
  name: string;
}

interface AdminArtistsWrapperProps {
  artists: ArtistData[];
}

export function AdminArtistsWrapper({ artists }: AdminArtistsWrapperProps) {
  const columns = [
    { key: "id" as const, header: "ID" },
    { key: "name" as const, header: "Name" },
  ];

  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Artists</h1>
      <DataTable columns={columns} data={artists} keyExtractor={(a) => a.id} />
    </div>
  );
}
