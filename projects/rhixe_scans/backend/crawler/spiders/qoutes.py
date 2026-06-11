import scrapy
from scrapy.utils.defer import deferred_to_future


class QoutesSpider(scrapy.Spider):
    name = "qoutes"
    allowed_domains = ["python-forum.io"]
    start_urls = [
        "https://python-forum.io",
    ]

    async def parse(self, response):
        additional_request = scrapy.Request(
            "https://python-forum.io/Thread-Exploring-async-await-without-knowing-how-they-work-ahead-of-time?pid=17292",
            callback=self.parse_deffered,
        )
        deferred = self.crawler.engine.download(additional_request)  # type: ignore  # noqa: PGH003
        additional_response = await deferred_to_future(deferred)
        yield additional_response

    def parse_deffered(self, response):
        yield {
            "url": response.url,
        }
