from playwright.sync_api import Page


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com'
    REL_URL = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.REL_URL:
            self.page.goto(f'{self.BASE_URL}{self.REL_URL}')
        else:
            raise NotImplementedError

    def find(self, locator):
        return self.page.locator(locator)
