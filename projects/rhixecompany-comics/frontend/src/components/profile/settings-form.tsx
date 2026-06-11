/**
 * Settings Form Component
 * Client component for managing user preferences
 */

"use client";

import { useState, useTransition } from "react";

import { updateUserPreferencesAction } from "@/actions/user-preferences.actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Slider } from "@/components/ui/slider";
import { Switch } from "@/components/ui/switch";

interface UserPreference {
  defaultLayout: "book" | "comic" | "webtoon";
  fontSize: number;
  lineHeight: "compact" | "normal" | "relaxed";
  notifyBookmarkUpdates: boolean;
  notifyComments: boolean;
  notifyNewChapters: boolean;
  pageNavigationStyle: "buttons" | "click" | "swipe";
  profilePublic: boolean;
  showReadingHistory: boolean;
  theme: "dark" | "light" | "system";
}

interface SettingsFormProps {
  initialData: UserPreference;
}

export default function SettingsForm({ initialData }: SettingsFormProps) {
  const [formData, setFormData] = useState(initialData);
  const [error, setError] = useState<null | string>(null);
  const [success, setSuccess] = useState(false);
  const [isPending, startTransition] = useTransition();

  const handleSelectChange = (field: string, value: string) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
    setError(null);
  };

  const handleToggle = (field: string, checked: boolean) => {
    setFormData((prev) => ({ ...prev, [field]: checked }));
    setError(null);
  };

  const handleSliderChange = (field: string, value: number[]) => {
    setFormData((prev) => ({ ...prev, [field]: value[0] }));
    setError(null);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(false);

    startTransition(async () => {
      const result = await updateUserPreferencesAction(formData);

      if (!result.ok) {
        setError(result.error);
        return;
      }

      setSuccess(true);
      setTimeout(() => setSuccess(false), 3000);
    });
  };

  return (
    <form
      className="space-y-6"
      onSubmit={(e) => {
        void handleSubmit(e);
      }}
    >
      {/* Theme & Display Section */}
      <Card>
        <CardHeader>
          <CardTitle>Display</CardTitle>
          <CardDescription>Customize how content is displayed</CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Theme */}
          <div className="space-y-2">
            <Label htmlFor="theme">Theme</Label>
            <Select onValueChange={(value) => handleSelectChange("theme", value)} value={formData.theme}>
              <SelectTrigger id="theme">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="light">Light</SelectItem>
                <SelectItem value="dark">Dark</SelectItem>
                <SelectItem value="system">System</SelectItem>
              </SelectContent>
            </Select>
          </div>

          {/* Font Size */}
          <div className="space-y-3">
            <div className="flex justify-between">
              <Label htmlFor="fontSize">Font Size</Label>
              <span className="text-sm text-muted-foreground">{formData.fontSize}px</span>
            </div>
            <Slider
              className="w-full"
              id="fontSize"
              max={24}
              min={12}
              onValueChange={(value) => handleSliderChange("fontSize", value)}
              step={1}
              value={[formData.fontSize]}
            />
          </div>

          {/* Line Height */}
          <div className="space-y-2">
            <Label htmlFor="lineHeight">Line Height</Label>
            <Select onValueChange={(value) => handleSelectChange("lineHeight", value)} value={formData.lineHeight}>
              <SelectTrigger id="lineHeight">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="compact">Compact</SelectItem>
                <SelectItem value="normal">Normal</SelectItem>
                <SelectItem value="relaxed">Relaxed</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </CardContent>
      </Card>

      {/* Reading Preferences Section */}
      <Card>
        <CardHeader>
          <CardTitle>Reading Preferences</CardTitle>
          <CardDescription>Customize your reading experience</CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Default Layout */}
          <div className="space-y-2">
            <Label htmlFor="defaultLayout">Default Layout</Label>
            <Select
              onValueChange={(value) => handleSelectChange("defaultLayout", value)}
              value={formData.defaultLayout}
            >
              <SelectTrigger id="defaultLayout">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="webtoon">Webtoon (Vertical scroll)</SelectItem>
                <SelectItem value="comic">Comic (Page grid)</SelectItem>
                <SelectItem value="book">Book (Spread view)</SelectItem>
              </SelectContent>
            </Select>
          </div>

          {/* Page Navigation */}
          <div className="space-y-2">
            <Label htmlFor="pageNavigationStyle">Page Navigation</Label>
            <Select
              onValueChange={(value) => handleSelectChange("pageNavigationStyle", value)}
              value={formData.pageNavigationStyle}
            >
              <SelectTrigger id="pageNavigationStyle">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="buttons">Buttons</SelectItem>
                <SelectItem value="swipe">Swipe / Tap</SelectItem>
                <SelectItem value="click">Click anywhere</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </CardContent>
      </Card>

      {/* Notification Preferences Section */}
      <Card>
        <CardHeader>
          <CardTitle>Notifications</CardTitle>
          <CardDescription>Choose what notifications you&apos;d like to receive</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-center justify-between">
            <div className="space-y-0.5">
              <Label htmlFor="notifyNewChapters">New Chapters</Label>
              <p className="text-sm text-muted-foreground">Get notified when new chapters are released</p>
            </div>
            <Switch
              checked={formData.notifyNewChapters}
              id="notifyNewChapters"
              onCheckedChange={(checked) => handleToggle("notifyNewChapters", checked)}
            />
          </div>

          <div className="flex items-center justify-between">
            <div className="space-y-0.5">
              <Label htmlFor="notifyComments">Comments</Label>
              <p className="text-sm text-muted-foreground">Get notified when someone replies to your comments</p>
            </div>
            <Switch
              checked={formData.notifyComments}
              id="notifyComments"
              onCheckedChange={(checked) => handleToggle("notifyComments", checked)}
            />
          </div>

          <div className="flex items-center justify-between">
            <div className="space-y-0.5">
              <Label htmlFor="notifyBookmarkUpdates">Bookmark Updates</Label>
              <p className="text-sm text-muted-foreground">Get notified about updates to your bookmarked comics</p>
            </div>
            <Switch
              checked={formData.notifyBookmarkUpdates}
              id="notifyBookmarkUpdates"
              onCheckedChange={(checked) => handleToggle("notifyBookmarkUpdates", checked)}
            />
          </div>
        </CardContent>
      </Card>

      {/* Privacy Preferences Section */}
      <Card>
        <CardHeader>
          <CardTitle>Privacy</CardTitle>
          <CardDescription>Control your privacy settings and what others can see</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-center justify-between">
            <div className="space-y-0.5">
              <Label htmlFor="profilePublic">Public Profile</Label>
              <p className="text-sm text-muted-foreground">Allow others to view your profile</p>
            </div>
            <Switch
              checked={formData.profilePublic}
              id="profilePublic"
              onCheckedChange={(checked) => handleToggle("profilePublic", checked)}
            />
          </div>

          <div className="flex items-center justify-between">
            <div className="space-y-0.5">
              <Label htmlFor="showReadingHistory">Reading History</Label>
              <p className="text-sm text-muted-foreground">Show what you&apos;re reading to others</p>
            </div>
            <Switch
              checked={formData.showReadingHistory}
              id="showReadingHistory"
              onCheckedChange={(checked) => handleToggle("showReadingHistory", checked)}
            />
          </div>
        </CardContent>
      </Card>

      {/* Error and Success Messages */}
      {error && <div className="rounded-lg bg-destructive/10 p-4 text-destructive">{error}</div>}

      {success && <div className="rounded-lg bg-green-500/10 p-4 text-green-600">Settings saved successfully!</div>}

      {/* Submit Button */}
      <div className="flex gap-4">
        <Button className="flex-1" disabled={isPending} type="submit">
          {isPending ? "Saving..." : "Save Settings"}
        </Button>
        <Button onClick={() => window.history.back()} type="button" variant="outline">
          Cancel
        </Button>
      </div>
    </form>
  );
}
