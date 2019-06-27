from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        login_field = self.find(*LoginPageLocators.REG_EMAIL_FIELD)
        login_field.send_keys(email)

        pass_field = self.find(*LoginPageLocators.REG_PASSWORD_FIELD)
        pass_field.send_keys(password)
        pass_confirm_field = self.find(*LoginPageLocators.REG_CONFIRM_PASSWORD_FIELD)
        pass_confirm_field.send_keys(password)

        register_button = self.find(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    @staticmethod
    def get_random_email(domen="fakemail.org"):
        return f"{str(time.time())}@{domen}"

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "'login' is not presented in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            "Register form is not presented"
