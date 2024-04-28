from tests_playwright.pages.base_page import BasePage
from playwright.sync_api import expect


YOGA_BUTTON = '.button.more'


class HomePage(BasePage):
    REL_URL = '/'

    def check_button_is_enabled(self):
        button = self.find(YOGA_BUTTON)
        expect(button).to_be_enabled()

    def click_the_button(self):
        button = self.find(YOGA_BUTTON)
        button.click()
