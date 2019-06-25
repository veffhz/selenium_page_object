from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")

    ADDED_TEXT = "has been added to your basket."
    TOTAL_IS_NOW = "Your basket total is now"

    #DIV_ALERT_SUCCESS = (By.CSS_SELECTOR, "div.alert.alert-success")
    ALERT_SUCCESS = (By.XPATH, f"//div[text()[contains(.,'{ADDED_TEXT}')]]")

    #DIV_ALERT_INFO = (By.CSS_SELECTOR, "div.alert.alert-info")
    P_ALERT_INFO = (By.XPATH, f"//div/p[text()[contains(.,'{TOTAL_IS_NOW}')]]")
