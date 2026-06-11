// import { hash } from '@/lib/encrypt';
import { PrismaClient } from '@prisma/client';
import sampleData from './sample-data';

async function main() {
  const prisma = new PrismaClient();

  // await prisma.account.deleteMany();
  // await prisma.session.deleteMany();
  // await prisma.verificationToken.deleteMany();
  // await prisma.user.deleteMany();
  await prisma.genre.deleteMany();
  await prisma.category.deleteMany();
  await prisma.author.deleteMany();
  await prisma.artist.deleteMany();
  await prisma.comic.deleteMany();
  await prisma.comicImage.deleteMany();
  await prisma.chapter.deleteMany();
  await prisma.chapterImage.deleteMany();

  await prisma.genre.createMany({ data: sampleData.genres });
  await prisma.category.createMany({ data: sampleData.categorys });
  await prisma.author.createMany({ data: sampleData.authors });
  await prisma.artist.createMany({ data: sampleData.artists });
  await prisma.comicImage.createMany({ data: sampleData.comicimages });
  await prisma.comic.createMany({ data: sampleData.comics });
  await prisma.chapterImage.createMany({ data: sampleData.chapterimages });
  await prisma.chapter.createMany({ data: sampleData.chapters });
  // const users = [];
  // for (let i = 0; i < sampleData.users.length; i++) {
  //   users.push({
  //     ...sampleData.users[i],
  //     password: await hash(sampleData.users[i].password),
  //   });
  //   console.log(
  //     sampleData.users[i].password,
  //     await hash(sampleData.users[i].password)
  //   );
  // }
  // await prisma.user.createMany({ data: users });

  console.log('Database seeded successfully!');
}

main();
