# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys
from pathlib import Path

import django
from django.conf import settings

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(os.path.join(BASE_DIR, "config"))  # noqa: PTH118
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")
django.setup()

BOT_NAME = "crawler"

SPIDER_MODULES = ["crawler.spiders"]
NEWSPIDER_MODULE = "crawler.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"  # noqa: E501

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",  # noqa: E501
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",  # noqa: E501
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",  # noqa: E501
    " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",  # noqa: E501
    "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",  # noqa: E501
    "Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko) PlayStation Vita Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2",  # noqa: E501
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02",  # noqa: E501
    "Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343",  # noqa: E501
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; YandexAccessibilityBot/3.0; +http://yandex.com/bots",
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
CONCURRENT_REQUESTS_PER_DOMAIN = 64
CONCURRENT_REQUESTS_PER_IP = 64

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False  # noqa: ERA001

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False  # noqa: ERA001

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {  # noqa: ERA001, RUF100
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",  # noqa: E501, ERA001
#    "Accept-Language": "en",
# }  # noqa: ERA001, RUF100

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    "crawler.middlewares.default.CrawlerSpiderMiddleware": 543,
    # "crawler.middlewares.main.SeleniumMiddleware": 800,
}
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "crawler.middlewares.rotate.RotateUserAgentMiddleware": 540,
    "crawler.middlewares.retry.TooManyRequestsRetryMiddleware": 541,
    "crawler.middlewares.default.CrawlerDownloaderMiddleware": 543,
    # "crawler.middlewares.mymain.MyCustomMiddleware": 800,
}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {  # noqa: ERA001, RUF100
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }  # noqa: ERA001, RUF100

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "crawler.pipelines.download_images.MyImagesPipeline": 1,
    "crawler.pipelines.default.CrawlerDefaultPipeline": 200,
    "crawler.pipelines.db.DbPipeline": 300,
    # "crawler.pipelines.redis.red.CrawlerRedisPipeline": 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True  # noqa: ERA001
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5 # noqa: ERA001
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60 # noqa: ERA001
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0 # noqa: ERA001
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False # noqa: ERA001

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 86400
HTTPCACHE_DIR = "cache"
HTTPCACHE_IGNORE_HTTP_CODES = list(range(300, 501))
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
HTTPCACHE_GZIP = False
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

FEED_EXPORT_ENCODING = "utf-8"
# DOWNLOAD_HANDLERS = {  # noqa: ERA001, RUF100
#     "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",  # noqa: E501, ERA001
#     "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",  # noqa: E501, ERA001
# }  # noqa: ERA001, RUF100
# FEEDS = {  # noqa: ERA001, RUF100
#     "comics.json": {
#         "format": "json",  # noqa: ERA001
#         "encoding": "utf8",  # noqa: ERA001
#         "store_empty": False,  # noqa: ERA001
#         "indent": 4,  # noqa: ERA001
#     },
# }  # noqa: ERA001, RUF100
FEEDS = {
    "comicsdata.json": {
        "format": "json",
        "encoding": "utf8",
        "store_empty": False,
        "item_classes": ["crawler.items.ComicItem"],
        "fields": None,
        "indent": 4,
    },
    "chaptersdata.json": {
        "format": "json",
        "encoding": "utf8",
        "store_empty": False,
        "item_classes": ["crawler.items.ChapterItem"],
        "fields": None,
        "indent": 4,
    },
}
RETRY_TIMES = 2
RETRY_ENABLED = True
RETRY_HTTP_CODES = list(range(300, 501))

DOWNLOAD_FAIL_ON_DATALOSS = True
LOG_LEVEL = "DEBUG"
# LOG_LEVEL = "INFO"  # noqa: ERA001, RUF100

# AWS
# IMAGES_STORE = "s3://bucket/images"  # noqa: ERA001
# IMAGES_STORE_S3_ACL = "public-read"  # noqa: ERA001
# AWS_ENDPOINT_URL = "http://minio.example.com:9000"  # noqa: ERA001
# AWS_USE_SSL = False  # or True (None by default)  # noqa: ERA001
# AWS_VERIFY = False  # or True (None by default)  # noqa: ERA001

