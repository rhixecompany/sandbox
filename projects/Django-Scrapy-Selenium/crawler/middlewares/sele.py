"""This module contains the ``SeleniumMiddleware`` scrapy middleware"""

from importlib import import_module

from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.http import HtmlResponse  # type: ignore  # noqa: PGH003
from scrapy_selenium.http import SeleniumRequest
from selenium.common import ElementNotInteractableException
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class NewSeleniumMiddleware:
    """Scrapy middleware handling the requests using selenium"""

    def __init__(
        self,
        driver_name,
        driver_executable_path,
        browser_executable_path,
        command_executor,
        driver_arguments,
    ):
        """Initialize the selenium webdriver

        Parameters
        ----------
        driver_name: str
            The selenium ``WebDriver`` to use
        driver_executable_path: str
            The path of the executable binary of the driver
        driver_arguments: list
            A list of arguments to initialize the driver
        browser_executable_path: str
            The path of the executable binary of the browser
        command_executor: str
            Selenium remote server endpoint
        """

        webdriver_base_path = f"selenium.webdriver.{driver_name}"

        driver_klass_module = import_module(f"{webdriver_base_path}.webdriver")
        driver_klass = getattr(driver_klass_module, "WebDriver")  # noqa: B009

        driver_options_module = import_module(f"{webdriver_base_path}.options")
        driver_options_klass = getattr(driver_options_module, "Options")  # noqa: B009

        driver_options = driver_options_klass()

        if browser_executable_path:
            driver_options.binary_location = browser_executable_path
        for argument in driver_arguments:
            driver_options.add_argument(argument)

        driver_kwargs = {
            "executable_path": driver_executable_path,
            f"{driver_name}_options": driver_options,
        }

        # locally installed driver
        if driver_executable_path is None:
            driver_kwargs = {
                "executable_path": driver_executable_path,
                f"{driver_name}_options": driver_options,
            }
            self.driver = driver_klass(**driver_kwargs)
        # remote driver
        elif command_executor is not None:
            from selenium import webdriver

            capabilities = driver_options.to_capabilities()
            self.driver = webdriver.Remote(
                command_executor=command_executor,
                desired_capabilities=capabilities,  # type: ignore  # noqa: PGH003
            )
        # webdriver-manager
        else:
            from selenium import webdriver
            from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            from selenium.webdriver.firefox.service import Service as FirefoxService
            from webdriver_manager.firefox import GeckoDriverManager

            if driver_name and driver_name.lower() == "firefox":
                options = FirefoxOptions()
                firefox_profile = FirefoxProfile()
                # firefox_profile.set_preference("javascript.enabled", True)  # noqa: E501, ERA001
                options.profile = firefox_profile

                options.add_argument(
                    "--headless",
                )
                options.add_argument(
                    "--no-sandbox",  # type: ignore  # noqa: PGH003
                )
                options.add_argument(
                    "--disable-gpu",
                )
                self.driver = webdriver.Firefox(
                    options=options,
                    service=FirefoxService(GeckoDriverManager().install()),
                )

    @classmethod
    def from_crawler(cls, crawler):
        """Initialize the middleware with the crawler settings"""

        driver_name = crawler.settings.get("SELENIUM_DRIVER_NAME")
        driver_executable_path = crawler.settings.get("SELENIUM_DRIVER_EXECUTABLE_PATH")
        browser_executable_path = crawler.settings.get(
            "SELENIUM_BROWSER_EXECUTABLE_PATH",
        )
        command_executor = crawler.settings.get("SELENIUM_COMMAND_EXECUTOR")
        driver_arguments = crawler.settings.get("SELENIUM_DRIVER_ARGUMENTS")

        if driver_name is None:
            msg = "SELENIUM_DRIVER_NAME must be set"
            raise NotConfigured(msg)

        # let's use webdriver-manager when nothing specified instead | RN just for Firefox  # noqa: E501
        if (driver_name.lower() != "firefox") and (
            driver_executable_path is None and command_executor is None
        ):
            msg = (
                "Either SELENIUM_DRIVER_EXECUTABLE_PATH "
                "or SELENIUM_COMMAND_EXECUTOR must be set"
            )
            raise NotConfigured(msg)

        middleware = cls(
            driver_name=driver_name,
            driver_executable_path=driver_executable_path,
            browser_executable_path=browser_executable_path,
            command_executor=command_executor,
            driver_arguments=driver_arguments,
        )

        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)

        return middleware

    def process_request(self, request, spider):
        """Process a request using the selenium driver if applicable"""

        if not isinstance(request, SeleniumRequest):
            return None

        self.driver.get(request.url)

        for cookie_name, cookie_value in request.cookies.items():  # type: ignore  # noqa: PGH003
            self.driver.add_cookie({"name": cookie_name, "value": cookie_value})

        if request.wait_until:
            # WebDriverWait(self.driver, request.wait_time).until(request.wait_until)  # type: ignore  # noqa: E501, ERA001, PGH003
            errors = [NoSuchElementException, ElementNotInteractableException]
            wait = WebDriverWait(
                self.driver,
                timeout=request.wait_time,  # type: ignore  # noqa: PGH003
                poll_frequency=0.2,
                ignored_exceptions=errors,
            )
            wait.until(request.wait_until)

        if request.screenshot:
            request.meta["screenshot"] = self.driver.get_screenshot_as_png()

        if request.script:
            self.driver.execute_script(request.script)

        body = str.encode(self.driver.page_source)

        # Expose the driver via the "meta" attribute
        request.meta.update({"driver": self.driver})

        return HtmlResponse(
            self.driver.current_url,
            body=body,
            encoding="utf-8",
            request=request,
        )

    def spider_closed(self):
        """Shutdown the driver when spider is closed"""

        self.driver.quit()
