import logging

from fixture.constants import Constants
from fixture.locators.locators import Locators
from fixture.pages.base_page import BasePage

logger = logging.getLogger("grocery")


class MainPage(BasePage):
    def click_button(self) -> None:
        """
        Click element by locator
        """
        self.click_element(locator=Locators.SEARCH_BTN)

    def search_input(self) -> None:
        """
        Search and input text on the search field
        """
        logger.info(f"Search {Constants.TEXT} on the grocery page")
        self.fill_element(data=Constants.TEXT, locator=Locators.SEARCH_INPUT)

    def find_title_text(self) -> str:
        """
         Find title's text and get it
        """
        return self.get_title_text()
