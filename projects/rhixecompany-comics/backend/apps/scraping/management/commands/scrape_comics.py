"""Scrapy/Selenium integration management commands."""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Scrape comics from external sources using Selenium automation"

    def add_arguments(self, parser):
        parser.add_argument("--source", type=str, default="", help="Source URL pattern to scrape")
        parser.add_argument("--output", type=str, default="", help="Output JSON file path")
        parser.add_argument("--headless", action="store_true", default=True, help="Run browser headless")
        parser.add_argument("--dry-run", action="store_true", default=False, help="Validate config only")

    def handle(self, *args, **options):
        source = options["source"] or os.getenv("SCRAPE_SOURCE", "")
        output = options["output"] or str(Path("scraped_data.json"))
        headless = options["headless"]
        dry_run = options["dry_run"]

        self.stdout.write(f"Source: {source or '(discovery mode)'}")
        self.stdout.write(f"Output: {output}")
        self.stdout.write(f"Headless: {headless}")

        if not source:
            self.stdout.write(self.style.WARNING("No source specified. Use --source or set SCRAPE_SOURCE env."))
            if dry_run:
                self.stdout.write(self.style.SUCCESS("Dry-run: Config looks valid."))
            return

        if dry_run:
            self.stdout.write(self.style.SUCCESS("Dry-run: Config looks valid. Ready to scrape."))
            return

        results = self._run_scraper(source, headless)
        Path(output).write_text(json.dumps(results, indent=2))
        self.stdout.write(self.style.SUCCESS(f"Scraped {len(results)} items → {output}"))

    def _run_scraper(self, source: str, headless: bool) -> list[dict]:
        """Execute Selenium scraper against the given source URL."""
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.support.ui import WebDriverWait
        except ImportError:
            self.stdout.write(self.style.ERROR("selenium not installed. Run: pip install selenium"))
            return []

        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

        driver = webdriver.Chrome(options=options)
        try:
            driver.get(source)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            time.sleep(2)

            items = driver.find_elements(By.CSS_SELECTOR, "a[href*='comic'], article, .comic-item")
            results = []
            for item in items[:50]:
                try:
                    results.append({
                        "text": item.text.strip(),
                        "href": item.get_attribute("href") or "",
                    })
                except Exception:
                    continue
            return results
        finally:
            driver.quit()
