from selenium.webdriver.common.by import By

class InventoryPage:

    page_title = (By.XPATH, "//span[text()='Products']")
    inventory_items = (By.XPATH, "//div[@class='inventory_item']")

    def __init__(self, driver):
        self.driver = driver

    def is_inventory_page_loaded(self):
        return self.driver.find_element(*self.page_title).is_displayed()

    def get_products_count(self):
        return len(self.driver.find_elements(*self.inventory_items))