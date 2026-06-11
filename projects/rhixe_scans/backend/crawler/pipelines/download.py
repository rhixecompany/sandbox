import hashlib
import mimetypes
from pathlib import Path
from typing import cast

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.http.request import NO_CALLBACK
from scrapy.http.request import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.python import to_bytes


class MyFilesPipeline(FilesPipeline):
    # Overridable Interface
    def get_media_requests(
        self,
        item,
        info,
    ):
        adapter = ItemAdapter(item)
        if adapter.get("file_urls"):
            if adapter.get("slug"):
                urls = ItemAdapter(item).get(self.file_urls_field, [])  # type: ignore  # noqa: PGH003
                return [
                    Request(
                        u,
                        callback=NO_CALLBACK,
                        meta={
                            "comicfolderslug": item.get("slug"),
                        },
                    )
                    for u in urls
                ]
            if adapter.get("comicslug") and adapter.get("chapterslug"):
                urls = ItemAdapter(item).get(self.file_urls_field, [])  # type: ignore  # noqa: PGH003
                return [
                    Request(
                        u,
                        callback=NO_CALLBACK,
                        meta={
                            "comicfolderslug": item.get("comicslug"),
                            "chapterfolderslug": item.get("chapterslug"),
                        },
                    )
                    for u in urls
                ]
            return None
        msg = f"Missing field in get_media_requests: {item!r}"
        raise DropItem(msg)

    def file_path(
        self,
        request,
        response,
        info,
        *,
        item,
    ):
        adapter = ItemAdapter(item)
        if adapter.get("file_urls"):
            if adapter.get("file_urls") and adapter.get("slug"):
                media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()  # nosec  # noqa: S324
                media_ext = Path(request.url).suffix
                # Handles empty and wild extensions by trying to guess the
                # mime type then extension or default to empty string otherwise
                if media_ext not in mimetypes.types_map:
                    media_ext = ""
                    media_type = mimetypes.guess_type(request.url)[0]
                    if media_type:
                        media_ext = cast(str, mimetypes.guess_extension(media_type))  # noqa: TC006
                return f"{request.meta['comicfolderslug']}/{media_guid}{media_ext}"
            if (
                adapter.get("file_urls")
                and adapter.get("comicslug")
                and adapter.get("chapterslug")
            ):
                media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()  # nosec  # noqa: S324
                media_ext = Path(request.url).suffix
                # Handles empty and wild extensions by trying to guess the
                # mime type then extension or default to empty string otherwise
                if media_ext not in mimetypes.types_map:
                    media_ext = ""
                    media_type = mimetypes.guess_type(request.url)[0]
                    if media_type:
                        media_ext = cast(str, mimetypes.guess_extension(media_type))  # noqa: TC006
                return f"{request.meta['comicfolderslug']}/{request.meta['chapterfolderslug']}/{media_guid}{media_ext}"  # noqa: E501
            return None
        msg = f"Missing field in file_path: {item!r}"
        raise DropItem(msg)

    def process_item(self, item, spider):
        return item
