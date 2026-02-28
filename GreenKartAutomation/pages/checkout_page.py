from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    place_order = (By.XPATH, "//button[text()='Place Order']")
    country_dropdown = (By.TAG_NAME, "select")
    agree = (By.CLASS_NAME, "chkAgree")
    proceed = (By.XPATH, "//button[text()='Proceed']")

    def place_order_step(self, country):
        try:
            self.wait.until(EC.element_to_be_clickable(self.place_order)).click()
            self.wait.until(EC.visibility_of_element_located(self.country_dropdown)).send_keys(country)
            self.driver.find_element(*self.agree).click()
            self.driver.find_element(*self.proceed).click()
        except Exception as e:
            print("Order failed:", e)
            raise