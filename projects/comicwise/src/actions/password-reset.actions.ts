/**
 * Password Reset Server Actions
 * Handle password reset functionality
 */

"use server";

import { revalidatePath } from "next/cache.js";

import { passwordResetDal } from "@/dal/password-reset-dal";
import { userDal } from "@/dal/user-dal";
import { requestPasswordResetSchema, resetPasswordSchema } from "@/schemas/password-reset.schema";

import type { ActionResult } from "@/types/actions-types";

export async function requestPasswordResetAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  const parsed = requestPasswordResetSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    const { email } = parsed.data;
    const user = await userDal.getByEmail(email);

    if (!user) {
      return { ok: true, data: { success: true } };
    }

    const token = globalThis.crypto.randomUUID();
    const expires = new Date(Date.now() + 60 * 60 * 1000);

    await passwordResetDal.create({
      email,
      token,
      expires,
    });

    return { ok: true, data: { success: true } };
  } catch {
    return { ok: false, error: "Failed to request password reset" };
  }
}

export async function resetPasswordAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  const parsed = resetPasswordSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    const { token, password } = parsed.data;

    const resetToken = await passwordResetDal.findByToken(token);
    if (!resetToken) {
      return { ok: false, error: "Invalid or expired token" };
    }

    await userDal.updatePassword(resetToken.email, password);
    await passwordResetDal.deleteByToken(token);

    revalidatePath("/sign-in");

    return { ok: true, data: { success: true } };
  } catch {
    return { ok: false, error: "Failed to reset password" };
  }
}
