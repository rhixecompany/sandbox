import logging

from api.libary.models import Chapter
from bs4 import BeautifulSoup
from django.db.models import Q
from scrapy.http.request import Request
from scrapy.loader import ItemLoader
from scrapy.spiders import Spider

from crawler.items import ChapterItem
from crawler.items import ComicItem

logger = logging.getLogger(__name__)


class Asuracomic1Spider(Spider):
    name = "asuracomic1"
    allowed_domains = ["gg.asuracomic.net", "asuracomic.net"]
    start_urls = [
        "https://asuracomic.net/series/killer-pietro-6fe8e840",
    ]

    def start_requests(self):
        # Custom start URLs

        for url in self.start_urls:
            yield Request(
                url=url,
                callback=self.comicpage,
            )
        msg = f"Pages: {self.start_urls}"
        logger.info(msg)

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
        chapters_time = response.xpath(
            '//div[contains(@class, "pl-4 py-2 border rounded-md group w-full hover:bg-[#343434] cursor-pointer border-[#A2A2A2]/20 relative")]/a/h3[contains(@class, "text-xs text-[#A2A2A2]")]/text()',  # noqa: E501
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
        if chapters:
            msg = f"Total Chapters found: {len(chapters)}"
            logger.info(msg)
            for x in chapters:
                chaps = Chapter.objects.filter(Q(link__in=response.urljoin(x)))
                if chaps.exists():
                    msg = f"{chaps} already exists"
                    logger.error(msg)
                else:
                    for nx, y in zip(chapters, chapters_time, strict=False):
                        yield Request(
                            url=response.urljoin(nx),
                            callback=self.chapterpage,
                            cb_kwargs={"chaptertime": y},
                            dont_filter=False,
                            meta={
                                "playwright": True,
                            },
                        )

        else:
            msg = f"No Chapters found at: {response.url}"
            logger.error(msg)
        msg = f"A New Comic found at: {response.url}"
        logger.info(msg)

    async def chapterpage(self, response, chaptertime, **kwargs):
        comictitle = response.xpath(
            "//div[@class='flex flex-col items-center space-y-2 pt-6 px-5 text-center']/p/a/span/text()",  # noqa: E501
        ).get()

        chaptertitle = (
            response.xpath(
                "//div[@class='relative flex w-full sm:max-w-60']/button/h2/text()",
            )
            .get()
            .split("-")[-1]
        )
        chaptername = (
            response.xpath(
                "//div[@class='relative flex w-full sm:max-w-60']/button/h2/text()",
            )
            .get()
            .split("-")[-0]
        )
        link = response.url
        chapterslug = f"{comictitle} {
            response.xpath(
                '//button[contains(@class, "px-3 py-2 dropdown-btn")]/h2/text()',
            )
            .get()
            .split('-')[-0]
        }"

        comicslug = response.xpath(
            "//div[@class='flex flex-col items-center space-y-2 pt-6 px-5 text-center']/p/a/span/text()",  # noqa: E501
        ).get()
        loader = ItemLoader(item=ChapterItem(), selector=response)
        loader.add_value("url", link)
        loader.add_value("updated_at", chaptertime)
        loader.add_value("comictitle", comictitle)
        loader.add_value("comicslug", comicslug)
        if chaptertitle.lower() != chaptername.lower():
            loader.add_value("chaptertitle", chaptertitle)
        loader.add_value("chaptername", chaptername)
        loader.add_value("chapterslug", chapterslug)
        image_urls = response.xpath(
            "//div[contains(@class, 'w-full mx-auto center')]/img[contains(@class, 'object-cover mx-auto')]/@src",  # noqa: E501
        ).getall()

        if image_urls:
            images = []
            for img in image_urls:
                images.append(response.urljoin(img))  # noqa: ERA001, PERF401, RUF100
            loader.add_value("image_urls", images)
            msg = f"Total Images found: {len(images)}"
            logger.info(msg)
        else:
            msg = f"No Images found at: {response.url}"
            logger.error(msg)
        item = loader.load_item()
        yield item
        msg = f"A New Chapter found at: {response.url}"
        logger.info(msg)
