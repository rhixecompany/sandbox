import logging

from scrapy.http.request import Request
from scrapy.spiders import Spider

logger = logging.getLogger(__name__)


class ComicSpider(Spider):
    name = "comic"
    allowed_domains = ["gg.asuracomic.net", "asuracomic.net"]
    start_urls = [
        f"https://asuracomic.net/series?page={i}&order=update" for i in range(1, 2)
    ]

    def start_requests(self):
        # Custom start URLs
        for url in self.start_urls:
            msg = f"Page: {url}"
            logger.info(msg)
            yield Request(
                url=url,
                callback=self.comicspage,
                dont_filter=False,
            )

    def comicspage(self, response):
        links = response.xpath(
            "//div[@class='grid grid-cols-2 sm:grid-cols-2 md:grid-cols-5 gap-3 p-4']/a/@href",  # noqa: E501
        ).getall()
        yield {"links": links}
