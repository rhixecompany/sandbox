import os
from contextlib import suppress
from io import BytesIO

from itemadapter import ItemAdapter
from PIL import Image
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.http.request import NO_CALLBACK
from scrapy.pipelines.files import _md5sum
from scrapy.pipelines.images import ImagesPipeline


class MyImagesPipeline(ImagesPipeline):


    def check_gif(self, image):
        if image.format == "GIF":
            return True
        return image.info.get("version") in ["GIF89a", "GIF87a"]

    def persist_gif(self, key, data, info):
        root, ext = os.path.splitext(key)  # noqa: PTH122
        key = key + ".gif"
        absolute_path = self.store._get_filesystem_path(key)  # type: ignore  # noqa: PGH003, SLF001
        self.store._mkdir(os.path.dirname(absolute_path), info)  # type: ignore  # noqa: PGH003, PTH120, SLF001
        with open(absolute_path, "wb") as f:  # noqa: PTH123
            f.write(data)

    def image_downloaded(self, response, request, info, *, item=None):
        adapter = ItemAdapter(item)
        if adapter.get("image_urls"):
            if adapter.get("image_urls") and adapter.get("slug"):
                checksum: str | None = None
                for path, image, buf in self.get_images(
                    response,
                    request,
                    info,
                    item=item,
                ):
                    if checksum is None:
                        buf.seek(0)
                        checksum = _md5sum(buf)
                    width, height = image.size

                    if path.startswith(adapter.get("slug")) and self.check_gif(image):  # type: ignore  # noqa: PGH003
                        self.persist_gif(path, response.body, info)
                    else:
                        self.store.persist_file(
                            path,
                            buf,
                            info,
                            meta={"width": width, "height": height},
                            headers={"Content-Type": "image/jpeg"},  # type: ignore  # noqa: PGH003
                        )
                assert checksum is not None
                return checksum
            if (
                adapter.get("image_urls")
                and adapter.get("comicslug")
                and adapter.get("chapterslug")
            ):
                checksum = None
                for path, image, buf in self.get_images(
                    response,
                    request,
                    info,
                    item=item,
                ):
                    if checksum is None:
                        buf.seek(0)
                        checksum = _md5sum(buf)
                    width, height = image.size

                    if path.startswith(adapter.get("comicslug")) and self.check_gif(  # type: ignore  # noqa: PGH003
                        image,
                    ):
                        self.persist_gif(path, response.body, info)
                    else:
                        self.store.persist_file(
                            path,
                            buf,
                            info,
                            meta={"width": width, "height": height},
                            headers={"Content-Type": "image/jpeg"},  # type: ignore  # noqa: PGH003
                        )
                assert checksum is not None
                return checksum
        msg = f"Missing field in MyImagesPipeline get_media_requests: {item!r}"
        raise DropItem(msg)

    def convert_image(
        self,
        image: Image.Image,
        size: tuple[int, int] | None = None,
        *,
        response_body: BytesIO,
    ) -> tuple[Image.Image, BytesIO]:
        if image.format in ("PNG", "WEBP") and image.mode == "RGBA":
            background = self._Image.new("RGBA", image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert("RGB")
        elif image.mode == "P":
            image = image.convert("RGBA")
            background = self._Image.new("RGBA", image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert("RGB")
        elif image.mode != "RGB":
            image = image.convert("RGB")

        if size:
            image = image.copy()
            try:
                # Image.Resampling.LANCZOS was added in Pillow 9.1.0
                # remove this try except block,
                # when updating the minimum requirements for Pillow.
                resampling_filter = self._Image.Resampling.LANCZOS
            except AttributeError:
                resampling_filter = self._Image.ANTIALIAS  # type: ignore[attr-defined]
            image.thumbnail(size, resampling_filter)
        elif image.format == "JPEG":
            return image, response_body

        buf = BytesIO()
        image.save(buf, "JPEG")
        return image, buf

    def get_media_requests(self, item, info):
        adapter = ItemAdapter(item)
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        if adapter.get("image_urls"):
            if adapter.get("image_urls") and adapter.get("slug"):
                return [
                    Request(
                        u,
                        callback=NO_CALLBACK,
                        meta={

                            "comicslug": item.get("slug"),
                        },
                    )
                    for u in urls
                ]
            if (
                adapter.get("image_urls")
                and adapter.get("comicslug")
                and adapter.get("chapterslug")
            ):
                return [
                    Request(
                        u,
                        callback=NO_CALLBACK,
                        meta={

                            "comicslug": item.get("comicslug"),
                            "chapterslug": item.get("chapterslug"),
                        },
                    )
                    for u in urls[1:2]
                ]
        msg = f"Missing field in MyImagesPipeline get_media_requests: {item!r}"
        raise DropItem(msg)

    def item_completed(self, results, item, info):
        with suppress(KeyError):
            images = [x for ok, x in results if ok]
            if not images:
                msg = f"MyImagesPipeline item_completed contains no images: {item!r}"
                raise DropItem(msg)
            adapter = ItemAdapter(item)
            adapter["images"] = images
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        adapter = ItemAdapter(item)
        if adapter.get("image_urls"):
            if adapter.get("image_urls") and adapter.get("slug"):
                image_file = request.url.split("/")[-1]
                return f"{request.meta['comicslug']}/{image_file}"
            if (
                adapter.get("image_urls")
                and adapter.get("comicslug")
                and adapter.get("chapterslug")
            ):
                image_file = request.url.split("/")[-1]
                return f"{request.meta['comicslug']}/{request.meta['chapterslug']}/{image_file}"  # noqa: E501
        msg = f"Missing field in file_path: {item!r}"
        raise DropItem(msg)
