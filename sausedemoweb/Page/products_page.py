from selenium.webdriver.common.by import By

class ProductsPage:

    add_to_cart_btn = (By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")
    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()