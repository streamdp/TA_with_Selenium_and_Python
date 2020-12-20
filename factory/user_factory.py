from TA_with_Selenium_and_Python.pages.locators import LoginPageLocators
from TA_with_Selenium_and_Python.pages.login_page import LoginPage


class UserFactory:
    def __init__(self, browser, email, password):
        self.browser = browser
        self.email = email
        self.password = password

    def register_user(self):
        page = LoginPage(self.browser, LoginPageLocators.LOGIN_PAGE_LINK)
        page.open()
        page.register_new_user(self.email, self.password)
        page.should_be_authorized_user()
