import { PrismaClient } from '@prisma/client';

const globalForPrisma = globalThis as unknown as { prisma: PrismaClient };

export const prisma =
  globalForPrisma.prisma ||
  new PrismaClient().$extends({
    result: {
      comic: {
        rating: {
          compute(comic) {
            return comic.rating.toString();
          },
        },
        // updated_at: {
        //   compute(comic) {
        //     const dateStr = comic.updated_at;
        //     const dateObj = new Date(dateStr);
        //     const isoDate = dateObj.toISOString();
        //     return isoDate;
        //   },
        // },
      },
      // chapter: {
      //   updated_at: {
      //     compute(chapter) {
      //       const dateStr = chapter.updated_at;
      //       const dateObj = new Date(dateStr);
      //       const isoDate = dateObj.toISOString();
      //       return isoDate;
      //     },
      //   },
      // },
    },
  });

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;
