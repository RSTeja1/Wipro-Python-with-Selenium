from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")

    def complete_checkout(self):
        try:
            self.driver.find_element(*self.first_name).send_keys("Vijay")
            self.driver.find_element(*self.last_name).send_keys("Testing")
            self.driver.find_element(*self.postal).send_keys("560001")
            self.driver.find_element(*self.continue_btn).click()
            self.driver.find_element(*self.finish_btn).click()
        except Exception as e:
            print("Checkout failed:", e)
            raise