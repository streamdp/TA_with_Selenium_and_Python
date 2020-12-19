from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MainPageLocators.MAIN_SITE_LINK)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MainPageLocators.MAIN_SITE_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
