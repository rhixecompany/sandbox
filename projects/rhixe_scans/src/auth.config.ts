import db from '@/lib/db';
import { schema } from '@/lib/schema';
import { PrismaAdapter } from '@auth/prisma-adapter';
import type { NextAuthConfig } from 'next-auth';
// import { encode as defaultEncode } from 'next-auth/jwt';
import Credentials from 'next-auth/providers/credentials';
import GitHub from 'next-auth/providers/github';
// import { v4 as uuid } from 'uuid';

const adapter = PrismaAdapter(db);
// Notice this is only an object, not a full Auth.js instance
export default {
  adapter,

  providers: [
    GitHub,
    Credentials({
      credentials: {
        email: {},
        password: {},
      },
      authorize: async (credentials) => {
        const validatedCredentials = schema.parse(credentials);

        const user = await db.user.findFirst({
          where: {
            email: validatedCredentials.email,
            password: validatedCredentials.password,
          },
        });

        if (!user) {
          throw new Error('Invalid credentials.');
        }

        return user;
      },
    }),
  ],
  session: {
    strategy: 'jwt',
    maxAge: 60 * 60 * 24, //  1 day
  },
  pages: {
    signIn: '/sign-in',
    newUser: '/sign-up',
    // signOut: '/logout',
  },
  // callbacks: {
  //   async jwt({ token, account }) {
  //     if (account?.provider === 'credentials') {
  //       token.credentials = true;
  //     }
  //     return token;
  //   },
  // },
  // jwt: {
  //   encode: async function (params) {
  //     if (params.token?.credentials) {
  //       const sessionToken = uuid();

  //       if (!params.token.sub) {
  //         throw new Error('No user ID found in token');
  //       }

  //       const createdSession = await adapter?.createSession?.({
  //         sessionToken: sessionToken,
  //         userId: params.token.sub,
  //         expires: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000),
  //       });

  //       if (!createdSession) {
  //         throw new Error('Failed to create session');
  //       }

  //       return sessionToken;
  //     }
  //     return defaultEncode(params);
  //   },
  // },
} satisfies NextAuthConfig;
