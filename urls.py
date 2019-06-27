BASE_LINK = "http://selenium1py.pythonanywhere.com"
PRODUCT_LINK_MAIN_PAGE = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209?promo=midsummer"

PRODUCT_LINK = f"{BASE_LINK}/catalogue/the-shellcoders-handbook_209/?promo=newYear"
PRODUCT_LINK_2 = f"{BASE_LINK}/catalogue/coders-at-work_207/?promo=newYear2019"
PRODUCT_LINK_3 = f"{BASE_LINK}/catalogue/the-city-and-the-stars_95/"

PRODUCT_PROMO_BASE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
offer_promo_links = [f"{PRODUCT_PROMO_BASE_LINK}/?promo=offer{no}" for no in range(10)]
