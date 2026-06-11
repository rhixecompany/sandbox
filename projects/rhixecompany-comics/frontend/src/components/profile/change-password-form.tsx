/**
 * Change Password Form Component
 * Client component for changing user password
 */

"use client";

import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";

import { changePasswordAction } from "@/actions/profile.actions";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export function ChangePasswordForm() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    currentPassword: "",
    newPassword: "",
    confirmPassword: "",
  });
  const [error, setError] = useState<null | string>(null);
  const [success, setSuccess] = useState(false);
  const [isPending, startTransition] = useTransition();
  const [passwordStrength, setPasswordStrength] = useState<"medium" | "strong" | "weak">("weak");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    setError(null);

    // Calculate password strength
    if (name === "newPassword") {
      let strength = 0;
      if (value.length >= 8) strength++;
      if (/[A-Z]/.test(value)) strength++;
      if (/[0-9]/.test(value)) strength++;
      if (/[^A-Za-z0-9]/.test(value)) strength++;

      if (strength <= 1) setPasswordStrength("weak");
      else if (strength === 2) setPasswordStrength("medium");
      else setPasswordStrength("strong");
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(false);

    if (formData.newPassword !== formData.confirmPassword) {
      setError("Passwords don't match");
      return;
    }

    startTransition(async () => {
      try {
        const result = await changePasswordAction(formData);
        if (result.ok) {
          setSuccess(true);
          setFormData({
            currentPassword: "",
            newPassword: "",
            confirmPassword: "",
          });
          setTimeout(() => {
            router.push("/profile");
          }, 1500);
        } else {
          setError(result.error);
        }
      } catch {
        setError("An error occurred while changing your password");
      }
    });
  };

  return (
    <form
      className="space-y-6 rounded-lg border border-border bg-card p-8"
      onSubmit={(e) => {
        void handleSubmit(e);
      }}
    >
      {/* Current Password */}
      <div>
        <label className="mb-2 block font-semibold">Current Password</label>
        <Input
          disabled={isPending}
          name="currentPassword"
          onChange={handleChange}
          placeholder="Enter your current password"
          required
          type="password"
          value={formData.currentPassword}
        />
      </div>

      {/* New Password */}
      <div>
        <label className="mb-2 block font-semibold">New Password</label>
        <Input
          disabled={isPending}
          name="newPassword"
          onChange={handleChange}
          placeholder="Enter your new password"
          required
          type="password"
          value={formData.newPassword}
        />
        {formData.newPassword && (
          <div className="mt-2 space-y-1">
            <div className="flex gap-2">
              <div
                className={`h-1 flex-1 rounded-full ${passwordStrength === "weak" ? "bg-red-500 dark:bg-red-600" : "bg-gray-200 dark:bg-gray-700"}`}
              />
              <div
                className={`h-1 flex-1 rounded-full ${
                  passwordStrength === "medium" || passwordStrength === "strong"
                    ? "bg-yellow-500 dark:bg-yellow-600"
                    : "bg-gray-200 dark:bg-gray-700"
                }`}
              />
              <div
                className={`h-1 flex-1 rounded-full ${passwordStrength === "strong" ? "bg-green-500 dark:bg-green-600" : "bg-gray-200 dark:bg-gray-700"}`}
              />
            </div>
            <p
              className={`text-xs font-semibold ${
                passwordStrength === "weak"
                  ? "text-red-500 dark:text-red-400"
                  : passwordStrength === "medium"
                    ? "text-yellow-500 dark:text-yellow-400"
                    : "text-green-500 dark:text-green-400"
              }`}
            >
              {passwordStrength.charAt(0).toUpperCase() + passwordStrength.slice(1)} password
            </p>
          </div>
        )}
        <div className="mt-2 space-y-1 text-xs text-muted-foreground">
          <p>✓ At least 8 characters</p>
          <p>✓ Contains uppercase letter</p>
          <p>✓ Contains number</p>
          <p>✓ Contains special character</p>
        </div>
      </div>

      {/* Confirm Password */}
      <div>
        <label className="mb-2 block font-semibold">Confirm Password</label>
        <Input
          disabled={isPending}
          name="confirmPassword"
          onChange={handleChange}
          placeholder="Confirm your new password"
          required
          type="password"
          value={formData.confirmPassword}
        />
      </div>

      {/* Error Message */}
      {error && <div className="rounded-lg bg-destructive/10 p-3 text-sm text-destructive">{error}</div>}

      {/* Success Message */}
      {success && (
        <div className="rounded-lg bg-green-50 p-3 text-sm text-green-700">
          Password changed successfully. Redirecting...
        </div>
      )}

      {/* Action Buttons */}
      <div className="flex justify-end gap-3">
        <Button disabled={isPending} onClick={() => router.back()} type="button" variant="outline">
          Cancel
        </Button>
        <Button disabled={isPending} type="submit">
          {isPending ? "Updating..." : "Change Password"}
        </Button>
      </div>
    </form>
  );
}
