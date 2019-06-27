import pytest
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .urls import PRODUCT_LINK, PRODUCT_LINK_2, PRODUCT_LINK_3
from .urls import offer_promo_links, PRODUCT_PROMO_BASE_LINK


def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_product_added_to_basket()


def test_guest_can_add_product2_to_cart(browser):
    page = ProductPage(browser, PRODUCT_LINK_2)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_product_added_to_basket()


@pytest.mark.parametrize('link', offer_promo_links)
@pytest.mark.skip(reason="Not need for every launch")
def test_guest_may_raise_except_with_use_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_product_added_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, PRODUCT_PROMO_BASE_LINK)
    page.open()
    page.add_to_basket()
    page.should_not_be_product_name_alert_success()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_PROMO_BASE_LINK)
    page.open()
    page.should_not_be_product_name_alert_success()


@pytest.mark.xfail
def test_message_dissapeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, PRODUCT_PROMO_BASE_LINK)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_name_alert_success()


def test_guest_should_see_login_link_on_product_page(browser, ):
    page = ProductPage(browser, PRODUCT_LINK_3)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK_3)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PROMO_BASE_LINK)
    page.open()
    page.go_to_cart_page()

    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_is_empty()
    cart_page.should_be_text_cart_is_empty()
