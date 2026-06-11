import json
import logging
from typing import TYPE_CHECKING

from extruct.jsonld import JsonLdExtractor
from scrapy.http.request import Request
from scrapy.spiders import Spider

if TYPE_CHECKING:
    from playwright.async_api import Page

logger = logging.getLogger(__name__)


class ComickSpider(Spider):
    name = "comick"

    def start_requests(self):
        # Custom start URLs
        yield Request(
            url="https://comick.io/home2/",
            callback=self.parse_first,
            meta={
                "playwright": True,
                "playwright_include_page": True,
            },
            errback=self.errback_close_page,
        )

    def parse_first(self, response):
        data = json.loads(response.xpath("//script[@id='__NEXT_DATA__']/text()").get())
        tags = [
            "comicsByCurrentSeason",
            "rank",
            "recentRank",
            "follows",
            "news",
            "extendedNews",
            "completions",
            "trending",
            "topFollowNewComics",
            "topFollowComics",
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
        for comic in comics:
            yield response.follow(
                response.urljoin(f"/comic/{comic["slug"]}/"),
                callback=self.comicpage,
            )

        msg = f"comics_count: {len(comics)}"
        logger.info(msg)

    def comicpage(self, response, **kwargs):

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
