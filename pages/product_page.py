from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_cart_button()
        self.should_be_product_name()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(ProductPageLocators.ADD_TO_CART_BUTTON), \
            "Item page is not contain add to cart button"

    def should_be_product_name(self):
        assert self.is_element_present(ProductPageLocators.PRODUCT_NAME), \
            "Name item is not available on this page "

    def add_to_cart(self):
        add_to_cart_button = self.get_presence_of_element_located(ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_inline_messages(self):
        return self.wait.until(self.EC.presence_of_all_elements_located(ProductPageLocators.MESSAGES))

    def get_product_name(self):
        return self.get_presence_of_element_located(ProductPageLocators.PRODUCT_NAME).text.strip()

    def get_product_price(self):
        return self.get_presence_of_element_located(ProductPageLocators.PRODUCT_PRICE).text.strip()

    def is_product_present_in_messages(self, product):
        messages = self.get_inline_messages()
        for element in messages:
            if product.strip() == element.text.strip():
                return True
        return False

    def should_be_correct_product_name_present_in_messages(self):
        product_name = self.get_product_name()
        assert self.is_product_present_in_messages(product_name), \
            f"Correct item name not present in messages. Should be {product_name}"

    def should_be_correct_product_price_present_in_messages(self):
        product_price = self.get_product_price()
        assert self.is_product_present_in_messages(product_price), \
            f"Correct item price not present in messages. Should be {product_price}"

    def should_be_name_and_price_displayed_correctly(self):
        self.should_be_correct_product_name_present_in_messages()
        self.should_be_correct_product_price_present_in_messages()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(ProductPageLocators.SUCCESS_MESSAGE, 5), \
            "Success message is not disappeared, but should not be"
