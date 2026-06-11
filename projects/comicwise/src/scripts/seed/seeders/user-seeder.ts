/**
 * UserSeeder - seeds users from JSON or generates synthetic users
 *
 * Features:
 * - Synthetic user generation via --count flag with role distribution
 * - Password hashing with bcryptjs (configurable rounds via --bcrypt-rounds)
 * - Auto-reduced bcrypt rounds in CI environments
 * - Email-based deduplication (unique constraint on email)
 * - Cache-first lookups to avoid redundant DB queries
 * - Role validation (user, admin, moderator)
 * - DiceBear avatar URL generation
 */

import bcrypt from "bcryptjs";
import { eq } from "drizzle-orm";

import { db } from "@/database/db";
import { user } from "@/database/schema";
import { type UserSeedItem, userSeedItemSchema } from "@/schemas/seed/user.seed";

import appConfig, { getEnv } from "appConfig";

import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

// Role distribution ratios for synthetic generation
const ROLE_RATIOS = { admin: 0.3, moderator: 0.3, user: 0.4 } as const;
const DEFAULT_BCRYPT_ROUNDS = 10;
const CI_BCRYPT_ROUNDS = 4;

/**
 * Generate synthetic users with role distribution and avatar URLs
 */
function generateSyntheticUsers(count: number): UserSeedItem[] {
  const users: UserSeedItem[] = [];
  const adminCount = Math.round(count * ROLE_RATIOS.admin);
  const modCount = Math.round(count * ROLE_RATIOS.moderator);
  const userCount = count - adminCount - modCount;

  const roleSlots: Array<"admin" | "moderator" | "user"> = [
    ...Array<"admin">(adminCount).fill("admin"),
    ...Array<"moderator">(modCount).fill("moderator"),
    ...Array<"user">(userCount).fill("user"),
  ];

  for (let i = 0; i < roleSlots.length; i++) {
    const role = roleSlots[i];
    const idx = i + 1;
    const email = `${role}-${idx}@comicwise.test`;
    const name = `${role.charAt(0).toUpperCase() + role.slice(1)} User ${idx}`;

    users.push({
      email,
      name,
      password: `${role}Pass${idx}!`,
      role,
      image: `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(email)}`,
      emailVerified: null,
      status: true,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
  }

  return users;
}

/**
 * UserSeeder loads users from JSON or generates synthetic users
 *
 * Handles:
 * - Synthetic generation via --count option with role distribution
 * - Password hashing with bcryptjs (configurable rounds)
 * - Email-based deduplication (DB unique constraint)
 * - Cache-first lookups to avoid redundant DB queries
 * - Role validation (user, admin, moderator)
 * - UUID generation for user IDs
 */
export class UserSeeder extends BaseSeeder<UserSeedItem> {
  private bcryptRounds: number;

  constructor(cache: LookupCache, options: SeedOptions) {
    super("users", userSeedItemSchema, cache, options);
    this.dependencies = []; // Users have no dependencies

    // Determine bcrypt rounds: explicit flag > CI auto-reduce > default
    if (options.bcryptRounds != null) {
      this.bcryptRounds = options.bcryptRounds;
    } else if (getEnv().CI === "true") {
      this.bcryptRounds = CI_BCRYPT_ROUNDS;
      logger.info(`CI detected — using ${CI_BCRYPT_ROUNDS} bcrypt rounds for speed`);
    } else {
      this.bcryptRounds = DEFAULT_BCRYPT_ROUNDS;
    }
  }

  protected getDataSources(): string[] {
    return ["user"];
  }

  protected getUniqueField(): string {
    return "email";
  }

  protected async transformData(raw: UserSeedItem): Promise<unknown> {
    return raw;
  }

  /**
   * Override loadData to support synthetic generation via --count
   */
  async loadData(): Promise<UserSeedItem[]> {
    if (this.options.count != null && this.options.count > 0) {
      const synthetic = generateSyntheticUsers(this.options.count);
      logger.info(
        `Generated ${synthetic.length} synthetic users (${Math.round(ROLE_RATIOS.admin * 100)}% admin, ${Math.round(ROLE_RATIOS.moderator * 100)}% mod, ${Math.round(ROLE_RATIOS.user * 100)}% user)`
      );
      return synthetic;
    }
    return super.loadData();
  }

  async insertBatch(data: UserSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let skipped = 0;
    let updated = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        // Check cache first
        if (this.cache.users.has(item.email)) {
          skipped++;
          continue;
        }

        // Check database for existing user by email
        const existing = await db.query.user.findFirst({
          where: eq(user.email, item.email),
        });

        if (existing) {
          this.cache.users.set(item.email, existing.id);

          // Handle force overwrite with smart update (only if data changed)
          if (this.options.forceOverwrite) {
            const hasChanges =
              existing.name !== item.name ||
              existing.role !== (item.role ?? "user") ||
              existing.status !== (item.status ?? true) ||
              existing.image !== (item.image ?? null);

            if (hasChanges) {
              const passwordToHash = item.password ?? appConfig.seeding.defaultPassword;
              const hashedPassword = await bcrypt.hash(passwordToHash, this.bcryptRounds);

              await db
                .update(user)
                .set({
                  name: item.name,
                  role: item.role ?? "user",
                  status: item.status ?? true,
                  image: item.image ?? null,
                  password: hashedPassword,
                  updatedAt: new Date(),
                })
                .where(eq(user.id, existing.id));
              updated++;
            } else {
              skipped++; // Same data, no update needed
            }
          } else {
            skipped++;
          }
          continue;
        }

        // Hash password before insertion (use default from appConfig if not provided in seed)
        const passwordToHash = item.password ?? appConfig.seeding.defaultPassword;
        const hashedPassword = await bcrypt.hash(passwordToHash, this.bcryptRounds);

        // Insert new user
        const result = await db
          .insert(user)
          .values({
            id: item.id ?? crypto.randomUUID(),
            name: item.name,
            email: item.email,
            password: hashedPassword,
            role: item.role ?? "user",
            status: item.status ?? true,
            image: item.image ?? null,
            emailVerified: item.emailVerified ?? null,
            createdAt: item.createdAt ?? new Date(),
            updatedAt: item.updatedAt ?? new Date(),
          })
          .returning();

        if (result.length > 0) {
          inserted++;
          this.cache.users.set(item.email, result[0].id);
        }
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({
          itemIndex: i,
          value: data[i],
          message,
        });
        logger.debug(`Error inserting user: ${message}`);
      }
    }

    const duration = Date.now() - startTime;

    return {
      entityName: this.entityName,
      inserted,
      updated,
      skipped,
      errors,
      duration,
      success: errors.length === 0,
    };
  }
}
