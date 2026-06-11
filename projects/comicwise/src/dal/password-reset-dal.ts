/**
 * Password Reset Token DAL (Data Access Layer)
 * Manages password reset token operations
 */

import { and, eq, gt } from "drizzle-orm";

import { db } from "@/database/db";
import { passwordResetToken } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type PasswordResetTokenType = typeof passwordResetToken.$inferSelect;

export interface CreatePasswordResetInput {
  email: string;
  expires: Date;
  token: string;
}

export class PasswordResetDal extends BaseDal<PasswordResetTokenType> {
  async list(_options?: DalOptions): Promise<PasswordResetTokenType[]> {
    throw new Error("Use findByEmail instead");
  }

  async getById(_id: number | string): Promise<null | PasswordResetTokenType> {
    throw new Error("Use findByToken instead");
  }

  async create(data: unknown): Promise<PasswordResetTokenType> {
    const input = data as CreatePasswordResetInput;
    const [result] = await db.insert(passwordResetToken).values(input).returning();

    if (!result) {
      throw new Error("Failed to create password reset token");
    }

    return result;
  }

  async update(_id: number | string, _data: unknown): Promise<null | PasswordResetTokenType> {
    throw new Error("Password reset tokens cannot be updated");
  }

  async delete(_id: number | string): Promise<void> {
    throw new Error("Use deleteByEmail or deleteByToken instead");
  }

  async findByEmail(email: string): Promise<null | PasswordResetTokenType> {
    const results = await db.query.passwordResetToken.findMany({
      where: eq(passwordResetToken.email, email),
      orderBy: (t) => t.expires,
    });

    const validToken = results.find((t) => t.expires > new Date());
    return validToken ?? null;
  }

  async findByToken(token: string): Promise<null | PasswordResetTokenType> {
    const result = await db.query.passwordResetToken.findFirst({
      where: and(eq(passwordResetToken.token, token), gt(passwordResetToken.expires, new Date())),
    });

    return result ?? null;
  }

  async deleteByEmail(email: string): Promise<void> {
    await db.delete(passwordResetToken).where(eq(passwordResetToken.email, email));
  }

  async deleteByToken(token: string): Promise<void> {
    await db.delete(passwordResetToken).where(eq(passwordResetToken.token, token));
  }

  async deleteExpired(): Promise<number> {
    const results = await db.delete(passwordResetToken).where(gt(passwordResetToken.expires, new Date())).returning();

    return results.length;
  }
}

export const passwordResetDal = new PasswordResetDal();
