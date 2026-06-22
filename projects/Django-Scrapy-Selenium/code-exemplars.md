# Code Exemplars — Django-Scrapy-Selenium

## 1. Scrapy Spider

```python
import scrapy

class ComicSpider(scrapy.Spider):
    name = "comics"
    start_urls = ["https://example.com/comics"]

    def parse(self, response):
        for comic in response.css(".comic-item"):
            yield {
                "title": comic.css("h2::text").get(),
                "url": comic.css("a::attr(href)").get(),
                "image": comic.css("img::attr(src)").get(),
            }
```

## 2. Selenium Scraper

```javascript
import { Builder, By, until } from "selenium-webdriver";

async function scrapeComics() {
  const driver = await new Builder().forBrowser("chrome").build();
  try {
    await driver.get("https://example.com/comics");
    await driver.wait(until.elementLocated(By.css(".comic-item")), 10000);
    const titles = await driver.findElements(By.css("h2"));
    // ... extract data
  } finally {
    await driver.quit();
  }
}
```
