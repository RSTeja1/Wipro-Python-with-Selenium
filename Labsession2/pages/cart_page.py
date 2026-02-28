from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    checkout_btn = (By.ID, "checkout")

    def go_to_checkout(self):
        try:
            self.driver.find_element(*self.checkout_btn).click()
        except Exception as e:
            print("Cart navigation failed:", e)
            raise