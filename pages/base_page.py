from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.EC = EC
        self.browser.implicitly_wait(timeout)
        self.wait = WebDriverWait(self.browser, timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.get_presence_of_element_located(locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator):
        try:
            self.get_presence_of_element_located(locator)
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_presence_of_element_located(self, locator):
        return self.wait.until(self.EC.presence_of_element_located(locator))

    def go_to_login_page(self):
        link = self.get_presence_of_element_located(BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.get_presence_of_element_located(BasePageLocators.BASKET_BUTTON)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
