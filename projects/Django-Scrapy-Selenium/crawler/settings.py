import os  # noqa: I001

from shutil import which
import sys
from pathlib import Path

import django
from django.conf import settings


from scrapy.utils.reactor import install_reactor

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(os.path.join(BASE_DIR, "config"))  # noqa: PTH118
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")
django.setup()

BOT_NAME = "crawler"

SPIDER_MODULES = ["crawler.spiders"]
NEWSPIDER_MODULE = "crawler.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"  # noqa: E501

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",  # noqa: E501
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",  # noqa: E501
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",  # noqa: E501
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",  # noqa: E501
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",  # noqa: E501
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",  # noqa: E501
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 128

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 128
CONCURRENT_REQUESTS_PER_IP = 128

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    "crawler.middlewares.default.CrawlerSpiderMiddleware": 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "crawler.middlewares.rotate.RotateUserAgentMiddleware": 540,
    "crawler.middlewares.retry.TooManyRequestsRetryMiddleware": 541,
    "crawler.middlewares.default.CrawlerDownloaderMiddleware": 543,
    "crawler.middlewares.sele.NewSeleniumMiddleware": 800,
    # "scrapy_selenium.middlewares.SeleniumMiddleware": 800,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    "scrapy.extensions.telnet.TelnetConsole": None,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# # The initial download delay
AUTOTHROTTLE_START_DELAY = 0
# # The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 5
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 128
# # Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
# HTTPCACHE_EXPIRATION_SECS = 0  # noqa: ERA001
# HTTPCACHE_DIR = "httpcache"  # noqa: ERA001
# HTTPCACHE_IGNORE_HTTP_CODES = list(range(300, 501))  # noqa: ERA001
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"  # noqa: E501, ERA001
# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_CLASS = "crawler.utils.RequestFingerprinter"
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = install_reactor(
    "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
)
FEED_EXPORT_ENCODING = "utf-8"

# Local store
IMAGES_STORE = settings.MEDIA_ROOT

# # Production store
# AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID  # noqa: ERA001
# AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY  # noqa: ERA001
# AWS_STORAGE_BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME  # noqa: ERA001
# IMAGES_STORE = "s3://{}/media/".format(AWS_STORAGE_BUCKET_NAME)  # noqa: ERA001
# AWS_REGION_NAME = settings.AWS_S3_REGION_NAME  # noqa: ERA001
RETRY_TIMES = 2
RETRY_ENABLED = True
RETRY_HTTP_CODES = list(range(300, 501))
MEDIA_ALLOW_REDIRECTS = True
DOWNLOAD_FAIL_ON_DATALOSS = True
LOG_LEVEL = "INFO"
LOG_FORMATTER = "crawler.utils.PoliteLogFormatter"
ADDONS = {
    "crawler.addon.MyAddon": 1,
}
EXTENSIONS = {"crawler.extensions.SpiderOpenCloseLogging": 500}
IMAGES_EXPIRES = 730


# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # noqa: ERA001
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"  # noqa: ERA001
# SCHEDULER_PERSIST = False  # noqa: ERA001
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"  # noqa: ERA001
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # noqa: ERA001
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"  # noqa: ERA001
# REDIS_URL = settings.CELERY_BROKER_URL  # noqa: ERA001
# SCHEDULER_FLUSH_ON_START = True  # noqa: ERA001

SELENIUM_DRIVER_NAME = "firefox"
SELENIUM_DRIVER_EXECUTABLE_PATH = which("geckodriver")
# SELENIUM_BROWSER_EXECUTABLE_PATH = "C:/'Program Files'/'Mozilla Firefox'/firefox.exe"  # noqa: E501, ERA001
SELENIUM_BROWSER_EXECUTABLE_PATH = which("firefox")
# SELENIUM_DRIVER_EXECUTABLE_PATH = "./geckodriver" # noqa: ERA001
# SELENIUM_BROWSER_EXECUTABLE_PATH = "C:/'Program Files'/'Mozilla Firefox'/firefox.exe"  # noqa: E501, ERA001
SELENIUM_DRIVER_ARGUMENTS = [
    "--headless",
    "--no-sandbox",
    "--disable-gpu",
    "-profile",
    "./profile",
]  # change it to ['-headless'] run in headless mode

ITEM_PIPELINES = {
    "crawler.pipelines.download.CrawlerDownloadPipeline": 1,
    "crawler.pipelines.dupelicate.CrawlerDupelicatePipeline": 200,
    "crawler.pipelines.appsdb.CrawlerAppsDbPipeline": 300,
    # "crawler.pipelines.redis.red.CrawlerRedisPipeline": 400,
}

FEEDS = {
    "comics.json": {
        "format": "json",
        "encoding": "utf8",
        "store_empty": False,
        "item_classes": ["crawler.items.ComicItem"],
        "fields": None,
        "indent": 4,
    },
    "chapters.json": {
        "format": "json",
        "encoding": "utf8",
        "store_empty": False,
        "item_classes": ["crawler.items.ChapterItem"],
        "fields": None,
        "indent": 4,
    },
}
