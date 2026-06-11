import asyncio
import inspect
import logging
import platform
import warnings
from contextlib import suppress
from dataclasses import dataclass
from dataclasses import field as dataclass_field
from functools import partial
from ipaddress import ip_address
from time import time
from typing import Awaitable  # noqa: UP035
from typing import Callable  # noqa: UP035
from typing import Dict  # noqa: UP035
from typing import Optional
from typing import Tuple  # noqa: UP035
from typing import Type  # noqa: UP035
from typing import TypeVar
from typing import Union

from playwright._impl._errors import TargetClosedError
from playwright.async_api import BrowserContext
from playwright.async_api import BrowserType
from playwright.async_api import Download as PlaywrightDownload
from playwright.async_api import Error as PlaywrightError
from playwright.async_api import Page
from playwright.async_api import Playwright as AsyncPlaywright
from playwright.async_api import (
    PlaywrightContextManager,  # type: ignore  # noqa: PGH003
)
from playwright.async_api import Request as PlaywrightRequest
from playwright.async_api import Response as PlaywrightResponse
from playwright.async_api import Route
from scrapy import Spider
from scrapy import signals
from scrapy.core.downloader.handlers.http import HTTPDownloadHandler
from scrapy.crawler import Crawler
from scrapy.exceptions import NotSupported
from scrapy.exceptions import ScrapyDeprecationWarning
from scrapy.http import Request
from scrapy.http import Response
from scrapy.http.headers import Headers
from scrapy.responsetypes import responsetypes
from scrapy.settings import Settings
from scrapy.utils.defer import deferred_from_coro
from scrapy.utils.misc import load_object
from scrapy.utils.reactor import verify_installed_reactor
from scrapy_playwright._utils import _encode_body
from scrapy_playwright._utils import _get_float_setting
from scrapy_playwright._utils import _get_header_value
from scrapy_playwright._utils import _get_page_content
from scrapy_playwright._utils import _is_safe_close_error
from scrapy_playwright._utils import _maybe_await
from scrapy_playwright._utils import _ThreadedLoopAdapter
from scrapy_playwright.headers import use_scrapy_headers
from scrapy_playwright.page import PageMethod
from twisted.internet.defer import Deferred
from twisted.internet.defer import inlineCallbacks

__all__ = ["ScrapyPlaywrightDownloadHandler"]


PlaywrightHandler = TypeVar(
    "PlaywrightHandler",
    bound="ScrapyPlaywrightDownloadHandler",
)


logger = logging.getLogger("scrapy-playwright")


DEFAULT_BROWSER_TYPE = "chromium"
DEFAULT_CONTEXT_NAME = "default"
PERSISTENT_CONTEXT_PATH_KEY = "user_data_dir"


@dataclass
class BrowserContextWrapper:
    context: BrowserContext
    semaphore: asyncio.Semaphore
    persistent: bool


@dataclass
class Download:
    body: bytes = b""
    url: str = ""
    suggested_filename: str = ""
    exception: Optional[Exception] = None  # noqa: UP007
    response_status: int = 200
    headers: dict = dataclass_field(default_factory=dict)

    def __bool__(self) -> bool:
        return bool(self.body) or bool(self.exception)


@dataclass
class Config:
    cdp_url: Optional[str]  # noqa: UP007
    cdp_kwargs: dict
    connect_url: Optional[str]  # noqa: UP007
    connect_kwargs: dict
    browser_type_name: str
    launch_options: dict
    max_pages_per_context: int
    max_contexts: Optional[int]  # noqa: UP007
    startup_context_kwargs: dict
    navigation_timeout: Optional[float]  # noqa: UP007
    restart_disconnected_browser: bool
    target_closed_max_retries: int = 3
    use_threaded_loop: bool = False

    @classmethod
    def from_settings(cls, settings: Settings) -> "Config":
        if settings.get("PLAYWRIGHT_CDP_URL") and settings.get(
            "PLAYWRIGHT_CONNECT_URL",
        ):
            msg = "Setting both PLAYWRIGHT_CDP_URL and PLAYWRIGHT_CONNECT_URL is not supported"  # noqa: E501
            logger.error(msg)
            raise NotSupported(msg)
        cfg = cls(
            cdp_url=settings.get("PLAYWRIGHT_CDP_URL"),
            cdp_kwargs=settings.getdict("PLAYWRIGHT_CDP_KWARGS") or {},
            connect_url=settings.get("PLAYWRIGHT_CONNECT_URL"),
            connect_kwargs=settings.getdict("PLAYWRIGHT_CONNECT_KWARGS") or {},
            browser_type_name=settings.get("PLAYWRIGHT_BROWSER_TYPE")
            or DEFAULT_BROWSER_TYPE,
            launch_options=settings.getdict("PLAYWRIGHT_LAUNCH_OPTIONS") or {},
            max_pages_per_context=settings.getint("PLAYWRIGHT_MAX_PAGES_PER_CONTEXT"),
            max_contexts=settings.getint("PLAYWRIGHT_MAX_CONTEXTS") or None,
            startup_context_kwargs=settings.getdict("PLAYWRIGHT_CONTEXTS"),
            navigation_timeout=_get_float_setting(
                settings,
                "PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT",
            ),
            restart_disconnected_browser=settings.getbool(
                "PLAYWRIGHT_RESTART_DISCONNECTED_BROWSER",
                default=True,
            ),
            use_threaded_loop=platform.system() == "Windows"
            or settings.getbool("_PLAYWRIGHT_THREADED_LOOP", False),  # noqa: FBT003
        )
        cfg.cdp_kwargs.pop("endpoint_url", None)
        cfg.connect_kwargs.pop("ws_endpoint", None)
        if not cfg.max_pages_per_context:
            cfg.max_pages_per_context = settings.getint("CONCURRENT_REQUESTS")
        if (cfg.cdp_url or cfg.connect_url) and cfg.launch_options:
            logger.warning(
                "Connecting to remote browser, ignoring PLAYWRIGHT_LAUNCH_OPTIONS",
            )
        return cfg


