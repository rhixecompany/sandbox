import json
import logging

from extruct.jsonld import JsonLdExtractor
from playwright.async_api import Dialog
from playwright.async_api import Page
from playwright.async_api import Response as PlaywrightResponse
from scrapy.http.request import Request
from scrapy.spiders import Spider
from scrapy_playwright.page import PageMethod

logger = logging.getLogger(__name__)


async def scroll_page(page: Page) -> str:
    await page.wait_for_selector(selector="script#__NEXT_DATA__")
    # await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")  # noqa: E501, ERA001
    return page.url


class Comick1Spider(Spider):
    name = "comick1"
    allowed_domains = ["comick.io"]
    start_urls = [
        "https://comick.io/home2/",
    ]

    def start_requests(self):
        # Custom start URLs
        for url in self.start_urls:
            yield Request(
                url=url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": [
                        PageMethod(scroll_page),
                    ],
                    "playwright_page_event_handlers": {
                        "dialog": self.handle_dialog,
                        "response": self.handle_response,
                    },
                },
                callback=self.comicspage,
                errback=self.errback_close_page,
                dont_filter=False,
            )
        msg = f"Pages: {self.start_urls}"
        logger.info(msg)

    async def comicspage(self, response, **kwargs):

        data = json.loads(response.xpath("//script[@id='__NEXT_DATA__']/text()").get())
        tags = [
            "comicsByCurrentSeason",
            # "rank",
            # "recentRank",
            # "follows",
            # "news",
            # "extendedNews",
            # "completions",
            # "trending",
            # "topFollowNewComics",
            # "topFollowComics",
        ]
        for tag in tags:
            if tag == "comicsByCurrentSeason":
                comics = data["props"]["pageProps"]["data"][f"{tag}"]["data"]
            elif tag in {"topFollowNewComics", "topFollowComics", "trending"}:
                ntags = ["7", "30", "90"]
                for ntag in ntags:
                    comics = data["props"]["pageProps"]["data"][f"{tag}"][f"{ntag}"]
            else:
                comics = data["props"]["pageProps"]["data"][f"{tag}"]

        for comic in comics[0:3]:
            msg = f"view: {response.urljoin(f"/comic/{comic["slug"]}/")}"
            logger.info(msg)
            yield response.follow(
                response.urljoin(f"/comic/{comic["slug"]}/"),
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": [
                        PageMethod(scroll_page),
                    ],
                    "playwright_page_event_handlers": {
                        "dialog": self.handle_dialog,
                        "response": self.handle_response,
                    },
                },
                callback=self.comicpage,
                errback=self.errback_close_page,
                dont_filter=False,
            )

    async def comicpage(self, response, **kwargs):

        jslde = JsonLdExtractor()
        imagedata = jslde.extract(response.body)
        data = json.loads(
            response.xpath(
                "//script[@id='__NEXT_DATA__']/text()",
            ).get(),
        )
        comic = data["props"]["pageProps"]

        yield {
            "data": comic,
            "image": imagedata,
        }

    async def errback_close_page(self, failure):
        page: Page = failure.request.meta["playwright_page"]
        await page.close()

    async def handle_dialog(self, dialog: Dialog) -> None:
        logger.info(f"Handled dialog with message: {dialog.message}")  # noqa: G004
        await dialog.dismiss()

    async def handle_response(self, response: PlaywrightResponse) -> None:
        logger.info(f"Received response with URL {response.url}")  # noqa: G004
