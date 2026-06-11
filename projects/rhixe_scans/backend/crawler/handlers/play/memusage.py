from contextlib import suppress
from importlib import import_module
from typing import List  # noqa: UP035

from scrapy.exceptions import NotConfigured
from scrapy.extensions.memusage import MemoryUsage
from scrapy_playwright.handler import ScrapyPlaywrightDownloadHandler
from scrapy_playwright.handler import logger

_MIB_FACTOR = 1024**2


class ScrapyPlaywrightMemoryUsageExtension(MemoryUsage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        try:
            self.psutil = import_module("psutil")
        except ImportError as exc:
            msg = "The psutil module is not available"
            raise NotConfigured(msg) from exc

    def _get_main_process_ids(self) -> List[int]:  # noqa: UP006
        try:
            return [
                handler.playwright_context_manager._connection._transport._proc.pid  # noqa: PGH003, RUF100, SLF001 # type: ignore
                for handler in self.crawler.engine.downloader.handlers._handlers.values()  # noqa: E501, PGH003, RUF100, SLF001 # type: ignore
                if isinstance(handler, ScrapyPlaywrightDownloadHandler)
                and handler.playwright_context_manager
            ]
        except Exception:  # noqa: BLE001
            return []

    def _get_descendant_processes(self, process) -> list:
        children = process.children()
        result = children.copy()
        for child in children:
            result.extend(self._get_descendant_processes(child))
        return result

    def _get_total_playwright_process_memory(self) -> int:
        process_list = [
            self.psutil.Process(pid) for pid in self._get_main_process_ids()
        ]
        for proc in process_list.copy():
            process_list.extend(self._get_descendant_processes(proc))
        total_process_size = 0
        for proc in process_list:
            with suppress(
                Exception,
            ):  # might fail if the process exited in the meantime
                total_process_size += proc.memory_info().rss
        logger.debug(
            "Total Playwright process memory: %i Bytes (%i MiB)",
            total_process_size,
            total_process_size / _MIB_FACTOR,
        )
        return total_process_size

    def get_virtual_size(self) -> int:
        return super().get_virtual_size() + self._get_total_playwright_process_memory()
