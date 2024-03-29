"""
Специально неправильный селектор registration_link
вместо BasePageLocators.LOGIN_LINK в странице
"""

from .urls import PRODUCT_LINK_MAIN_PAGE as PRODUCT_LINK, BASE_LINK
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytest.mark.xfail(reason="incorrect id registration_link")
    def test_guest_can_go_to_login_link(self, browser):
        page = MainPage(browser, PRODUCT_LINK)
        page.open()
        page.go_to_login_page()

    @pytest.mark.xfail(reason="incorrect id registration_link")
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, PRODUCT_LINK)
        page.open()
        page.should_be_login_link()

    @pytest.mark.xfail(reason="incorrect id registration_link")
    def test_guest_should_be_login_page(self, browser):
        page = MainPage(browser, PRODUCT_LINK)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.open()
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, BASE_LINK)
    page.open()
    page.go_to_cart_page()

    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_is_empty()
    cart_page.should_be_text_cart_is_empty()
