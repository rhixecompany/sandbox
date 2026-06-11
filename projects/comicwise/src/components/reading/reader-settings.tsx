"use client";

import { Settings, X } from "lucide-react";
import { useCallback, useEffect, useState } from "react";

import { Button } from "@/components/ui/button";
import { useReaderStore } from "@/stores/reader-store";

interface ReaderSettingsProps {
  isOpen: boolean;
  onClose: () => void;
}

export function ReaderSettings({ isOpen, onClose }: ReaderSettingsProps) {
  const { settings, updateSettings, resetSettings } = useReaderStore();
  // Initialize state from settings and keep them in sync via key prop on parent or controlled component pattern
  const [brightness, setBrightness] = useState(settings.brightness);
  const [contrast, setContrast] = useState(settings.contrast);

  // Update local state when settings change externally (e.g., from reset)
  // This is acceptable because it's derived state that should track the source
  useEffect(() => {
    if (brightness !== settings.brightness) {
      setBrightness(settings.brightness);
    }
    if (contrast !== settings.contrast) {
      setContrast(settings.contrast);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [settings.brightness, settings.contrast]);

  const handleBrightnessChange = useCallback(
    (value: number) => {
      setBrightness(value);
      updateSettings({ brightness: value });
    },
    [updateSettings]
  );

  const handleContrastChange = useCallback(
    (value: number) => {
      setContrast(value);
      updateSettings({ contrast: value });
    },
    [updateSettings]
  );

  const handleViewModeChange = useCallback(
    (mode: "double" | "single") => {
      updateSettings({ viewMode: mode });
    },
    [updateSettings]
  );

  const handleAutoScrollChange = useCallback(
    (enabled: boolean) => {
      updateSettings({ autoScroll: enabled });
    },
    [updateSettings]
  );

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
      <div className="w-full max-w-md rounded-lg bg-white p-6 shadow-lg dark:bg-gray-900">
        {/* Header */}
        <div className="flex items-center justify-between border-b pb-4">
          <div className="flex items-center gap-2">
            <Settings className="h-5 w-5" />
            <h2 className="text-lg font-semibold">Reader Settings</h2>
          </div>
          <Button className="h-8 w-8 p-0" onClick={onClose} size="sm" variant="ghost">
            <X className="h-4 w-4" />
          </Button>
        </div>

        {/* Settings Content */}
        <div className="space-y-6 py-4">
          {/* Brightness */}
          <div>
            <label className="mb-2 block text-sm font-medium">Brightness: {brightness}%</label>
            <input
              className="h-2 w-full cursor-pointer appearance-none rounded-lg bg-gray-200 dark:bg-gray-700"
              max="150"
              min="50"
              onChange={(e) => handleBrightnessChange(Number(e.target.value))}
              type="range"
              value={brightness}
            />
          </div>

          {/* Contrast */}
          <div>
            <label className="mb-2 block text-sm font-medium">Contrast: {contrast}%</label>
            <input
              className="h-2 w-full cursor-pointer appearance-none rounded-lg bg-gray-200 dark:bg-gray-700"
              max="150"
              min="50"
              onChange={(e) => handleContrastChange(Number(e.target.value))}
              type="range"
              value={contrast}
            />
          </div>

          {/* View Mode */}
          <div>
            <label className="mb-2 block text-sm font-medium">View Mode</label>
            <div className="flex gap-2">
              <Button
                className="flex-1"
                onClick={() => handleViewModeChange("single")}
                size="sm"
                variant={settings.viewMode === "single" ? "default" : "outline"}
              >
                Single Page
              </Button>
              <Button
                className="flex-1"
                onClick={() => handleViewModeChange("double")}
                size="sm"
                variant={settings.viewMode === "double" ? "default" : "outline"}
              >
                Double Page
              </Button>
            </div>
          </div>

          {/* Auto Scroll */}
          <div className="flex items-center justify-between">
            <label className="text-sm font-medium">Auto Scroll</label>
            <input
              checked={settings.autoScroll}
              className="h-4 w-4 cursor-pointer rounded border-gray-300"
              onChange={(e) => handleAutoScrollChange(e.target.checked)}
              type="checkbox"
            />
          </div>

          {/* Keyboard Shortcuts */}
          <div className="rounded bg-gray-100 p-3 dark:bg-gray-800">
            <p className="mb-2 text-xs font-semibold">Keyboard Shortcuts:</p>
            <ul className="space-y-1 text-xs text-gray-600 dark:text-gray-400">
              <li>
                <kbd>←</kbd> <kbd>→</kbd> Navigate pages
              </li>
              <li>
                <kbd>+</kbd> <kbd>−</kbd> Zoom in/out
              </li>
              <li>
                <kbd>R</kbd> Rotate image
              </li>
              <li>
                <kbd>0</kbd> Reset view
              </li>
              <li>
                <kbd>Ctrl</kbd> + Scroll Zoom
              </li>
            </ul>
          </div>
        </div>

        {/* Footer */}
        <div className="flex gap-2 border-t pt-4">
          <Button className="flex-1" onClick={() => resetSettings()} size="sm" variant="outline">
            Reset to Defaults
          </Button>
          <Button className="flex-1" onClick={onClose} size="sm">
            Done
          </Button>
        </div>
      </div>
    </div>
  );
}
