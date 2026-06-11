/**
 * Comic Pagination Controls (Client Component)
 * Section 23.3 from docs/dev.content.md
 */

"use client";

import { useRouter, useSearchParams } from "next/navigation";

import { Button } from "@/components/ui/button";

interface ComicPaginationControlsProps {
  page: number;
  query: string;
  totalPages: number;
}

export function ComicPaginationControls({ page, totalPages, query }: ComicPaginationControlsProps) {
  const router = useRouter();
  const searchParams = useSearchParams();

  const handlePageChange = (newPage: number) => {
    const params = new URLSearchParams(searchParams);
    params.set("page", newPage.toString());
    if (query) params.set("query", query);
    router.push(`?${params.toString()}`);
  };

  return (
    <div className="flex justify-center gap-2">
      <Button disabled={page === 1} onClick={() => handlePageChange(page - 1)} variant="outline">
        Previous
      </Button>

      {Array.from({ length: Math.min(5, totalPages) }).map((_, i) => {
        const pageNum = i + 1;
        return (
          <Button
            key={pageNum}
            onClick={() => handlePageChange(pageNum)}
            variant={page === pageNum ? "default" : "outline"}
          >
            {pageNum}
          </Button>
        );
      })}

      <Button
        data-testid="pagination-next"
        disabled={page === totalPages}
        onClick={() => handlePageChange(page + 1)}
        variant="outline"
      >
        Next
      </Button>
    </div>
  );
}
