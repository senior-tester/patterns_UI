import allure
from tests_selenium.pages.locators import sale_page as loc
from tests_selenium.pages.base_page import BasePage


class SalePage(BasePage):
    REL_URL = '/sale.html'

    @allure.step('Check page header')
    def check_header_is_(self, header_text):
        header = self.find(loc.SALE_HEADER)
        assert header.text == header_text
