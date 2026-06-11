from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_argument("start-maximized")
# run in headless mode
options.add_argument("--headless")

# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)  # noqa: FBT003
s = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

# Selenium Stealth settings
stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

driver.get("https://comick.io/comic/00-jujutsu-kaisen/")
# wait for the interstitial page to load
sleep(10)
# Perform actions on the page
parent_element = driver.find_element(
    By.XPATH,
    "//*[@class='md:hidden col-span-3 break-words max-md:mb-4']",
)
# child_element = parent_element.find_element(By.XPATH, ".//h1/text()")
element = driver.find_element(By.XPATH, "//*[@id='__NEXT_DATA__']")
# assert parent_element.is_displayed()
print(parent_element)  # noqa: T201
print(element)  # noqa: T201
# close browser
driver.quit()
