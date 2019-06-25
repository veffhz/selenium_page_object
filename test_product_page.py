from .pages.product_page import ProductPage

product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
product_link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_product_added_to_basket()


def test_guest_can_add_product2_to_cart(browser):
    page = ProductPage(browser, product_link2)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_product_added_to_basket()