from selenium import webdriver
import pytest
from tests_selenium.pages.home_page import HomePage
from tests_selenium.pages.sale_page import SalePage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
