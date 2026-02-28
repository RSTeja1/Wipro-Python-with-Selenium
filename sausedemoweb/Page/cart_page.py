from selenium.webdriver.common.by import By

class CartPage:

    checkout_btn = (By.XPATH, "//button[@id='checkout']")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()