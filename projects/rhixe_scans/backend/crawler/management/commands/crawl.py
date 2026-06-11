import logging

from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy.utils.reactor import install_reactor

from crawler.spiders.asuracomic import AsuracomicSpider

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "A  Custom command to  asuracomic AsuracomicSpider"

    def handle(self, *args, **options):

        install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
        crawlsettings = get_project_settings()
        configure_logging(crawlsettings)
        process = CrawlerProcess(settings=crawlsettings)
        logger.info("starting spider")
        process.crawl(AsuracomicSpider)
        process.start()  # type: ignore  # noqa: PGH003

        logger.info("ending spider")
