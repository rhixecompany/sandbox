"use client";
import { ChevronLeft, ChevronRight } from "lucide-react";
import Image from "next/image";

import { Button } from "@/components/ui/button";
import { useReaderStore } from "@/stores/use-reader-store";

interface ReaderViewProps {
  chapterTitle: string;
  images: Array<{ id: number; imageUrl: string; pageNumber: number }>;
}

export function ReaderView({ images, chapterTitle }: ReaderViewProps) {
  const { currentPage, totalPages, setTotalPages, nextPage, prevPage } = useReaderStore();

  // Set total on mount
  if (totalPages !== images.length) setTotalPages(images.length);

  const current = images[currentPage - 1];

  return (
    <div className="flex flex-col items-center gap-4">
      <div className="flex w-full items-center justify-between px-4">
        <Button disabled={currentPage === 1} onClick={prevPage} size="icon" variant="outline">
          <ChevronLeft className="h-4 w-4" />
        </Button>
        <span className="text-sm text-muted-foreground">
          {chapterTitle} — Page {currentPage} / {totalPages}
        </span>
        <Button disabled={currentPage === totalPages} onClick={nextPage} size="icon" variant="outline">
          <ChevronRight className="h-4 w-4" />
        </Button>
      </div>
      {current && (
        <div className="relative w-full max-w-2xl">
          <Image
            alt={`Page ${current.pageNumber}`}
            className="w-full object-contain"
            height={1200}
            priority={currentPage <= 2}
            src={current.imageUrl}
            width={800}
          />
        </div>
      )}
    </div>
  );
}
