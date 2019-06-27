import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_promo_url()
        self.should_be_basket_form()
        self.should_be_add_button()

    def should_be_product_added_to_basket(self):
        self.should_be_product_name_alert_success()
        self.should_be_product_price_alert_info()

        name = self.get_product_name()
        self.should_be_eq_product_name(name)

        price = self.get_product_price()
        self.should_be_eq_product_price(price)

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        h1_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return h1_name.text

    def get_product_price(self):
        p_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return p_price.text

    def should_be_promo_url(self):
        promo = "promo"
        assert f"{promo}" in self.browser.current_url, \
            f"'{promo}' is not presented in current url"

    def should_be_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_FORM), \
            "Basket form is not presented"

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def should_be_product_name_alert_success(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), \
            "Alert success is not presented"

    def should_not_be_product_name_alert_success(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
            "Alert success is presented"

    def should_be_disappeared_name_alert_success(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), \
            "Alert success is not disappeared"

    def should_be_product_price_alert_info(self):
        assert self.is_element_present(*ProductPageLocators.P_ALERT_INFO), \
            "Alert info is not presented"

    def should_be_eq_product_name(self, name):
        added_text = f"{name} {ProductPageLocators.ADDED_TEXT}"

        div = self.find(*ProductPageLocators.ALERT_SUCCESS)
        assert div.text == added_text, \
            f"Product added text not eq: '{added_text}' '{div.text}'"

    def should_be_eq_product_price(self, price):
        total_is_now_text = f"{ProductPageLocators.TOTAL_IS_NOW_TEXT} {price}"

        p = self.find(*ProductPageLocators.P_ALERT_INFO)
        assert p.text == total_is_now_text, \
            f"Price text not eq: '{total_is_now_text}' '{p.text}'"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
