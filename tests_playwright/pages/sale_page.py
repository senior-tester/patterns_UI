from tests_playwright.pages.base_page import BasePage
from playwright.sync_api import expect


HEADER = 'h1'


class SalePage(BasePage):
    REL_URL = '/sale.html'

    def check_title_is_(self, title_text):
        title = self.find(HEADER)
        expect(title).to_have_text(title_text)
