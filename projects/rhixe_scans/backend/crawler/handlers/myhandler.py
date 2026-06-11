from scrapy.core.downloader.handlers.http import HTTPDownloadHandler


class MyCustomHTTPHandler(HTTPDownloadHandler):
    def download_request(self, request, spider):
        request.headers.setdefault(b"Authorization", b"Bearer mysecrettoken")
        spider.logger.info(f"Processing request: {request}")  # noqa: G004
        response = super().download_request(request, spider)
        if b"Error" in response.body:  # type: ignore  # noqa: PGH003
            spider.logger.warning(f"Error found in response: {response}")  # noqa: G004
        return response
