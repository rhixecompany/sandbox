from shutil import which

from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait


def test_eight_components():
    driver = setup()

    title = driver.title
    print(title)  # noqa: T201

    driver.implicitly_wait(0.5)
    revealed = driver.find_element(
        By.XPATH,
        "//div[contains(@class, 'w-full mx-auto center')]/img[contains(@class, 'object-cover mx-auto')]",  # noqa: E501
    )

    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(
        driver,
        timeout=2,
        poll_frequency=0.2,
        ignored_exceptions=errors,
    )
    wait.until(lambda d: revealed.is_displayed())
    images = []
    imgs = driver.find_elements(
        By.XPATH,
        "//div[contains(@class, 'w-full mx-auto center')]/img[contains(@class, 'object-cover mx-auto')]",  # noqa: E501
    )
    for im in imgs:
        images.append(im.get_attribute("src"))  # noqa: PERF401

    print(images)  # noqa: T201

    teardown(driver)


def get_default_firefox_options():
    options = Options()
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("javascript.enabled", True)  # noqa: FBT003
    options.profile = firefox_profile
    options.add_argument("-headless")
    options.binary_location = which("firefox")  # type: ignore  # noqa: PGH003
    return options


def get_default_firefox_service():
    gecko = which("geckodriver")
    return webdriver.FirefoxService(
        executable_path=gecko,  # type: ignore  # noqa: PGH003
        service_args=["--profile-root", "./profile", "--log", "debug"],
    )


def setup():
    service = get_default_firefox_service()  # type: ignore  # noqa: PGH003
    options = get_default_firefox_options()
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://asuracomic.net/series/nano-machine-923317b4/chapter/239")
    return driver


def teardown(driver):
    driver.quit()


test_eight_components()
