from tests_selenium.pages.locators import home_page as loc
import allure
from tests_selenium.pages.base_page import BasePage


class HomePage(BasePage):
    REL_URL = '/'

    @allure.step('Check that button is enabled')
    def check_button_is_enabled(self):
        button = self.find(loc.YOGA_BUTTON)
        assert button.is_enabled()

    @allure.step('Click the button')
    def click_the_button(self):
        button = self.find(loc.YOGA_BUTTON)
        button.click()
