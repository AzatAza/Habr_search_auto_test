from selenium.webdriver.common.by import By


class Locators:
    SEARCH_BTN = (By.XPATH, '//a[contains(@href,"search")]')
    SEARCH_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/main/div/div/div/div/div/div[2]/form/div/input')
