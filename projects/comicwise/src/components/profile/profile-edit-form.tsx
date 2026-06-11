/**
 * Profile Edit Form Component
 * Client component for editing user profile
 */

"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";

import { updateProfileAction } from "@/actions/profile.actions";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

interface ProfileEditFormProps {
  initialData: {
    bio?: string;
    email: string;
    image?: string;
    name: string;
  };
}

export function ProfileEditForm({ initialData }: ProfileEditFormProps) {
  const router = useRouter();
  const [formData, setFormData] = useState({
    name: initialData.name,
    email: initialData.email,
    bio: initialData.bio || "",
    image: initialData.image || "",
  });
  const [error, setError] = useState<null | string>(null);
  const [success, setSuccess] = useState(false);
  const [isPending, startTransition] = useTransition();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    setError(null);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(false);

    if (!formData.name.trim()) {
      setError("Name is required");
      return;
    }

    startTransition(async () => {
      try {
        const result = await updateProfileAction(formData);
        if (result.ok) {
          setSuccess(true);
          setTimeout(() => {
            router.push("/profile");
          }, 1500);
        } else {
          setError(result.error);
        }
      } catch {
        setError("An error occurred while updating your profile");
      }
    });
  };

  return (
    <form
      className="space-y-6 rounded-lg border bg-card p-6"
      onSubmit={(e) => {
        void handleSubmit(e);
      }}
    >
      {/* Name Field */}
      <div>
        <label className="mb-2 block font-semibold">Name</label>
        <Input
          disabled={isPending}
          name="name"
          onChange={handleChange}
          placeholder="Your name"
          required
          type="text"
          value={formData.name}
        />
      </div>

      {/* Email Field */}
      <div>
        <label className="mb-2 block font-semibold">Email</label>
        <Input
          disabled={isPending}
          name="email"
          onChange={handleChange}
          placeholder="your.email@example.com"
          type="email"
          value={formData.email}
        />
        <p className="mt-1 text-xs text-muted-foreground">Update your contact email</p>
      </div>

      {/* Bio Field */}
      <div>
        <label className="mb-2 block font-semibold">Bio</label>
        <Textarea
          disabled={isPending}
          maxLength={500}
          name="bio"
          onChange={handleChange}
          placeholder="Tell us about yourself..."
          rows={4}
          value={formData.bio}
        />
        <p className="mt-1 text-xs text-muted-foreground">{formData.bio.length}/500 characters</p>
      </div>

      {/* Image URL Field */}
      <div>
        <label className="mb-2 block font-semibold">Profile Image URL</label>
        <Input
          disabled={isPending}
          name="image"
          onChange={handleChange}
          placeholder="https://example.com/image.jpg"
          type="url"
          value={formData.image}
        />
      </div>

      {/* Error Message */}
      {error && <div className="rounded-lg bg-destructive/10 p-3 text-sm text-destructive">{error}</div>}

      {/* Success Message */}
      {success && (
        <div className="rounded-lg bg-green-50 p-3 text-sm text-green-700 dark:bg-green-950/30 dark:text-green-300">
          Profile updated successfully. Redirecting...
        </div>
      )}

      {/* Action Buttons */}
      <div className="flex justify-end gap-3">
        <Button disabled={isPending} onClick={() => router.back()} type="button" variant="outline">
          Cancel
        </Button>
        <Button disabled={isPending} type="submit">
          {isPending ? "Saving..." : "Save Changes"}
        </Button>
      </div>
    </form>
  );
}
