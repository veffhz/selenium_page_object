from selenium.webdriver.common.by import By


class MainPageLocators:
    def __init__(self):
        pass

    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    def __init__(self):
        pass

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
