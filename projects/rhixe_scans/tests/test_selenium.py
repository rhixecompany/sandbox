from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa: N812
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_argument("start-maximized")  # noqa: ERA001
# run in headless mode
# options.add_argument("--headless")

# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)  # noqa: FBT003
s = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)


try:
    driver.get("https://comick.io/comic/00-jujutsu-kaisen/")
    # Define a timeout for the explicit wait (e.g., 10 seconds)
    wait = WebDriverWait(driver, 10)
    # Wait for a specific element to be visible and clickable
    element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@class='md:hidden col-span-3 break-words max-md:mb-4']/h1"),
        ),
    )
    # # Perform actions on the element
    # element.click()
    # You can also wait for the page title to change
    wait.until(EC.title_contains("Jujutsu Kaisen | ComicK"))
    title_element = (
        driver.find_element(
            By.XPATH,
            "//*[@class='md:hidden col-span-3 break-words max-md:mb-4']/h1",
        ),
    )
    text = title_element.text  # type: ignore  # noqa: PGH003.getText();
    print(text)

finally:
    # Close the driver
    driver.quit()
