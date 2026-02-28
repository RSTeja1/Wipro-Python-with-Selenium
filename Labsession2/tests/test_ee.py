import pytest
import time
from Labsession2.utils.driver_setup import get_driver
from Labsession2.config import BASE_URL, USERNAME, PASSWORD
from Labsession2.pages.login_page import LoginPage
from Labsession2.pages.inventory_page import InventoryPage
from Labsession2.pages.cart_page import CartPage
from Labsession2.pages.checkout_page import CheckoutPage

def test_saucedemo_ee():

    driver = get_driver()

    try:
        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login(USERNAME, PASSWORD)
        time.sleep(3)
        inventory = InventoryPage(driver)
        inventory.add_product_to_cart()
        time.sleep(3)
        cart = CartPage(driver)
        cart.go_to_checkout()
        time.sleep(3)
        checkout = CheckoutPage(driver)
        checkout.complete_checkout()
        time.sleep(3)

        assert "checkout-complete" in driver.current_url


    except Exception as e:
        print("Test Failed:", e)
        raise

    finally:
        driver.quit()