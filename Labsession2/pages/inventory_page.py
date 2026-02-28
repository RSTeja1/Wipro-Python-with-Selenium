from selenium.webdriver.common.by import By

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        try:
            self.driver.find_element(*self.add_backpack).click()
            self.driver.find_element(*self.cart_icon).click()
        except Exception as e:
            print("Add to cart failed:", e)
            raise