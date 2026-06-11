import logging

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.utils import IntegrityError
from itemadapter.adapter import ItemAdapter
from scrapy.exceptions import DropItem

from api.apps.models import Artist
from api.apps.models import Author
from api.apps.models import Chapter
from api.apps.models import ChapterImage
from api.apps.models import Comic
from api.apps.models import ComicImage
from api.apps.models import Genre
from api.apps.models import Type

logger = logging.getLogger(__name__)


class CrawlerAppsDbPipeline:
    def process_item(self, item, spider):  # noqa: C901, PLR0912, PLR0915
        adapter = ItemAdapter(item)
        if adapter.get("images"):
            if adapter.get("images") and adapter.get("slug"):
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
                    ty = Type.objects.filter(Q(name__icontains=te)).update_or_create(
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
                        raise DropItem(  # noqa: B904
                            msg,
                        )
                else:
                    msg = f"ComicItem has not images: {item!r}"
                    raise DropItem(msg)
                return item
            if (
                adapter.get("images")
                and adapter.get("comicslug")
                and adapter.get("chapterslug")
            ):
                chapterimages = item.get("images")
                comicslug = item["comicslug"]
                comictitle = item["comictitle"]
                name = item["chaptername"]
                title = item.get("chaptertitle", "")
                slug = item["chapterslug"]
                url = item["url"]
                spider = item["spider"]
                updated_at = item["updated_at"]
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
                                #     image=img_file,comic=comic,chapter=ch,  # noqa: E501, ERA001
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
                                )[
                                    0
                                ]
                        except IntegrityError:
                            msg = f"{slug}: Already Exists"
                            logger.info(
                                msg,
                            )
                    else:
                        msg = f"ChapterItem has not images: {item!r}"
                        raise DropItem(
                            msg,
                        )
                else:
                    msg = f"{comictitle}: Does Already not Exists, Item:{item!r}"
                    raise DropItem(
                        msg,
                    )

                return item
            return None
        msg = f"CrawlerAppsDbPipeline Item has a Missing field in: {item!r}"
        raise DropItem(msg)
