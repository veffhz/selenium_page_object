from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_CART_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")

    ADDED_TEXT = "has been added to your basket."
    TOTAL_IS_NOW_TEXT = "Your basket total is now"

    ALERT_SUCCESS = (By.XPATH, f"//div[text()[contains(.,'{ADDED_TEXT}')]]")
    P_ALERT_INFO = (By.XPATH, f"//div/p[text()[contains(.,'{TOTAL_IS_NOW_TEXT}')]]")


class CartPageLocators:
    EMPTY_BASKET_TEXT = "Your basket is empty."

    EMPTY_BASKET_P = (By.CSS_SELECTOR, "#content_inner p")
    NOT_EMPTY_CART = (By.CSS_SELECTOR, "#basket_formset")

