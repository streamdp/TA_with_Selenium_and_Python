import pytest

from .factory.user_factory import UserFactory
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "iPf8xTeigFy37Qp"
        UserFactory(browser, email, password).register_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_name_and_price_displayed_correctly()


def test_guest_can_to_go_to_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.should_be_product_page()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="the bug will be fixed soon")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail
                                  ),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_name_and_price_displayed_correctly()
