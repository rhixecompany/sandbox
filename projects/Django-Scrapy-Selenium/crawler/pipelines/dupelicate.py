from itemadapter.adapter import ItemAdapter
from scrapy.exceptions import DropItem

from api.apps.models import Comic


class CrawlerDupelicatePipeline:
    def __init__(self):
        self.slug_seen = list(
            Comic.objects.prefetch_related(
                "comicitems",
                "comicchapters",
                "genres",
                "followers",
            )
            .select_related("author", "type", "artist", "user")
            .all()
            .values_list("slug", flat=True)
            .distinct(),
        )

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("image_urls"):
            if adapter.get("slug"):
                if adapter["slug"] in self.slug_seen:
                    msg = f"ComicItem Already Exists In The Database:{item!r}"
                    raise DropItem(msg)
                item["spider"] = spider.name
                return item
            if adapter.get("comicslug") and adapter.get("chapterslug"):
                item["spider"] = spider.name
                return item
            return None

        msg = f"CrawlerDupelicatePipeline Item has a Missing field:{item!r}"
        raise DropItem(
            msg,
        )