# GCLOUD
# IMAGES_STORE = "gs://bucket/images/"  # noqa: ERA001
# GCS_PROJECT_ID = "project_id"  # noqa: ERA001
# IMAGES_STORE_GCS_ACL = "publicRead"  # noqa: ERA001

# Aws
# AWS_ACCESS_KEY_ID = "ae187701acd22a77779ce3ebfa32e101"  # noqa: ERA001
# AWS_SECRET_ACCESS_KEY = "c92576a34dd08fbd5932efe0a32cf363f5a17c5af1da5ec4c390da815dab6962"  # noqa: E501, ERA001
# AWS_REGION_NAME =  "us-east-2"  # noqa: ERA001
# AWS_ENDPOINT_URL = "https://fowvdrdkbqhmevigbkyb.supabase.co/storage/v1/s3"  # noqa: E501, ERA001
# IMAGES_STORE_S3_ACL = "bucket-owner-full-control"  # noqa: ERA001
# # IMAGES_STORE_S3_ACL = "public-read"  # noqa: ERA001
# # AWS_USE_SSL = False  # noqa: ERA001
# # AWS_VERIFY = False  # noqa: ERA001
# AWS_USE_SSL = True  # noqa: ERA001
# AWS_VERIFY = True  # noqa: ERA001
# IMAGES_STORE = "s3://mystore/media/"  # noqa: ERA001


# # LOCAL
IMAGES_STORE = settings.MEDIA_ROOT

IMAGES_URLS_FIELD = "image_urls"
IMAGES_RESULT_FIELD = "images"

# 1460 days of delay for files expiration
FILES_EXPIRES = 1460

# 730 days of delay for images expiration
IMAGES_EXPIRES = 730


# IMAGES_THUMBS = {  # noqa: ERA001, RUF100
#     "small": (50, 50),  # noqa: ERA001
#     "big": (270, 270),  # noqa: ERA001
# }  # noqa: ERA001, RUF100


IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110

MEDIA_ALLOW_REDIRECTS = True

# REDIS_URL = settings.CELERY_BROKER_URL  # noqa: ERA001
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # noqa: ERA001
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"  # noqa: ERA001
# SCHEDULER_PERSIST = False  # noqa: ERA001

# # SELENIUM_DRIVER_NAME = "firefox"  # noqa: ERA001
# # SELENIUM_DRIVER_EXECUTABLE_PATH = which("geckodriver")  # noqa: ERA001
# # SELENIUM_BROWSER_EXECUTABLE_PATH = which("firefox")  # noqa: ERA001
# SELENIUM_DRIVER_NAME = "chrome"  # noqa: ERA001
# SELENIUM_DRIVER_EXECUTABLE_PATH = None  # noqa: ERA001
# # SELENIUM_DRIVER_EXECUTABLE_PATH = which("chromedriver")  # noqa: ERA001
# # SELENIUM_BROWSER_EXECUTABLE_PATH = which("chrome")  # noqa: ERA001

# SELENIUM_DRIVER_ARGUMENTS = [  # noqa: ERA001, RUF100
#     # "--headless",
#     "--disable-blink-features=AutomationControlled",  # noqa: ERA001
#     "--no-sandbox",
#     "--disable-gpu",
#     "--enable-javascript",
#     "--disable-extensions",
#     "--block-ads",
#     "--enable-unsafe-swiftshader",
# ]  # change it to ['-headless'] to run in headless mode
# PLAYWRIGHT_PROCESS_REQUEST_HEADERS = None  # noqa: ERA001
# settings.py
DOWNLOAD_HANDLERS = {
    "http": "crawler.handlers.play.handler.ScrapyPlaywrightDownloadHandler",
    "https": "crawler.handlers.play.handler.ScrapyPlaywrightDownloadHandler",
}
