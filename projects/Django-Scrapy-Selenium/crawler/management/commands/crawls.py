# from django.conf import settings  # noqa: ERA001
import logging

from django.core.management.base import BaseCommand

# from redis import from_url  # noqa: ERA001
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import defer
from twisted.internet import reactor

from api.apps.models import Chapter
from api.apps.models import ChapterImage
from api.apps.models import Comic
from api.apps.models import ComicImage
from crawler.spiders.asuracomics import AsuracomicsSpider

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "A  Custom command to  run AsuracomicSpider"

    def handle(self, *args, **options):
        # urls = [f"https://asuracomic.net/series?page={i}" for i in range(1, 18)]  # noqa: E501, ERA001
        # redisclient = from_url(settings.CELERY_BROKER_URL)  # noqa: ERA001
        # redisclient.rpush(
        #     "asuracomics_queue:start_urls",  # noqa: ERA001
        #     urls,
        # )  # noqa: ERA001, RUF100
        crawlsettings = get_project_settings()
        configure_logging(crawlsettings)

        runner = CrawlerRunner(settings=crawlsettings)

        @defer.inlineCallbacks
        def run():
            yield runner.crawl(AsuracomicsSpider)

            reactor.stop()  # type: ignore  # noqa: PGH003

        run()
        reactor.run()  # type: ignore  # noqa: PGH003
        comics = (
            Comic.objects.prefetch_related(
                "comicitems",
                "comicchapters",
                "genres",
                "followers",
            )
            .select_related("author", "type", "artist", "user")
            .all()
        )

        comic_images = ComicImage.objects.select_related("comic").all()
        chapters = (
            Chapter.objects.prefetch_related("chapteritems")
            .select_related("comic")
            .all()
        )

        chapter_images = ChapterImage.objects.select_related("comic", "chapter").all()
        context = {
            "Comics": comics.values(),
            "ComicsImage": comic_images.values(),
            "Chapters": chapters.values(),
            "ChaptersImage": chapter_images.values(),
            "Comics_Count": comics.count(),
            "ComicsImage_Count": comic_images.count(),
            "Chapters_Count": chapters.count(),
            "ChaptersImage_Count": chapter_images.count(),
        }

        logger.info(context)
