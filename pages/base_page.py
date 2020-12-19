from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.EC = EC
        self.browser.implicitly_wait(timeout)
        self.wait = WebDriverWait(self.browser, 5)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.wait.until(self.EC.presence_of_element_located(locator))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator):
        try:
            self.wait.until(self.EC.presence_of_element_located(locator))
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
