from selenium.webdriver.common.by import By

class ConfirmationPage:

    confirmation_header = (By.XPATH, "//h2[text()='Thank you for your order!']")
    back_home_btn = (By.XPATH, "//button[@id='back-to-products']")

    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_header(self):
        return self.driver.find_element(*self.confirmation_header).text

    def click_back_home(self):
        self.driver.find_element(*self.back_home_btn).click()