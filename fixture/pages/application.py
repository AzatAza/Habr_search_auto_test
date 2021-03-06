from fixture.pages.main_page import MainPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.title = driver.title
        self.search = MainPage(self)

    def quit(self):
        self.driver.quit()

    def open_main_page(self):
        self.driver.get(self.url)
