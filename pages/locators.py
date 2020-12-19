from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_SITE_LINK = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators:
    LOGIN_PAGE_LINK = "accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_INPUT_EMAIL = (By.ID, "id_login-username")
    LOGIN_INPUT_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    LOGIN_RESET_PASSWORD_LINK = (By.CSS_SELECTOR, "#login_form > p > a ")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_INPUT_EMAIL = (By.ID, "id_registration-email")
    REGISTER_INPUT_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_INPUT_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
