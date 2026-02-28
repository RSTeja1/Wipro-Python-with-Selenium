from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    search_box = (By.CLASS_NAME, "search-keyword")
    add_btn = (By.XPATH, "//button[text()='ADD TO CART']")
    cart_icon = (By.CLASS_NAME, "cart-icon")
    checkout_btn = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def search_product(self, product):
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_box)).send_keys(product)
        except Exception as e:
            print("Search failed:", e)
            raise

    def add_to_cart(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.add_btn)).click()
        except Exception as e:
            print("Add to cart failed:", e)
            raise

    def go_to_checkout(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()
            self.wait.until(EC.element_to_be_clickable(self.checkout_btn)).click()
        except Exception as e:
            print("Checkout navigation failed:", e)
            raise