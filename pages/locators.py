from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    LANGUAGE_SELECTOR = (By.CSS_SELECTOR, "select[name='language']")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    CONTENT_INNER = (By.CSS_SELECTOR, "#content_inner > p")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")
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


class ProductPageLocators:
    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_PAGE_LINK_FOR_TEST_TEST = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    WRITE_REVIEW_BUTTON = (By.ID, "write_review")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    IN_STOCK_AVAILABILITY = (By.CSS_SELECTOR, ".instock.availability")
    TAG_STRONG = (By.TAG_NAME, "strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div .alertinner")
