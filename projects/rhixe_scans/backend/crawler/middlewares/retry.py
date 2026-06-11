import logging

from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message
from twisted.internet import defer
from twisted.internet import reactor

logger = logging.getLogger(__name__)


async def async_sleep(delay, return_value=None):
    deferred = defer.Deferred()
    reactor.callLater(delay, deferred.callback, return_value)  # type: ignore  # noqa: PGH003
    return await deferred


class TooManyRequestsRetryMiddleware(RetryMiddleware):
    """
    Modifies RetryMiddleware to delay retries on status 429.
    """

    DEFAULT_DELAY = 4  # Delay in seconds.
    MAX_DELAY = 8  # Sometimes, RETRY-AFTER has absurd values

    async def process_response(self, request, response, spider):
        """
        Like RetryMiddleware.process_response, but, if response status is 429,
        retry the request only after waiting at most self.MAX_DELAY seconds.
        Respect the Retry-After header if it's less than self.MAX_DELAY.
        If Retry-After is absent/invalid, wait only self.DEFAULT_DELAY seconds.
        """

        if request.meta.get("dont_retry", False):
            return response

        if response.status in self.retry_http_codes:
            if response.status == 429:  # noqa: PLR2004
                retry_after = response.headers.get("retry-after")
                try:
                    retry_after = int(retry_after)  # type: ignore  # noqa: PGH003
                except (ValueError, TypeError):
                    delay = self.DEFAULT_DELAY
                else:
                    delay = min(self.MAX_DELAY, retry_after)
                logger.info(f"Retrying {request} in {delay} seconds.")  # noqa: G004

                spider.crawler.engine.pause()  # type: ignore  # noqa: PGH003
                await async_sleep(delay)
                spider.crawler.engine.unpause()  # type: ignore  # noqa: PGH003

            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response

        return response
