"use client";

/**
 * useKeyboardNavigation Hook
 * Handles keyboard shortcuts and common navigation patterns
 *
 * Reference: WCAG 2.1.1 Keyboard, Phase 4D Accessibility
 */

import { useEffect, useRef } from "react";

import { KEYBOARD_KEYS } from "@/lib/accessibility";

interface KeyboardNavigationOptions {
  enabled?: boolean;
  onArrowDown?: () => void;
  onArrowLeft?: () => void;
  onArrowRight?: () => void;
  onArrowUp?: () => void;
  onEnter?: () => void;
  onEscape?: () => void;
  onTab?: (shift: boolean) => void;
}

/**
 * Hook for handling keyboard navigation
 *
 * @param options Keyboard event handlers
 *
 * @example
 * ```tsx
 * useKeyboardNavigation({
 *   onEscape: () => closeDialog(),
 *   onArrowDown: () => moveToNextItem(),
 *   onEnter: () => selectCurrentItem(),
 * });
 * ```
 */
export function useKeyboardNavigation(options: KeyboardNavigationOptions): void {
  const { onEscape, onEnter, onArrowUp, onArrowDown, onArrowLeft, onArrowRight, onTab, enabled = true } = options;

  useEffect(() => {
    if (!enabled) return;

    const handleKeyDown = (event: KeyboardEvent) => {
      switch (event.key) {
        case KEYBOARD_KEYS.ESCAPE:
          if (onEscape) {
            event.preventDefault();
            onEscape();
          }
          break;

        case KEYBOARD_KEYS.ENTER:
        case " ": // Space also triggers buttons
          if (onEnter) {
            event.preventDefault();
            onEnter();
          }
          break;

        case KEYBOARD_KEYS.ARROW_UP:
          if (onArrowUp) {
            event.preventDefault();
            onArrowUp();
          }
          break;

        case KEYBOARD_KEYS.ARROW_DOWN:
          if (onArrowDown) {
            event.preventDefault();
            onArrowDown();
          }
          break;

        case KEYBOARD_KEYS.ARROW_LEFT:
          if (onArrowLeft) {
            event.preventDefault();
            onArrowLeft();
          }
          break;

        case KEYBOARD_KEYS.ARROW_RIGHT:
          if (onArrowRight) {
            event.preventDefault();
            onArrowRight();
          }
          break;

        case KEYBOARD_KEYS.TAB:
          if (onTab) {
            onTab(event.shiftKey);
          }
          break;

        default:
          break;
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [onEscape, onEnter, onArrowUp, onArrowDown, onArrowLeft, onArrowRight, onTab, enabled]);
}

/**
 * useFocusManagement Hook
 * Manages focus trap, focus restoration, and visible focus indicators
 *
 * Reference: WCAG 2.4.3 Focus Order, 2.4.7 Focus Visible
 */

interface FocusManagementOptions {
  autoFocus?: boolean; // Auto-focus first focusable element
  shouldRestoreFocus?: boolean; // Restore focus to trigger element on close
  shouldTrap?: boolean; // Trap focus within element (for modals)
}

/**
 * Hook for managing focus in dialogs/modals
 *
 * @param containerRef Reference to focusable container
 * @param options Focus management options
 * @returns Object with focus control methods
 *
 * @example
 * ```tsx
 * const dialogRef = useRef<HTMLDivElement>(null);
 * const { restoreFocus } = useFocusManagement(dialogRef, {
 *   shouldTrap: true,
 *   shouldRestoreFocus: true,
 * });
 *
 * const closeDialog = () => {
 *   restoreFocus();
 *   setOpen(false);
 * };
 * ```
 */
export function useFocusManagement(
  containerRef: React.RefObject<HTMLElement>,
  options: FocusManagementOptions = {}
): {
  restoreFocus: () => void;
  trapFocus: (event: React.KeyboardEvent) => void;
} {
  const { shouldTrap = true, shouldRestoreFocus = true, autoFocus = true } = options;

  const previouslyFocusedElementRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Store previously focused element for restoration
    if (shouldRestoreFocus) {
      previouslyFocusedElementRef.current = document.activeElement as HTMLElement;
    }

    // Auto-focus first focusable element
    if (autoFocus) {
      const focusableSelectors = [
        "button",
        "[href]",
        "input",
        "select",
        "textarea",
        "[tabindex]:not([tabindex='-1'])",
      ].join(",");

      const focusableElements = containerRef.current.querySelectorAll<HTMLElement>(focusableSelectors);
      if (focusableElements.length > 0) {
        focusableElements[0].focus();
      }
    }
  }, [shouldTrap, shouldRestoreFocus, autoFocus, containerRef]);

  const trapFocus = (event: React.KeyboardEvent) => {
    if (!shouldTrap || !containerRef.current) return;

    if (event.key !== KEYBOARD_KEYS.TAB) return;

    // Get all focusable elements
    const focusableSelectors = [
      "button",
      "[href]",
      "input",
      "select",
      "textarea",
      "[tabindex]:not([tabindex='-1'])",
    ].join(",");

    const focusableElements = containerRef.current.querySelectorAll<HTMLElement>(focusableSelectors);

    if (focusableElements.length === 0) return;

    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];
    const isShiftTab = event.shiftKey;

    // Tab from last element → focus first
    if (!isShiftTab && document.activeElement === lastElement) {
      event.preventDefault();
      firstElement.focus();
    }

    // Shift+Tab from first element → focus last
    if (isShiftTab && document.activeElement === firstElement) {
      event.preventDefault();
      lastElement.focus();
    }
  };

  const restoreFocus = () => {
    if (
      shouldRestoreFocus &&
      previouslyFocusedElementRef.current &&
      previouslyFocusedElementRef.current instanceof HTMLElement
    ) {
      previouslyFocusedElementRef.current.focus();
    }
  };

  return { trapFocus, restoreFocus };
}

/**
 * useAccessibleAnnouncement Hook
 * Announces updates to screen readers using aria-live regions
 *
 * Reference: WCAG 4.1.3 Status Messages
 */

type AnnouncementPoliteness = "assertive" | "polite";

/**
 * Hook for announcing messages to screen readers
 *
 * @param containerId ID of aria-live region container
 * @returns Function to announce messages
 *
 * @example
 * ```tsx
 * const announce = useAccessibleAnnouncement("announcer");
 *
 * const handleError = (error: string) => {
 *   announce(error, "assertive");
 * };
 * ```
 */
export function useAccessibleAnnouncement(
  containerId = "announcer"
): (message: string, politeness?: AnnouncementPoliteness) => void {
  return (message: string, politeness: AnnouncementPoliteness = "polite") => {
    const container = document.getElementById(containerId);
    if (!container) {
      console.warn(`Announcement container with id '${containerId}' not found. Add a div with aria-live region.`);
      return;
    }

    // Set politeness level
    container.setAttribute("aria-live", politeness);

    // Clear previous content
    container.textContent = "";

    // Force reflow to trigger announcement
    void container.offsetHeight;

    // Add new content
    container.textContent = message;
  };
}

/**
 * Example: How to use useAccessibleAnnouncement in a component
 *
 * See AccessibilityAnnouncer component for complete example with forms
 */
