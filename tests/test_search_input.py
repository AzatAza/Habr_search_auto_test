from fixture.constants import Constants


class TestMainPage:
    def test_search_input(self, app):
        """
        Steps:
        1. Open main page
        2. Add existing product in search input
        3. Check result
        """
        app.open_main_page()
        app.search.click_button()
        app.search.search_input()
        assert Constants.TEXT in app.search.find_title_text()
