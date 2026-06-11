import logging

from api.libary.models import Chapter
from api.libary.models import ChapterImage
from api.libary.models import Comic
from api.libary.models import ComicImage
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import defer
from twisted.internet import reactor

from crawler.pipelines.redis import connection
from crawler.spiders.asuracomic import AsuracomicSpider

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "A  Custom command to  run AsuracomicSpider"

    def handle(self, *args, **options):
        crawlsettings = get_project_settings()
        configure_logging(crawlsettings)
        server = connection.from_settings(crawlsettings)
        key = "run_queue:start_urls"
        data = ""
        server.rpush(key, data)

        runner = CrawlerRunner(settings=crawlsettings)

        @defer.inlineCallbacks
        def run():
            yield runner.crawl(AsuracomicSpider)

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
