import logging

from scrapy.http.request import Request
from scrapy.loader import ItemLoader
from scrapy.spiders import Spider
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa: N812

from api.apps.models import Comic
from crawler.items import ChapterItem
from crawler.items import ComicItem

logger = logging.getLogger(__name__)


class AsuracomicSpider(Spider):
    name = "asuracomic"
    start_urls = list(
        Comic.objects.prefetch_related(
            "comicitems",
            "comicchapters",
            "genres",
            "followers",
        )
        .select_related("author", "type", "artist", "user")
        .all()
        .values_list("url", flat=True)
        .distinct()[0:5],
    )

    # redis_key = "asurachapter_queue:start_urls"  # noqa: ERA001

    # redis_batch_size = 1  # noqa: ERA001

    # max_idle_time = 0  # noqa: ERA001

    def start_requests(self):
        for url in self.start_urls:
            yield Request(
                url=url,
                callback=self.comicpage,
            )

    def comicpage(self, response):  # noqa: C901, PLR0912, PLR0915
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
            '//p[contains(@class, "text-sm text-[#A2A2A2] relative top-px")]/text()',
        )
        loader.add_xpath(
            "status",
            "//div[@class='bg-[#343434] px-2 py-2 flex items-center justify-between rounded-[3px] w-full']/h3[2]/text()",  # noqa: E501
        )
        loader.add_xpath(
            "type",
            "//div[@class='bg-[#343434] px-2 py-2 flex items-center justify-between rounded-[3px] w-full'][2]/h3[2]/text()",  # noqa: E501
        )
        image = response.xpath("//img[@class='rounded mx-auto md:mx-0 ']/@src").get()
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
        cimages = []
        cimages.append(response.urljoin(image))
        if image2:
            cimages.append(response.urljoin(image2))
        loader.add_value("image_urls", cimages)
        loader.add_value(
            "numchapters",
            len(
                chapters,
            ),
        )
        genres = response.xpath(
            "//div[@class='flex flex-row flex-wrap gap-3']/button/text()",
        ).getall()
        if genres:
            loader.add_xpath(
                "genres",
                "//div[@class='flex flex-row flex-wrap gap-3']/button/text()",
            )
        des = response.xpath(
            '//div[contains(@class, "col-span-12 sm:col-span-9")]/span/p/text()',
        ).getall()
        desem = response.xpath(
            '//div[contains(@class, "col-span-12 sm:col-span-9")]/span/p/strong/em/text()',  # noqa: E501
        ).getall()
        newdes = response.xpath(
            '//div[contains(@class, "col-span-12 sm:col-span-9")]/span/text()',
        ).getall()
        newdesem = response.xpath(
            '//div[contains(@class, "col-span-12 sm:col-span-9")]/span/strong/em/text()',  # noqa: E501
        ).getall()
        newdesem1 = response.xpath(
            '//div[contains(@class, "col-span-12 sm:col-span-9")]/span/p/strong[1]/text()',  # noqa: E501
        ).getall()
        olddes = response.xpath(
            '//div[contains(@class, "col-span-12 sm:col-span-9")]/span/div/div/div[1]/text()',  # noqa: E501
        ).getall()
        oldesem = response.xpath(
            '//div[contains(@class, "col-span-12 sm:col-span-9")]/span/div/div/div[1]/strong/em/text()',  # noqa: E501
        ).getall()
        newdesem2 = response.xpath(
            '//div[contains(@class, "col-span-12 sm:col-span-9")]/span/p/strong[2]/em/text()',  # noqa: E501
        ).getall()
        newdesem3 = response.xpath(
            '//div[contains(@class, "col-span-12 sm:col-span-9")]/span/p/strong[2]/em/text()',  # noqa: E501
        ).getall()
        if des:
            mydes = f"{des}"
            loader.add_value("description", mydes)
            if desem:
                mydesem = f"{desem} {des}"
                loader.add_value("description", mydesem)
        if newdes and not des:
            mynewdes = f"{newdes}"
            loader.add_value("description", mynewdes)
            if newdes and newdesem and not des:
                newdesem1div = f"{newdesem}{newdes}"
                loader.add_value("description", newdesem1div)
        if olddes and not des:
            olddesdiv = f"{olddes}"
            loader.add_value("description", olddesdiv)
            if olddes and oldesem and not des:
                oldesemdiv = f"{olddes}{oldesem}"
                loader.add_value("description", oldesemdiv)
        if newdesem1 and newdesem and not des and not olddes:
            newdesemdiv1 = f"{newdesem}{newdesem1}"
            loader.add_value("description", newdesemdiv1)
        if newdesem2 and newdesem1 and newdesem and not des and not olddes:
            newdesemdiv2 = f"{newdesem}{newdesem1}{newdesem2}"
            loader.add_value("description", newdesemdiv2)
        if (
            newdesem3
            and newdesem2
            and newdesem1
            and newdesem
            and not des
            and not olddes
        ):
            newdesemdiv3 = f"{newdesem}{newdesem1}{newdesem2}{newdesem3}"
            loader.add_value("description", newdesemdiv3)
        item = loader.load_item()
        yield item
        if chapters:
            msg = f"Total Chapters found: {len(chapters)}"
            logger.info(msg)
            for x, y in zip(chapters, chapters_time, strict=False):
                yield SeleniumRequest(
                    url=response.urljoin(x),
                    wait_time=20,
                    wait_until=EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//div[contains(@class, 'w-full mx-auto center')]/img[contains(@class, 'object-cover mx-auto')]",  # noqa: E501
                        ),
                    ),
                    callback=self.parse,
                    cb_kwargs={"chaptertime": y},
                )
        else:
            msg = f"No Chapters found at: {response.url}"
            logger.error(msg)
        msg = f"A New Comic found at: {response.url}"
        logger.info(msg)

    def parse(self, response, chaptertime):
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
        url = response.url

        chapterslug = f"{comictitle} {response.xpath(
                '//button[contains(@class, "px-3 py-2 dropdown-btn")]/h2/text()',
            )
            .get()
            .split("-")[-0]}"

        comicslug = response.xpath(
            "//div[@class='flex flex-col items-center space-y-2 pt-6 px-5 text-center']/p/a/span/text()",  # noqa: E501
        ).get()
        loader = ItemLoader(item=ChapterItem(), selector=response)
        loader.add_value("url", url)
        loader.add_value("updated_at", chaptertime)
        loader.add_value("comictitle", comictitle)
        loader.add_value("comicslug", comicslug)
        if chaptertitle.lower() != chaptername.lower():
            loader.add_value("chaptertitle", chaptertitle)
        loader.add_value("chaptername", chaptername)
        loader.add_value("chapterslug", chapterslug)
        image_urls = response.xpath(
            '//div[contains(@class, "w-full mx-auto center")]/img[contains(@class, "object-cover mx-auto")]/@src',  # noqa: E501
        ).getall()
        if image_urls:
            images = []
            for img in image_urls:
                images.append(response.urljoin(img))  # noqa: PERF401
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
