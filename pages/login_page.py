from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_PAGE_LINK_END in self.browser.current_url, \
            f"Login link {self.browser.current_url}\n is incorrect, must contain {LoginPageLocators.LOGIN_PAGE_LINK_END}"

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "Login form is not available on this page"

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.REGISTER_FORM), \
            "Register form is not available on this page "

    def register_new_user(self, email, password):
        self.get_presence_of_element_located(LoginPageLocators.REGISTER_INPUT_EMAIL).send_keys(email)
        self.get_presence_of_element_located(LoginPageLocators.REGISTER_INPUT_PASSWORD).send_keys(password)
        self.get_presence_of_element_located(LoginPageLocators.REGISTER_INPUT_CONFIRM_PASSWORD).send_keys(password)
        self.get_presence_of_element_located(LoginPageLocators.REGISTER_BUTTON).click()
        self.is_element_present(LoginPageLocators.REGISTRATION_SUCCESS)
