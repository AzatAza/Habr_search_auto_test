from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=10) -> WebElement:
        """
        Find element on the page
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find {locator}",
        )
        return element

    def click_element(self, locator) -> None:
        """
        Click_element == click()
        """
        element = self.find_element(locator)
        element.click()

    def fill_element(self, data, locator) -> None:
        """
        Fill element == send_keys()
        """
        element = self.find_element(locator)
        if data:
            element.clear()
            element.send_keys(data)
            element.send_keys(Keys.ENTER)

    def get_title_text(self) -> str:
        """
        Get title's text
        """
        title_text = self.app.driver.title
        return title_text