class ScrapyPlaywrightDownloadHandler(HTTPDownloadHandler):
    playwright_context_manager: Optional[PlaywrightContextManager] = None  # noqa: UP007
    playwright: Optional[AsyncPlaywright] = None  # noqa: UP007

    def __init__(self, crawler: Crawler) -> None:
        super().__init__(settings=crawler.settings, crawler=crawler)
        verify_installed_reactor(
            "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        )
        crawler.signals.connect(self._engine_started, signals.engine_started)
        self.stats = crawler.stats
        self.config = Config.from_settings(crawler.settings)

        if self.config.use_threaded_loop:
            _ThreadedLoopAdapter.start(id(self))

        self.browser_launch_lock = asyncio.Lock()
        self.context_launch_lock = asyncio.Lock()
        self.context_wrappers: Dict[str, BrowserContextWrapper] = {}  # noqa: UP006
        if self.config.max_contexts:
            self.context_semaphore = asyncio.Semaphore(value=self.config.max_contexts)

        # headers
        if "PLAYWRIGHT_PROCESS_REQUEST_HEADERS" in crawler.settings:
            if crawler.settings["PLAYWRIGHT_PROCESS_REQUEST_HEADERS"] is None:
                self.process_request_headers = None
            else:
                self.process_request_headers = load_object(
                    crawler.settings["PLAYWRIGHT_PROCESS_REQUEST_HEADERS"],
                )
        else:
            self.process_request_headers = use_scrapy_headers

        self.abort_request: Optional[  # noqa: UP007
            Callable[[PlaywrightRequest], Union[Awaitable, bool]]  # noqa: UP007
        ] = None
        if crawler.settings.get("PLAYWRIGHT_ABORT_REQUEST"):
            self.abort_request = load_object(
                crawler.settings["PLAYWRIGHT_ABORT_REQUEST"],
            )

    @classmethod
    def from_crawler(
        cls: Type[PlaywrightHandler],  # noqa: UP006
        crawler: Crawler,
    ) -> PlaywrightHandler:
        return cls(crawler)

    def _deferred_from_coro(self, coro: Awaitable) -> Deferred:
        if self.config.use_threaded_loop:
            return _ThreadedLoopAdapter._deferred_from_coro(coro)  # noqa: SLF001
        return deferred_from_coro(coro)

    def _engine_started(self) -> Deferred:
        """Launch the browser. Use the engine_started signal as it supports returning deferreds."""  # noqa: E501
        return self._deferred_from_coro(self._launch())

    async def _launch(self) -> None:
        """Launch Playwright manager and configured startup context(s)."""
        logger.info("Starting download handler")
        self.playwright_context_manager = PlaywrightContextManager()
        self.playwright = await self.playwright_context_manager.start()
        self.browser_type: BrowserType = getattr(
            self.playwright,
            self.config.browser_type_name,
        )
        if self.config.startup_context_kwargs:
            logger.info(
                "Launching %i startup context(s)",
                len(self.config.startup_context_kwargs),
            )
            await asyncio.gather(
                *[
                    self._create_browser_context(name=name, context_kwargs=kwargs)
                    for name, kwargs in self.config.startup_context_kwargs.items()
                ],
            )
            self._set_max_concurrent_context_count()
            logger.info("Startup context(s) launched")
            self.stats.set_value("playwright/page_count", self._get_total_page_count())  # type: ignore  # noqa: PGH003

    async def _maybe_launch_browser(self) -> None:
        async with self.browser_launch_lock:
            if not hasattr(self, "browser"):
                logger.info("Launching browser %s", self.browser_type.name)
                self.browser = await self.browser_type.launch(
                    **self.config.launch_options,
                )
                logger.info("Browser %s launched", self.browser_type.name)
                self.stats.inc_value("playwright/browser_count")  # type: ignore  # noqa: PGH003
                self.browser.on("disconnected", self._browser_disconnected_callback)  # type: ignore  # noqa: PGH003

    async def _maybe_connect_remote_devtools(self) -> None:
        async with self.browser_launch_lock:
            if not hasattr(self, "browser"):
                logger.info("Connecting using CDP: %s", self.config.cdp_url)
                self.browser = await self.browser_type.connect_over_cdp(
                    self.config.cdp_url, **self.config.cdp_kwargs  # type: ignore  # noqa: COM812, PGH003
                )
                logger.info("Connected using CDP: %s", self.config.cdp_url)
                self.stats.inc_value("playwright/browser_count")  # type: ignore  # noqa: PGH003
                self.browser.on("disconnected", self._browser_disconnected_callback)  # type: ignore  # noqa: PGH003

    async def _maybe_connect_remote(self) -> None:
        async with self.browser_launch_lock:
            if not hasattr(self, "browser"):
                logger.info("Connecting to remote Playwright")
                self.browser = await self.browser_type.connect(
                    self.config.connect_url, **self.config.connect_kwargs  # type: ignore  # noqa: COM812, PGH003
                )
                logger.info("Connected to remote Playwright")
                self.stats.inc_value("playwright/browser_count")  # type: ignore  # noqa: PGH003
                self.browser.on("disconnected", self._browser_disconnected_callback)  # type: ignore  # noqa: PGH003

    async def _create_browser_context(
        self,
        name: str,
        context_kwargs: Optional[dict],  # noqa: UP007
        spider: Optional[Spider] = None,  # noqa: UP007
    ) -> BrowserContextWrapper:
        """Create a new context, also launching a local browser or connecting
        to a remote one if necessary.
        """
        if hasattr(self, "context_semaphore"):
            await self.context_semaphore.acquire()
        context_kwargs = context_kwargs or {}
        persistent = remote = False
        if context_kwargs.get(PERSISTENT_CONTEXT_PATH_KEY):
            context = await self.browser_type.launch_persistent_context(
                **context_kwargs,
            )
            persistent = True
        elif self.config.cdp_url:
            await self._maybe_connect_remote_devtools()
            context = await self.browser.new_context(**context_kwargs)
            remote = True
        elif self.config.connect_url:
            await self._maybe_connect_remote()
            context = await self.browser.new_context(**context_kwargs)
            remote = True
        else:
            await self._maybe_launch_browser()
            context = await self.browser.new_context(**context_kwargs)

        context.on(
            "close",
            self._make_close_browser_context_callback(name, persistent, remote, spider),
        )
        self.stats.inc_value("playwright/context_count")  # type: ignore  # noqa: PGH003
        self.stats.inc_value(f"playwright/context_count/persistent/{persistent}")  # type: ignore  # noqa: PGH003
        self.stats.inc_value(f"playwright/context_count/remote/{remote}")  # type: ignore  # noqa: PGH003
        logger.debug(
            "Browser context started: '%s' (persistent=%s, remote=%s)",
            name,
            persistent,
            remote,
            extra={
                "spider": spider,
                "context_name": name,
                "persistent": persistent,
                "remote": remote,
            },
        )
        if self.config.navigation_timeout is not None:
            context.set_default_navigation_timeout(self.config.navigation_timeout)
        self.context_wrappers[name] = BrowserContextWrapper(
            context=context,
            semaphore=asyncio.Semaphore(value=self.config.max_pages_per_context),
            persistent=persistent,
        )
        self._set_max_concurrent_context_count()
        return self.context_wrappers[name]

    async def _create_page(self, request: Request, spider: Spider) -> Page:
        """Create a new page in a context, also creating a new context if necessary."""
        context_name = request.meta.setdefault(
            "playwright_context",
            DEFAULT_CONTEXT_NAME,
        )
        # this block needs to be locked because several attempts to launch a context
        # with the same name could happen at the same time from different requests
        async with self.context_launch_lock:
            ctx_wrapper = self.context_wrappers.get(context_name)
            if ctx_wrapper is None:
                ctx_wrapper = await self._create_browser_context(
                    name=context_name,
                    context_kwargs=request.meta.get("playwright_context_kwargs"),
                    spider=spider,
                )

        await ctx_wrapper.semaphore.acquire()
        page = await ctx_wrapper.context.new_page()
        self.stats.inc_value("playwright/page_count")  # type: ignore  # noqa: PGH003
        total_page_count = self._get_total_page_count()
        logger.debug(
            "[Context=%s] New page created, page count is %i (%i for all contexts)",
            context_name,
            len(ctx_wrapper.context.pages),
            total_page_count,
            extra={
                "spider": spider,
                "context_name": context_name,
                "context_page_count": len(ctx_wrapper.context.pages),
                "total_page_count": total_page_count,
                "scrapy_request_url": request.url,
                "scrapy_request_method": request.method,
            },
        )
        self._set_max_concurrent_page_count()
        if self.config.navigation_timeout is not None:
            page.set_default_navigation_timeout(self.config.navigation_timeout)

        page.on("close", self._make_close_page_callback(context_name))
        page.on("crash", self._make_close_page_callback(context_name))
        page.on("request", self._increment_request_stats)
        page.on("response", self._increment_response_stats)
        if logger.getEffectiveLevel() <= logging.DEBUG:
            page.on("request", _make_request_logger(context_name, spider))
            page.on("response", _make_response_logger(context_name, spider))

        return page

    def _get_total_page_count(self):
        return sum(len(ctx.context.pages) for ctx in self.context_wrappers.values())

    def _set_max_concurrent_page_count(self):
        count = self._get_total_page_count()
        current_max_count = self.stats.get_value("playwright/page_count/max_concurrent")  # type: ignore  # noqa: PGH003
        if current_max_count is None or count > current_max_count:
            self.stats.set_value("playwright/page_count/max_concurrent", count)  # type: ignore  # noqa: PGH003

    def _set_max_concurrent_context_count(self):
        current_max_count = self.stats.get_value(  # type: ignore  # noqa: PGH003
            "playwright/context_count/max_concurrent",
        )
        if current_max_count is None or len(self.context_wrappers) > current_max_count:
            self.stats.set_value(  # type: ignore  # noqa: PGH003
                "playwright/context_count/max_concurrent",
                len(self.context_wrappers),
            )

    @inlineCallbacks  # type: ignore  # noqa: PGH003
    def close(self) -> Deferred:  # type: ignore  # noqa: PGH003
        logger.info("Closing download handler")
        yield super().close()  # type: ignore  # noqa: PGH003
        yield self._deferred_from_coro(self._close())  # type: ignore  # noqa: PGH003
        if self.config.use_threaded_loop:
            _ThreadedLoopAdapter.stop(id(self))

    async def _close(self) -> None:
        with suppress(TargetClosedError):
            await asyncio.gather(
                *[ctx.context.close() for ctx in self.context_wrappers.values()],
            )
        self.context_wrappers.clear()
        if hasattr(self, "browser"):
            logger.info("Closing browser")
            await self.browser.close()
        if self.playwright_context_manager:
            await self.playwright_context_manager.__aexit__()
        if self.playwright:
            await self.playwright.stop()

    def download_request(self, request: Request, spider: Spider) -> Deferred:
        if request.meta.get("playwright"):
            return self._deferred_from_coro(self._download_request(request, spider))
        return super().download_request(request, spider)

    async def _download_request(self, request: Request, spider: Spider) -> Response:
        counter = 0
        while True:
            try:
                return await self._download_request_with_retry(
                    request=request,
                    spider=spider,
                )
            except TargetClosedError as ex:
                counter += 1
                if counter > self.config.target_closed_max_retries:
                    raise ex  # noqa: TRY201
                logger.debug(
                    "Target closed, retrying to create page for %s",
                    request,
                    extra={
                        "spider": spider,
                        "scrapy_request_url": request.url,
                        "scrapy_request_method": request.method,
                        "exception": ex,
                    },
                )

    async def _download_request_with_retry(
        self,
        request: Request,
        spider: Spider,
    ) -> Response:
        page = request.meta.get("playwright_page")
        if not isinstance(page, Page) or page.is_closed():
            page = await self._create_page(request=request, spider=spider)
        context_name = request.meta.setdefault(
            "playwright_context",
            DEFAULT_CONTEXT_NAME,
        )

        _attach_page_event_handlers(
            page=page,
            request=request,
            spider=spider,
            context_name=context_name,
        )

        # We need to identify the Playwright request that matches the Scrapy request
        # in order to override method and body if necessary.
        # Checking the URL and Request.is_navigation_request() is not enough, e.g.
        # requests produced by submitting forms can produce false positives.
        # Let's track only the first request that matches the above conditions.
        initial_request_done = asyncio.Event()

        await page.unroute("**")
        await page.route(
            "**",
            self._make_request_handler(
                context_name=context_name,
                method=request.method,
                url=request.url,
                headers=request.headers,
                body=request.body,
                encoding=request.encoding,
                spider=spider,
                initial_request_done=initial_request_done,
            ),
        )

        await _maybe_execute_page_init_callback(
            page=page,
            request=request,
            context_name=context_name,
            spider=spider,
        )

        try:
            return await self._download_request_with_page(request, page, spider)
        except Exception as ex:
            if not request.meta.get("playwright_include_page") and not page.is_closed():
                logger.warning(
                    "Closing page due to failed request: %s exc_type=%s exc_msg=%s",
                    request,
                    type(ex),
                    str(ex),
                    extra={
                        "spider": spider,
                        "context_name": context_name,
                        "scrapy_request_url": request.url,
                        "scrapy_request_method": request.method,
                        "exception": ex,
                    },
                    exc_info=True,
                )
                await page.close()
                self.stats.inc_value("playwright/page_count/closed")  # type: ignore  # noqa: PGH003
            raise

    async def _download_request_with_page(
        self,
        request: Request,
        page: Page,
        spider: Spider,
    ) -> Response:
        # set this early to make it available in errbacks even if something fails
        if request.meta.get("playwright_include_page"):
            request.meta["playwright_page"] = page

        start_time = time()
        response, download = await self._get_response_and_download(
            request,
            page,
            spider,
        )
        if isinstance(response, PlaywrightResponse):
            await _set_redirect_meta(request=request, response=response)
            headers = Headers(await response.all_headers())
            headers.pop("Content-Encoding", None)
        elif not download:
            logger.warning(
                "Navigating to %s returned None, the response"
                " will have empty headers and status 200",
                request,
                extra={
                    "spider": spider,
                    "context_name": request.meta.get("playwright_context"),
                    "scrapy_request_url": request.url,
                    "scrapy_request_method": request.method,
                },
            )
            headers = Headers()

        await self._apply_page_methods(page, request, spider)
        body_str = await _get_page_content(
            page=page,
            spider=spider,
            context_name=request.meta.get("playwright_context"),  # type: ignore  # noqa: PGH003
            scrapy_request_url=request.url,
            scrapy_request_method=request.method,
        )
        request.meta["download_latency"] = time() - start_time

        server_ip_address = None
        if response is not None:
            request.meta["playwright_security_details"] = (
                await response.security_details()
            )
            with suppress(KeyError, TypeError, ValueError):
                server_addr = await response.server_addr()
                server_ip_address = ip_address(server_addr["ipAddress"])  # type: ignore  # noqa: PGH003

        if download and download.exception:
            raise download.exception

        if not request.meta.get("playwright_include_page"):
            await page.close()
            self.stats.inc_value("playwright/page_count/closed")  # type: ignore  # noqa: PGH003

        if download:
            request.meta["playwright_suggested_filename"] = download.suggested_filename
            respcls = responsetypes.from_args(url=download.url, body=download.body)
            download_headers = Headers(download.headers)
            download_headers.pop("Content-Encoding", None)
            return respcls(
                url=download.url,
                status=download.response_status,
                headers=download_headers,
                body=download.body,
                request=request,
                flags=["playwright"],
            )

        body, encoding = _encode_body(headers=headers, text=body_str)
        respcls = responsetypes.from_args(headers=headers, url=page.url, body=body)
        return respcls(
            url=page.url,
            status=response.status if response is not None else 200,
            headers=headers,
            body=body,
            request=request,
            flags=["playwright"],
            encoding=encoding,  # type: ignore  # noqa: PGH003
            ip_address=server_ip_address,
        )

    async def _get_response_and_download(
        self,
        request: Request,
        page: Page,
        spider: Spider,
    ) -> Tuple[Optional[PlaywrightResponse], Optional[Download]]:  # noqa: UP006, UP007
        response: Optional[PlaywrightResponse] = None  # noqa: UP007
        download: Download = Download()  # updated in-place in _handle_download
        download_started = asyncio.Event()
        download_ready = asyncio.Event()

        async def _handle_download(dwnld: PlaywrightDownload) -> None:
            download_started.set()
            self.stats.inc_value("playwright/download_count")  # type: ignore  # noqa: PGH003
            try:
                if failure := await dwnld.failure():
                    msg = f"Failed to download {dwnld.url}: {failure}"
                    raise RuntimeError(msg)  # noqa: TRY301
                download.body = (await dwnld.path()).read_bytes()
                download.url = dwnld.url
                download.suggested_filename = dwnld.suggested_filename
            except Exception as ex:  # noqa: BLE001
                download.exception = ex
            finally:
                download_ready.set()

        async def _handle_response(response: PlaywrightResponse) -> None:
            download.response_status = response.status
            download.headers = await response.all_headers()
            download_started.set()

        page_goto_kwargs = request.meta.get("playwright_page_goto_kwargs") or {}
        page_goto_kwargs.pop("url", None)
        page.on("download", _handle_download)
        page.on("response", _handle_response)
        try:
            response = await page.goto(url=request.url, **page_goto_kwargs)
        except PlaywrightError as err:
            if not (
                self.config.browser_type_name in ("firefox", "webkit")  # noqa: RUF021
                and "Download is starting" in err.message
                or self.config.browser_type_name == "chromium"  # noqa: RUF021
                and "net::ERR_ABORTED" in err.message
            ):
                raise

            logger.debug(
                "Navigating to %s failed",
                request.url,
                extra={
                    "spider": spider,
                    "context_name": request.meta.get("playwright_context"),
                    "scrapy_request_url": request.url,
                    "scrapy_request_method": request.method,
                },
            )
            await download_started.wait()

            if download.response_status == 204:  # noqa: PLR2004
                raise err  # noqa: TRY201

            logger.debug(
                "Waiting on download to finish for %s",
                request.url,
                extra={
                    "spider": spider,
                    "context_name": request.meta.get("playwright_context"),
                    "scrapy_request_url": request.url,
                    "scrapy_request_method": request.method,
                },
            )
            await download_ready.wait()
        finally:
            page.remove_listener("download", _handle_download)
            page.remove_listener("response", _handle_response)

        return response, download if download else None

    async def _apply_page_methods(
        self,
        page: Page,
        request: Request,
        spider: Spider,
    ) -> None:
        context_name = request.meta.get("playwright_context")
        page_methods = request.meta.get("playwright_page_methods") or ()
        if isinstance(page_methods, dict):
            page_methods = page_methods.values()
        for pm in page_methods:
            if isinstance(pm, PageMethod):
                try:
                    if callable(pm.method):
                        method = partial(pm.method, page)
                    else:
                        method = getattr(page, pm.method)
                except AttributeError as ex:
                    logger.warning(
                        "Ignoring %r: could not find method",
                        pm,
                        extra={
                            "spider": spider,
                            "context_name": context_name,
                            "scrapy_request_url": request.url,
                            "scrapy_request_method": request.method,
                            "exception": ex,
                        },
                        exc_info=True,
                    )
                else:
                    pm.result = await _maybe_await(method(*pm.args, **pm.kwargs))
                    await page.wait_for_load_state(
                        timeout=self.config.navigation_timeout,
                    )
            else:
                logger.warning(
                    "Ignoring %r: expected PageMethod, got %r",
                    pm,
                    type(pm),
                    extra={
                        "spider": spider,
                        "context_name": context_name,
                        "scrapy_request_url": request.url,
                        "scrapy_request_method": request.method,
                    },
                )

    def _increment_request_stats(self, request: PlaywrightRequest) -> None:
        stats_prefix = "playwright/request_count"
        self.stats.inc_value(stats_prefix)  # type: ignore  # noqa: PGH003
        self.stats.inc_value(f"{stats_prefix}/resource_type/{request.resource_type}")  # type: ignore  # noqa: PGH003
        self.stats.inc_value(f"{stats_prefix}/method/{request.method}")  # type: ignore  # noqa: PGH003
        if request.is_navigation_request():
            self.stats.inc_value(f"{stats_prefix}/navigation")  # type: ignore  # noqa: PGH003

    def _increment_response_stats(self, response: PlaywrightResponse) -> None:
        stats_prefix = "playwright/response_count"
        self.stats.inc_value(stats_prefix)  # type: ignore  # noqa: PGH003
        self.stats.inc_value(  # type: ignore  # noqa: PGH003
            f"{stats_prefix}/resource_type/{response.request.resource_type}",
        )
        self.stats.inc_value(f"{stats_prefix}/method/{response.request.method}")  # type: ignore  # noqa: PGH003

    async def _browser_disconnected_callback(self) -> None:
        close_context_coros = [
            ctx_wrapper.context.close()
            for ctx_wrapper in self.context_wrappers.values()
        ]
        self.context_wrappers.clear()
        with suppress(TargetClosedError):
            await asyncio.gather(*close_context_coros)
        logger.debug("Browser disconnected")
        if self.config.restart_disconnected_browser:
            del self.browser

    def _make_close_page_callback(self, context_name: str) -> Callable:
        def close_page_callback() -> None:
            if context_name in self.context_wrappers:
                self.context_wrappers[context_name].semaphore.release()

        return close_page_callback

    def _make_close_browser_context_callback(
        self,
        name: str,
        persistent: bool,  # noqa: FBT001
        remote: bool,  # noqa: FBT001
        spider: Optional[Spider] = None,  # noqa: UP007
    ) -> Callable:
        def close_browser_context_callback() -> None:
            self.context_wrappers.pop(name, None)
            if hasattr(self, "context_semaphore"):
                self.context_semaphore.release()
            logger.debug(
                "Browser context closed: '%s' (persistent=%s, remote=%s)",
                name,
                persistent,
                remote,
                extra={
                    "spider": spider,
                    "context_name": name,
                    "persistent": persistent,
                    "remote": remote,
                },
            )

        return close_browser_context_callback

    def _make_request_handler(  # noqa: C901, PLR0913
        self,
        context_name: str,
        method: str,
        url: str,
        headers: Headers,
        body: Optional[bytes],  # noqa: UP007
        encoding: str,
        spider: Spider,
        initial_request_done: asyncio.Event,
    ) -> Callable:
        async def _request_handler(  # noqa: C901
            route: Route,
            playwright_request: PlaywrightRequest,
        ) -> None:
            """Override request headers, method and body."""
            if self.abort_request:
                should_abort = await _maybe_await(
                    self.abort_request(playwright_request),
                )
                if should_abort:
                    await route.abort()
                    logger.debug(
                        "[Context=%s] Aborted Playwright request <%s %s>",
                        context_name,
                        playwright_request.method.upper(),
                        playwright_request.url,
                        extra={
                            "spider": spider,
                            "context_name": context_name,
                            "scrapy_request_url": url,
                            "scrapy_request_method": method,
                            "playwright_request_url": playwright_request.url,
                            "playwright_request_method": playwright_request.method,
                        },
                    )
                    self.stats.inc_value("playwright/request_count/aborted")  # type: ignore  # noqa: PGH003
                    return None  # noqa: RET501

            overrides: dict = {}

            if self.process_request_headers is None:
                final_headers = await playwright_request.all_headers()
            elif (sig := inspect.signature(self.process_request_headers)) and (
                "browser_type_name" in sig.parameters
                and "playwright_request" in sig.parameters
                and "scrapy_request_data" in sig.parameters
            ):
                overrides["headers"] = final_headers = await _maybe_await(
                    self.process_request_headers(
                        browser_type_name=self.config.browser_type_name,
                        playwright_request=playwright_request,
                        scrapy_request_data={
                            "method": method,
                            "url": url,
                            "headers": headers,
                            "body": body,
                            "encoding": encoding,
                        },
                    ),
                )
            else:
                warnings.warn(
                    "Accepting positional arguments in the function passed to the"
                    " PLAYWRIGHT_PROCESS_REQUEST_HEADERS setting is deprecated. The function"  # noqa: E501
                    " should accept three (3) keyword arguments instead:"
                    " browser_type_name: str,"
                    " playwright_request: playwright.async_api.Request,"
                    " scrapy_request_data: dict",
                    category=ScrapyDeprecationWarning,
                    stacklevel=1,
                )
                overrides["headers"] = final_headers = await _maybe_await(
                    self.process_request_headers(
                        self.config.browser_type_name,  # type: ignore  # noqa: PGH003
                        playwright_request,
                        headers,
                    ),
                )

            # if the current request corresponds to the original scrapy one
            if (
                playwright_request.url.rstrip("/") == url.rstrip("/")
                and playwright_request.is_navigation_request()
                and not initial_request_done.is_set()
            ):
                initial_request_done.set()
                if method.upper() != playwright_request.method.upper():
                    overrides["method"] = method
                if body:
                    overrides["post_data"] = body.decode(encoding)
                # the request that reaches the callback should contain the final headers
                headers.clear()
                headers.update(final_headers)

            del final_headers

            original_playwright_method: str = playwright_request.method
            try:
                await route.continue_(**overrides)
                if overrides.get("method"):
                    logger.debug(
                        "[Context=%s] Overridden method for Playwright request"
                        " to %s: original=%s new=%s",
                        context_name,
                        playwright_request.url,
                        original_playwright_method,
                        overrides["method"],
                        extra={
                            "spider": spider,
                            "context_name": context_name,
                            "scrapy_request_url": url,
                            "scrapy_request_method": method,
                            "playwright_request_url": playwright_request.url,
                            "playwright_request_method_original": original_playwright_method,  # noqa: E501
                            "playwright_request_method_new": overrides["method"],
                        },
                    )
            except PlaywrightError as ex:
                if _is_safe_close_error(ex):
                    logger.warning(
                        "Failed processing Playwright request: <%s %s> exc_type=%s exc_msg=%s",  # noqa: E501
                        playwright_request.method,
                        playwright_request.url,
                        type(ex),
                        str(ex),
                        extra={
                            "spider": spider,
                            "context_name": context_name,
                            "scrapy_request_url": url,
                            "scrapy_request_method": method,
                            "playwright_request_url": playwright_request.url,
                            "playwright_request_method": playwright_request.method,
                            "exception": ex,
                        },
                        exc_info=True,
                    )
                else:
                    raise

        return _request_handler


def _attach_page_event_handlers(
    page: Page,
    request: Request,
    spider: Spider,
    context_name: str,
) -> None:
    event_handlers = request.meta.get("playwright_page_event_handlers") or {}
    for event, handler in event_handlers.items():
        if callable(handler):
            page.on(event, handler)  # type: ignore  # noqa: PGH003
        elif isinstance(handler, str):
            try:
                page.on(event, getattr(spider, handler))
            except AttributeError as ex:
                logger.warning(
                    "Spider '%s' does not have a '%s' attribute,"
                    " ignoring handler for event '%s'",
                    spider.name,
                    handler,
                    event,
                    extra={
                        "spider": spider,
                        "context_name": context_name,
                        "scrapy_request_url": request.url,
                        "scrapy_request_method": request.method,
                        "exception": ex,
                    },
                    exc_info=True,
                )


async def _set_redirect_meta(request: Request, response: PlaywrightResponse) -> None:
    """Update a Scrapy request with metadata about redirects."""
    redirect_times: int = 0
    redirect_urls: list = []
    redirect_reasons: list = []
    redirected = response.request.redirected_from
    while redirected is not None:
        redirect_times += 1
        redirect_urls.append(redirected.url)
        redirected_response = await redirected.response()
        reason = None if redirected_response is None else redirected_response.status
        redirect_reasons.append(reason)
        redirected = redirected.redirected_from
    if redirect_times:
        request.meta["redirect_times"] = redirect_times
        request.meta["redirect_urls"] = list(reversed(redirect_urls))
        request.meta["redirect_reasons"] = list(reversed(redirect_reasons))


async def _maybe_execute_page_init_callback(
    page: Page,
    request: Request,
    context_name: str,
    spider: Spider,
) -> None:
    page_init_callback = request.meta.get("playwright_page_init_callback")
    if page_init_callback:
        try:
            page_init_callback = load_object(page_init_callback)
            await page_init_callback(page, request)
        except Exception as ex:  # noqa: BLE001
            logger.warning(
                "[Context=%s] Page init callback exception for %s exc_type=%s exc_msg=%s",  # noqa: E501
                context_name,
                repr(request),
                type(ex),
                str(ex),
                extra={
                    "spider": spider,
                    "context_name": context_name,
                    "scrapy_request_url": request.url,
                    "scrapy_request_method": request.method,
                    "exception": ex,
                },
                exc_info=True,
            )


def _make_request_logger(context_name: str, spider: Spider) -> Callable:
    async def _log_request(request: PlaywrightRequest) -> None:
        log_args = [
            context_name,
            request.method.upper(),
            request.url,
            request.resource_type,
        ]
        referrer = await _get_header_value(request, "referer")
        if referrer:
            log_args.append(referrer)
            log_msg = "[Context=%s] Request: <%s %s> (resource type: %s, referrer: %s)"
        else:
            log_msg = "[Context=%s] Request: <%s %s> (resource type: %s)"
        logger.debug(
            log_msg,
            *log_args,
            extra={
                "spider": spider,
                "context_name": context_name,
                "playwright_request_url": request.url,
                "playwright_request_method": request.method,
                "playwright_resource_type": request.resource_type,
            },
        )

    return _log_request


def _make_response_logger(context_name: str, spider: Spider) -> Callable:
    async def _log_response(response: PlaywrightResponse) -> None:
        log_args = [context_name, response.status, response.url]
        location = await _get_header_value(response, "location")
        if location:
            log_args.append(location)
            log_msg = "[Context=%s] Response: <%i %s> (location: %s)"
        else:
            log_msg = "[Context=%s] Response: <%i %s>"
        logger.debug(
            log_msg,
            *log_args,
            extra={
                "spider": spider,
                "context_name": context_name,
                "playwright_response_url": response.url,
                "playwright_response_status": response.status,
            },
        )

    return _log_response
