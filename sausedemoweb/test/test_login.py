import pytest
import os
import time
from datetime import datetime

from sausedemoweb.Page.login_page2 import LoginPage
from sausedemoweb.Page.inventory_page import InventoryPage
from sausedemoweb.Page.products_page import ProductsPage
from sausedemoweb.Page.cart_page import CartPage
from sausedemoweb.Page.checkout_page import CheckoutPage
from sausedemoweb.Page.checkoutoverview_page import CheckoutOverviewPage
from sausedemoweb.Page.confirmation_page import ConfirmationPage
from sausedemoweb.Utilities.excel_utils import get_excel_data
from sausedemoweb.Utilities.loggers import get_logger


test_data = get_excel_data("C:/Users/ansur/Downloads/LoginData.xlsx", "Sheet1")


@pytest.mark.parametrize("username,password", test_data)
def test_e2e_order_flow(driver, username, password):

    log = get_logger()

    # OPEN WEBSITE
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    log.info(f"Starting test for user: {username}")

    # LOGIN
    login = LoginPage(driver)
    login.login(username, password)
    time.sleep(2)

    # ---------- NEGATIVE LOGIN ----------
    if username == "locked_out_user":

        assert "Epic sadface" in login.get_error_message()
        log.info("Locked user rejected correctly")

        os.makedirs("screenshots", exist_ok=True)
        file_name = f"locked_user_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(os.path.join("screenshots", file_name))
        return

    # ---------- INVENTORY PAGE ----------
    time.sleep(2)
    inventory = InventoryPage(driver)
    assert inventory.is_inventory_page_loaded()
    log.info("Login successful")

    # ADD PRODUCT
    product = ProductsPage(driver)
    product.add_product()
    time.sleep(2)

    product.go_to_cart()
    time.sleep(2)
    log.info("Product added to cart")

    # CART PAGE
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(2)
    log.info("Checkout started")

    # CHECKOUT INFO PAGE
    checkout = CheckoutPage(driver)
    checkout.enter_details(fname="Surya", lname="Tester", zipc="600002")
    time.sleep(2)

    checkout.click_continue()
    time.sleep(2)
    log.info("Entered checkout information")

    # OVERVIEW PAGE
    overview = CheckoutOverviewPage(driver)
    assert overview.is_overview_page_loaded()
    log.info("Overview page loaded: " + overview.get_total_price())

    overview.click_finish()
    time.sleep(2)

    # CONFIRMATION PAGE
    confirm = ConfirmationPage(driver)
    assert "Thank you for your order!" in confirm.get_confirmation_header()
    log.info("Order placed successfully")

    confirm.click_back_home()
    time.sleep(2)