import logging

from bs4 import BeautifulSoup
from scrapy.http.request import Request
from scrapy.loader import ItemLoader
from scrapy.spiders import Spider

from crawler.items import ComicItem

logger = logging.getLogger(__name__)


class Asuracomic2Spider(Spider):
    name = "asuracomic2"
    allowed_domains = ["gg.asuracomic.net", "asuracomic.net"]
    start_urls = [
        "https://asuracomic.net/series?page=1&order=update",
    ]

    def start_requests(self):
        # Custom start URLs
        for url in self.start_urls:
            msg = f"Page: {url}"
            logger.info(msg)
            yield Request(
                url=url,
                # meta={
                #     "impersonate": "chrome124",
                # },
                callback=self.comicspage,
            )

    def comicspage(self, response):
        urls = [
            f"https://asuracomic.net/series?page={i}&order=update" for i in range(2, 3)
        ]
        links = response.xpath(
            "//div[@class='grid grid-cols-2 sm:grid-cols-2 md:grid-cols-5 gap-3 p-4']/a/@href",  # noqa: E501
        ).getall()
        if links:
            for link in links:
                yield response.follow(
                    response.urljoin(link),
                    callback=self.comicpage,
                )
                msg = f"A New Page found at: {response.urljoin(link)}"
                logger.info(msg)
        # if urls:
        #     for url in urls:
        #         msg = f"Page: {url}"
        #         logger.info(msg)
        #         yield Request(
        #             url=url,
        #             # meta={
        #             #     "impersonate": "chrome124",
        #             # },
        #             callback=self.comicspage,
        #         )

    def comicpage(self, response):
        loader = ItemLoader(item=ComicItem(), selector=response)
        loader.add_xpath(
            "title",
            '//span[contains(@class, "text-xl font-bold")]/text()',
        )
        loader.add_xpath("slug", '//span[contains(@class, "text-xl font-bold")]/text()')

        loader.add_xpath(
            "serialization",
            "//div[@class='grid grid-cols-1 md:grid-cols-2 gap-5 mt-8']/div[1]/h3[2]/text()",  # noqa: E501
        )
        loader.add_xpath(
            "author",
            "//div[@class='grid grid-cols-1 md:grid-cols-2 gap-5 mt-8']/div[2]/h3[2]/text()",  # noqa: E501
        )
        loader.add_xpath(
            "artist",
            "//div[@class='grid grid-cols-1 md:grid-cols-2 gap-5 mt-8']/div[3]/h3[2]/text()",  # noqa: E501
        )
        loader.add_xpath(
            "rating",
            '//span[contains(@class, "ml-1 text-xs")]/text()',
        )
        loader.add_xpath(
            "status",
            "//div[@class='bg-[#343434] px-2 py-2 flex items-center justify-between rounded-[3px] w-full']/h3[2]/text()",  # noqa: E501
        )
        loader.add_xpath(
            "category",
            "//div[@class='bg-[#343434] px-2 py-2 flex items-center justify-between rounded-[3px] w-full'][2]/h3[2]/text()",  # noqa: E501
        )
        loader.add_xpath(
            "genres",
            "//div[@class='flex flex-row flex-wrap gap-3']/button/text()",
        )
        image = response.xpath(
            '//div[contains(@class, "relative col-span-full")]/img[contains(@class, "rounded mx-auto")]/@src',  # noqa: E501
        ).get()
        image2 = response.xpath(
            '//div[contains(@class, "bigcover")]/img[contains(@data-nimg, "1")]/@src',
        ).get()

        chapters = response.xpath(
            '//div[contains(@class, "pl-4 py-2 border rounded-md group w-full hover:bg-[#343434] cursor-pointer border-[#A2A2A2]/20 relative")]/a/@href',  # noqa: E501
        ).getall()[0:1]
        comic_time = response.xpath(
            '//div[contains(@class, "pl-4 py-2 border rounded-md group w-full hover:bg-[#343434] cursor-pointer border-[#A2A2A2]/20 relative")]/a/h3[contains(@class, "text-xs text-[#A2A2A2]")]/text()',  # noqa: E501
        ).get()
        loader.add_value("updated_at", comic_time)
        loader.add_value("url", response.url)
        images = []
        images.append(response.urljoin(image))
        if image2:
            images.append(response.urljoin(image2))
        loader.add_value("image_urls", images)
        loader.add_value(
            "numchapters",
            len(
                chapters,
            ),
        )
        soup = BeautifulSoup(response.text, "lxml")
        # Find all elements with both 'class1' and 'class2'
        des_tag = (
            soup.find(class_=["col-span-12", "sm:col-span-9"])
            .find("span", class_=["font-medium", "text-sm", "text-[#A2A2A2]"])  # type: ignore  # noqa: PGH003
            .select("p")  # type: ignore  # noqa: PGH003
        )
        if not des_tag:
            new_des_tag = soup.find(
                class_=["col-span-12", "sm:col-span-9"],
            ).find(  # type: ignore  # noqa: PGH003
                "span",
                class_=["font-medium", "text-sm", "text-[#A2A2A2]"],  # type: ignore  # noqa: PGH003
            )  # type: ignore  # noqa: PGH003
            if new_des_tag:
                loader.add_value(
                    "description",
                    [str(des.text.strip().replace("\n", "")) for des in new_des_tag],  # type: ignore  # noqa: PGH003
                )  # type: ignore  # noqa: E501, PGH003, RUF100
        if des_tag:
            loader.add_value(
                "description",
                [str(des.text.strip().replace("\n", "")) for des in des_tag],
            )  # type: ignore  # noqa: PGH003
        item = loader.load_item()
        yield item
        msg = f"A New Comic found at: {response.url}"
        logger.info(msg)
