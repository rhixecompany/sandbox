import json
import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.db.utils import IntegrityError
from django.utils.timezone import now

from api.apps.models import Artist
from api.apps.models import Author
from api.apps.models import Chapter
from api.apps.models import ChapterImage
from api.apps.models import Comic
from api.apps.models import ComicImage
from api.apps.models import Genre
from api.apps.models import Type

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generates comics for apps"

    def handle(self, *args, **options):  # noqa: C901, PLR0915
        def save_data():  # noqa: C901, PLR0912, PLR0915
            base = settings.BASE_DIR
            comics_file = str(base / "comics.json")
            chapters_file = str(base / "chapters.json")
            with open(comics_file) as comic_file:  # noqa: PTH123
                comics_data = json.load(comic_file)
                for item in comics_data:
                    images = item.get("images")
                    title = item["title"]
                    slug = item["slug"]
                    description = item.get("description", "")
                    rating = item["rating"]
                    status = item["status"]
                    url = item["url"]
                    spider = item["spider"]
                    updated_at = item["updated_at"]
                    numchapters = item["numchapters"]
                    numitems = len(images)
                    serialization = item["serialization"]
                    te = item.get("type", "")
                    author = item.get("author", "")
                    artist = item.get("artist", "")
                    genres = item.get("genres", "")
                    usermodel = get_user_model()
                    user = usermodel.objects.filter(
                        Q(email__icontains="admin@rhixe.company")
                        | Q(username__icontains="adminbot"),
                    ).first()
                    if not user:
                        user = usermodel.objects.create_superuser(
                            email="admin@rhixe.company",
                            username="adminbot",
                            password="R4I7gcJHX",  # noqa: S106
                        )
                    if images:
                        ty = Type.objects.filter(
                            Q(name__icontains=te),
                        ).update_or_create(
                            name=te,
                        )[0]
                        au = Author.objects.filter(
                            Q(name__icontains=author),
                        ).update_or_create(name=author)[0]
                        ar = Artist.objects.filter(
                            Q(name__icontains=artist),
                        ).update_or_create(name=artist)[0]
                        comquery = Q(slug__icontains=slug) | Q(title__icontains=title)

                        try:
                            co = Comic.objects.filter(
                                comquery,
                            ).update_or_create(
                                description=description,
                                url=url,
                                spider=spider,
                                numchapters=numchapters,
                                numitems=numitems,
                                serialization=serialization,
                                title=title,
                                slug=slug,
                                rating=rating,
                                status=status,
                                updated_at=updated_at,
                                type=ty,
                                artist=ar,
                                author=au,
                                user=user,
                            )[0]
                            for genre in genres:
                                try:
                                    ge = Genre.objects.filter(
                                        Q(name__icontains=genre),
                                    ).update_or_create(name=genre)[0]
                                    co.genres.add(ge)
                                    co.save()
                                except IntegrityError:
                                    msg = f"{genre}: Already Exists"
                                    logger.info(
                                        msg,
                                    )
                            for image in images:
                                img_file = image["path"]
                                img_url = image["url"]
                                panquery = Q(url__icontains=img_url) | Q(
                                    image__icontains=img_file,
                                )
                                ComicImage.objects.filter(
                                    panquery,
                                ).update_or_create(
                                    url=img_url,
                                    image=img_file,
                                    comic=co,
                                )[0]
                        except IntegrityError:
                            msg = f"{title}: Already Exists"
                            logger.info(
                                msg,
                            )
            with open(chapters_file) as chapter_file:  # noqa: PTH123
                chapters_data = json.load(chapter_file)
                for citem in chapters_data:
                    chapterimages = citem.get("images")
                    comicslug = citem["comicslug"]
                    comictitle = citem["comictitle"]
                    name = citem["chaptername"]
                    title = citem.get("chaptertitle", "")
                    slug = citem["chapterslug"]
                    url = citem["url"]
                    spider = citem["spider"]
                    updated_at = citem.get("updated_at", now())
                    numpages = len(chapterimages)
                    chapterquery = Q(slug__iexact=slug) | Q(name__iexact=name)
                    comicquery = Q(slug__iexact=comicslug) | Q(title__iexact=comictitle)
                    comic = (
                        Comic.objects.prefetch_related(
                            "comicitems",
                            "comicchapters",
                            "genres",
                            "followers",
                        )
                        .select_related("author", "type", "artist", "user")
                        .filter(comicquery)
                        .first()
                    )
                    if (
                        Comic.objects.prefetch_related(
                            "comicitems",
                            "comicchapters",
                            "genres",
                            "followers",
                        )
                        .select_related("author", "type", "artist", "user")
                        .filter(comicquery)
                        .exists()
                    ):
                        if chapterimages:
                            try:
                                ch = Chapter.objects.filter(
                                    chapterquery,
                                ).update_or_create(
                                    title=title,
                                    url=url,
                                    spider=spider,
                                    numpages=numpages,
                                    name=name,
                                    slug=slug,
                                    updated_at=updated_at,
                                    comic=comic,
                                )[0]
                                for img in chapterimages:
                                    cimg_file = img["path"]
                                    cimg_url = img["url"]
                                    panelquery = Q(url__icontains=cimg_url) | Q(
                                        image__icontains=cimg_file,
                                    )
                                    # img_file = comic.get_comic_images_children()[0]  # noqa: E501, ERA001
                                    # if ChapterImage.objects.filter(
                                    #     image=img_file,  # noqa: ERA001
                                    #     comic=comic,  # noqa: ERA001
                                    #     chapter=ch,  # noqa: E501, ERA001, RUF100
                                    # ).exists():
                                    #     oldimg = ChapterImage.objects.filter(  # noqa: E501, ERA001, RUF100
                                    #         image=img_file,  # noqa: ERA001
                                    #         comic=comic,  # noqa: ERA001
                                    #         chapter=ch,  # noqa: ERA001
                                    #     )  # noqa: ERA001, RUF100
                                    #     oldimg.delete()  # noqa: ERA001
                                    ChapterImage.objects.filter(
                                        panelquery,
                                    ).update_or_create(
                                        url=cimg_url,
                                        image=cimg_file,
                                        comic=comic,
                                        chapter=ch,
                                    )[0]
                            except IntegrityError:
                                msg = f"{slug}: Already Exists"
                                logger.info(
                                    msg,
                                )
                        else:
                            msg = f"ChapterItem has not images: {citem}"
                            logger.info(
                                msg,
                            )
                    else:
                        msg = f"{comictitle}: Does Already not Exists"
                        logger.info(
                            msg,
                        )

            context = {
                "Comic": Comic.objects.all(),
                "ComicImageItem": ComicImage.objects.all(),
                "Comic_Count": Comic.objects.count(),
                "ComicImageItem_Count": ComicImage.objects.count(),
                "Chapter": Chapter.objects.all(),
                "ChapterImagesItem": ChapterImage.objects.all(),
                "Chapter_Count": Chapter.objects.count(),
                "ChapterImageItem_Count": ChapterImage.objects.count(),
            }

            logger.info(
                context,
            )

        save_data()
