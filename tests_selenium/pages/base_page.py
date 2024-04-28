import allure
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com'
    REL_URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open the page')
    def open(self):
        if self.REL_URL:
            self.driver.get(f'{self.BASE_URL}{self.REL_URL}')
        else:
            print('Unable to open the page without relative url')
            raise NotImplementedError('Unable to open the page without relative url')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)
