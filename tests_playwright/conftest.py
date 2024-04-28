from playwright.sync_api import Page
import pytest
from tests_playwright.pages.home_page import HomePage
from tests_playwright.pages.sale_page import SalePage


@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    yield page


@pytest.fixture()
def home_page(page):
    return HomePage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
