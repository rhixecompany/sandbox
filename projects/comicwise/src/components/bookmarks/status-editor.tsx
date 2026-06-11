"use client";

import { Loader2 } from "lucide-react";
import { useCallback, useRef, useState, useTransition } from "react";

import { updateBookmarkStatusAction } from "@/actions/bookmark.actions";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { useFocusManagement } from "@/hooks/use-keyboard-navigation";
import { useBookmarkStore } from "@/stores/use-bookmark-store";

import type { BookmarkStatus } from "@/schemas/bookmark-schema";

interface StatusEditorProps {
  /**
   * Comic ID to update
   */
  comicId: number;

  /**
   * Comic title (for display in modal)
   */
  comicTitle?: string;

  /**
   * Current bookmark status
   */
  currentStatus?: BookmarkStatus;

  /**
   * Whether modal is open
   */
  isOpen: boolean;

  /**
   * Callback when modal should close
   */
  onOpenChange: (open: boolean) => void;

  /**
   * Callback after status is updated
   */
  onStatusChange?: (newStatus: BookmarkStatus) => void;
}

/**
 * StatusEditor
 *
 * Modal dialog for changing a bookmark's status.
 * Features:
 * - Shows all 5 status options
 * - Visual indication of current status
 * - Loading state during save
 * - Error handling
 * - Optimistic UI update
 * - Accessible dialog
 *
 * Usage:
 * ```tsx
 * const [isOpen, setIsOpen] = useState(false);
 *
 * return (
 *   <>
 *     <button onClick={() => setIsOpen(true)}>Change Status</button>
 *     <StatusEditor
 *       comicId={123}
 *       comicTitle="Manga Title"
 *       currentStatus="Reading"
 *       isOpen={isOpen}
 *       onOpenChange={setIsOpen}
 *       onStatusChange={(status) => console.log(status)}
 *     />
 *   </>
 * );
 * ```
 */
export function StatusEditor({
  comicId,
  comicTitle,
  currentStatus,
  isOpen,
  onOpenChange,
  onStatusChange,
}: StatusEditorProps) {
  const [isPending, startTransition] = useTransition();
  const [selectedStatus, setSelectedStatus] = useState<BookmarkStatus | null>(currentStatus || null);
  const [error, setError] = useState<null | string>(null);
  const dialogRef = useRef<HTMLDivElement>(null!);

  // Focus management for accessibility
  const { restoreFocus } = useFocusManagement(dialogRef, {
    shouldTrap: true,
    shouldRestoreFocus: true,
    autoFocus: true,
  });

  // Zustand store for optimistic updates
  const updateBookmark = useBookmarkStore((state) => state.updateBookmark);

  // Status options with descriptions
  const statusOptions: Array<{
    color: string;
    description: string;
    label: string;
    value: BookmarkStatus;
  }> = [
    {
      value: "Reading",
      label: "Currently Reading",
      description: "I'm actively reading this comic",
      color: "bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400",
    },
    {
      value: "Plan to Read",
      label: "Plan to Read",
      description: "I want to read this comic later",
      color: "bg-purple-100 text-purple-700 dark:bg-purple-900/30 dark:text-purple-400",
    },
    {
      value: "Completed",
      label: "Completed",
      description: "I've finished this series",
      color: "bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400",
    },
    {
      value: "On Hold",
      label: "On Hold",
      description: "I'm paused, might continue later",
      color: "bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400",
    },
    {
      value: "Dropped",
      label: "Dropped",
      description: "I won't continue reading this",
      color: "bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400",
    },
  ];

  // Handle status change
  const handleStatusChange = useCallback((status: BookmarkStatus) => {
    setSelectedStatus(status);
    setError(null);
  }, []);

  // Handle save
  const handleSave = useCallback(() => {
    if (!selectedStatus) return;

    startTransition(async () => {
      try {
        const result = await updateBookmarkStatusAction({
          comicId,
          status: selectedStatus,
        });

        if (result.ok) {
          // Optimistic update
          updateBookmark(comicId, { status: selectedStatus });

          // Callback
          onStatusChange?.(selectedStatus);

          // Close modal
          onOpenChange(false);
        } else {
          setError(result.error || "Failed to update status");
        }
      } catch (err) {
        console.error("[StatusEditor]", err);
        setError("Something went wrong");
      }
    });
  }, [selectedStatus, comicId, updateBookmark, onStatusChange, onOpenChange]);

  // Handle dialog open change
  const handleOpenChange = (open: boolean) => {
    if (!open) {
      setError(null);
      // Reset selected status when closing
      setSelectedStatus(currentStatus || null);
      // Restore focus to the element that opened the dialog
      restoreFocus();
    }
    onOpenChange(open);
  };

  const hasChanged = selectedStatus !== currentStatus;

  return (
    <Dialog onOpenChange={handleOpenChange} open={isOpen}>
      <DialogContent className="max-w-sm" ref={dialogRef}>
        <DialogHeader>
          <DialogTitle>
            Change Status
            {comicTitle && <p className="mt-1 text-sm font-normal text-gray-600 dark:text-gray-400">{comicTitle}</p>}
          </DialogTitle>
          <DialogDescription>Select a new status for this comic</DialogDescription>
        </DialogHeader>

        {/* Status Options */}
        <div className="space-y-2 py-4">
          {statusOptions.map((option) => (
            <button
              className={`w-full rounded-lg border-2 p-3 text-left transition-all ${
                selectedStatus === option.value
                  ? "border-blue-500 bg-blue-50 dark:bg-blue-900/10"
                  : "border-gray-200 hover:border-gray-300 dark:border-gray-700 dark:hover:border-gray-600"
              }`}
              key={option.value}
              onClick={() => handleStatusChange(option.value)}
            >
              <div className="flex items-start gap-2">
                {/* Radio button */}
                <div
                  className={`mt-0.5 h-4 w-4 flex-shrink-0 rounded-full border-2 ${
                    selectedStatus === option.value
                      ? "border-blue-500 bg-blue-500"
                      : "border-gray-300 dark:border-gray-600"
                  }`}
                />

                {/* Label and description */}
                <div className="min-w-0 flex-1">
                  <div className="font-medium text-gray-900 dark:text-white">{option.label}</div>
                  <div className="text-xs text-gray-600 dark:text-gray-400">{option.description}</div>
                </div>

                {/* Status badge */}
                <span className={`ml-2 rounded px-2 py-0.5 text-xs font-medium whitespace-nowrap ${option.color}`}>
                  {option.label}
                </span>
              </div>
            </button>
          ))}
        </div>

        {/* Error message */}
        {error && (
          <div className="rounded-md bg-red-50 p-3 text-sm text-red-700 dark:bg-red-900/20 dark:text-red-400">
            {error}
          </div>
        )}

        {/* Actions */}
        <div className="flex gap-2 pt-4">
          <Button className="flex-1" disabled={isPending} onClick={() => handleOpenChange(false)} variant="outline">
            Cancel
          </Button>
          <Button className="flex-1" disabled={!hasChanged || isPending} onClick={handleSave}>
            {isPending && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            {isPending ? "Saving..." : "Save"}
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  );
}

export default StatusEditor;
