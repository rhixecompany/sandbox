from itemadapter.adapter import ItemAdapter
from scrapy.exceptions import DropItem


class CrawlerDefaultPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("image_urls"):
            if adapter.get("image_urls") and adapter.get("slug"):
                item["spider"] = spider.name
                return item
            if (
                adapter.get("image_urls")
                and adapter.get("comicslug")
                and adapter.get("chapterslug")
            ):
                item["spider"] = spider.name
                return item
            return None
        msg = f"CrawlerDefaultPipeline Item has a Missing field:{item!r}"
        raise DropItem(
            msg,
        )
