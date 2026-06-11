"use client";

import { ChevronLeft, ChevronRight, RotateCcw, ZoomIn, ZoomOut } from "lucide-react";
import Image from "next/image";
import { useCallback, useEffect, useRef, useState } from "react";

import { Button } from "@/components/ui/button";

interface ImageViewerProps {
  chapterTitle?: string;
  currentPageIndex: number;
  images: string[];
  onPageChange: (index: number) => void;
}

export function ImageViewer({ images, currentPageIndex, onPageChange, chapterTitle }: ImageViewerProps) {
  const [zoom, setZoom] = useState(100);
  const [rotation, setRotation] = useState(0);
  const containerRef = useRef<HTMLDivElement>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [dragStart, setDragStart] = useState({ x: 0, y: 0 });
  const [panPos, setPanPos] = useState({ x: 0, y: 0 });
  const [touchStart, setTouchStart] = useState({ x: 0, y: 0 });

  // Handle zoom
  const handleZoom = useCallback((delta: number) => {
    setZoom((prev) => Math.max(50, Math.min(300, prev + delta)));
  }, []);

  // Handle rotation
  const handleRotate = useCallback(() => {
    setRotation((prev) => (prev + 90) % 360);
  }, []);

  // Handle keyboard shortcuts
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "ArrowLeft") {
        onPageChange(Math.max(0, currentPageIndex - 1));
      } else if (e.key === "ArrowRight") {
        onPageChange(Math.min(images.length - 1, currentPageIndex + 1));
      } else if (e.key === "+") {
        handleZoom(10);
      } else if (e.key === "-") {
        handleZoom(-10);
      } else if (e.key === "r") {
        handleRotate();
      } else if (e.key === "0") {
        setZoom(100);
        setRotation(0);
        setPanPos({ x: 0, y: 0 });
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [currentPageIndex, images.length, onPageChange, handleZoom, handleRotate]);

  // Handle mouse wheel for zoom
  useEffect(() => {
    const handleWheel = (e: WheelEvent) => {
      if (e.ctrlKey) {
        e.preventDefault();
        handleZoom(e.deltaY < 0 ? 10 : -10);
      }
    };

    const container = containerRef.current;
    if (container) {
      container.addEventListener("wheel", handleWheel, { passive: false });
      return () => container.removeEventListener("wheel", handleWheel);
    }
  }, [handleZoom]);

  // Handle mouse drag for panning
  const handleMouseDown = (e: React.MouseEvent) => {
    if (zoom <= 100) return;
    setIsDragging(true);
    setDragStart({ x: e.clientX - panPos.x, y: e.clientY - panPos.y });
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!isDragging) return;
    setPanPos({
      x: e.clientX - dragStart.x,
      y: e.clientY - dragStart.y,
    });
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  // Handle touch swipe for page navigation (mobile/tablet)
  const handleTouchStart = (e: React.TouchEvent) => {
    if (e.touches.length === 1) {
      setTouchStart({ x: e.touches[0].clientX, y: e.touches[0].clientY });
    }
  };

  const handleTouchEnd = (e: React.TouchEvent) => {
    if (e.changedTouches.length === 1) {
      const touchEnd = { x: e.changedTouches[0].clientX, y: e.changedTouches[0].clientY };
      const swipeThreshold = 50; // Minimum pixels for swipe detection
      const deltaX = touchEnd.x - touchStart.x;
      const deltaY = touchEnd.y - touchStart.y;

      // Detect horizontal swipe (ignore small movements and vertical swipes)
      if (Math.abs(deltaX) > swipeThreshold && Math.abs(deltaX) > Math.abs(deltaY)) {
        if (deltaX > 0) {
          // Swiped right - go to previous page
          goToPreviousPage();
        } else {
          // Swiped left - go to next page
          goToNextPage();
        }
      }
    }
  };

  // Navigation handlers
  const goToPreviousPage = () => {
    onPageChange(Math.max(0, currentPageIndex - 1));
  };

  const goToNextPage = () => {
    onPageChange(Math.min(images.length - 1, currentPageIndex + 1));
  };

  const currentImage = images[currentPageIndex];

  return (
    <div className="flex h-full flex-col bg-black text-white">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-gray-700 px-4 py-3">
        <div className="flex-1">
          <h3 className="text-sm font-medium">{chapterTitle}</h3>
          <p className="text-xs text-gray-400">
            Page {currentPageIndex + 1} of {images.length}
          </p>
        </div>

        {/* Zoom & Rotation Controls */}
        <div className="flex items-center gap-2">
          <Button
            className="hover:bg-gray-700"
            onClick={() => handleZoom(-10)}
            size="sm"
            title="Zoom Out (- key)"
            variant="ghost"
          >
            <ZoomOut className="h-4 w-4" />
          </Button>
          <span className="w-12 text-center text-sm">{zoom}%</span>
          <Button
            className="hover:bg-gray-700"
            onClick={() => handleZoom(10)}
            size="sm"
            title="Zoom In (+ key)"
            variant="ghost"
          >
            <ZoomIn className="h-4 w-4" />
          </Button>
          <div className="mx-1 h-4 w-px bg-gray-600" />
          <Button className="hover:bg-gray-700" onClick={handleRotate} size="sm" title="Rotate (r key)" variant="ghost">
            <RotateCcw className="h-4 w-4" />
          </Button>
          <Button
            className="text-xs hover:bg-gray-700"
            onClick={() => {
              setZoom(100);
              setRotation(0);
              setPanPos({ x: 0, y: 0 });
            }}
            size="sm"
            title="Reset (0 key)"
            variant="ghost"
          >
            Reset
          </Button>
        </div>
      </div>

      {/* Image Container */}
      <div
        className="flex-1 overflow-hidden bg-black"
        onMouseDown={handleMouseDown}
        onMouseLeave={handleMouseUp}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
        onTouchEnd={handleTouchEnd}
        onTouchStart={handleTouchStart}
        ref={containerRef}
        style={{ cursor: isDragging ? "grabbing" : "grab" }}
      >
        <div className="flex h-full items-center justify-center">
          <div
            style={{
              transform: `scale(${zoom / 100}) rotate(${rotation}deg) translate(${panPos.x}px, ${panPos.y}px)`,
              transformOrigin: "center",
              transition: isDragging ? "none" : "transform 0.2s ease-out",
            }}
          >
            {currentImage ? (
              <Image
                alt={`Page ${currentPageIndex + 1}`}
                className="max-h-[80vh] w-auto object-contain"
                height={1600}
                priority
                src={currentImage}
                width={1200}
              />
            ) : (
              <div className="flex h-96 w-96 items-center justify-center rounded bg-gray-800">
                <span className="text-gray-400">No image</span>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Navigation Footer */}
      <div className="flex items-center justify-between border-t border-gray-700 px-4 py-3">
        <Button
          className="gap-2"
          disabled={currentPageIndex === 0}
          onClick={goToPreviousPage}
          size="sm"
          title="Previous Page (← key)"
          variant="outline"
        >
          <ChevronLeft className="h-4 w-4" />
          Previous
        </Button>

        {/* Page Indicator */}
        <div className="flex items-center gap-2">
          <input
            className="w-12 rounded border border-gray-600 bg-gray-700 px-2 py-1 text-center text-sm text-white"
            max={images.length}
            min={1}
            onChange={(e) => {
              const page = Math.max(1, Math.min(images.length, parseInt(e.target.value) || 1));
              onPageChange(page - 1);
            }}
            type="number"
            value={currentPageIndex + 1}
          />
          <span className="text-sm text-gray-400">/ {images.length}</span>
        </div>

        <Button
          className="gap-2"
          disabled={currentPageIndex === images.length - 1}
          onClick={goToNextPage}
          size="sm"
          title="Next Page (→ key)"
          variant="outline"
        >
          Next
          <ChevronRight className="h-4 w-4" />
        </Button>
      </div>

      {/* Keyboard Help */}
      <div className="border-t border-gray-700 bg-gray-900 px-4 py-2 text-xs text-gray-400">
        <span>← → navigate • +/- zoom • R rotate • 0 reset • Ctrl+Scroll zoom</span>
      </div>
    </div>
  );
}
