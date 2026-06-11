import logging

from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerRunner as Crawler
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import defer
from twisted.internet import reactor

from crawler.spiders.asuracomic import AsuracomicSpider

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "A  Custom command to  run AsuracomicSpider"

    def handle(self, *args, **options):
        crawlsettings = get_project_settings()
        configure_logging(crawlsettings)
        logger.info("starting spider")
        runner = Crawler(settings=crawlsettings)

        @defer.inlineCallbacks
        def run():
            yield runner.crawl(AsuracomicSpider)

            reactor.stop()  # type: ignore  # noqa: PGH003

        run()
        reactor.run()  # type: ignore  # noqa: PGH003
        logger.info("ending spider")
