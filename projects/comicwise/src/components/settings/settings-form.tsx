"use client";

/**
 * Settings Form Component
 * Manage user preferences with a form interface
 */

import { useState, useTransition } from "react";

import { updateUserPreferencesAction } from "@/actions/user-preferences.actions";

import type { UpdateUserPreferenceInput, UserPreference } from "@/types/user-preferences";

interface SettingsFormProps {
  initialPreferences: UserPreference;
}

export function SettingsForm({ initialPreferences }: SettingsFormProps) {
  const [preferences, setPreferences] = useState(initialPreferences);
  const [error, setError] = useState<null | string>(null);
  const [success, setSuccess] = useState(false);
  const [isPending, startTransition] = useTransition();

  const handleChange = <K extends keyof UpdateUserPreferenceInput>(key: K, value: UpdateUserPreferenceInput[K]) => {
    setPreferences((prev) => ({
      ...prev,
      [key]: value,
    }));
    setError(null);
    setSuccess(false);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(false);

    startTransition(async () => {
      const input: UpdateUserPreferenceInput = {
        theme: preferences.theme,
        defaultLayout: preferences.defaultLayout,
        pageNavigationStyle: preferences.pageNavigationStyle,
        fontSize: preferences.fontSize,
        lineHeight: preferences.lineHeight,
        notifyNewChapters: preferences.notifyNewChapters,
        notifyComments: preferences.notifyComments,
        notifyBookmarkUpdates: preferences.notifyBookmarkUpdates,
        profilePublic: preferences.profilePublic,
        showReadingHistory: preferences.showReadingHistory,
      };

      const result = await updateUserPreferencesAction(input);
      if (!result.ok) {
        setError(result.error);
      } else {
        setPreferences(result.data);
        setSuccess(true);
        setTimeout(() => setSuccess(false), 3000);
      }
    });
  };

  return (
    <form
      className="space-y-8"
      onSubmit={(e) => {
        void handleSubmit(e);
      }}
    >
      {/* Theme Section */}
      <div className="rounded-lg border bg-white p-6">
        <h2 className="mb-4 text-lg font-semibold text-gray-900">Appearance</h2>

        <div className="space-y-4">
          {/* Theme */}
          <div>
            <label className="mb-2 block text-sm font-medium text-gray-700">Theme</label>
            <select
              className="w-full rounded-lg border px-4 py-2 focus:border-transparent focus:ring-2 focus:ring-blue-500"
              onChange={(e) => handleChange("theme", e.target.value as "dark" | "light" | "system")}
              value={preferences.theme}
            >
              <option value="light">Light</option>
              <option value="dark">Dark</option>
              <option value="system">System</option>
            </select>
          </div>

          {/* Font Size */}
          <div>
            <label className="mb-2 block text-sm font-medium text-gray-700">Font Size: {preferences.fontSize}px</label>
            <input
              className="w-full"
              max="24"
              min="12"
              onChange={(e) => handleChange("fontSize", parseInt(e.target.value))}
              step="1"
              type="range"
              value={preferences.fontSize}
            />
          </div>

          {/* Line Height */}
          <div>
            <label className="mb-2 block text-sm font-medium text-gray-700">Line Height</label>
            <select
              className="w-full rounded-lg border px-4 py-2 focus:border-transparent focus:ring-2 focus:ring-blue-500"
              onChange={(e) => handleChange("lineHeight", e.target.value as "compact" | "normal" | "relaxed")}
              value={preferences.lineHeight}
            >
              <option value="compact">Compact</option>
              <option value="normal">Normal</option>
              <option value="relaxed">Relaxed</option>
            </select>
          </div>
        </div>
      </div>

      {/* Reading Preferences Section */}
      <div className="rounded-lg border bg-white p-6">
        <h2 className="mb-4 text-lg font-semibold text-gray-900">Reading Preferences</h2>

        <div className="space-y-4">
          {/* Layout */}
          <div>
            <label className="mb-2 block text-sm font-medium text-gray-700">Default Layout</label>
            <select
              className="w-full rounded-lg border px-4 py-2 focus:border-transparent focus:ring-2 focus:ring-blue-500"
              onChange={(e) => handleChange("defaultLayout", e.target.value as "book" | "comic" | "webtoon")}
              value={preferences.defaultLayout}
            >
              <option value="webtoon">Webtoon (Vertical)</option>
              <option value="comic">Comic (Horizontal)</option>
              <option value="book">Book (Double Page)</option>
            </select>
          </div>

          {/* Navigation Style */}
          <div>
            <label className="mb-2 block text-sm font-medium text-gray-700">Page Navigation</label>
            <select
              className="w-full rounded-lg border px-4 py-2 focus:border-transparent focus:ring-2 focus:ring-blue-500"
              onChange={(e) => handleChange("pageNavigationStyle", e.target.value as "buttons" | "click" | "swipe")}
              value={preferences.pageNavigationStyle}
            >
              <option value="buttons">Buttons</option>
              <option value="swipe">Swipe Gestures</option>
              <option value="click">Click to Navigate</option>
            </select>
          </div>
        </div>
      </div>

      {/* Notification Settings Section */}
      <div className="rounded-lg border bg-white p-6">
        <h2 className="mb-4 text-lg font-semibold text-gray-900">Notifications</h2>

        <div className="space-y-4">
          {[
            {
              key: "notifyNewChapters",
              label: "New Chapters",
              description: "Get notified when new chapters are released",
            },
            {
              key: "notifyComments",
              label: "Comments & Replies",
              description: "Get notified when someone replies to your comments",
            },
            {
              key: "notifyBookmarkUpdates",
              label: "Bookmark Updates",
              description: "Get notified about updates to your bookmarked comics",
            },
          ].map((notification) => (
            <label className="flex items-start" key={notification.key}>
              <input
                checked={preferences[notification.key as keyof typeof preferences] as boolean}
                className="mt-1 mr-3 h-4 w-4 rounded"
                onChange={(e) => handleChange(notification.key as keyof UpdateUserPreferenceInput, e.target.checked)}
                type="checkbox"
              />
              <div>
                <div className="font-medium text-gray-900">{notification.label}</div>
                <div className="text-sm text-gray-600">{notification.description}</div>
              </div>
            </label>
          ))}
        </div>
      </div>

      {/* Privacy Settings Section */}
      <div className="rounded-lg border bg-white p-6">
        <h2 className="mb-4 text-lg font-semibold text-gray-900">Privacy</h2>

        <div className="space-y-4">
          {[
            {
              key: "profilePublic",
              label: "Public Profile",
              description: "Allow others to view your profile",
            },
            {
              key: "showReadingHistory",
              label: "Show Reading History",
              description: "Display your reading history on your profile",
            },
          ].map((privacy) => (
            <label className="flex items-start" key={privacy.key}>
              <input
                checked={preferences[privacy.key as keyof typeof preferences] as boolean}
                className="mt-1 mr-3 h-4 w-4 rounded"
                onChange={(e) => handleChange(privacy.key as keyof UpdateUserPreferenceInput, e.target.checked)}
                type="checkbox"
              />
              <div>
                <div className="font-medium text-gray-900">{privacy.label}</div>
                <div className="text-sm text-gray-600">{privacy.description}</div>
              </div>
            </label>
          ))}
        </div>
      </div>

      {/* Error Message */}
      {error && <div className="rounded-lg border border-red-200 bg-red-50 p-4 text-red-700">{error}</div>}

      {/* Success Message */}
      {success && (
        <div className="rounded-lg border border-green-200 bg-green-50 p-4 text-green-700">
          Settings saved successfully!
        </div>
      )}

      {/* Submit Button */}
      <button
        className="w-full rounded-lg bg-blue-600 px-6 py-3 font-medium text-white transition-colors hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
        disabled={isPending}
        type="submit"
      >
        {isPending ? "Saving..." : "Save Settings"}
      </button>
    </form>
  );
}
