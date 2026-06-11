import { PrismaClient } from '@prisma/client';

const prismaClientSingleton = () => {
  return new PrismaClient().$extends({
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
};

declare const globalThis: {
  prismaGlobal: ReturnType<typeof prismaClientSingleton>;
} & typeof global;

const db = globalThis.prismaGlobal ?? prismaClientSingleton();

export default db;

if (process.env.NODE_ENV !== 'production') globalThis.prismaGlobal = db;
