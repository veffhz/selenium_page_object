from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(CartPage, self).__init__(*args, **kwargs)

    def should_be_cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.NOT_EMPTY_CART), \
            "Cart is not empty"

    def should_be_text_cart_is_empty(self):
        p = self.find(*CartPageLocators.EMPTY_BASKET_P)

        assert CartPageLocators.EMPTY_BASKET_TEXT in p.text, \
            f"Cart empty text incorrect: '{p.text}'"

    def should_be_cart_is_not_empty(self):
        assert self.is_element_present(*CartPageLocators.NOT_EMPTY_CART), \
            "Cart is empty"
