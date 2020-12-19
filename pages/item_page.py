from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def should_be_item_page(self):
        self.should_be_add_to_cart_button()
        self.should_be_item_name()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(ItemPageLocators.ADD_TO_CART_BUTTON), \
            "Item page is not contain add to cart button"

    def should_be_item_name(self):
        assert self.is_element_present(ItemPageLocators.ITEM_NAME), \
            "Name item is not available on this page "

    def add_to_cart(self):
        add_to_cart_button = self.wait.until(self.EC.presence_of_element_located(ItemPageLocators.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()

    def get_inline_messages(self):
        return self.wait.until(self.EC.presence_of_all_elements_located(ItemPageLocators.MESSAGES))

    def get_item_name(self):
        return self.wait.until(self.EC.presence_of_element_located(ItemPageLocators.ITEM_NAME)).text.strip()

    def get_item_price(self):
        return self.wait.until(self.EC.presence_of_element_located(ItemPageLocators.ITEM_PRICE)).text.strip()

    def is_item_present_in_messages(self, item):
        messages = self.get_inline_messages()
        for element in messages:
            if item.strip() == element.text.strip():
                return True
        return False

    def should_be_correct_item_name_present_in_messages(self):
        item_name = self.get_item_name()
        assert self.is_item_present_in_messages(item_name), \
            f"Correct item name not present in messages. Should be {item_name}"

    def should_be_correct_item_price_present_in_messages(self):
        item_price = self.get_item_price()
        assert self.is_item_present_in_messages(item_price), \
            f"Correct item price not present in messages. Should be {item_price}"

    def should_be_name_and_price_displayed_correctly(self):
        self.should_be_correct_item_name_present_in_messages()
        self.should_be_correct_item_price_present_in_messages()
