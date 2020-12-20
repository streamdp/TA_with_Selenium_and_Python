from .base_page import BasePage
from selenium.webdriver.support.select import Select
from .locators import BasketPageLocators
from .locators import BasePageLocators

languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en-gb": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}


class BasketPage(BasePage):
    def get_selected_language(self):
        select = Select(self.get_presence_of_element_located(BasePageLocators.LANGUAGE_SELECTOR))
        return select.first_selected_option.get_attribute("value")

    def should_be_correct_text(self):
        inner_content = self.get_presence_of_element_located(BasketPageLocators.CONTENT_INNER).text.strip()
        correct_text = languages.get(self.get_selected_language())
        page_text = inner_content[:len(correct_text)]
        assert correct_text == page_text, \
            f"Invalid empty cart message, must be {correct_text}, but found {page_text}"

    def should_be_empty_basket(self):
        self.is_not_element_present(BasketPageLocators.BASKET_ITEMS)
        self.should_be_correct_text()
