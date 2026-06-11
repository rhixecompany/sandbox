import asyncio
import logging
import os

from selenium_driverless import webdriver
from selenium_driverless.scripts.network_interceptor import InterceptedRequest
from selenium_driverless.scripts.network_interceptor import NetworkInterceptor

logger = logging.getLogger(__name__)

proxy = os.getenv("mobileproxyuk")  # noqa: SIM112
if proxy is None:
    logger.error("no proxy found in env")


async def on_request(data: InterceptedRequest):
    if "api" in data.request.url and data.request.method == "POST":
        global auth  # noqa: PLW0603
        try:
            if data.request.headers["authorization"]:
                auth = data.request.headers
                logger.info(auth)
        except KeyError:
            logger.error("no auth header found in req")  # noqa: TRY400


async def main():
    options = webdriver.ChromeOptions()
    if proxy:
        options.single_proxy = proxy
    async with webdriver.Chrome(options=options) as driver:  # noqa: SIM117
        async with NetworkInterceptor(driver, on_request=on_request):
            await driver.get("https://comick.io/comic/00-jujutsu-kaisen/")
            await driver.sleep(6)


asyncio.run(main())
