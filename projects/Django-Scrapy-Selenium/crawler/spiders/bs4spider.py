import scrapy
from bs4 import BeautifulSoup


class Bs4Spider(scrapy.Spider):
    name = "bs4_spider"
    start_urls = [
        "https://asuracomic.net/series/surviving-the-game-as-a-barbarian-888b4a68/chapter/81",
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract data using BeautifulSoup
        title = soup.find("title").text  # type: ignore  # noqa: PGH003
        links = [a["href"] for a in soup.find_all("a")]
        images = [img["src"] for img in soup.find_all("img")]
        # Yield items or requests as needed
        yield {"title": title, "links": links, "image_urls": images}
