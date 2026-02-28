from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")
    continue_btn = (By.XPATH, "//input[@id='continue']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_details(self, fname, lname, zipc):

        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(fname)
        self.wait.until(EC.visibility_of_element_located(self.last_name)).send_keys(lname)
        self.wait.until(EC.visibility_of_element_located(self.postal_code)).send_keys(zipc)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_btn)).click()