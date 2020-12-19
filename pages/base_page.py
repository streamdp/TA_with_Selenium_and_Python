from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
