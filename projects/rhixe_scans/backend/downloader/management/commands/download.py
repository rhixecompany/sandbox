import asyncio
import logging

from django.core.management.base import BaseCommand

from downloader.main import scraper

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "A  Custom command to  run Process"

    def handle(self, *args, **options):

        logger.info("starting process")
        url = "https://www.scrapingcourse.com/ecommerce/"
        asyncio.run(scraper(url))
