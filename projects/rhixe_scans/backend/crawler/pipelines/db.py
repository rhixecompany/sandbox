import logging

from api.libary.models import Artist
from api.libary.models import Author
from api.libary.models import Category
from api.libary.models import Chapter
from api.libary.models import ChapterImage
from api.libary.models import Comic
from api.libary.models import ComicImage
from api.libary.models import Genre
from api.libary.models import Website
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.utils import IntegrityError
from itemadapter.adapter import ItemAdapter
from scrapy.exceptions import DropItem

logger = logging.getLogger(__name__)


class DbPipeline:
    def process_item(self, item, spider):  # noqa: C901, PLR0912, PLR0915
        adapter = ItemAdapter(item)
        if adapter.get("image_urls"):
            usermodel = get_user_model()
            user = usermodel.objects.filter(
                Q(email__icontains="admin@rhixe.company")
                | Q(username__icontains="adminbot"),
            ).first()
            if not user:
                user = usermodel.objects.create_superuser(  # type: ignore  # noqa: PGH003
                    email="admin@rhixe.company",
                    username="adminbot",
                    password="R4I7gcJHX",  # noqa: S106
                )
            if adapter.get("image_urls") and adapter.get("slug"):
                image_urls = item.get("image_urls")
                images = item.get("images")
                title = item["title"]
                slug = item["slug"]
                description = item.get("description")
                rating = item["rating"]
                status = item["status"]
                updated_at = item["updated_at"]
                numchapters = item["numchapters"]
                numimages = len(image_urls)
                serialization = item["serialization"]
                link = item.get("url")
                category = item.get("category")
                author = item.get("author")
                artist = item.get("artist")
                genres = item.get("genres")

                newauthor = Author.objects.update_or_create(name=author)[0]
                newartist = Artist.objects.update_or_create(name=artist)[0]
                newcategory = Category.objects.update_or_create(name=category)[0]
                oldwebsite = Website.objects.filter(
                    Q(name__exact=item["spider"]),
                ).first()
                if not oldwebsite:
                    oldwebsite = Website.objects.update_or_create(
                        name=item["spider"],
                    )[0]
                comic = Comic.objects.get_comic_search(  # type: ignore  # noqa: PGH003
                    slug,
                    title,
                )
                if comic.exists():
                    msg = f"{slug} - {title} Exists"
                    raise DropItem(msg)
                try:
                    newcomic = Comic.objects.update_or_create(
                        user=user,
                        title=title,
                        slug=slug,
                        description=description,
                        rating=rating,
                        status=status,
                        link=link,
                        website=oldwebsite,
                        updated_at=updated_at,
                        numchapters=numchapters,
                        numimages=numimages,
                        serialization=serialization,
                        category=newcategory,
                        author=newauthor,
                        artist=newartist,
                    )[0]
                    if genres:
                        for genre in genres:
                            newgenre = Genre.objects.update_or_create(
                                name=genre,
                            )[0]

                            newcomic.genres.add(newgenre)
                            newcomic.save()
                    if image_urls and images:
                        for img_link, img in zip(image_urls, images, strict=False):
                            imgs = ComicImage.objects.filter(
                                Q(image=img["path"]) & Q(link__exact=img_link),
                            )
                            if imgs.exists():
                                pass
                            else:
                                im = ComicImage.objects.update_or_create(
                                    link=img["url"],
                                    image=img["path"],
                                    status=img["status"],
                                    checksum=img["checksum"],
                                    comic=newcomic,
                                )[0]
                                msg = f"saving {im.image.url}"
                                logger.info(msg)
                    elif image_urls and not images:
                        for img_link in image_urls:
                            ComicImage.objects.get_or_create(
                                link=img_link,
                                comic=newcomic,
                            )[0]
                    elif images and not image_urls:
                        for img in images:
                            ComicImage.objects.get_or_create(
                                link=img["url"],
                                image=img["path"],
                                status=img["status"],
                                checksum=img["checksum"],
                                comic=newcomic,
                            )[0]

                except IntegrityError:
                    msg = f"{slug} - {title} Exists "
                    raise DropItem(msg)  # noqa: B904, RUF100, TRY400
                return item
            if (
                adapter.get("image_urls")
                and adapter.get("comicslug")
                and adapter.get("chapterslug")
            ):
                image_urls = item.get("image_urls")
                images = item.get("images")
                comicslug = item["comicslug"]
                comictitle = item["comictitle"]
                name = item["chaptername"]
                title = item.get("chaptertitle", "")
                slug = item["chapterslug"]
                link = item.get("url")
                updated_at = item.get("updated_at")
                numimages = len(image_urls)
                oldwebsite = Website.objects.filter(
                    Q(name__exact=item["spider"]),
                ).first()
                if not oldwebsite:
                    oldwebsite = Website.objects.update_or_create(
                        name=item["spider"],
                    )[0]
                comic = Comic.objects.get_comic_search(  # type: ignore  # noqa: PGH003
                    comictitle,
                    comicslug,
                )
                if (
                    comic.exists()  # type: ignore  # noqa: PGH003
                ):
                    dbcomic = comic.first()
                    chapter = Chapter.objects.get_chapter_search(  # type: ignore  # noqa: PGH003
                        slug,
                    )
                    if chapter.exists():
                        msg = f"{slug} - {comictitle} Exists"
                        raise DropItem(
                            msg,
                        )
                    try:
                        newchapter = Chapter.objects.update_or_create(
                            title=title,
                            slug=slug,
                            name=name,
                            link=link,
                            website=oldwebsite,
                            updated_at=updated_at,
                            numimages=numimages,
                            comic=dbcomic,
                        )[0]
                        if image_urls and images:
                            for img_link, img in zip(image_urls, images, strict=False):
                                imgs = ChapterImage.objects.filter(
                                    Q(image=img["path"]) & Q(link__exact=img_link),
                                )
                                if imgs.exists():
                                    pass
                                else:
                                    im = ChapterImage.objects.update_or_create(
                                        link=img["url"],
                                        image=img["path"],
                                        status=img["status"],
                                        checksum=img["checksum"],
                                        chapter=newchapter,
                                        comic=dbcomic,
                                    )[0]
                                    msg = f"saving {im.image.url}"
                                    logger.info(msg)
                        elif image_urls and not images:
                            for img_link in image_urls:
                                ChapterImage.objects.get_or_create(
                                    link=img_link,
                                    chapter=newchapter,
                                    comic=dbcomic,
                                )[0]
                        elif images and not image_urls:
                            for img in images:
                                ChapterImage.objects.get_or_create(
                                    link=img["url"],
                                    image=img["path"],
                                    status=img["status"],
                                    checksum=img["checksum"],
                                    chapter=newchapter,
                                    comic=dbcomic,
                                )[0]

                    except IntegrityError:
                        msg = f"{slug} - {name} Exists"
                        raise DropItem(msg)  # noqa: B904, RUF100, TRY400

                else:
                    msg = f"{comictitle} Does Not Exists"
                    raise DropItem(
                        msg,
                    )
                return item

        msg = f"DbPipeline Item has a Missing field in: {item!r}"
        raise DropItem(msg)
