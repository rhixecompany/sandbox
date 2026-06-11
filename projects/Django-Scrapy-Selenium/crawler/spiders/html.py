import logging

from scrapy.spiders import Spider
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa: N812

logger = logging.getLogger(__name__)


class HtmlSpider(Spider):
    name = "html"
    start_urls = [
        # "https://asuracomic.net/",  # noqa: ERA001
        # "https://asuracomic.net/series?page=2",  # noqa: ERA001
        # "https://asuracomic.net/series/reaper-of-the-drifting-moon-0fc74b94",  # noqa: E501, ERA001
        # "https://asuracomic.net/series/nano-machine-923317b4",  # noqa: ERA001
        "https://asuracomic.net/series/nano-machine-923317b4/chapter/239",
        # "https://asuracomic.net/series/nano-machine-923317b4/chapter/1",  # noqa: E501, ERA001
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=20,
                wait_until=EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[contains(@class, 'w-full mx-auto center')]/img[contains(@class, 'object-cover mx-auto')]",  # noqa: E501
                    ),
                ),
            )

    def parse(self, response):
        image_urls = response.xpath(
            '//div[contains(@class, "w-full mx-auto center")]/img[contains(@class, "object-cover mx-auto")]/@src',  # noqa: E501
        ).getall()
        if image_urls:
            images = []
            for img in image_urls:
                images.append(response.urljoin(img))  # noqa: PERF401
            yield {
                "image_urls": images,
            }
        msg = f"A New Comic found at: {response.url}"
        logger.info(msg)
