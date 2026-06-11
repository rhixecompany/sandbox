import { DrizzleAdapter } from "@auth/drizzle-adapter";

import { db } from "./database/db";
import { account, session, user, verificationToken } from "./database/schema";

const adapter = DrizzleAdapter(db, {
  usersTable: user,
  accountsTable: account,
  sessionsTable: session,
  verificationTokensTable: verificationToken,
});

export default adapter;
