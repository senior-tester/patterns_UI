import allure


@allure.title('skjdhskdjf')
def test_yoga_button(home_page):
    home_page.open()
    home_page.check_button_is_enabled()


def test_click_button(home_page):
    home_page.open()
    home_page.click_the_button()
