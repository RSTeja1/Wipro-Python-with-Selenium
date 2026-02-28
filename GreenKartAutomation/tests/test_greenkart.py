import time

import pytest
from GreenKartAutomation.config import BASE_URL, PRODUCT_NAME, COUNTRY_NAME
from GreenKartAutomation.utils.driver_setup import get_driver
from GreenKartAutomation.pages.product_page import ProductPage
from GreenKartAutomation.pages.checkout_page import CheckoutPage
def test_greenkart_e2e():

    driver = get_driver()

    try:
        driver.get(BASE_URL)
        time.sleep(2)

        product = ProductPage(driver)
        product.search_product(PRODUCT_NAME)
        time.sleep(2)
        product.add_to_cart()
        time.sleep(2)
        product.go_to_checkout()
        time.sleep(2)

        checkout = CheckoutPage(driver)
        checkout.place_order_step(COUNTRY_NAME)
        time.sleep(2)

        assert "Thank you" in driver.page_source
        time.sleep(2)

    finally:
        driver.quit()