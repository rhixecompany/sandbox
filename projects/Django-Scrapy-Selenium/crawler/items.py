# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dateparser import parse
from django.utils.text import slugify
from itemloaders.processors import MapCompose
from itemloaders.processors import TakeFirst
from scrapy.item import Field
from scrapy.item import Item
from w3lib.html import remove_comments
from w3lib.html import remove_tags
from w3lib.html import strip_html5_whitespace


def gen_slug(value):
    return slugify(value)


def get_slug(value):
    return value.split("/")[-1].split("-")[-0]


def get_des(value):
    return (
        value.replace("\\n", "")
        .replace("\r", "")
        .replace("\\r", "")
        .replace("rn", "")
        .replace("rnrnxa0 ", "")
        .replace("kindness.", "")
        .replace("\xa0", "")
        .replace("\\xa0", "")
        .replace("//", "")
        .replace("\\", "")
        .replace("\\", "")
        .replace("\n", "")
        .replace("/n", "")
        .replace("['", "")
        .replace("']", "")
        .replace("'", "")
    )


def get_date(value):
    return parse(value, languages=["en"], date_formats=["%d/%m/%Y"]).date()  # type: ignore  # noqa: PGH003


def get_html(value):
    return remove_tags(value)


def strip_html(value):
    return strip_html5_whitespace(value)


def comments_html(value):
    return remove_comments(value)


class ComicItem(Item):
    title = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    description = Field(
        input_processor=MapCompose(get_des, strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    slug = Field(input_processor=MapCompose(gen_slug), output_processor=TakeFirst())

    rating = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    status = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    type = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    updated_at = Field(
        input_processor=MapCompose(get_date),
        output_processor=TakeFirst(),
    )
    serialization = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )

    author = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    artist = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    genres = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
    )
    url = Field(output_processor=TakeFirst())
    spider = Field(output_processor=TakeFirst())
    numchapters = Field(output_processor=TakeFirst())
    image_urls = Field()
    images = Field()


class ChapterItem(Item):
    comictitle = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    comicslug = Field(
        input_processor=MapCompose(gen_slug),
        output_processor=TakeFirst(),
    )
    chaptertitle = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    chaptername = Field(
        input_processor=MapCompose(strip_html, comments_html, get_html),
        output_processor=TakeFirst(),
    )
    chapterslug = Field(
        input_processor=MapCompose(gen_slug, get_html),
        output_processor=TakeFirst(),
    )
    updated_at = Field(
        input_processor=MapCompose(get_date),
        output_processor=TakeFirst(),
    )
    url = Field(output_processor=TakeFirst())
    spider = Field(output_processor=TakeFirst())
    image_urls = Field()
    images = Field()
