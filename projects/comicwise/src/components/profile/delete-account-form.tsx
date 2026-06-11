"use client";

/**
 * Delete Account Form Component
 * Handles account deletion with email confirmation
 */

import { AlertCircle } from "lucide-react";
import { useRouter } from "next/navigation";
import { type FormEvent, useState } from "react";

import { deleteAccountAction } from "@/actions/profile.actions";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

interface DeleteAccountFormProps {
  userEmail: string;
  userId: string;
}

export function DeleteAccountForm({ userEmail }: DeleteAccountFormProps) {
  const router = useRouter();
  const [emailConfirmation, setEmailConfirmation] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<null | string>(null);
  const [success, setSuccess] = useState(false);

  const emailMatches = emailConfirmation === userEmail;

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError(null);
    setSuccess(false);

    if (!emailMatches) {
      setError("Email confirmation does not match");
      return;
    }

    setIsLoading(true);
    try {
      const result = await deleteAccountAction();

      if (!result.ok) {
        setError(result.error ?? "Failed to delete account");
        setIsLoading(false);
        return;
      }

      setSuccess(true);

      // Redirect after a brief delay
      setTimeout(() => {
        router.push("/sign-in");
      }, 1500);
    } catch (err) {
      setError(err instanceof Error ? err.message : "An unexpected error occurred");
      setIsLoading(false);
    }
  };

  if (success) {
    return (
      <div className="rounded-lg border border-green-200 bg-green-50 p-6 text-center dark:border-green-900/30 dark:bg-green-950/30">
        <h2 className="mb-2 text-lg font-semibold text-green-900 dark:text-green-300">Account Deleted</h2>
        <p className="text-green-700 dark:text-green-300/80">
          Your account has been successfully deleted. Redirecting...
        </p>
      </div>
    );
  }

  return (
    <form
      className="space-y-6 rounded-lg border border-border bg-card p-6"
      onSubmit={(e) => {
        void handleSubmit(e);
      }}
    >
      {/* Email Confirmation Field */}
      <div className="space-y-2">
        <label className="text-sm font-medium">
          Type your email to confirm deletion:
          <div className="text-xs font-normal text-muted-foreground">We need to verify your identity</div>
        </label>
        <Input
          autoComplete="off"
          disabled={isLoading}
          onChange={(e) => setEmailConfirmation(e.target.value)}
          placeholder={userEmail}
          type="email"
          value={emailConfirmation}
        />
        <p className="text-xs text-muted-foreground">
          Enter <code className="rounded bg-muted px-1">{userEmail}</code> to proceed
        </p>
      </div>

      {/* Error Alert */}
      {error && (
        <Alert className="border-destructive/50 bg-destructive/5">
          <AlertCircle className="h-4 w-4 text-destructive" />
          <AlertDescription className="text-destructive">{error}</AlertDescription>
        </Alert>
      )}

      {/* Action Buttons */}
      <div className="flex gap-4">
        <Button disabled={!emailMatches || isLoading} type="submit" variant="destructive">
          {isLoading ? "Deleting..." : "Yes, Delete My Account"}
        </Button>
        <Button disabled={isLoading} onClick={() => window.history.back()} type="button" variant="outline">
          Cancel
        </Button>
      </div>

      {/* Additional Info */}
      <div className="rounded-lg bg-muted p-4 text-sm">
        <p className="font-semibold">What happens when you delete your account?</p>
        <ul className="mt-2 list-inside list-disc space-y-1 text-muted-foreground">
          <li>Your profile and all personal data will be permanently removed</li>
          <li>You will no longer be able to sign in</li>
          <li>Your bookmarks, comments, and ratings will be deleted</li>
          <li>This action cannot be reversed</li>
        </ul>
      </div>
    </form>
  );
}
