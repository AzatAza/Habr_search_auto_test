import logging


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fixture.pages.application import Application

logger = logging.getLogger("habr")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://habr.com/",
        help="Habr url",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    ),


@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")

    # Driver's options
    chrome_options = Options()
    if headless == "false":
        chrome_options.headless = False
    else:
        chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    logger.info(f"Start app on {url}")
    app = Application(driver, url)
    yield app
    app.quit()
